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
$parserScript = Join-Path $repoRoot "scripts\thinkscript_parser.py"

if (-not (Test-Path $SourcePath)) { throw "Source file not found: $SourcePath" }
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw "Python is required on PATH." }

# Run parser and capture JSON result
$json = python $parserScript $SourcePath --json
$result = $json | ConvertFrom-Json

if (-not $result) { throw "Parser returned no result." }

$errors = @($result.issues | Where-Object { $_.severity -eq 'error' })

Write-Host "Statements: $($result.statements.Count)"
foreach ($i in $result.issues) {
    $suffix = if ($i.line) { " (line $($i.line))" } else { "" }
    Write-Host "[$($i.severity.ToUpper())] $($i.rule)$($suffix): $($i.message)"
}

if ($Mode -eq 'fail' -and $errors.Count -gt 0) {
    exit 1
}

exit 0
