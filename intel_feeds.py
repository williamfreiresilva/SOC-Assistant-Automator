import requests
import os

ABUSECH_API_KEY = "e0751203070789de5a8477e60d9b504adc497a78d3f4d841"
OTX_API_KEY = "7d9b652c8f3aadc2a0dc2d2138326c3265735d87c8407db487b5d91e85632402"
GREYNOISE_API_KEY = "Qk8tDw6DZd8ZBA8IAaJ3n2tVTSXVwgGvq2PmCSyJOyLqLA5VHmHEr2PF7Y0yZdav"

def abusech_threatfox_lookup(ip):
    url = "https://threatfox-api.abuse.ch/api/v1/"
    body = {
        "query": "search_ioc",
        "search_term": ip,
        "api_key": ABUSECH_API_KEY
    }
    try:
        response = requests.post(url, json=body, timeout=10)
        return response.json() if response.ok else {"error": "Abuse.ch lookup failed"}
    except Exception as e:
        return {"error": str(e)}

def otx_lookup(ip):
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general"
    headers = {"X-OTX-API-KEY": OTX_API_KEY}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.json() if response.ok else {"error": "OTX lookup failed"}
    except Exception as e:
        return {"error": str(e)}

def greynoise_lookup(ip):
    url = f"https://api.greynoise.io/v3/community/{ip}"
    headers = {"key": GREYNOISE_API_KEY}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.json() if response.ok else {"error": "GreyNoise lookup failed"}
    except Exception as e:
        return {"error": str(e)}

def enrich_all_sources(ip):
    abusech_data = abusech_threatfox_lookup(ip)
    otx_data = otx_lookup(ip)
    greynoise_data = greynoise_lookup(ip)
    return abusech_data, otx_data