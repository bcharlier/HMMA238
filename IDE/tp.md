# Integrated development environment

An integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger.

## Python specific IDE

There are many IDE for python... but few are good. There is no real "canonical" choice as `Rstudio` is **the one** for R user.

As python is a real jackknife programming language, depending on your goal (data scientific program, web, etc...) you may choose a specific IDE for a particular task.

- Scientific computing : Pyzo, Spyder 
- Generic: PyCharm, VScode

We warmly recommend you to use an IDE.

## VScode/Codium

For instance you can use `VScode`. This is a powerful, cross-platform IDE that comes with many extensions.

On the FdS-Linux box, there is a fork of `vscode` called `vscodium`. You may launch it via the GUI or through the following command line

```bash
$ vscodium
```

### Install an extension

We will install the `python` extension. To install it:

1. Open Visual Studio Code
2. Open the Extensions tab (left bar of the VScode window or press `Ctrl+Shift+X`)
3. Type `python` to find the python extension from Microsoft
4. Click the `Install` button, then the `Enable` button

or

1. Open Visual Studio Code
2. Press `Ctrl+P` to open the Quick Open dialog
3. Type `ext install ms-python.python` to find the extension
4. Click the `Install` button, then the `Enable` button

or

1. Run in a terminal 

```bash
$ vscodium --install-extension ms-python.python
```

**Exercise:**

1. Install the extension called `Anaconda Extension Pack`

### An advance text editor

The `keyboard shortcuts Reference guide` is available in the `help` menu (or with `Ctrl+K Ctrl+R` shortcut). It can be very useful to learn few shortcut. For instance:

- Learn how the **multicursor** work (E.g Search for an occurrence with  `Ctrl + d`)
- Learn how to move an entire line  with `Alt + up`
- etc...

### Using VScode as a Python IDE

Follow the tutorial <https://code.visualstudio.com/docs/python/python-tutorial> to set up `vscode` to use it as a python IDE. In particular, you have to learn how to debug a simple python script <https://code.visualstudio.com/docs/python/debugging>.
