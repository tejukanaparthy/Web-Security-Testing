import time
import requests

ZAP_URL = "http://localhost:8080"

TARGET_URL = "https://www.netflix.com/"

def start_active_scan(target):
    """Start an active scan using OWASP ZAP"""
    scan_url = f"{ZAP_URL}/JSON/ascan/action/scan/?url={target}"
    response = requests.get(scan_url)
    scan_id = response.json().get("scan")
    print(f"Scan started with ID: {scan_id}")
    return scan_id

def check_scan_status(scan_id):
    """Check scan progress"""
    while True:
        status_url = f"{ZAP_URL}/JSON/ascan/view/status/?scanId={scan_id}"
        status = requests.get(status_url).json().get("status")
        print(f"Scan progress: {status}%")
        if status == "100":
            break
        time.sleep(5)

def get_scan_results():
    """Retrieve scan results"""
    results_url = f"{ZAP_URL}/JSON/core/view/alerts/"
    results = requests.get(results_url).json()
    print("Scan Results:", results)

# Run scan
scan_id = start_active_scan(TARGET_URL)
check_scan_status(scan_id)
get_scan_results()
