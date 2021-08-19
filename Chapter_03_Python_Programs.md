# Chapter 3: Python Programs

## Interactive Terminal

In your shell type `python` like this:
```
$ python
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The `>>>` is the prompt where you type your code.  Within the Python interactive shell you can evaluate expressions.  Try doing some arithmetic like this:
```python
>>> 1 + 2
3
```
And use the `print()` function:
```python
>>> print("Hello Class")
Hello Class
```

## Variables

* Variables hold values.  They are strings with numbers and underscores `_`.  They cannot start with a number. 
* It is best to use descriptive names
* Python convention is to use underscores between words such as `secret_code` rather than capital letters such as `secretCode`.
* Following conventions makes code more readable and understandable to others and to yourself at a later point.
```python
>>> student_age = 19
>>> student_age
19
>>> print(student_age)
19
```

## Comments
* Block comments: A newline starting with a `#`.  
* Inline comments: A `#` will comment out the rest of the line.
* Conventions:
  * Write complete sentences
  * Single space after th `#`
  * At least 2 spaces before inline `#`
  * Don't describe what is already obvious

___
### [Outline](README.md), Next: [Chapter 4: Strings and Indexing](Chapter_04_Strings_and_Indexing.md)
