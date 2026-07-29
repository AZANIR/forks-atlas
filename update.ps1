<#
.SYNOPSIS
    Локальний запуск оновлення каталогу (Windows).

.DESCRIPTION
    Те саме, що робить GitHub Actions, але на цій машині. Токен береться з
    `gh auth token`, тому окремо нічого налаштовувати не треба.

.PARAMETER Push
    Закомітити й запушити, якщо data/forks.json змінився.

.EXAMPLE
    .\update.ps1
    .\update.ps1 -Push
#>
[CmdletBinding()]
param([switch]$Push)

$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

python scripts/update.py --self-test
python scripts/update.py

if (-not $Push) {
    Write-Host "`nГотово. Запустіть з -Push, щоб закомітити зміни." -ForegroundColor Cyan
    return
}

# Дата генерації в README змінюється щоразу, тому ознакою реальних змін
# лишається лише знімок даних.
git diff --quiet -- data/forks.json
if ($LASTEXITCODE -eq 0) {
    Write-Host "Змін немає — коміт пропущено." -ForegroundColor DarkGray
    return
}

git add -A
git commit -m "Оновлення каталогу форків"
git push
