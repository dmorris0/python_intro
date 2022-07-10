# Chapter 5: Numbers and Math

## Integers and Floating Point Numbers
Numbers without decimals default to integers:
```python
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
```
* Convert strings to numbers
```python
>>> int("100")
100
>>> float("200")
200.0
```
* `e` notation for floats
```python
>>> 1e3
1000.0
>>> 1e-3
0.001
```
* Infinity:
```python
>>> big = float("inf")
>>> big
inf
>>> n = 2e400
>>> n
inf
>>> type(n)
<class 'float'>
```

## Arithmetic Operations

Recommended notation: use spaces between operators and digits
```python
>>> 1 + 2
3
```
Adding, Subtracting, Multiplying and Dividing floats and integers.  When one number is a float the output will be a float. 
```python
>>> 2 + 3.0
5.0
>>> 2 - 3.0
-1.0
>>> 3 * 2.0
6.0
```
Also division creates a float:
```python
>>> 12 / 3
4.0
```
This can be cast to an integer:
```python
>>> int( 12 / 3 )
4
```
But integer division `//` is preferable and it rounds down:
```python
>>> 12 // 3
4
>>> 5.0 // 2
2.0
>>> -5 // 2
-3
```
* Divide by zero:
```python
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
* Exponents: `a ** b` means `a` raised to the power of `b`
```python
>>> 2 ** 2
4
>>> 2 ** 2.5
5.656854249492381
>>> 4 ** 0.5
2.0
```
* Negative exponents work as expected (i.e. 1 over the result of a positive exponent)
```python
>>> 2 ** -1
0.5
```
* Order of precedence:
   * Operators `*`, `/`,`//`, and `%` all have equal precendence and are higher than `+` and `-`.

* Optional: Review Section 5.4 of the book to understand this:
```python
>>> 0.1 + 0.3
0.4
>>> 0.1 + 0.2
0.30000000000000004
```
* Rounding for numbers ending in the digit `5` 
```python
>>> round(2.5)        # Round down if digit to the left is even
2
>>> round(3.5)        # Round up if digit to the left is odd
4
```
If the digit to the left of the `5` is even, then rounds down and if odd then rounds up.  Try this example:
```python
>>> round(1.2345, 3)
```
* Absolute numbers
```python
>>> abs(3)
3
>>> abs(-5.0)
5.0
```
* The modulo operator: `%`.  In the expression `y % x`, `y` is divided by `x` the remainder is returned.  This is useful for turning a large number `y` into an output from `0` to `x-1`
```
>>> 26 % 8
2
``` 
* Power `pow` is the same as `**` and has 2 arguments:
```python
>>> pow(3, 2)
9
```
With three arguments `pow(x, y, z)` is the same as `(x ** y) % z`, where `%` is the modulo:
```python
>>> pow(2, 3, 3)
2
```
* Printing numbers with `f`-strings is convenient.  Precede the first quote with an `f` and use curly braces to insert variables and notation:
```python
>>> n = 1.2468
>>> f"n is {n}"
'n is 1.2468'
>>> f"n is approximately {n:.2f}"
'n is approximately 1.25
```
Here `.2f` indicates a **fixed-point floating** number with 2 digits after the decimal place.  Notice that is is rounded as with `round()`

## Exercise: Row and Column Indexing an Image

Consider an image with height `H` and width `W`.  Now index all the pixels linearly, starting with the first row, then the second row and on.  The pixel index, `p`, will have `W*H` values in the range `0` to `H*W-1` inclusive.  Now write an expression that transforms the index `p` into a tuple `(r,c)` where `r` is the row index and `c` the column index.  Hint: the only operators you need are `%` and `//`.  When you have it, try it out on pixel indices from a `6x8` image and confirm that it works.  Here are the pixel indices as well as row and column indices so you can check your code:
```
   c: 0   1   2   3   4   5   6   7
r    ------------------------------ 
0  [[ 0,  1,  2,  3,  4,  5,  6,  7],
1   [ 8,  9, 10, 11, 12, 13, 14, 15],
2   [16, 17, 18, 19, 20, 21, 22, 23],
3   [24, 25, 26, 27, 28, 29, 30, 31],
4   [32, 33, 34, 35, 36, 37, 38, 39],
5   [40, 41, 42, 43, 44, 45, 46, 47]]
```

___
### [Outline](../README.md), Next: [Chapter 6: Functions and Loops](Chapter_06_Functions_and_Loops.md)

