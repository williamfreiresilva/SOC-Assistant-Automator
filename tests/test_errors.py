# tests/test_errors.py
from scan import run_nmap_scan
from scanner_openvas import run_openvas_scan

def test_invalid_ip():
    result, status = run_nmap_scan("999.999.999.999")
    assert "error" in result

def test_openvas_fail():
    result = run_openvas_scan("localhost")
    assert isinstance(result, dict)
