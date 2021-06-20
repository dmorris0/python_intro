# Chapter 9 Tuples, Lists and Dictionaries

## Tuples

### Creating Tuples
A tuple is an ordered sequence of elements:
```python
>>> my_tuple = (1,2,3)
>>> type(my_tuple)
<class 'tuple'>
```
A special tuple is the empty tuple:
```python
>>> my_empty_tuple = ()
>>> type(my_empty_tuple)
<class 'tuple'>
```
Defining tuples this way one must include commas.  The following is not a tuple:
```python
>>> my_var = (2)
>>> type(my_var)
<class 'int'>
```
In order to make a tuple of length 1, simply add a comma like this:
```python
>>> my_var = (2,)
>>> type(my_var)
<class 'tuple'>
```
Another way to create a tuple is with the `tuple` command:
```python
>>> tuple("Python")
('P', 'y', 't', 'h', 'o', 'n')
```
In this case it converts a string to a tuple.  

### Length and Indexing
Tuples have a length and can be indexed and sliced just like strings (see Chapter 4):
```python
>>> my_tuple = tuple("Python")\
>>> len(my_tuple)       # Length of tuple
6
>>> my_tuple[0]         # First element
>>> my_tuple[:1]        # Tuple containing first element
'P'
>>> my_tuple[:3]        # Tuple containing first 3 elements
('P', 'y', 't')
```
 ### Immutable
 Just like strings, tuples are immutable.  This means their elements cannot be changed, and no elements can be added or removed.

 ### Iterable
 Tuples are iterable, enabling use in loops such as `for`:
 ```python
>>> my_tuple = tuple("Python")\
>>> for letter in my_tuple:
...     print(letter.upper())
...
P
Y
T
H
O
N
```
### Packing and Unpacking
Another way to create a tuple is a comma-separated list of items:
```python
>>> xyz = 11.5, 2.3, 4.1
>>> xyz
(11.5, 2.3, 4.1)
```
Elements can be unpacked this way:
```python
>>> x, y, z = xyz
>>> x
11.5
```
And both can be done together on a single line:
```python 
>>> name, age = 'Brenda', 25
>>> name
'Brenda'
>>> age
25
```
Of course, the left and right sides must have the same number of elements.

You can return multiple elements from a function this way
```python
>>> def mult_divide(a,b):
...     return a*b, a/b
...
>>> mult_divide(4,2)
(8, 2.0)
```
___
## Lists

Like tuples, lists are ordered sequences that can be indexed and sliced.  The main difference is that lists are mutable, meaning that individual values can be changed.

### Creation
Some examples of creating lists:
```python
>>> students = ['Fred','Judy','Belinda']    # Lists use square brackets
>>> details = ['Judy','student',19]         # Lists can mix types
>>> letters = list("Python")                # Create list from string
>>> letters
['P', 'y', 't', 'h', 'o', 'n']
>>> numbers = list( range(8) )              # Create list from a range
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7]
>>> subnumbers = numbers[2::2]              # Create list by slicing another list
>>> subnumbers
[2, 4, 6]
```
### Change Elements
Elements of a list can be changed by indexing elements
```python
>>> trees = ['Elm','Birch','Oak']
>>> trees[0] = 'Pine'                       # Replace one element
>>> trees
['Pine', 'Birch', 'Oak']
>>> trees[1:4] = ['Spruce','Cedar','Carob'] # Replace multiple elements and extend
>>> trees
['Pine', 'Spruce', 'Cedar', 'Carob']
```

### `list.insert()` Method

The method `list.insert(index,value)` inserts `value` into a list at `index`.  Continuing the above example:
```python
>>> trees.insert(1, 'Maple')                # Insert at index 1
>>> trees
['Pine', 'Maple', 'Spruce', 'Cedar', 'Carob']
>>> trees.insert(20, 'Redwood')             # Inserting beyond end puts it at the end
>>> trees
['Pine', 'Maple', 'Spruce', 'Cedar', 'Carob', 'Redwood']
```
Note: `.insert()` is an in-place operation; it changes the data of the list, rather than making a copy.  The same is true for the following 3 methods:

### `list.append()` Method

The `list.append(value)` method adds `value` to the end of the list
```python
>>> trees.append('Fig')
>>> trees
['Pine', 'Maple', 'Spruce', 'Cedar', 'Carob', 'Redwood', 'Fig']
```

### `list.pop()` Method

The `list.pop()` method has an optional index argument.  With no argument is removes the last element and returns it.
```python
>>> tree = trees.pop()                      # Remove last element and return it
>>> tree
'Fig'
>>> trees
['Pine', 'Maple', 'Spruce', 'Cedar', 'Carob', 'Redwood']
>>> trees.pop(1)                            # Remove element at index 1 and return it
'Maple'
>>> trees
['Pine', 'Spruce', 'Cedar', 'Carob', 'Redwood']
```

### `list.extend()` Method

The `list.extend(list2)` extends the original list the elements of `list2`
```python
>>> trees.extend(['Apple', 'Orange'])
>>> trees
['Pine', 'Spruce', 'Cedar', 'Carob', 'Redwood', 'Apple', 'Orange']
```

### Number List Functions
The functions `sum()`, `max()` and `min()` operate on lists of numbers:
```python
>>> numbers = list( range(6) )
>>> numbers
[0, 1, 2, 3, 4, 5]
>>> sum(numbers)
15
>>> max(numbers)
5
>>> min(numbers)
0
```
### List Comprehension
List comprehension is a way to apply functions or operations on all the elements of an iterable, such as a list.  Some examples:
```python
>>> numbers = list( range(6) )
>>> cubes = [x**3 for x in numbers]
>>> cubes
[0, 1, 8, 27, 64, 125]
```
We see that `x` takes each successive value of the list, and then a new list is created from the starting operation applied to each element, here `x**3`.  

### Lists of Lists

An element of a list can be another list.  For example:
```python
>>> listx2 = [[0,1], [2,3], [4,5]]
>>> listx2
[[0, 1], [2, 3], [4, 5]]
>>> listx2[0]
[0, 1]
>>> listx2[0][1]
1
```

### Copying Lists

Assignment is not the same thing as copying.  
```python
>>> numbers = list(range(5))
>>> other = numbers             # Assignment of other to numbers
>>> other                       # Other points to the same memory as numbers
[0, 1, 2, 3, 4]
>>> numbers.append(5)
>>> other                       # If we change numbers, other also changes
[0, 1, 2, 3, 4, 5]
```
Here `numbers` is a name that points to a block of memory with a list.  With the assignment `other = numbers`, then `other` also points to this same block of memory.  So when we change the list pointed to by `numbers`, this is reflected in `others`.  This assignment has **not** copied the data in numbers.

To copy a list use slicing:
```python
>>> numbers = list(range(5))
>>> other = numbers[:]          # Here a copy is made
>>> numbers.append(5)           # Changing numbers does not affect other
>>> other
[0, 1, 2, 3, 4]
```

For lists of lists, slicing will not work for copying.  Why not?  Because a list of lists is a really a list of references to lists.  Copying a reference is not the same as copying the object.  This is called a **shallow** copy.  
```python
>>> listx2 = [[0,1], [2,3], [4,5]]
>>> list_shallow = listx2[:]        # This is a shallow copy
>>> listx2[0][0] = 10               # Changing listx2 changes list_shallow
>>> list_shallow
[[10, 1], [2, 3], [4, 5]]
```
To copy the the actual lists, you need a **deep** copy.  
```python
>>> import copy
>>> listx2 = [[0,1], [2,3], [4,5]]
>>> list_copy = copy.deepcopy(listx2)   # Deep copy
>>> listx2[0][0] = 10                   # Changing listx2 has no effect on list_copy
>>> list_copy
[[0, 1], [2, 3], [4, 5]]
```

