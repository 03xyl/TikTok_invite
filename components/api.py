import requests

headers = {
    "User-Agent": "my-app/0.0.1",
    "auth-type": "jwt-token"
}

proxies={
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}

response = requests.get("https://www.baidu.com/s", headers=headers,proxies=proxies)

print(response.text)

