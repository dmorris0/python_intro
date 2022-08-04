# Chapter 4: Strings and Indexing

The object `"Hello friend"` is a string which you can confirm with the `type()` method:

```python 
>>> type("Hello friend")
<class 'str'>
```

* Strings are defined using single or double quotes
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
Indexing is a key concept and is used extensively not just for strings, but lists and arrays.  It is worth spending some time to get familiary with how Python indexing works.  String indices start at `0` and proceed to `length-1`. They can also be indexed from `-length` to `-1`.  Here is one way to picture indexing on the string `b = 'Goodbye'` whose length is 7 characters:
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
* You can optionally set a step size to select every n'th element using: `[<start inclusive>:<stop exclusive>:<step size>]`
```python
>>> b[0:5:2]      # Every second element of the first 5 elements
'Gob'
>>> b[::2]        # Every second element
'Gobe'
```
* Negative steps work for reversing the order
```python
>>> b[::-1]       # Reverse order of b
'eybdooG'
>>> b[3::-1]      # Reverse first 4 elements of b
'dooG'
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
Using `f-strings` is often simpler and preferable for converting numbers to strings, such as when you want to display them.  Insert an 'f' infront of the first quote, and then use curly braces within the string to insert the number into the string.  
```python
>>> f"I ate {n1} apples and {n2} oranges"
'I ate 10 apples and 5 oranges'
```
In code you would typically include this in a `print()` function.  Also, you can set the number of decimal points and format using C-language formatting by following the number with a colon and the format like this:
```python
>>> print( f"The fraction being apples is: {n2/(n1+n2):.3}" )
The fraction being apples is: 0.333
```
For versions of Python prior to Python 3.6 which do not have `f-strings`, you can use the `.format()` function:
```python
>>> print( "I ate {} apples and {} oranges".format(n1,n2) )
I ate 10 apples and 5 oranges
```
## Find and Replace
The `.find()` method will return the first instance of a string:
```python
>>> example_text = "Hello friend! You my greatest friend."
>>> example_text.find("friend")             # Find first instance of "friend"
6
>>> example_text.replace("friend","enemy")  # Replace all instances of "friend" with "enemy"
'Hello enemy! You my greatest enemy.'
```
## End-of-line
Within code you will typically use the `print()` function to output to the terminal, and combining this with `f-strings` gives a lot of flexibility.  By default `print()` will append an end-of-line character to the output so that the next print will be on the next line.  Sometimes in loops you may want to print multiple statements to the same line, and can do this with the `end=""` option like this:
```
>>> print("Hello",end="")
Hello>>> 
```
___
## Exercises

The following exercises use this string
```python
>>> alphabet = "abcdefghijklmnopqrstuvwxyz"
```
1. Write an expression that returns every third element of the alphabet starting with the letter `c`
2. Write an expression that reverses the alphabet and returns every other letter starting with `z`
3. Write an expression that returns the last 10 letters in upper case
4. Write an expression that finds the index of the letter `z`
5. Using `f-strings` and the `alphabet` string above, write an expression outputs the following text: `"The capitalized even letters are BDFHJLNPRTVXZ"`

___
### [Outline](../README.md), Next: [Chapter 5: Numbers and Math](Chapter_05_Numbers_and_Math.md)
