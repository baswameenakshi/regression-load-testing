import requests

response = requests.get("https://your-api.com/test")
if response.status_code == 200:
    print("✅ Test Passed!")
else:
    print("❌ Test Failed!")
