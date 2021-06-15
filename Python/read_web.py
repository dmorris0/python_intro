import requests
resp = requests.get("https://www.egr.msu.edu/~dmorris/")
html = resp.text
print(html)
