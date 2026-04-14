[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$SourcePath,

    [ValidateSet('generate','debug','explain','validate','strategy','strategy-convert','study')]
    [string]$TaskType = 'generate',

    [ValidateSet('warn','fail')]
    [string]$Mode = 'warn'
)

$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$docPath = Join-Path $repoRoot ".github\skills\thinkscript-authoring\references\Thinkscript-Documentation-Scrape\thinkscript_documentation_cleaned.md"
$manifestPath = Join-Path $repoRoot "schemas\thinkscript_manifest.json"
$buildScript = Join-Path $repoRoot "scripts\build_thinkscript_manifest.py"
$parserScript = Join-Path $repoRoot "scripts\thinkscript_parser.py"

if (-not (Test-Path $SourcePath)) { throw "Source file not found: $SourcePath" }
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "Python is required on PATH." }

# Build/refresh manifest from local docs
python $buildScript --doc $docPath --out $manifestPath | Out-Null

# Run parser and capture JSON result
$json = python $parserScript $SourcePath --json
$result = $json | ConvertFrom-Json

if (-not $result) { throw "Parser returned no result." }

$errors = @($result.issues | Where-Object { $_.severity -eq 'error' })
$warnings = @($result.issues | Where-Object { $_.severity -eq 'warning' })

Write-Host "Statements: $($result.statements.Count)"
foreach ($i in $result.issues) {
    $line = if ($i.line) { " (line $($i.line))" } else { "" }
    Write-Host "[$($i.severity.ToUpper())] $($i.rule)$line: $($i.message)"
}

if ($Mode -eq 'fail' -and $errors.Count -gt 0) {
    exit 1
}

exit 0