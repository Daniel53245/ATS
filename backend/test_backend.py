import requests
import sys

def test_backend():
    base_url = "http://localhost:8000"
    
    # Test the test-user endpoint
    print("\nTesting /test-user endpoint...")
    try:
        response = requests.get(f"{base_url}/test-user")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the backend. Is it running?")
        sys.exit(1)
    
    # Test the docs endpoint
    print("\nTesting /docs endpoint...")
    try:
        response = requests.get(f"{base_url}/docs")
        print(f"Status Code: {response.status_code}")
        print("Docs endpoint is accessible")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the docs endpoint")
    
    # Test the OpenAPI schema
    print("\nTesting /openapi.json endpoint...")
    try:
        response = requests.get(f"{base_url}/openapi.json")
        print(f"Status Code: {response.status_code}")
        print("OpenAPI schema is accessible")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the OpenAPI schema endpoint")

if __name__ == "__main__":
    test_backend() 