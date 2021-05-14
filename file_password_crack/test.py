import httpx

r = httpx.get('http://httpbin.org')
print(r.text)
print(r.content)
print(r.json())
print(r.status_code)