import json
import time
from intel_feeds import enrich_all_sources
import os

WATCHLIST_FILE = "watchlist.json"
OUTPUT_DIR = "feeds/enriched"
os.makedirs(OUTPUT_DIR, exist_ok=True)

REFRESH_SECONDS = 3600  # 1 hour interval

def load_watchlist():
    with open(WATCHLIST_FILE, 'r') as f:
        return json.load(f)

def save_result(ip, data):
    safe_ip = ip.replace('.', '_')
    path = os.path.join(OUTPUT_DIR, f"{safe_ip}_intel.json")
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"[+] Saved intel result: {path}")

def run_ingestion():
    print("[+] Starting IOC ingestion loop")
    while True:
        try:
            iocs = load_watchlist()
            print(f"[+] Loaded {len(iocs)} IOCs from watchlist")
            for ip in iocs:
                enriched = enrich_all_sources(ip)
                save_result(ip, enriched)
            print(f"[+] Sleeping {REFRESH_SECONDS} seconds\n")
            time.sleep(REFRESH_SECONDS)
        except Exception as e:
            print(f"[!] Error in ingestion loop: {str(e)}")
            time.sleep(60)

if __name__ == "__main__":
    run_ingestion()