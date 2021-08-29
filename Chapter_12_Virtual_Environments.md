# Chapter 12: Virtual Environments

## Why Virtual Environments?

Python leaves much of its functionality to libraries.  Python code will import a library, or component of a library, and then can use it within the following lines of code.  Now most of these libraries do not come with the base Python install, but are part of packages that need to be installed before use.  Installing packages is simple, and to it is easy to obtain enormous functionality with just a few commands.

While this availability of a vast number of packages is the power of Python, it also creates compatibility problems.  Packages have many versions, and many versions of many packages are not compatible with each other.  To some extent, version compatibility can be handled by the installer, but package incompatibility means there are certain packages that cannot be installed at the same time.

The consequence of this incompatibility dilemma is that it is best that you do **not** install Python packages directly in the base environment.  Instead, create multiple separate environments, and install the packages you need within each environment.  There are tools for creating what are called *virtual environments* and easily switching between them.  Instructions for one method are given below. 

## Create a Virtual Environment

Likely you will create multiple virtual environments, so create a folder to store them.  I typically create a folder called `envs` in my `home` folder or in my `source` folder (depending if I'm in Linux or Windows).  Use `cd` to enter this folder in your terminal and then create a virtual environment with:
```
PS C:\Users\morri\source\envs> python -m venv av
```
This command is in Windows PowerShell, but the same command works in other systems, with the exception that you may need to call `python3` rather than `python`.  This will create a virtual environment called `av`.  If you look in your `envs` folder you will see an `av` folder that contains details of the `av` virtual environment.  

## Activate a Virtual Environment

To use a Virtual Environment you must activate it.  The `activate` script is located here: `envs/av/Scripts/activate`.  Simply call this script to start your environment.  For example, if you are located in the folder containing the `envs` folder, simply type:
```
PS C:\Users\morri\source> ./envs/av/Scripts/activate
(av) PS C:\Users\morri\source>
```
In Linux you would type: `source envs/av/Scripts/activate`.  Notice that once a virtual environment has been activated, each line with begin with the environment name in parentheses.  This tells you that if you install python packages, they will be installed for that virtual environment, and if you start Python, you'll be starting in that environment.

Note: PowerShell by default does not permit running scripts, and may give you an error saying scripts are disabled for the system.  A page describing this issue is here: https://adamtheautomator.com/run-powershell-script/.  In summary, you can enable scripts as follows:
1. Run a PowerShell with administrative priviledges
2. Call this command: `Set-ExecutionPolicy RemoteSigned`

After doing this you should be able to activate your virtual environment.

When you are done with your environment, you can either activate another environment, or can deactivate it with:
```
(av) PS C:\Users\morri\source> deactivate
PS C:\Users\morri\source>
```

## Installing Packages

As mentioned above, it is best not to install packages in your base Python environment, but rather to install them in a virtual environment.  Start by activating an environment as above.  Then to install `numpy`, a package we will use in the next chapter, use the following command:
```bash
(av) PS C:\Users\morri\source> python -m pip install numpy
Collecting numpy
  Downloading numpy-1.21.2-cp39-cp39-win_amd64.whl (14.0 MB)
     |████████████████████████████████| 14.0 MB 6.4 MB/s
Installing collected packages: numpy
Successfully installed numpy-1.21.2
WARNING: You are using pip version 21.1.3; however, version 21.2.4 is available.
You should consider upgrading via the 'C:\Users\morri\source\envs\av\Scripts\python.exe -m pip install --upgrade pip' command.
```
Here the `numpy` package was successfully installed in the `av` environment.  You may be prompted to upgrade pip, which you can do with the suggested command.  

## Run Python

Once you have installed the packages you need, simply call `python` from the command line to run it:
```
(av) PS C:\Users\morri\source> python
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Within VSCode, you can select this virtual environment for running your Python code by first opening a Python file.  Then in the bottom left menu bar you'll see the selected Python environment like this:

![Python Environment](.Images/python_venv.png)

If a different environment appears, click on it, and select the virtual environment you just created.  You may need to specify the path to the Python executable in `envs/av/bin/python.exe`.  Then you should see your virtual environment show up as above.


___
### [Outline](README.md), Next: [Chapter 13: Mathematical Tools](Chapter_13_Mathematical_Tools.md)


