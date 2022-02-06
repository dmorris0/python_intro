# Appendix 1: Solving Linear Equations

This is a self-contained appendix describing how one can use Python to solve systems of linear equations.  It does not assume any experience with Python, and provides the basic steps for someone solve linear equations using use Python.  

___
## 1. Problem Statement

Assume we have `N` unknown variables which we collect in a vector <img src="https://render.githubusercontent.com/render/math?math=x=[x_1,x_2,...,x_N]">.  Further assume we have `N` independent linear equations in these unknown variables.  These equations can be organized into the following standard form:

<img src="https://render.githubusercontent.com/render/math?math=Ax=b">

where `A` is a `N` X `N` square matrix containing the coefficients of `x`, and `b` is a length `N` vector containing constants in these equations.  Both `A` and `b` are known.  If `A` is full rank, this matrix equation can be solved by left multiplying by the inverse of `A` to give:

<img src="https://render.githubusercontent.com/render/math?math=x=A^{-1}b">

For large matrices, this is inefficient and there are faster numerical methods that solve this equation and give the same result.  We will use one such tool available in the Numpy package.
___
## 2. Set up Python

1. Ensure you have Python 3 installed.  In Windows, type `python` in a PowerShell, and if it is not installed, this will take you to the Windows Store to install Python.
2. Next, ensure you have Numpy installed.  If you are a more advanced Python user, installing it in a virtual environments is recommended as described in [Chapter 12](Chapter_12_Virtual_Environments.md), but for simplicity you can directly install Numpy (or confirm that it is already installed) with the following command in a terminal:
```
$ python -m pip install numpy
```
Note: the `$` is not typed -- it simply indicates the terminal prompt, which could be something like this `PS C:\Users\dmorris` in a Windows PowerShell.  

3. You are now ready to run Python which you can do as follows:
```
$ python
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
This creates an interactive environment with a "`>>>`"  prompt.   

4. Next make sure you can import the numpy package with the command:
```
>>> import numpy as np
```
If there is an error, likely something went wrong installing Numpy.  Type `exit()` to quit Python and make sure Numpy is successfully installed.  

___
## 3. Example System of Equations

We will show how to solve a system of linear equations with an example.  Let's say you wanted to solve for three unknown parameters and your `A` matrix, which must be `3` X `3`, is the following: 
```
[[ 3, -2,  0],
 [-2,  4, -1],
 [ 0, -1,  5]]
```
and your `3`-vector `b` is:
```
[ 2, -1,  1]
```
___
## 4. Steps to Solve for `x`
The following are the steps to solve for `x`.  

1. If Python is not running, start it and import Numpy with:
```
$ python
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
```

2. Create `A` and `b` as Numpy arrays:
```
>>> A = np.array( [[3,-2,0],[-2,4,-1],[0,-1,5]] )
>>> b = np.array( [2,-1,1] )
```
You can confirm that they are entered correctly by typing the variable names like this:
```
>>> A
array([[ 3, -2,  0],
       [-2,  4, -1],
       [ 0, -1,  5]])
>>> b
array([ 2, -1,  1])
```

3. Use Numpy to solve for the unknown vector `x`:
```
>>> x = np.linalg.solve(A, b)
>>> x
array([0.81081081, 0.21621622, 0.24324324])
```
There you go -- you've solved for the 3 unknown parameters with a couple lines of code!  The same method will work for `N` of any size, as long as `A` and `b` are the correct size. Additional documentation for [solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html) and other Numpy functions is online.

4. It is always a good idea to sanity check your result.  If we do a matrix multiplication: `Ax`, with the calculated `x`, then this should give us `b` (from the top equation).  Let's confirm this as follows:
```
>>> np.matmul(A, x)
array([ 2., -1.,  1.])
```
And yes, this is the same as the `b` vector we set above, confirming that we obtained the correct `x`.  Finally, to exit the interactive Python type:
```
>>> exit()
```
___
### [Outline](README.md)

