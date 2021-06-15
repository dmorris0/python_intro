# Chapter 6 Functions and Loops

Example of a built-in function: `len()`
* Functions are values:
```
>>> len

>>> type(len)

```
The name `len` can be reassigned:
```
>>> len = "Hello"
>>> len
'Hello'
>>> type(len)

```
This is a bad idea because you no longer have access to the built-in function `len()`.  Doing this in your code creates confusion, so best to avoid it.  You can regain access to the built in function with
```
>>> del len
>>> len

```
## Executing functions
Typing the name of a function does not execute it
```
>>> len
```
Rather following it with parentheses will execute the function
```
>>> len()

```
This executes `len()`, although in this case results in an error since `len()` requires exactly one argument.  Functions can require any number of arguments, including zero arguments and optional arguments.  

* Functions optionally return values and have side effects
```
>>> n_digits = len("1234")
>>> n_digits
4
>>> return_val = print("Hello")
>>> return_val

```
This latter case is a special type:
```
>>> type(return_val)

>>> print(return_val)
None
```

## Defining your own functions

Create a file called `arithmetic.py` in the current folder.  Add this text and save it.
```
def multiply(x, y):
    """ Returns the product of x and y """
    result = x * y
    return result
```
Now to use your new function, you can import it as follows:
```
>>> from arithmetic import multiply
>>> a = multiply(3, 4)
>>> a
12
```
Notice the indentation.  The body must be indented identically (except for loops inside it).  Note that spaces and tabs are not identical, and it is best to use just one or the other.  In VSCode you can set tabs to create 4 spaces, which is what I do.

The function will exit on a `return` statement and return this value.  With no `return` statement, a `None` will be returned.

Notice the documentation in triple quotes.  This starts on the line right after the function definition, and can extend to multiple lines.  This is provided to the help function as follows:
```
>>> help(multiply)
Help on function multiply in module arithmetic:

multiply(x, y)
    Returns the product of x and y

```
So it is a good idea to document each function you write in this way.  

