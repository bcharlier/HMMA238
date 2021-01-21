# Integrated development environment

An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development.
An IDE normally consists of at least a source code editor, build automation tools and a debugger.

## `python` specific IDE

There are many IDE for python, but none are perfect, and there is no consensus in the `python` community. There is no real "canonical" choice as `Rstudio` is **the one** for `R` user.

As `python` is a real jackknife programming language, depending on your goal (data scientific program, web development, etc.) you may choose a specific IDE for a particular task.

- Scientific computing : Pyzo, Spyder 
- Generic: PyCharm, VSCode

We warmly recommend you to use an IDE, and we will mostly describe VSCode in what follows.

## VSCode/Codium

For instance you can use `VSCode`. This is a powerful, cross-platform IDE that comes with many extensions.

On the FdS-Linux box, there is a fork of `vscode` called `vscodium`.
You may launch it via the GUI or through the following command line

```bash
$ vscodium
```

### Install a VSCode extension

We will install the `python` extension.
To install it:

1. Open VSCode.
2. Open the Extensions tab (left bar of the VSCode window or simply press `Ctrl+Shift+X`)
3. Type `python` to find the python extension from Microsoft
4. Click the `Install` button, then the `Enable` button

or

1. Open VSCode
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

The `keyboard shortcuts Reference guide` is available in the `help` menu (or with `Ctrl+K Ctrl+R` shortcut).
It can be very useful to learn some shortcuts.
For instance:

- Learn how **multicursors** work (e.g., search for an occurrence with  `Ctrl+d`)
- Create aligned **multicursors** with `Ctrl+Shift`
- Learn how to move an entire line  with `Alt+up`
- etc.

### Using VSCode as a `python` IDE

Follow the tutorial <https://code.visualstudio.com/docs/python/python-tutorial> to set up `vsCode` to use it as a python IDE.
In particular, you have to learn how to debug a simple `python` script <https://code.visualstudio.com/docs/python/debugging>.
