Param(
  [Parameter(Mandatory=$true)][string]$RepoName,
  [ValidateSet('public','private','internal')][string]$Visibility='public',
  [string]$Description='Chess variant project (console + GUI + AI)'
)

# Requires: set $env:GITHUB_TOKEN with repo scope and $env:GITHUB_USER
if (-not $env:GITHUB_USER) { Write-Error 'Please set $env:GITHUB_USER to your GitHub username.'; exit 1 }
if (-not $env:GITHUB_TOKEN) { Write-Error 'Please set $env:GITHUB_TOKEN to a GitHub Personal Access Token (repo scope).'; exit 1 }

$api = 'https://api.github.com/user/repos'
$body = @{ name=$RepoName; description=$Description; private=($Visibility -ne 'public') } | ConvertTo-Json
$headers = @{ Authorization = "token $($env:GITHUB_TOKEN)"; 'User-Agent' = 'chess-variant-setup' }

Write-Host "Creating GitHub repo $RepoName ($Visibility) ..."
$resp = Invoke-RestMethod -Method Post -Uri $api -Headers $headers -Body $body
$cloneUrl = $resp.clone_url
if (-not $cloneUrl) { Write-Error 'Failed to create repository via API.'; exit 1 }

Write-Host "Setting remote origin -> $cloneUrl"
Push-Location "$PSScriptRoot\..\"
if (-not (Test-Path '.git')) { Write-Error 'Run this script from within the project folder after git init.'; exit 1 }
git remote remove origin 2>$null
git remote add origin $cloneUrl
git push -u origin main
Pop-Location

Write-Host 'Done.'

