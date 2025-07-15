import subprocess

def run_openvas_scan(ip_address):
    print(f"[+] Triggering OpenVAS scan on {ip_address}...")
    try:
        result = subprocess.run([
            "gvm-cli", "socket",
            "--gmp-username", "admin", "--gmp-password", "admin",
            "--xml", f'<create_target><name>{ip_address}</name><hosts>{ip_address}</hosts></create_target>'
        ], capture_output=True, text=True, timeout=60)
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    except subprocess.TimeoutExpired:
        return {"error": "OpenVAS: Timeout expired"}
    except Exception as e:
        return {"error": f"OpenVAS: {str(e)}"}