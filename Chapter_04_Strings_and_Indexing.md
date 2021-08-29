# Chapter 4: Strings and Indexing

The object `"Hello friend"` is a string which you can confirm with the `type()` method:

```python 
>>> type("Hello friend")
<class 'str'>
```

* Stings are defined using single or double quotes
* You can place single quotes inside double quotes and vice versa:
```python
>>> a = 'Melinda said "Hello!"'
>>> print(a)
Melinda said "Hello!"
```
* Strings can be concatenated with a `+`
```python
>>> b = "Goodbye"
>>> c = a + b     # + sign concatenates two strings
>>> c
'Melinda said "Hello!"goodbye'
```
* Find the length of a string with the `len()` function:
```python
>>> len(b)
7
```
## Indexing and Slicing
Indexing is a key concept and is used extensively not just for strings, but lists and arrays.  It is worth spending some time to get familiary with how Python indexing works.  String indices start at `0` and proceed to the `length-1`. They can also be indexed from `-length` to `-1`.  Here is one way to picture indexing on the string `b = 'Goodbye'` whose length is 7 characters:
```
String:  |  G  o  o  d  b  y  e  |  G  o  o  d  b  y  e |
Indices: | -7 -6 -5 -4 -3 -2 -1  |  0  1  2  3  4  5  6 |
```
* Elements can be indexed as follows:
```python
>>> b[0]          # First element (for any string)
'G'
>>> b[1]          # Second element
'o'
>>> b[6]          # Last element (for string of length 7)
'e'
>>> b[-1]         # Last element (for any string)
'e'
>>> b[-7]         # First element (for string of length 7)
'G'
```
* Exceeding the length results in either direction results in an error
```python
>>> b[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
* Using slicing you can select portions of the string using the format `[<start inclusive>:<stop exclusive>]`.  Pay attention to the fact that the elements returned **exclude** the stop element:
```python
>>> b[0:2]        # First two elements, i.e. elements 0, 1
'Go'
>>> b[0:7]        # First seven elements, i.e. elements 0, ..., 6
'Goodbye'
>>> b[4:7]        # Elements 4, 5, 6
'bye'
>>> b[-7:-3]      # Elements -7, -6, -5, -4
'Good'
```
* To index from the start, drop the first element. To index to the end, drop the second element.
```python
>>> b[:3]         # First 3 elements
'Goo'
>>> b[4:]         # Element 4 to the end
'bye'
>>> b[-3:]        # Last 3 elements
'bye'
>>> b[:]          # All elements
'Goodbye'
```
* Can optionally set step size to select every n'th element using: `[<start inclusive>:<stop exclusive>:<step size>]`
```python
>>> b[0:5:2]      # Every second element of the first 5 elements
'Gob'
>>> b[::2]        # Every second element
'Gobe'
```
## Immutability and Methods
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
Or for versions of Python prior to Python 3.6 which do not have `f-strings`, you can use:
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
### [Outline](README.md), Next: [Chapter 5: Numbers and Math](Chapter_05_Numbers_and_Math.md)
