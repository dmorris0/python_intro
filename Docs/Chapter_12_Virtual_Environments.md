# Chapter 12: Virtual Environments

## Why Virtual Environments?

Python leaves much of its functionality to libraries.  Python code will import a library, or component of a library, and then can use it within the following lines of code.  Now most of these libraries do not come with the base Python install, but are part of packages that need to be installed before use.  Installing packages is simple, and to it is easy to obtain enormous functionality with just a few commands.

However, the vast number of packages in Python creates compatibility problems.  Packages have many versions, and many versions of many packages are not compatible with each other.  To some extent, version compatibility can be handled by the installer, but package incompatibility means there are certain packages that cannot be installed at the same time.

The consequence of this incompatibility dilemma is that it is best that you do **not** install Python packages directly in the base Python environment.  Instead, create multiple separate virtual environments, and install the packages you need within each virtual environment.  It is easy to create virtual environments and to switch between them.  Instructions are given below. 

## Create a Virtual Environment

Likely you will create multiple virtual environments, so I recommend creating a folder to store them.  I typically create a folder called `venvs` in my `home` folder or in my `source` folder (depending if I'm in Linux or Windows).  Use `cd` to enter this folder in your terminal and then create a virtual environment with:
```
PS C:\Users\morri\source\venvs> python -m venv av
```
or with:
```
PS C:\Users\morri\source\venvs> python -m venv --system-site-packages av
```
This command is in Windows PowerShell, but the same command works in other systems, with the exception that you may need to call `python3` rather than `python` in Linux.  This will create a virtual environment called `av`.  If you look in your `venvs` folder you will see an `av` folder that contains details of the `av` virtual environment.  

The difference between the above two commands is the optional argument: `--system-site-packages`.  With this argument included, the vitual environment will inherit packages that are installed in the your base Python.  If you want your virtual environment to have all it's own packages, then don't include this.  But if the base Python already has packages you need and would rather not duplicate them in your virtual environment, then include this option.  Note that some packages, such as `scikit-learn`, can use a lot of disk space.  

## Activate a Virtual Environment

To use a Virtual Environment you must activate it.  In Windows the `activate.ps1` script is located in the `Scripts` subfolder.  Simply call this script to start your environment.  For example, if you are located in the folder containing the `venvs` folder, simply type:
```
PS C:\Users\morri\source> .\venvs\av\Scripts\activate.ps1
(av) PS C:\Users\morri\source>
```
In Linux you would type: `source envs/av/bin/activate`.  Notice that once a virtual environment has been activated, each line will begin with the environment name in parentheses.  This tells you that if you install python packages, they will be installed for that virtual environment, and if you start Python, you'll be starting in that environment.

Note: PowerShell by default does not permit running scripts, and may give you an error saying scripts are disabled for the system, see https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies.  You can enable scripts as follows:
1. Run a PowerShell with administrative priviledges
2. Call this command: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

After doing this you should be able to activate your virtual environment.

When you are done with your environment, you can either activate another environment, or can deactivate it with:
```
(av) PS C:\Users\morri\source> deactivate
PS C:\Users\morri\source>
```

## An Easier Way to Activate your Virtual Environment

This section is purely optional and you can skip it if you prefer and move on to the next section: [Installing Packages](#installing-packages).

It can be tedious to type out the full path name in order to activate your virtual environment.  And you may have multiple virtual environments, making it not feasible to create an alias to activate each environment.  A solution to this is to create a PowerShell function for initializing your virtual environments.  First find your PowerShell `$profile` file name by typing:
```
echo $profile
```
This should return the full path and name of a file similar to: `Microsoft.PowerShell_profile.ps1`.  Then open this file with Visual Studio, or create it if it doesn't exist, and add the following lines to it:
```
# Virtual environment folder: adjust the following path for your system:
$venvfolder = 'C:\Users\morri\source\venvs'
# ---
# Activate python virtual environments.  Call with:
#   act <virtualenv_name>
# Or call without arguments to get a list of virtual environments
function act([string]$virtualenv)
{
  if ($virtualenv -eq "")
  {
    Get-ChildItem $venvfolder
  } else 
  {
    $cmd = $venvfolder + "\" + $virtualenv + "\Scripts\activate.ps1"    
    & $cmd
  }
}
```
You'll need to change the line: `$venvfolder = 'C:\Users\morri\source\venvs` to instead include the full path to the folder containing your virtual environment folder.  The function `act` (short for activate) created in this code will enable you to activate any virtual environment created in this folder.

Now this file is a script that is called each time a PowerShell is started.  To try it out, first open a new PowerShell.  In this new PowerShell test the function `act` by typing:
```
act
```
This should list the contents of your `venvs` folder, which will be your virtual environments.  You should see your recently created `av` virtual environment.  Then to activate the `av` virtual environment, simply type:
```
act av
```
If you create new virtual environments in this same `venvs` folder, you'll be able to activate any of them with: `act <environment_name>`

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
You should consider upgrading via the 'C:\Users\morri\source\venvs\av\Scripts\python.exe -m pip install --upgrade pip' command.
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

If a different environment appears, click on it, and select the virtual environment you just created.  You may need to specify the path to the Python executable in `venvs/av/bin/python.exe`.  Then you should see your virtual environment show up as above.


___
### [Outline](../README.md), Next: [Chapter 13: Numpy](Chapter_13_Numpy.ipynb)


