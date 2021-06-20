# Chapter 8 Conditional Logic and Control Flow

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

|Precendence Order, top to bottom |
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

## Constrolling Flow of Code
An `if` statement will control the flow of execution depending on the output of a condition.  For example:
```python
>>> if 2 + 4 < 8:
...     print("We are below target")
...     print("Got to work harder")
...
We are below target
Got to work harder
```
Notice the colon after the condition.  Also all subsequent statements that are indented will be executed if the condition is `True`.

We can add an `else` to provide a sequence of commands when the condition is `False`
```python
>>> if 9 < 8:
...     print("We are below target")
... else:
...     print("We are above target")
...
We are above target
```
In addition any number of `elif` statements, that mean `else if`, can be added:
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
## Exceptions

