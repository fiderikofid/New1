import requests


url = 'https://httpbin.org/redirect-to'
# payload = open("request.json")
headers = {"accept": "text/html", "Content-Type": "application/x-www-form-urlencoded"}
 # "url"="https%3A%2F%2Fhttpbin.org%2F%23%2FRedirects%2Fpost_redirect_to&status_code=200"
r = requests.post(url, headers=headers)

print(r.headers["Content-Type"])
print("resp", r)