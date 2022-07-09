# Chapter 8: Conditional Logic and Control Flow

This chapter discusses
* Comparing 2 variables
* Using `if` statements to control flow
* Handling errors with `try` and `except`

Boolean comparators output a `True` or `False`.  The operators are:

Comparator | Example | Meaning
-- | -- | --
`>` | `a > b` | `a` is greater than `b`
`<` | `a < b` | `a` is less than `b`
`>=`| `a >= b` | `a` is greater than or equal to `b`
`<=`| `a <= b` | `a` is less than or equal to `b`
`!=`| `a != b` | `a` is not equal to `b`
`==`| `a == b` | `a` is equal to `b`

Note that the last of these is a double `==` operator.  This is is different than the assignment operator, which is a single `=` sign.  It is important not to mix these up.

Some examples:
```python
>>> 2 == 3
False
>>> 2 <= 3
True
```
Strings can be compared:
```python
>>> "a" != "c"
True
>>> "b" < "c"
True
```
Strings are ordered as they would be in a dictionary.

## Logical Operators

The logical operators are `and`, `or`, and `not`.  They combine boolean expressions and output another boolean expression.  Some examples:
```python
>>> 2 < 3 and 4 < 5
True
>>> 2 < 3 and 5 > 6
False
>>> 2 < 3 or 5 > 6
True
>>> not 2 < 3
False
```
The order of precedence can sometimes be important.  The following is the order of precedence:

|Precedence, top to bottom |
|--|
| <,>,<=,>=,==,!= |
| not |
| and |
| or |

For example:
```python
>>> False == not True
  File "<stdin>", line 1
    False == not True
             ^
SyntaxError: invalid syntax
```
This gives an error because the comparator `==` is applied before the `not`, and it does not make sense to compare `False` with `not`.  This can be addressed with parentheses:
```python
>>> False == (not True)
True
```
In most cases, to aid clarity and avoid mistakes, it is preferable to avoid relying on precedence and rather use parentheses.

## Controlling Flow of Code
An `if` statement will control the flow of execution depending on the output of a condition.  For example:
```python
>>> if 2 + 4 < 8:
...     print("We are below target")
...     print("Got to work harder")
...
We are below target
Got to work harder
```
Notice the colon after the condition.  Also, all subsequent statements that are indented will be executed if the condition is `True`.

We can add an `else` to provide a sequence of commands when the condition is `False`
```python
>>> if 9 < 8:
...     print("We are below target")
... else:
...     print("We are above target")
...
We are above target
```
In addition any number of `elif` statements, that mean "else if", can be added:
```python
>>> result = 3
>>> if result >= 4:
...     print('You did great')
... elif result >= 3: 
...     print('You did well')
... elif result >= 2:
...     print('You did average')
... elif result >= 1:
...     print('You passed')
... else:
...     print('You failed')
...
You did well
```
In all these cases, the indentation is used to indicate which expressions are executed when a condition is satisfied.

## `break` and `continue`

A `break` will immediately exit from a loop:
```python
>>> for letter in "smorgasbord":
...     if letter == 'r':  
...         break           # Quit loop when reaching 'r'
...     print(letter)
...
s
m
o
```
A `continue` will immediately skip to the next iteration of the loop:
```python
>>> for letter in "smorgasbord":
...     if letter < 'r':
...         continue        # Skip any letters < 'r'
...     print(letter)
...
s
r
s
r
```
## Errors and Exceptions

A **syntax error** is the most common error you will likely encounter as you learn Python, for example:
```python
>>> if True print('Hello')
  File "<stdin>", line 1
    if True print('Hello')
            ^
SyntaxError: invalid syntax
```
Python identifies the line with the error and indicates the first point at which the error is identified (the up-arrow). Then at the start of the bottom line identifies this error is of type: `SyntaxError`, and includes a short description.  In this case we are missing a colon `:`.  A function with a syntax error will often give an error before running.

**Exceptions** are runtime errors.  Some examples include:
```python
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 10 * new_variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'new_variable' is not defined
>>> '4' + 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> int('22.3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '22.3'
```
Notice the exception types: `ZeroDivisionError`, `NameError`, `TypeError`, and `ValueError`.  There are a variety of additional exception types which are listed [here](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).  Knowing the exception type provides a way to handle it, as explained next.

## Exception Handling

Let's say we want to ensure the user inputs an integer:
```python
>>> while True:
...     try:
...         val = int(input("Input a number: "))
...         break    # Exit while loop when we have a valid number
...     except ValueError:
...         print("Not a valid number, try again")
...
Input a number: hello
Not a valid number, try again
Input a number: 25.6
Not a valid number, try again
Input a number: 17
```
This `except ValueError:` line captures only exceptions of type `ValueError`.  If you press `Ctrl-C` instead of inputting text, the result will be:
```python
Input a number: Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
KeyboardInterrupt
```
This generates a `KeyboardInterrupt` exception which is not handled by this except and so stops the code. This is good, as typically you want `Ctrl-C` to stop execution of the code. 

Consider what would happen if we used a bare `except` with no exception type like the below, and if you pressed `Ctrl-C` at the input line:
```python
>>> while True:
...     try:
...         val = int(input("Input a number: "))
...         break    # Exit while loop when we have a valid number
...     except:
...         print("Not a valid number, try again")
...
Input a number: Not a valid number, try again
Input a number: Not a valid number, try again
Input a number: Not a valid number, try again
Input a number: 1
```
I pressed `Ctrl-C` three times, and the code kept redirecting me to input a number.  The only way I got out was to input a valid number.  If there were some actual error inside the `try:` block, then this code could get into an infinite loop that you could not stop with a `Ctrl-C`.  Usually it is best to avoid bare `except:` statements, and rather to include appropriate exception type that you plan to handle.

## More In-Depth Examples
You may wish to skip the next examples on a first reading. You can add multiple `except` lines, each with one or more different exception types.  The following are two instructive examples from [https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)
```python
>>> import sys
>>> try:
...     f = open('myfile.txt')
...     s = f.readline()
...     i = int(s.strip())
... except OSError as err:
...     print("OS error: {0}".format(err))
... except ValueError:
...     print("Could not convert data to an integer.")
... except:
...     print("Unexpected error:", sys.exc_info()[0])
...     raise
... 
```
Here each `except` handles a separate error type.  The final bare `except` handles all other types, and notice that it subsequently raises an exception with `raise`.
```python
>>> import sys
>>> for arg in sys.argv[1:]:
...     try:
...         f = open(arg, 'r')
...     except OSError:
...         print('cannot open', arg)
...     else:
...         print(arg, 'has', len(f.readlines()), 'lines')
...         f.close()
... 
```
Here `sys.argv` is a list of arguments passed to a Python file, and so is only useful as part of a Python program (and not in the interactive terminal).  This attempts to open each input argument as a file.  If it cannot open it, the `except OSError:` command causes it to display a message and go on to the next.  The `else:` block that reads the file will be executed only if the `try:` block is successful.  It is better to keep this code in its own block, rather than as part of the try block as otherwise it would be protected by the `try`-`except` pair and we may wish other exceptions to be raised if its contents are not what we expect.

___
### [Outline](../README.md), Next: [Chapter 9: Tuples, Lists and Dictionaries](Chapter_09_Tuples_Lists_and_Dictionaries.md)