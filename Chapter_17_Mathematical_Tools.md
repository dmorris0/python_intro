# Chapter 17: Mathematical Tools

One of the main reasons Python is so popular is that a vast array of tools easily available and usable directly in the language.  This chapter introduces some key some mathematical packages useful for data science and engineering.  Each tool has its own extensive documentation, and the goal of this chapter is just to motivate you to explore and use these packages.

**Numpy** is mathematical package that supports multidimensional arrays and operations on them such as matrix multiplication and linear algebra, see: [https://numpy.org/doc/](https://numpy.org/doc/).  All of the other packages described here rely on Numpy.  It is important to be familiar with multidimensional arrays and various ways they can be manipulated and accessed.

**Scipy** is a collection of mathematical and statistical tools built on Numpy.  Tools include various representations for rotations, as well as clustering, interpolation, sparse arrays, and statistical distributions.   Documentation is available here: [https://docs.scipy.org/doc/scipy/tutorial/general.html](https://docs.scipy.org/doc/scipy/tutorial/general.html).  

**Matplotlib** is a powerful toolbox for 2D and 3D plotting, see: [https://matplotlib.org/](https://matplotlib.org/).  

**OpenCV** provides many image processing and computer vision tools.  While written in C++, it provides a fairly extensive Python interface, enabling it to be used as a Python toolbox, see: [https://docs.opencv.org/4.5.3/](https://docs.opencv.org/4.5.3/).



## Installation and Help

It is best to install these tools in a virtual environment, see [Chapter 16](Chapter_16_Virtual_Environment.md).  First **activate** your virtual environment and then, from the shell command line, install them with
```
python -m pip install numpy scipy matplotlib opencv-python
```
If a package is already installed, this will simply skip it.  Also, any packages that are prerequisites will be installed. 

Now, after the packages are installed they can be accessed by running Python and using the `import` command as explained in [Chapter 11: Modules and Packages](Chapter_11_Modules_and_Packages.md).  For example, Numpy is usually imported with
```python
>>> import numpy as np
```
Besides online documentation, you can get documentation in your interactive terminal with the `help()` function:
```python
>>> help(np.stack)
```
This will give details on usage of the Numpy `stack()` function.  This is a good way to determine what arguments a function needs.

## Arrays

Arrays provide significant computational efficiencies over lists.  Consider various ways to represent 3D points, such as those collected from a lidar.  A single point could be represented as a class with a `.x`, `.y`, `.z`, or as a list with 3 elements or as a 1D numpy array with 3 elements.  A point cloud could then be either a list of points or a 2D numpy array which stacks 1D point arrays.  Performing an operation over all the points, such as rotating them, could be done by iterating over the list or else as a matrix multiplication applied to the array.  Both are equivalent mathematically, and lists are more flexible, but array operations are faster.  For operations on just a few points (10s or so), which representation you use does not make too much difference.  When there are 10,000 or 100,000 points, which could be a single lidar scan, then array operations could be orders of magnitude faster.  In addition, Numpy and other packages supply operations that are very efficient over arrays and much slower over lists.

Let's do a simple example to compare a list operation with an array operation.  First, let's represent a collection of four 3D points as a list:
```python
>>> point_list = [[1.,0.,0.],[1.,2.,1.],[3.,0.,1.],[4.,2.,0.]]
>>> point_list
[[1.0, 0.0, 0.0], [1.0, 2.0, 1.0], [3.0, 0.0, 1.0], [4.0, 2.0, 0.0]]
```
To add `1` to each element you can use list comprehension:
```python
>>> new_point_list = [ [x[0]+1,x[1]+1,x[2]+1] for x in point_list]
>>> new_point_list
[[2.0, 1.0, 1.0], [2.0, 3.0, 2.0], [4.0, 1.0, 2.0], [5.0, 3.0, 1.0]]
```
Clearly that is a little awkward, besides being slow for long lists.  

Now lets convert our list of lists to a Numpy array:
```python
>>> import numpy as np
>>>
>>> point_array = np.asarray(point_list)
>>> point_array
array([[1., 0., 0.],
       [1., 2., 1.],
       [3., 0., 1.],
       [4., 2., 0.]])
```
Our points have been stored as a 2D array with each row being a point and stacked vertically.  Now let's add `1` to each element:
```python
>>> new_point_array = point_array + 1
>>> new_point_array
array([[2., 1., 1.],
       [2., 3., 2.],
       [4., 1., 2.],
       [5., 3., 1.]])
```
Much easier eh?  And faster to boot!

## Array Indexing

The same indexing and slicing that we saw used for strings is available for each dimension of Numpy arrays.  Thus, for example we have:
```python
>>> new_point_array[0,1]
1.0
>>> new_point_array[0,:]
array([2., 1., 1.])
>>> new_point_array[:,0]
array([2., 2., 4., 5.])
```
Notice that the slices are returned as 1D arrays.  There are many more details to learn about indexing and adding dimensions to array which you can find in the official documentation: [https://numpy.org/doc/stable/reference/arrays.indexing.html](https://numpy.org/doc/stable/reference/arrays.indexing.html).  I strongly recommend you review this page. 

## Rotations

A common operation we will need is to rotate points, and these are best done using arrays.  Scipy has a rotation class that can read in rotations defined in multiple formats including Euler angles, rotation matrices and quaternions.  Its internal representation is hidden, but it can display a rotation in any of these formats.  Official documentation is [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html?highlight=rotation#scipy.spatial.transform.Rotation).  Let's try it out.
```python
>>> from scipy.spatial.transform import Rotation as R
>>>
>>> rot = R.from_euler('XYZ',[0,0,45],degrees=True)
>>> rot
<scipy.spatial.transform.rotation.Rotation object at 0x00000182D609E210>
```
We can view the rotation in various representations like this:
```python
>>> rot.as_euler('XYZ')
array([0.        , 0.        , 0.78539816])
>>> rot.as_matrix()
array([[ 0.70710678, -0.70710678,  0.        ],
       [ 0.70710678,  0.70710678,  0.        ],
       [ 0.        ,  0.        ,  1.        ]])
```
To actually rotate points, we could extract a rotation matrix and multiply a 2D array of points like this:
```python
>>> np.matmul( rot.as_matrix(), point_array.T )
array([[ 0.70710678, -0.70710678,  2.12132034,  1.41421356],
       [ 0.70710678,  2.12132034,  2.12132034,  4.24264069],
       [ 0.        ,  1.        ,  1.        ,  0.        ]])
```
Here we have used the Numpy `matmul()` function to do matrix multiplication.  We've also applied `.T` to the `point_array` to transpose it so that points are columns before we multiply by `rot`.  You may wish to transpose the result with a `.T` so that the output is put back in row format.

Now a simpler and preferred way to rotate the points is to let the Scipy class itself apply the rotation to raw point array like this:
```python
>>> rot.apply(point_array)
array([[ 0.70710678,  0.70710678,  0.        ],
       [-0.70710678,  2.12132034,  1.        ],
       [ 2.12132034,  2.12132034,  1.        ],
       [ 1.41421356,  4.24264069,  0.        ]])
```
This rotates each point, stored as a length-3 row, and keeps it in the same row format.

## Images

Images are another data type for which Numpy arrays are useful.  We will use OpenCV to read and process an image.  

```python
>>> img = cv.imread('source/repos/python_intro/.Images/book.png')
```
Here I have provided the full path from where Python is running to the `book.png` image in this repo.  You'll need to adjust the path to point to this image from where you are running Python.  Now let's examine the image we just read in:
```python
>>> type(img)
<class 'numpy.ndarray'>
```
We can see it is a Numpy array.  If you instead got `<class 'NoneType'>`, then the `imread()` function failed to read in the image; most likely because you gave it the wrong path.  Correct your path and read in the image.  To determine where Python is running from you can do:
```python
>>> import os
>>> os.getcwd()
'C:\\Users\\morri'
```
I assume you have successfully read in the image, and it is a `numpy.ndarray`.  Let's examine its size and type:
```python
>>> img.shape
(247, 160, 3)
>>> img.dtype
dtype('uint8')
```
We see that it is a 3D array; the `.shape` is a tuple with array dimensions, in this case: (height,width,nchannels).  The channels are (blue, green, red), as this is the default format for OpenCV, which differs from the more usual (red, green, blue) format.  The data type is an unsigned 8-bit type (`uint8`) which stores numbers from 0 to 255 inclusive.  We can extract the 3 components of a sample single pixel as follows:
```python
>>> img[22,28]
array([212, 187, 143], dtype=uint8)
```
These three values are the (blue, green, red) values for that pixel.  Review Numpy [indexing](https://numpy.org/doc/stable/reference/arrays.indexing.html) if this isn't clear.

Let's say our goal is to find the horizontal image gradient of the grayscale version of this image.  Here are the steps we would take.
```python
>>> img = img.astype(np.float32) / 255 
```
This converts to 32-bit floating point array and scales to a range of 0 to 1, which is the usual range for floating point images.  It is best to use floating point rather than unsigned integers because the output range can be negative or could be larger than the maximum `uint8` value of 255.
```python
>>> img.dtype
dtype('float32')
```

Next, convert the image to grayscale with `cvtColor`, which is a general purpose colorspace transformation utility:
```python
>>> gimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
```
This grayscale image is the same size, except with a single channel:
```python
>>> gimg.shape
(247, 160)
```
Finally, let's apply a Sobel operator to obtain the image gradient in x:
```python
>>> gx = cv.Sobel(gimg,cv.CV_32F,1,0,ksize=5)
```
To see the meaning of the parameters, use: `help(cv.Sobel)`


## Plotting

OpenCV has some graphical display functions including showing images.  For instance:
```python
>>> cv.imshow('Image',img)
>>> cv.waitKey(2)
```
This will show an image in a window:

![Image](.Images/show_book.png)

When you are done, clear it with:
```python
>>> cv.destroyAllWindows()
```

More sophisticated plotting is available with Matplotlib.  Here is an example using Matplotlib to plot the image gradient image, `gx`, along with a colorbar:

```python
>>> import matplotlib.pyplot as plt
>>>
>>> fig = plt.figure(num='Image Gradient')
>>> ax = fig.subplots(1,1)
>>> pcm = ax.imshow(gx, cmap='gray')
>>> ax.axis('off')
>>> plt.title('Horizontal Gradient')
>>> cbax = fig.add_axes([0.8, 0.1, 0.05, 0.8])
>>> plt.colorbar(pcm, cax=cbax)
>>> plt.show()
```
The result is an image like this:

![Image Gradient](.Images/sobel.png)

There is extensive documentation at [matplotlib.org/](matplotlib.org/) with many examples that are easily findable with a simple search.

## Broadcasting

Our final topic is that of broadcasting in Numpy.  This enables efficient repetitive operations on arrays.  But before describing it, let's review elementwise operations.  Start with two arrays of points:
```python
>>> import numpy as np
>>> points = np.array([[1.,0.,0.],[1.,2.,1.],[3.,0.,1.],[4.,2.,0.]])
>>> points
array([[1., 0., 0.],
       [1., 2., 1.],
       [3., 0., 1.],
       [4., 2., 0.]])
>>> opoints = np.flip(points,axis=0)
>>> opoints
array([[4., 2., 0.],
       [3., 0., 1.],
       [1., 2., 1.],
       [1., 0., 0.]])
```
If we add or multiply `points` and `opoints`, these operations are done elementwise.  For example:
```python
>>> spoints = points + opoints
>>> spoints
array([[5., 2., 0.],
       [4., 2., 2.],
       [4., 2., 2.],
       [5., 2., 0.]])
```
For this to operate elementwise, it is important that `points` and `opoints` are the same size.  Now, let's say we want to translate `spoints` by a single 3-vector:
```
>>> t = np.array([1.,4.,9.]) 
```
How might we add `t` to `spoints`?  

One way would be to stack 4 copies of `t` along `axis=0` to create a new `4 X 3` matrix and then do an elementwise addition.  For small arrays this is okay, but can be quite inefficient for large arrays.  A better way is through **broadcasting**.  

I will describe broadcasting for adding two `N` dimensional arrays `A` and `B`, although broadcasting also applies to other elementwise operations like multiplication and division.  To add `A` and `B`, the size of each corresponding dimension must be the same **OR** if any dimension sizes differ, then one of the sizes must be 1.  What happens is that `A` and `B` are replicated along any singleton dimension to the size of the other.  

Let's look at some examples
```python
>>> A = np.eye(3)
>>> A
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> B = 2*np.arange(3)[:,None]
>>> B
array([[0],
       [2],
       [4]])
```
The `None` is added to create an extra dimension for the vector. Now let's add these arrays:
```python
>>> C = A + B
>>> C
array([[1., 0., 0.],
       [2., 3., 2.],
       [4., 4., 5.]])
```
To see what happened, let's compare the shapes of `A`: `(3,3)`, and `B`: `(3,1)`.  Both have the same size for dimension 0, but for dimension 1, `A` has size 3 while `B` has size 1.  This means `B` will be replicated along dimension 1.  That is, the above gives the same result as:
```python
>>> C = A + np.repeat(B,3,axis=1)
>>> C
array([[1., 0., 0.],
       [2., 3., 2.],
       [4., 4., 5.]])
```
Using broadcasting this can be done more efficiently and without allocated extra temporary memory with the `repeat()` method.   And broadcasting works for arrays of any number of dimensions.  

There is one more detail.  If `A` or `B` has fewer dimensions than the other, then additional leading dimensions of size 1 are added so that both arrays have the same number of dimensions.  Let's consider some examples and whether `A` and `B` can be broadcast to create `C`:

| `A.shape` | `B.shape` | `C.shape` or invalid |
| --- |--- | --- |
| `(6,4,2)` | `(6,1,2)` | `(6,4,2)` |
| `(4,2,5)` | `(4,3,5)` | invalid [Dimension 1 has a `2` and `3`] |
| `(3,1,2,6)` | `(3,5,2,1)` | `(3,5,2,6)` |
| `(5,4)` | `(3,5,1)` | `(3,5,4)` [A leading 1 is added to `(5,4) --> (1,5,4)`] |
| `(4,5)` | `(4,5,1)` | invalid [Adding a leading dimension to `A` gives size `(1,4,5)`]

Now let's return to our task of translating `spoints` with `t`.  
```python
>>> spoints = np.array([[5., 2., 0.], [4., 2., 2.], [4., 2., 2.], [5., 2., 0.]])
>>> spoints
array([[5., 2., 0.],
       [4., 2., 2.],
       [4., 2., 2.],
       [5., 2., 0.]])
>>> t = np.array([1.,4.,9.]) 
>>> t
array([1., 4., 9.])
```
It should now be clear what we can simply add them:
```python
>>> npoints = spoints + t
>>> npoints
array([[ 6.,  6.,  9.],
       [ 5.,  6., 11.],
       [ 5.,  6., 11.],
       [ 6.,  6.,  9.]])
```
What is happening here?  `spoints` is size `(4,3)` while `t` is size `(3)`.  When added, `t` is first converted to size `(1,3)`, and then replicated four times along the first dimension and then added.  Thus each of the four 3D points is translated by `t` by leveraging broadcasting.


___
### [Outline](README.md), Next: [Chapter 18: Conclusion](Chapter_18_Conclusion.md)

