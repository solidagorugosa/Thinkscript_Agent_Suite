[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Path,

    [Parameter(Mandatory = $true)]
    [ValidateSet('generate','debug','explain','validate','strategy','strategy-convert','study')]
    [string]$TaskType,

    [ValidateSet('warn','fail')]
    [string]$Mode = 'warn'
)

$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$selfCheck = Join-Path $repoRoot "scripts\self-check-thinkscript.ps1"

if (-not (Test-Path $Path)) { throw "File not found: $Path" }
if (-not (Test-Path $selfCheck)) { throw "Missing required script: $selfCheck" }

$hasError = $false

function Test-ThinkScriptTarget {
    param(
        [Parameter(Mandatory = $true)][string]$SourceFile,
        [Parameter(Mandatory = $true)][string]$Kind
    )

    & $selfCheck -SourcePath $SourceFile -TaskType $Kind -Mode $Mode
    if ($LASTEXITCODE -ne 0) { $script:hasError = $true }
}

$ext = [System.IO.Path]::GetExtension($Path).ToLowerInvariant()
$mappedTask = if ($TaskType -eq 'strategy-convert') { 'strategy' } else { $TaskType }

if ($ext -in @('.thinkscript', '.ts')) {
    Test-ThinkScriptTarget -SourceFile $Path -Kind $mappedTask
}
elseif ($ext -in @('.md', '.txt')) {
    $content = Get-Content -Raw -Path $Path

    if ($TaskType -eq 'validate') {
        $fenceAny = '(?ms)(`{3,4})\s*[a-zA-Z0-9_-]*\s*\r?\n.*?\r?\n\1'
        if ([regex]::IsMatch($content, $fenceAny)) {
            Write-Host "[ERROR] P-VAL-2: Validation output must not include code blocks."
            $hasError = $true
        }
    }

    $fenceTs = '(?ms)(`{3,4})\s*thinkscript\s*\r?\n(.*?)\r?\n\1'
    $codeBlocks = [regex]::Matches($content, $fenceTs)

    if ($codeBlocks.Count -eq 0 -and $TaskType -ne 'validate') {
        Write-Host "[ERROR] P-CODE-1: No fenced thinkscript code block found."
        $hasError = $true
    }

    $i = 0
    foreach ($m in $codeBlocks) {
        $i++
        $tmp = Join-Path $env:TEMP ("ts_validate_" + [guid]::NewGuid().ToString("N") + "_$i.ts")
        Set-Content -Path $tmp -Value $m.Groups[2].Value -Encoding UTF8
        Test-ThinkScriptTarget -SourceFile $tmp -Kind $mappedTask
        Remove-Item $tmp -ErrorAction SilentlyContinue
    }
}
else {
    throw "Unsupported file type: $ext"
}

if ($hasError -and $Mode -eq 'fail') { exit 1 }
exit 0