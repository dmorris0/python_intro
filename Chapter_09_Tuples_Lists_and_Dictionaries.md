# Chapter 9: Tuples, Lists and Dictionaries

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
>>> my_tuple = tuple("Python")
>>> len(my_tuple)       # Length of tuple
6
>>> my_tuple[0]         # First element
'P'
>>> my_tuple[:1]        # Tuple containing first element
('P',)
>>> my_tuple[:3]        # Tuple containing first 3 elements
('P', 'y', 't')
```
 ### Immutable
 Just like strings, tuples are immutable.  This means their elements cannot be changed, and no elements can be added or removed.

 ### Iterable
 Tuples are iterable, enabling use in loops such as `for`:
 ```python
>>> my_tuple = tuple("Python")
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

### Short Diversion with the `+=` Operator

For lists which are mutable, the `+=` operator will extend a list, just like the `.extend()` method, and is an in-place operator.  For example:
```python
>>> a, b = [1, 2], [3, 4]
>>> a += b                # In-place operation extends a
>>> a
[1, 2, 3, 4]
```
For tuples, which are immutable, the `+=` operator will create a new tuple that is a combination of the base tuples and will overwrite the original tuple.  Here's an example:
```python
>>> a, b = (1, 2), (3, 4)
>>> a += b                # Automatically converted to: a = a + b
>>> a
(1, 2, 3, 4)
```
While this looks the same as for lists, Python determines that the tuple `a` has no in-place add operation and so instead converts `a += b` to `a = a + b`, which combines the two tuples and then overwrites the original tuple `a` with the combined tuple.

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
>>> listx2[0]         # Zeroth element is a list
[0, 1]
>>> listx2[0][1]      # Element 1 of zeroth list 
1
```

List comprehension can be applied to lists of lists.  For example say we wish to flatten a list of lists into a single list we can do the following:
```python
>>> list_of_lists = [[2,4,6], [1,3], [8,10,12,14]]
>>> new_list = [item for sublist in list_of_lists for item in sublist]
>>> new_list
[2, 4, 6, 1, 3, 8, 10, 12, 14]
```

### Iterate Over a List

While list comprehension operates over each element of a list, sometimes we need to do more complex operations over each element of a list.  A simple `for` loop (like we saw in Chapter 5) enables this:
```python
>>> fruit_list = ['apples','bananas','oranges']
>>> for fruit in fruit_list:
...     print(fruit)
...
apples
bananas
oranges
```
### `enumerate()` Function
In this loop there is no index, which is often a good thing, but sometimes we need an index.  This can be achieved with the `enumerate()` function which returns a tuple `(index, list_item)` when iterated.  Here is an example:
```python
>>> fruit_list = ['apples','bananas','oranges']
>>> for i,fruit in enumerate(fruit_list):
...     print(f'{i}. {fruit}')
...
0. apples
1. bananas
2. oranges
```
### `zip()` Function
If we have two (or more) lists of the same length, we can iterate over them together using the `zip()` function which collates them together into a tuple corresponding elements of each list passed into it.  Here is an example:  
```python
>>> fruit_list = ['apples','bananas','oranges']
>>> price_list = [1.5, 0.9, 2.0]
>>> for fruit,price in zip(fruit_list, price_list):
...     print(f'{fruit} cost ${price}')
...
apples cost $1.5
bananas cost $0.9
oranges cost $2.0
```
Often a better way to represent the above data is with a dictionary linking each fruit to its price, rather than two lists.  Dictionaries are described below.

### Copying Lists

**Important:** Assignment is not the same thing as copying.  
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

To copy a list use slicing or `.copy()`, for example:
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

### Sorting
A list can be sorted *in-place* using the `.sort()` method:
```python
>>> trees = ['Pine', 'Spruce', 'Cedar', 'Carob']
>>> trees.sort()
>>> trees
['Carob', 'Cedar', 'Pine', 'Spruce']
>>> numbers = [5, 2, 4, 1]
>>> numbers.sort()
>>> numbers
[1, 2, 4, 5]
```
A function can be provided as an optional argument called `key` whose output is used to sort the list.  The function must take one argument and output one value, and only the name without the parentheses is provided.  For example to sort on the length of a element, use the built-in function `len`:
```python
>>> trees = ['Pine', 'Spruce', 'Cedar', 'Carob']
>>> trees.sort(key=len)
>>> trees
['Pine', 'Cedar', 'Carob', 'Spruce']
```
You can provide a user-defined function for this too.  And a second argument `reverse` can be set to `True` to sort in reverse order.  For example, to sort in reverse order on the last letter of a name:
```python
>>> def last_letter(word):
...     return word[-1]         # Return last letter
...
>>> trees = ['Pine', 'Spruce', 'Cedar', 'Carob']
>>> trees.sort(key=last_letter, reverse=True)
>>> trees
['Cedar', 'Pine', 'Spruce', 'Carob']
```
Notice that we passed the name of the function to `key` without parentheses.

## Dictionaries

A dictionary stores element as `key-value` pairs.  To extract a `value`, one provides the key, rather than the index like in a tuple or list.  Keys and values can be of any type and any value, with the constraint that keys must be immutable. Here is an example:

```python
>>> capitals = { "United States":"Washington DC", "Canada":"Toronto", "Mexico":"Mexico City" }
>>> capitals
{'United States': 'Washington DC', 'Canada': 'Toronto', 'Mexico': 'Mexico City'}
```
Empty dictionaries can be created with
```python
>>> {}
{}
>>> dict()
{}
```

### Accessing values
Dictionaries do not have a pre-defined order, and are accessed by key:
```python
>>> capitals['Canada']
'Toronto'
```

### Add / delete an element
```python
>>> capitals['United Kingdom'] = 'London'
>>> del capitals['Canada']
>>> capitals
{'United States': 'Washington DC', 'Mexico': 'Mexico City', 'United Kingdom': 'London'}
```

### Existence of a Key
Accessing a key that does not exist gives an error:
```python
>>> capitals['Spain']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Spain'
```
The `in` keyword will check:
```python
>>> 'Brazil' in capitals
False
```
Combine this with an `if` statement like this:
```python
>>> if 'United Kingdom' in capitals:
...     print('We have a destination')
...
We have a destination
```

### Iterate over a Dictionary
To iterate over `keys` use:
```python
>>> for key in capitals:
...     print(key)
...
United States
Mexico
United Kingdom
```
To iterate and obtain both the `key` and `value` for each element use the `.items()` function:
```python
>>> for country, capital in capitals.items():
...     print(f'{capital} is the capital of {country}')
...
Washington DC is the capital of United States
Mexico City is the capital of Mexico
London is the capital of United Kingdom
```

___
### [Outline](README.md), Next: [Chapter 10: Classes](Chapter_10_Classes.md)


