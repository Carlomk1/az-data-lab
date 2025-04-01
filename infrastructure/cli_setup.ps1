# setup cli for azure: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?pivots=winget
Write-Host "Check if Azure CLI is installed"

if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    Write-Host "Azure CLI will be installed with WinGet..."
    winget install --exact --id Microsoft.AzureCLI --silent
} else {
    Write-Host "Azure CLI is already installed"
}

Write-Host "Start Azure Login..."
az login

Write-Host "Show Azure Account info..."
az account show
