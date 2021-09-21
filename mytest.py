import requests
example = """
i = 1
while i<n:
    print(i)
    i += i
i = 1 if i <1 else 0
if i > n and i>100:
    if i<n:
        print(i)
    elif i>n:
        print(i)
    else:
        print(i)
    print(i)
for i in range(10):
    print(i)
"""
url = "http://192.168.10.2:8888/api/compute"
d = {
    "code": example
}
rep = requests.post(url, json=d)
print(rep.content)