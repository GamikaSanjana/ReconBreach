import sys
from reconnaissance import start_recon
from exploit import start_exploit
from post_exploitation import start_post_exploit
from vulnerability_scanners import nessus_scanner, openvas_scanner, nikto_scanner
from ai_model import load_model, predict_vulnerabilities
from tools import sql_injection_tool, xss_tool, ssrf_tool
from reports import generate_report
from config import get_config

def main(target):
    # Load configuration
    config = get_config()

    # Step 1: Run reconnaissance
    print("[*] Running reconnaissance...")
    recon_data = start_recon(target)

    # Step 2: Scan with vulnerability scanners (Nessus, OpenVAS, Nikto)
    print("[*] Running vulnerability scanners...")
    nessus_results = nessus_scanner.scan(target)
    openvas_results = openvas_scanner.scan(target)
    nikto_results = nikto_scanner.scan(target)

    # Step 3: AI-based vulnerability prediction
    print("[*] Predicting vulnerabilities using AI model...")
    model = load_model(config["ai_model_path"])
    vulnerabilities = predict_vulnerabilities(model, recon_data)

    # Step 4: Generate exploit payloads
    print("[*] Generating exploit payloads...")
    payloads = []
    if "SQL Injection" in vulnerabilities:
        payloads.append(sql_injection_tool.generate_payload())
    if "XSS" in vulnerabilities:
        payloads.append(xss_tool.generate_payload())
    if "SSRF" in vulnerabilities:
        payloads.append(ssrf_tool.generate_payload())

    # Step 5: Attempt exploitation
    print("[*] Attempting exploitation...")
    exploit_results = start_exploit(target, payloads)

    # Step 6: Post-exploitation tasks (pivoting, privilege escalation)
    print("[*] Attempting post-exploitation...")
    post_exploit_results = start_post_exploit(target)

    # Step 7: Generate dynamic report
    print("[*] Generating report...")
    generate_report(recon_data, vulnerabilities, exploit_results, post_exploit_results, nessus_results, openvas_results, nikto_results)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else input("Enter target IP or URL: ")
    main(target)
