import requests

def scan_vulnerabilities(target):
    test_urls = [
        f"http://{target}/?id=1'",
        f"http://{target}/?q=<script>alert(1)</script>"
    ]
    findings = []

    for url in test_urls:
        try:
            response = requests.get(url, timeout=1)
            if "sql" in response.text.lower() or "syntax" in response.text.lower():
                findings.append(f"Potential SQL Injection found at {url}")
            if "<script>alert(1)</script>" in response.text:
                findings.append(f"Possible XSS vulnerability at {url}")
        except requests.exceptions.RequestException:
            findings.append(f"Could not connect to {url}")

    return "\\n".join(findings) if findings else "No obvious vulnerabilities detected."
