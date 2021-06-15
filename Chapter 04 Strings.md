# Chapter 3 Strings

```python 
>>> type("Hello friend")
<class 'str'>
```

* Stings defined using single or double quotes
* Can place single quotes inside double quotes and vice versa
```
>>> a = 'Melinda said "Hello!"'
>>> print(a)
Melinda said "Hello!"
```
* Strings can be concatenated
```
>>> b = "Now goodbye"
>>> c = a + b
>>> c
'Melinda said "Hello!"Now goodbye'
>>> print(c)
Melinda said "Hello!"Now goodbye
```
* Length of a string
```
>>> len(a)
21
```
## Indexing and Slicing
Indexing is a key concept and is used extensively not just for strings, but lists and arrays.  It is worth spending some time to get familiary with how Python indexing works.  String indices start at `0` and proceed to the `length-1`. They can also be indexed from `-length` to `-1`.  
* Example indices:
```
>>> a[0]
'M'
>>> a[1]
'e'
>>> a[20]
'"'
>>> a[-1]
'"'
>>> a[-21]
'M'
```
* Exceeding the length results in either direction results in an error
```
>>> a[21]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
* Using slicing you can select portions of the string using the format `[<start inclusive>:<stop exclusive>]`
```
>>> a[0:2]
'Me'
>>> a[0:7]
'Melinda'
>>> a[15:21]
'ello!"'
>>> a[-21:-14]
'Melinda'
```
* To index from the start, drop the first element. To index to the end, drop the second element.
```
>>> a[:7]
'Melinda'
>>> a[15:]
'ello!"'
>>> a[-6:]
'ello!"'
>>> a[:]
'Melinda said "Hello!"'
```
* Can optionally set step size to select every n'th element using: `[<start inclusive>:<stop exclusive>:<step size>]`
```
>>> a[0:7:2]
'Mlna'
>>> a[::2]
'Mlnasi Hlo"'
```
## Methods
```python
>>> "Hello Friend".lower()
'hello friend'
```
