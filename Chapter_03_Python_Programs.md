# Chapter 3: Python Programs

## Interactive Terminal

In your terminal window type `python` to start an interactive Python environment.  (Note that if you are using Ubuntu and are not running a virtual environment, then to run Python type `python3`.)
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

* Variables hold values.  They are strings containing only letters, numbers and underscores `"_"`.  They cannot start with a number. 
* It is best to use descriptive names
* Python's convention for *variables* is to use underscores between words such as `secret_code` rather than camel case such as `SecretCode`.  (The latter is used for classes.)

Note that even though it is not required, it is important to follow Python's conventions as this makes your code much more readable and understandable to others and to yourself.  
```python
>>> student_age = 19
>>> student_age
19
>>> print(student_age)
19
```

## Comments
Judicious comments within your code can greatly improve understanding of your code for others and yourself at a later date.
* Block comments: A newline starting with a `#`.  
* Inline comments: A `#` will comment out the rest of the line.

**Conventions**:
* Write complete sentences
* Use a single space after the `#`
* At least 2 spaces before an inline `#`
* Don't describe what is already obvious
  * Ex: if you have the line `number_of_cars = 5`, don't add a comment `# Number of cars`

___
### [Outline](README.md), Next: [Chapter 4: Strings and Indexing](Chapter_04_Strings_and_Indexing.md)
