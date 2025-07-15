import nmap

def run_nmap_scan(ip_address):
    scanner = nmap.PortScanner()
    print(f"[+] Scanning {ip_address} with NMAP + vulners...")
    try:
        scanner.scan(hosts=ip_address, arguments='-sV --script vulners')
        result = scanner[ip_address] if ip_address in scanner.all_hosts() else {}
        status = scanner[ip_address].state() if ip_address in scanner.all_hosts() else "unknown"
        return result, status
    except Exception as e:
        return {"error": f"NMAP scan failed: {str(e)}"}, "error"