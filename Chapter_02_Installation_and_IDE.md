# Chapter 2: Python and IDE Installation

## Download Python

Download the latest version of Python from [https://www.python.org/](https://www.python.org/).  These notes assume you have Python 3.8 or later.  Most Windows devices should use the recommended `Windows Installer (64bit)` option.  Downloading from this site will give you the full Python version, rather than the more limited version available in the Windows Store.  The rest of this chapter will describe the Windows installation of Python and VSCode, although a similar process applies to other operating systems.  

## Install Python

If you downloaded the `Windows Installer`, then click on it to start the installation.  You should see a window like this:

![Install Python](.Images/python_install.png)

First check the box next to `Add Python to PATH`, and then click on `Install Now`.  You can find more details on Windows Python installations here: [https://docs.python.org/3/using/windows.html](https://docs.python.org/3/using/windows.html).  

## Disable App Auto-Install

If you type `python` in the command line, Windows will by default take you to the Store to prompt you to install the App version.  You should disable this as follows.

In the Windows Settings menu select `Apps & Features`, and from this select `App execution aliases`

![Apps & Features](.Images/python_apps_features.png)

In this window, turn off all of the Python App Installer options like this:

![Python](.Images/python_app_installer.png)

## Test Python

In a command window type `python` and you should see something like the following:
```
C:\Users\morri>python
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
If you get an error like this:
```
C:\Users\morri>python
'python' is not recognized as an internal or external command,
operable program or batch file.
```
Then try `python3`.  If that still doesn't work, you likely do not have python in your path.  You can add it using the environment variables menu

![Environment Variables](.Images/python_environment_3.png)

Check the path for your Python installation and add it (both the base folder and the Scripts folder).  

If when you type `python` you instead are taken to the Windows store, then you must have missed disabling one of the App Installer options in section [Disable App Auto-Install
](##-Disable-App-Auto-Install).  Make sure to do this and then test python again.

You should now have a working interactive Python interpreter.  You can exit it with:
```python
>>> exit()
```

## Visual Studio Code

These notes will use VSCode.  Download and install it from: [https://code.visualstudio.com/](https://code.visualstudio.com/).

### The Python Extension

VSCode supports Python formatting and color-coding through and extension.  To install the Python extension, click on the Extensions icon on the left, type `python`, select the top item from Microsoft, and click on install.

![Python in VSCode](.Images/vs_python.png)

### Terminal in VS Code

You can open a terminal within VSCode.  In the `View` menu select `Terminal`:

![View Menu](.Images/vs_terminal.png)

Then from in the terminal type `python`

![Python in Terminal](.Images/vs_terminal_2.png)

Note: if you have installed Python while VSCode is running, then Python may not be in your path.  You can simply restart VSCode, and that should solve it.

You can use Python within a VSCode terminal, or a separate terminal window; whichever you prefer.  The terminal defaults to PowerShell, which sometimes does not work well with Python.  You can switch to the Command shell from the pulldown menu on the top-right of the terminal panel (to the right of the `+` sign).

To make the `Command Prompt` default instead of `Power Shell`, do the following:
1. Press `Ctrl` + `Shift` + `p`
2. Type `profile` in the text box
3. Select `Terminal: Select Default Profile`
4. Select `Command Prompt`

You will need to restart VSCode for this to take effect.

### View Notes in VSCode

To open these notes in VSCode, first clone this repository.  Then in the `File` menu select `Open Folder` and open the cloned repo folder.  After you open a Markdown file (.md), click on the preview button on the top right to see it graphically.

### Auto Save

I prefer to edit with auto-save on, which is not the default.  You can toggle this option from the `File` menu.

___
### [Outline](README.md), Next: [Chapter 3: Python Programs](Chapter_03_Python_Programs.md)