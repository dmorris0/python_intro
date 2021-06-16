# Chapter 6 Functions and Loops

Example of a built-in function: `len()`
* Functions are values:
```python
>>> len
<built-in function len>
>>> type(len)
<class 'builtin_function_or_method'>
```
The name `len` can be reassigned:
```python
>>> len = "Hello"
>>> len
'Hello'
>>> type(len)
<class 'str'>
```
This is a bad idea because you no longer have access to the built-in function `len()`.  Doing this in your code creates confusion, so best to avoid it.  You can regain access to the built in function with
```python
>>> del len
>>> len
<built-in function len>
```
## Executing functions
Typing the name of a function does not execute it
```python
>>> len
<built-in function len>
```
Rather following it with parentheses will execute the function
```python
>>> len()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: len() takes exactly one argument (0 given)
```
This executes `len()`, although in this case results in an error since `len()` requires exactly one argument.  Functions can require any number of arguments, including zero arguments and optional arguments.  

* Functions optionally return values and have side effects
```python
>>> n_digits = len("1234")
>>> n_digits
4
>>> return_val = print("Hello")
>>> return_val

```
This latter case is a special type:
```python
>>> type(return_val)
<class 'NoneType'>
>>> print(return_val)
None
```

## Defining your own functions

Create a file called `arithmetic.py` in the current folder.  Add this text and save it.
```python
def multiply(x, y):
    """ Returns the product of x and y """
    result = x * y
    return result    
```
Now to use your new function, you can import it as follows:
```python
>>> from arithmetic import multiply
>>> a = multiply(3, 4)
>>> a
12
```
Notice the indentation.  The body must be indented identically (except for loops inside it).  Note that spaces and tabs are not identical, and it is best to use just one or the other.  In VSCode I set tabs to create 4 spaces by clicking on the `Spaces` or `Tabs` indicator on the bottom bar, and then selecting `Indent Using Spaces`, and then selecting the number of spaces:

![Spaces Indentation](.Images/indentation.png)

The function will exit on a `return` statement and return this value.  With no `return` statement, a `None` will be returned.

Notice the documentation in triple quotes.  This starts on the line right after the function definition, and can extend to multiple lines.  This is provided to the help function as follows:
```python
>>> help(multiply)
Help on function multiply in module arithmetic:

multiply(x, y)
    Returns the product of x and y

```
So it is a good idea to document each function you write in this way.  For functions with many or complicated arguments, add explanations for each argument.

