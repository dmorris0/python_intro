# Chapter 11: Modules and Packages

Writing all your Python functions in a single file quickly becomes impractical.  

It is much preferable to organize your code in files or **modules**, as each file is called.  A group of files in a folder (and subfolders) can be made into a **package**.  

___
## Create a Module

Let's dive in by creating a module.  First select `New File` in the `File` menu of VSCode.  Then save it as `simple.py` in a folder called `test_module` which can be located whereever you like on your computer.  

Now add some functions to module `simple.py` such as the following:
```python
def replicate(mystr, ntimes):
    return mystr * ntimes

def concat( str1, str2):
    return str1 + str2
```
Save this file as a `.py` file, not as a `.txt` file.  You're done -- you've created a module.

___
## Importing from a Module

There are three ways to import from a module:

| Module Import Method | Description |
| ---    | ---         |
| `import <module_name>` | Imports into namespace `<module_name>` |
| `import <module_name> as <other_name>` | Imports into namespace `<other_name>` |
| `from <module_name> import <item_name>` | Imports selected items into the current namespace | 

The key concept is the **namespace** of a module.  If you have two functions with the same name, they will conflict with each other, and one will supercede the other.  This would be a problem if a function in a module that you import has the same name as one of your functions.  Python avoids this by importing each module into its own namespace, which by default is the name of the module.  

### Using `import <module_name>`
Let's try it out.  Create a new file called `run.py` and save it in the `test_module` folder.  Then try importing and using functions from `simple.py`.  Here are some attempts you can make:
```python
import simple

print(replicate('Hello',3))
print(concat('Short','Tall'))
```
Run your module by bringing `run.py` to the foreground, pressing `f5` and selecting `Python File`.  Does it work?  You should get an error:
```python
Exception has occurred: NameError
name 'replicate' is not defined
  File "C:\Users\morri\source\test\run.py", line 3, in <module>
    print(replicate('hello',3))
```
Our error is that `replicate` is not defined.  This is because when we call `import simple`, replicate will be in the `simple` namespace.  Try modifying your code to call `simple.replicate()` like this and run it:
```python
import simple

print(simple.replicate('Hello',3))
print(simple.concat('Short','Tall'))
```

### Using `import <module_name> as <other_name>`
Sometimes it is useful to rename a namespace.  One reason is to shorten the namespace, and another could be to easily switch between modules with different names but the same functions.  Let's try that by changing your code in `run.py`:
```python
import simple as sim

print(sim.replicate('Short',4))
print(sim.concat('Short','Tall'))
```

### Using `from <module_name> import <item_name>`
The third way to import is to import selected items directly into the current namespace.  Try the following:
```python
from simple import replicate

print(replicate('Short',4))
print(concat('Short','Tall'))
```
You can now call `replicate()` directly.  But you should get an error with the `concat()` function which you haven't imported.  You will have to import it as well like this:
```python
from simple import replicate, concat

print(replicate('Short',4))
print(concat('Short','Tall'))
```

These examples showed importing functions, and the command is identical to import a class.  

## Packages

A package is a folder containing modules and possibly subfolders containing more modules.  Here's an example of a single folder package called `my_package`:
```
my_package/
    |-- __init__.py
    |-- module1.py
    |-- module2.py
```
Notice that the `my_package` folder includes a file `__init__.py`, which can be empty or include code to specify which modules and items to include.  Here we will only consider the empty case which is needed for Python to interpret the `my_package` folder as a package.  

Let's create an example package.  First create a folder to work in called `testing`, and within this create a folder called `my_package`.  Also within testing create your Python script to test your package with called `main.py`.  The structure should look like this:
```
testing/
    |-- main.py
    |-- my_package/
            |-- __init__.py
            |-- module1.py
            |-- module2.py
```
In the `my_package` folder create an empty file called `__init__.py`, and two modules as follows.  In `module1.py` put the code:
```python
def start_car():
    print('Car is started')
```
In `module2.py` put the code:
```python
def drive_car():
    print('Driving')
```
Now we are ready to start importing the package.
___
### Importing a package
There are 4 ways to import from a package
| Package Import Method | Description |
| ---    | ---         |
| `import <package_name>` | Imports into namespace `<package_name>` |
| `import <package_name> as <other_name>` | Imports into namespace `<other_name>` |
| `from <package_name> import <module_name>` | Imports selected module into `<module_name>` namespace |
| `from <package_name> import <module_name> as <other_name>` | Imports selected module into `<other_name>` namespace |

Try each of these import methods with your new package.  To get you started, here is the first import method as part of `main.py`:
```python
import my_package

my_package.module1.start_car()
my_package.module2.drive_car()
```
Notice that the namespaces need to be explicitly used to access the functions in the modules.

Now adjust `main.py` to successfully use each of the following import commands:
```python
import my_package as mp
```
```python
from my_package import module1, module2
```
```python
from my_package import module1 as m1, module2 as m2
```
```python
from my_package.module1 import start_car
from my_package.module2 import drive_car
```

### Sub-packages
It is easy to add a sub-package to our package.  Simply add a subfolder and module like this:
```
testing/
    |-- main.py
    |-- my_package/
            |-- __init__.py
            |-- module1.py
            |-- module2.py
            |-- sub_package/
                    |-- __init__.py
                    |-- module3.py
```
Let `module3.py` contain the code:
```python
def stop_car():
    print('Car stopped')
```
Now add an appropriate import line to `main.py` so that you can call the function `stop_car()`.

It is straightforward to add additional folders and modules to build up complex packages.  It is good practise to keep each module small as this increases flexibility, portability and readability.

___
### [Outline](README.md), Next: [Chapter 16: Virtual Environments](Chapter_16_Virtual_Environments.md)

