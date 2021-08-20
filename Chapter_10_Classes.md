# Chapter 10: Classes

A few examples of a class called `Cat`.  First the simplest class definition:
```python
>>> class Cat:
...     pass
...
>>> a = Car()
>>> a
<__main__.Car object at 0x0000023848FB4E80>
>>> b = Car()
>>> a == b
False
```
Here `a` and `b` are instances of a `Car` class.  They differ as they are separate blocks of memory.  

Note that Python classes by convention use camelcase, namely with capital letters in each word like this: `SportsCar`.

The Python file `car.py` in the `python` folder has an example of a more involved `Car` class:
```python
class Car:
    
    n_wheels = 4
    
    def __init__(self, make):
        self.make = make
    
    def __str__(self):
        return f'{self.make} with {self.n_wheels} wheels'
    
    def my_needs(self):
        print('I need a tank of fuel')
```
Notice the 4 components.  
* The first line or lines after the `class` definition contain the class attributes.  In this case `n_wheels` is a class attribute and will be `4` for all instances of the class.
* The `__init__(self, make)` is a special function that initializes the class.  `self` is a special parameter that is automatically provided and refers to the instance itself.  The remaining parameters are provided on instantiation.
* The `__str__(self)` is a special optional function the must return a string.  This is what `print()` receives when it is called on a class instance.
* The `my_needs(self)` function is a method of this class.  

To try out this class, copy and paste the above lines into an interactive terminal.  They try the following:
```python
>>> car1 = Car('Ford')
```
We have created a `Car` instance with make being `Ford`.  Now the following function calls the `__str__` method:
```python
>>> print(car1)
Ford with 4 wheels
```
We can also call other methods:
```python
>>> car1.my_needs()
I need a tank of fuel
```

## Inheritance

A child class inherits the attributes and methods of its parent class.  The child class can override these attributes and methods, and it can add additional attributes and methods.  The following is a simple example from the `car.py` file:
```python
class ElectricCar(Car):

    def my_needs(self):
        print(f'I need a {self.make} supercharger')
```
The command `class ElectricCar(Car)` causes the `ElectricCar` class to inherit all the attributes and methods of the `Car` class.  Within this class definition we have re-defined one of the methods `my_needs()`.  This overrides the method of the same name defined in the parent class.  Let's try it out by copy and pasting the above into your interactive terminal, and then doing the following:
```python
>>> car2 = ElectricCar('Tesla')
>>> print(car2)
Tesla with 4 wheels
>>> car2.my_needs()
I need a Tesla supercharger
```
Notice that the `my_needs()` function is defined by the child class.

The `isintance` method shows that `car2` is both a `Car` and an `ElectricCar`:
```python
>>> isinstance(car2,Car)
True
>>> isinstance(car2,ElectricCar)
True
>>> isinstance(car1,ElectricCar)
False
```


___
### [Outline](README.md), Next: [Chapter 11: Modules](Chapter_11_Modules.md)

