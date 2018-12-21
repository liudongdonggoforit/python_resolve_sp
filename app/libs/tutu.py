import requests
import json
import base64

data = {"sourceUrl": "http://vm.tiktok.com/JQ6Qat/", "flatform": "18"}
baseUrl = base64.b64decode("aHR0cDovL3ZtLnRpa3Rvay5jb20vSlE2UWF0Lw==")
result = requests.get("http://127.0.0.1:5011/tutu?url=aHR0cDovL3ZtLnRpa3Rvay5jb20vSlE2UWF0Lw==").text
# result = requests.get("http://127.0.0.1:5010/v1.0/22/aHR0cDovL3ZtLnRpa3Rvay5jb20vSlE2UWF0Lw==").text
print(result)
