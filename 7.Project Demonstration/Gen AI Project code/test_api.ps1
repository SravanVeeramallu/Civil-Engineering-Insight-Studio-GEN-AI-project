$env:GOOGLE_API_KEY = Get-Content .env | Where-Object { $_ -match "GOOGLE_API_KEY" } | ForEach-Object { $_.Split("=")[1].Trim() }
Write-Host "Testing key: $($env:GOOGLE_API_KEY.Substring(0,5))..."

try {
    $response = Invoke-RestMethod -Uri "https://generativelanguage.googleapis.com/v1beta/models?key=$($env:GOOGLE_API_KEY)" -Method Get
    Write-Host "Success! Models found:"
    $response.models | ForEach-Object { Write-Host $_.name }
} catch {
    Write-Host "Error:"
    Write-Host $_.Exception.Message
    Write-Host $_.ErrorDetails.Message
}
