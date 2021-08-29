# Chapter 3: Python Programs

## Interactive Terminal

In your shell type `python` to start an interactive terminal.  (Note that if you are using Ubuntu and are not running a virtual environment, then to run Python type `python3`.)
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
Comments within your code easier to understand for others and yourself at a later date, especially if you follow Python conventions.
* Block comments: A newline starting with a `#`.  
* Inline comments: A `#` will comment out the rest of the line.
* **Conventions**:
  * Write complete sentences
  * Use a single space after the `#`
  * At least 2 spaces before an inline `#`
  * Don't describe what is already obvious
    * Ex: if you have the line `number_of_cars = 5`, don't add a comment `# Number of cars`

___
### [Outline](README.md), Next: [Chapter 4: Strings and Indexing](Chapter_04_Strings_and_Indexing.md)
