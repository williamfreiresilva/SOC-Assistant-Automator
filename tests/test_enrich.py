# tests/test_enrich.py
from intel_feeds import enrich_all_sources

def test_enrich_valid_ip():
    result = enrich_all_sources("1.1.1.1")
    assert "abuse_ch" in result
    assert "otx" in result
    assert "greynoise" in result
