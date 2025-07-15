# tests/test_triage.py
import subprocess

def test_scan_ip():
    ip = "8.8.8.8"
    result = subprocess.run(["python", "scanner.py", ip], capture_output=True, text=True)
    assert "Results saved" in result.stdout or "Scan failed" in result.stdout
