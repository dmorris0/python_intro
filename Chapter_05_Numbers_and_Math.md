# Chapter 5 Numbers and Math

## Integers and Floating Point Numbers
```python
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
```
* Convert strings to integers
```python
>>> int("100")
100
>>> float("200")
200.0
```
* E notation for floats
```python
>>> 1e3
1000.0
>>> 1e-3
0.001
```
* Infinity:
```python
>>> n = 2e400
>>> n
inf
>>> type(n)
<class 'float'>
```

## Arithmetic Operations

Reommended notation: use spaces between operators and digits
```python
>>> 1 + 2
3
```
Adding, Subtracting, Multiplying and Dividing floats and integers:
```python
>>> 2 + 3.0
5.0
```
```python
>>> 2 - 3.0
-1.0
```
```python
>>> 3 * 2.0
6.0
```
```python
>>> 12 / 3
4.0
```
```python
>>> int( 12 / 3 )
4
```
* Integer division `//` divides and rounds down:
```python
>>> 12 // 3
4
>>> 5.0 / 2
2.0
>>> -5 / 2
-3
```
* Divide by zero:
```python
>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
* Exponents
```python
>>> 2 ** 2
4
>>> 2 ** 2.5
5.656854249492381
>>> 4 ** 0.5
2.0
```
* Negative exponents are the same as dividing 1 by the number raised to a positive exponent
```python
>>> 2 ** -1
0.5
```
* Order of precedence:
   * Operators `*`, `/`,`//`, and `%` all have equal precendence and are higher than `+` and `-`.

* Try Exercise 5.3

* Optional: Review Section 5.4 to understand this:
```python
>>> 0.1 + 0.3
0.4
>>> 0.1 + 0.2
0.30000000000000004
```
* Rounding
```python
>>> round(2.5)
2
>>> round(3.5)
4
```
If the digit to the left of the `5` is even, then rounds down and if odd then rounds up.
```python
>>> round(1.2345, 3)

```
* Absolute number
```python
>>> abs(3)
3
>>> abs(-5.0)
-5.0
```
* Power `pow` is the same as `**` and has 2 arguments:
```python
>>> pow(3, 2)
9
```
With three arguments `pow(x, y, z)` is the same as `(x ** y) % z`
```python
>>> pow(2, 3, 3)
2
```
* Printing Numbers
```python
>>> n = 1.2468
>>> f"n is {n}"
'n is 1.2468'
>>> f"n is approximately {n:.2f}"
'n is approximately 1.25
```
Here `.2f` indicates a **fixed-point floating** number with 2 digits after the decimal place.  Notice that is is rounded as with `round()`

