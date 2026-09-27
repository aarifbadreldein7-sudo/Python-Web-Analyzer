import requests


url = input("Enter website url: ")

try:
    response = requests.get(url, timeout=5)

    
    print("Status Code:", response.status_code)
    print("Server:", response.headers.get("server"))
    print("Content-Type:", response.headers.get("content-type"))
    print("Content-Encoding:", response.headers.get("content-encoding"))
    print("Content-Length:", response.headers.get("content-length"))
    print("Final URL:", response.url)
    print("Response History:",len(response.history))
    print("Response Time:", response.elapsed.total_seconds())


except requests.RequestException:
    print("Couldn't connect to website!")


