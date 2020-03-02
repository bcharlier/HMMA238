# How to create a python module

## What it a python module

You already know it: this is a set of python functions and statements.

### A file

A module can be a single file:

```python
>>> import fibo
```

This does not enter the names of the functions defined in `fibo` directly in the current symbol table; it only enters the module name `fibo` there. Using the module name you can access the functions:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
>>> fibo.__file__
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

When importing a module, several methods/members are (automatically) defined. Their names are usually prefixed and suffixed by `__`. E.g.

```python
>>> fibo.__name__
'fibo'
>>> fibo.__file__
'/home/.../HMMA238/Python-modules/fibo.py'
```

### ... or a directory

You can also import a full directory (containing many python files stored in sub-folder)... You have already imported the `numpy` module

```python
>>> import numpy as np
>>> np.array([0, 1, 2, 3]).rehape(2, 2)
```

In fact, you have imported the following folder:

```python
>>> np.__path__
['/usr/lib/python3/dist-packages/numpy']
```

... and more precisely **this** file

```python
>>> np.__file__
'/usr/lib/python3/dist-packages/numpy/__init__.py'
```

Any (sub-)directory of your python module should contains a `__init__.py` file!

**Useful tips:**

- The `__init__.py` can contain a list of function to be loaded when the module is imported. It can allows you to expose functions to user in a concise way.

- you can import module with relative path. See: <https://realpython.com/absolute-vs-relative-python-imports/>

### The `dir()` Function

The built-in function `dir()` is used to find out which names a module defines. It returns a sorted list of strings:

```python
>>> import fibo, numpy
>>> dir(fibo)
>>> fibo.__dir__
>>> dir(numpy)
>>> numpy.__dir__
```

To list every element in your symbol table simply call `dir()`.

Reference: <https://docs.python.org/3/tutorial/modules.html#the-dir-function>

### Namespaces

A namespace is a set of names (functions, variables, etc...). Different namespaces can co-exist at a given time but are completely isolated. In this way you can control which function you are using.

 A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.

```python
>>> cos(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cos' is not defined
>>> import math, numpy as np
>>> math.cos(3)
-0.9899924966004454
>>> np.cos(3)
-0.9899924966004454
```

References: <https://www.programiz.com/python-programming/namespace>

### The Module Search Path

When a module named `spam` is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named `spam.py` in a list of directories given by the variable `sys.path`. `sys.path` is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).

- The environment variable `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable `PATH`).

Reference: <https://docs.python.org/3/tutorial/modules.html#the-module-search-path>

### Checking if a module exists

Find the loader for a module, optionally within the specified path.

```python
>>> import importlib
>>> spam_spec = importlib.util.find_spec("spam")
>>> found = spam_spec is not None
```

See <https://docs.python.org/3/library/importlib.html#importlib.find_loader> an <https://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it>

### Lazy import

A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the **first time** the module name is encountered in an `import` statement.

To force a module to be reloaded, you can use `importlib.reload()`.

See: <https://docs.python.org/3/library/importlib.html#importlib.reload>

### “Compiled” Python files

To speed up loading modules, Python caches the compiled version of each module in the  `__pycache__` directory under the name `module.version.pyc`, where the version encodes the format of the compiled file; it generally contains the Python version number. 

For example, in CPython release 3.3 the compiled version of spam.py would be cached as `__pycache__/spam.cpython-33.pyc`. This naming convention allows compiled modules from different releases and different versions of Python to coexist.

**Useful tips:**

- You should add `__pycache__` entry in your `.gitignore` file to avoid to add compiled python file to your project.

## The Python Package Index (Pypi) repository

The Python Package Index, abbreviated as PyPI, is the official third-party software repository for Python. PyPI primarily hosts Python packages in the form of archives called `sdists` (source distributions) or pre-compiled "wheels."

**Exercise:**

1. Go to <https://test.pypi.org/> and 

### Pip

`pip` is a *de facto* standard package-management system used to install and manage software packages from pypi.

```bash
$ pip install some-package-name
$ pip uninstall some-package-name
$ pip search some-package-name
```

**Exercise:**

  1. Install the modules `download`, `setuptools`, `pandas`, `pygal` and `pygal_maps_fr`
  2. List all the package in your venv using pip.

It is possible to install a **local** module with pip

```bash
$ pip install /path/to/my/local/module
```

where `/path/to/my/local/module` is the path to the module. But if some change occurs in the `/path/to/my/local/module` folder, the module will not be reloaded... Not very useful during the development step. To force python to reload the module at each change use the `-e` option:

```bash
$ pip install -e /path/to/my/local/module
```

## Creating a Python module

References: <https://python-packaging.readthedocs.io/en/latest/>

### Picking A Name

Python module/package names should generally follow the following constraints:

- All lowercase
- Unique on pypi, even if you don't want to make your package publicly available (you might want to specify it privately as a dependency later)
- Underscore-separated or no word separators at all (don't use hyphens)

We are going to create a module called `biketrauma` able to visualize the `bycicle_db` used in the other lectures.

### Module structure

The initial directory structure for `biketrauma` should look like this:

```
packaging_tutorial/
    biketrauma/
        __init__.py
    data/
    setup.py
    .gitignore
```

The top level directory is the root of our VCS repository `packaging_tutorial.git`. The sub-directory, `biketrauma`, is the actual Python module.

**Exercise:** We are going to create a new python module that can be used to visualize the bike dataset.

  1. Create a new folder `~/packaging_tutorial/` and initialize a git in it
  2. Create a `.gitignore` file to ignore `__pycache__` and `.vscode` files  
  3. Push your work into a new repository on your github
  4. Create an empty sub-folder `~/packaging_tutorial/data`. How to add it to git?
  5. Create a sub-folder `~/packaging_tutorial/biketrauma`. This is where our python module will be stored
  6. Create a `~/packaging_tutorial/biketrauma/__init__.py` file where a string `__version__` defined at `0.0,1`.
  7. Create **an empty** `~/packaging_tutorial/setup.py` file.
  8. Commit and push into your repository

Read also: <https://packaging.python.org/guides/single-sourcing-package-version/>.

### Sub-modules

The final directory structure of our module will look like:

```bash
  packaging_tutorial/
      biketrauma/
          __init__.py
          io/
            __init__.py
          preprocess/
            __init__.py
          vis/
            __init__.py
      data/
      setup.py
```

**Exercise:** there is some python files in the `modules_files` folder:

  1. Add some sub-folders to `biketrauma` called `io` (for input/output), `preprocess`, `vis` (for visualization).
  2. Populate the `preprocess` sub-module with the `get_accident.py` file
  3. Populate the `vis` sub-module with the `plot_location.py` file
  4. Populate the `io` sub-module with the file `dl_db.py` (it downloads the bike data-set). At the loading step your sub-module should create the variables

```python
  url = "https://www.data.gouv.fr/fr/datasets/r/ab84353b-498b-4ef5-9a02-a6403f2ead96"
  path_target = os.path.join(os.path.realpath(__file__), "..", "data", "bicycle_db.csv")
```

### Adding Additional Files

In order to load the functions in the `io`, `preprocess` and `vis` sub-modules, you can add the following lines to the `~/packaging_tutorial/biketrauma/__init__.py`:

```python
from .io import dl_db
from .vis import get_accidents
from .preprocess import get_accidents
```

**Exercise:**

  1. Create a file `format_date.py` in the `biketrauma.preprocess` module in which a function `format_date` format the date of the dataset in international format.
  2. This function should accessible with the command 

```python
import biketrauma

df = biketrauma.dl_db()
df_nicely_formated = biketrauma.format_date(df)
```

### Package the module with `setuptools`

The main setup configuration file, `setup.py`, should contain a single call to `setuptools.setup()`, like so:

```python
from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='http://github.com/xxxxxxxxxxx.git',
  author='xxxxxxxxxxx',
  author_email='xxxxxxxxxx@xxxxxxxxxxxxx.xxx',
  license='MIT',
  packages=['biketrauma'],
  zip_safe=False
)
```

To create a `sdist` package (a source distribution):

```bash
$ cd ~/packaging_tutorial/
$ python setup.py sdist
```

This will create `dist/biketrauma-0.0.1.tar.gz` inside the top-level directory. You can now install it with

```bash
$ pip install ~/packaging_tutorial/dist/biketrauma-0.0.1.tar.gz
```

See <https://setuptools.readthedocs.io/en/latest/setuptools.html> and <https://packaging.python.org/tutorials/packaging-projects/>

### Upload on PyPi

TODO