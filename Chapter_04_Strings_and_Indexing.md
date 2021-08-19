# Chapter 4: Strings and Indexing

The object `"Hello friend"` is a string which you can confirm:

```python 
>>> type("Hello friend")
<class 'str'>
```

* Stings are defined using single or double quotes
* Can place single quotes inside double quotes and vice versa
```python
>>> a = 'Melinda said "Hello!"'
>>> print(a)
Melinda said "Hello!"
```
* Strings can be concatenated with a `+`
```python
>>> b = "Now goodbye"
>>> c = a + b     # + sign concatenates two strings
>>> c
'Melinda said "Hello!"Now goodbye'
>>> print(c)
Melinda said "Hello!"Now goodbye
```
* Find the length of a string with the `len()` function:
```python
>>> len(a)
21
```
## Indexing and Slicing
Indexing is a key concept and is used extensively not just for strings, but lists and arrays.  It is worth spending some time to get familiary with how Python indexing works.  String indices start at `0` and proceed to the `length-1`. They can also be indexed from `-length` to `-1`.  
* Example indices for the above-defined string `a`, that is length 21:
```python
>>> a[0]          # First element of string
'M'
>>> a[1]          # Second element
'e'
>>> a[20]         # Last element (for string of length 21)
'"'
>>> a[-1]         # Last element (for any string)
'"'
>>> a[-21]        # First element (for string of length 21)
'M'
```
* Exceeding the length results in either direction results in an error
```python
>>> a[21]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
* Using slicing you can select portions of the string using the format `[<start inclusive>:<stop exclusive>]`
```python
>>> a[0:2]        # First two elements, i.e. 0, 1
'Me'
>>> a[0:7]        # First seven elements
'Melinda'
>>> a[15:21]      # Elements 15 through 20
'ello!"'
>>> a[-21:-14]
'Melinda'
```
* To index from the start, drop the first element. To index to the end, drop the second element.
```python
>>> a[:7]         # First 7 elements
'Melinda'
>>> a[15:]        # Element 15 to the end
'ello!"'
>>> a[-6:]        # Last 6 elements
'ello!"'
>>> a[:]          # All elements
'Melinda said "Hello!"'
```
* Can optionally set step size to select every n'th element using: `[<start inclusive>:<stop exclusive>:<step size>]`
```python
>>> a[0:7:2]      # Every second element of the first 7 elements
'Mlna'
>>> a[::2]        # Every second element
'Mlnasi Hlo"'
```
## Immuntability and Methods
* Strings are **immutable**. That is, they cannot be changed:
```python
>>> text = "Hello"
>>> text[0] = "h"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
Nevertheless there are methods that operate on strings, such as `.lower()` and `.upper()`: 
```python
>>> "Hello Friend".lower()
'hello friend'
```
These methods do not change the actual string, but rather return a copy with the operation applied.
* Other useful methods remove whitespace from the left, right or both:
```python
>>> name = "  Samuel Becket  "
>>> name.lstrip()         # Remove left whitespace
'Samuel Becket  '
>>> name.rstrip()         # Remove right whitespace
'  Samuel Becket'
>>> name.strip()          # Remove left and right whitespace
'Samuel Becket'
```
* Check if a string starts with a particular string:
```python
>>> name.startswith("Samuel")
False
>>> name.strip().startswith("Samuel")
True
```
* User input
```python
>>> prompt = "What is your name? "
>>> name = input(prompt)
What is your name? Queen Elizabeth
>>> name
'Queen Elizabeth'
```

## Strings and Numbers
* Arithmetic operations on strings:
```python
>>> num = "2"
>>> num + num         # String concatenation
"22"
>>> 3 * num           # String repitition
"222"
>>> num + 3           # + cannot combine a string and a number
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
The above is wrong as `+` cannot add a number to a string.  First convert the string to a number:
```python
>>> int(num) + 3
5
>>> float(num) + 3
5.0
```
Or convert the number to a string:
```python
>>> n1, n2 = 10, 5
>>> "I ate " + str(n1) + " apples and " + str(n2) + " oranges" 
'I ate 10 apples and 5 oranges'
```
Using `f-strings` is often simpler and preferable for converting strings to numbers:
```python
>>> f"I ate {n1} apples and {n2} oranges"
'I ate 10 apples and 5 oranges'
```
Or for version of Python prior to Python 3.6 which do not have `f-strings`, you can use:
```python
>>> "I ate {} apples and {} oranges".format(n1,n2)
'I ate 10 apples and 5 oranges'
```
## Find and Replace
The `.find()` method will return the first instance of a string:
```python
>>> text = "Hello friend! You my greatest friend."
>>> text.find("friend")             # Find first instance of "friend"
6
>>> text.replace("friend","enemy")  # Replace all instances of "friend" with "enemy"
'Hello enemy! You my greatest enemy.'
```

___
### Go to: [Outline](README.md), or: [Chapter 5: Numbers and Math](Chapter_05_Numbers_and_Math.md)
