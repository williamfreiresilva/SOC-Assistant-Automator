from scan import run_nmap_scan
from enrichment import enrich_all_sources
from scanner_openvas import run_openvas_scan
from reporter import save_json, render_html_report
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <ip_address>")
        exit(1)

    ip = sys.argv[1]

    scan_result, status = run_nmap_scan(ip)
    abuse_data, vt_data = enrich_all_sources(ip)
    openvas_data = run_openvas_scan(ip)

    report = {
        "scanned_at": __import__('datetime').datetime.utcnow().isoformat(),
        "target": ip,
        "status": status,
        "scan": scan_result,
        "abuseipdb": abuse_data,
        "virustotal": vt_data,
        "openvas": openvas_data
    }

    save_json(report)
    render_html_report(report)