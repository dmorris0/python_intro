Introduction to Python

Book:
Python Basics: A Practical Introduction to Python 3, 4th edition

Basics are easy:
```python
print("Hello class!")
```

Example more complex function, see `read_web.py`:
```python
import requests
resp = requests.get("https://www.egr.msu.edu/~dmorris/")
html = resp.text
print(html)
```
