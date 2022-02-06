# Appendix 1: Solving Linear Equations

This is a self-contained appendix describing how one can use Python to solve systems of linear equations.  It does not assume any experience with Python, and provides the basic steps for someone solve linear equations using use Python.  

## Problem Statement

Assume we have `N` unknown variables which we collect in a vector <img src="https://render.githubusercontent.com/render/math?math=x=[x_1,x_2,...,x_N]">.  Further assume we have `N` independent linear equations in these unknown variables.  These equations can be organized into the following standard form:

<img src="https://render.githubusercontent.com/render/math?math=Ax=b">

where `A` is a `N` X `N` square matrix containing the coefficients of `x`, and `b` is a `N` vector containing constants in these equations.  Both `A` and `b` are known.  If `A` is full rank, this matrix equation can be solved by left multiplying by the inverse of `A` to give:

<img src="https://render.githubusercontent.com/render/math?math=x=A^{-1}b">

For large matrices, this is inefficient and there are faster numerical methods that solve these equations and give the same result.  We will use one such tool available in the Numpy package.

## Set up Python

1. Ensure you have a working Python 3 install, see [Chapter 2](Chapter_02_Installation_and_IDE.md).  There's no need to install an integrated developer environment (IDE) as shown in this chapter.
2. Ensure you have Numpy installed.  If you are a more advanced Python user, it is recommended to use a virtual environment as described in [Chapter 12](Chapter_12_Virtual_Environments.md), but for simplicity you can simply install numpy (or confirm that it is installed if it already is) with the following command in the terminal:
```
$ python -m pip install numpy
```
Note: the `$` is not typed -- it simply indicates the terminal prompt, which could be something like this `PS C:\Users\dmorris` on a Windows PowerShell.  

3. Your are now ready to run Python which you can do as follows:
```
$ python
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
This creates an interactive environment with the prompt: `>>>`.  

4. Now you can import the numpy package with the command:
```
>>> import numpy as np
```
If there is an error, something went wrong installing the numpy package.  Type `exit()` to quit Python and make sure numpy successfully installs.  

## Example System of Equations

We will show how to solve a system of linear equations with an example.  Let's say you wanted to solve for three unknown parameters and your `3` X `3` `A` matrix is the following: 
```
[[ 3, -2,  0],
 [-2,  4, -1],
 [ 0, -1,  5]]
```
and your `3`-vector `b` is:
```
[ 2, -1,  1]
```
The following are the steps to do this, once you have started Python and imported Numpy (as shown above):

1. Create `A` and `b` as numpy arrays as follows:
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

2. Use Numpy to solve for the unknown vecto `x`:
```
>>> x = np.linalg.solve(A, b)
>>> x
array([0.81081081, 0.21621622, 0.24324324])
```
There you go -- you've solved for the 3 unknown parameters with a couple lines of code!  The same method will work for any number of unknowns, as long as you have the same number of equations. You can find online documentation for the [solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html) function and other Numpy functions. 

3. It is always a good idea to sanity check your result.  If we do a matrix multiplication: `Ax`, with the calculated `x`, then this should give us `b` (from the top equation).  Let's confirm this as follows:
```
>>> np.matmul(A, x)
array([ 2., -1.,  1.])
```
And yes, this is the same as the `b` vector we set above, confirming that we obtained the correct `x`.  And finally, to exit the interactive Python type:
```
>>> exit()
```
___
### [Outline](README.md)

