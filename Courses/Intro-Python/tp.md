# An introduction to Python

    Joseph Salmon: joseph.salmon@umontpellier.fr
    Benjamin Charlier: benjamin.charlier@umontpellier.fr


## Shell, terminal and console

The **shell** is the program which actually processes commands and returns output, e.g., Bash, zsh, etc... 

A **terminal** refers to a wrapper program which runs a shell.

The **console** is a special sort of terminal (low level).

https://superuser.com/questions/144666/what-is-the-difference-between-shell-console-and-terminal

## Python

Python 2.0 was released in 2000. It is deprecated and no more security updates are done!

Python 3.0, a major, backwards-incompatible release, was released in 2008. 

https://en.wikipedia.org/wiki/History_of_Python

## Structure your work

Open a terminal. In a shell locate yourself in the HMMA238 repository where and then 

```
$ cd HMMA238/Courses/Intro-Python
```
We assume you are at this level from now on in your architecture.

# How to launch a Python program

* A python script has an extension in `.py`: 

* Every lines of a python script are parsed and executed excepted **comments** starting by the symbol **`#`**.

* To launch a Python script from a terminal:

```
$ python my_script.py
```

**Example:**

Consider the file `hello-world.py` in the directory ```HMMA238/Courses/Intro-Python/scripts/```. You can investigate its content and run in your terminal:

```bash
ls scripts/
cat scripts/hello-world.py
python ./scripts/hello-world.py
```


### Python interpreter (interactive mode)

The Python interpreter can be launched with the command ``python``.

<!-- <img src="files/images/python-screenshot.jpg" width="600"> -->
<img src="https://raw.github.com/jrjohansson/scientific-python-lectures/master/images/python-screenshot.jpg" width="600">

It allows to:

* memorize previously launched commands with the arrows (up and down).
* search in history with ctrl+R
* auto-completion with Tab.
* inline code edition

### IPython

IPython is a more refined interactive shell.

<!-- <img src="files/images/ipython-screenshot.jpg" width="600"> -->
<img src="https://raw.github.com/jrjohansson/scientific-python-lectures/master/images/ipython-screenshot.jpg" width="600">

One can:

* memorize previously launched commands with the arrows (up and down).
* search in history with ctrl+R
* auto-completion with Tab.
* inline code edition
* easy documentation access
* debug

**Note**: running ```ipython --pylab``` will help opening several images. 

### Rendering with VS Code

**Sources**: https://code.visualstudio.com/docs/languages/python

- linter (`Ctrl` + `shift` + `p`, linter, Flake8)
- debugger
- Spell checker (e.g., Code Spell Checker)
- shortcuts <https://code.visualstudio.com/docs/getstarted/keybindings>
---
<font color='red'> **Exercise**: </font>

Use the code from <https://www.algorithm-archive.org/contents/euclidean_algorithm/euclidean_algorithm.html> and modify it so that no warning is displayed. This will require some elements on **pep8** (cf. https://realpython.com/python-pep8/).

---


### Run shell command from python

It is possible to run a system command from a python interpreter.
In a **jupyter notebook** or in an **ipython** instance, its sufficient to start the line with a `!`:


```python
# same output... but with by calling directly a shell
! pwd
```


```python
# download the file with a shell
! wget http://josephsalmon.eu/enseignement/Montpellier/HMMA238/hello-world.py scripts/hello-world.py

# Equivalent code in python
# import urllib.request
# url = 'http://josephsalmon.eu/enseignement/Montpellier/HMMA238/hello-world.py'
# urllib.request.urlretrieve(url, 'script/hello-world.py')
```


```python
! ls scripts/hello-world.py
```


```python
! cat scripts/hello-world.py
```


```python
! python ./scripts/hello-world.py
```


```python
run ./scripts/hello-world.py
```

### Jupyter notebook (not recommended anymore)

**Warning**: not recommended anymore for this course (in particular to avoid versioning overload), hence to read on your own.

[Jupyter notebook](https://jupyter.org/) is similar to Mathematica, Matlab or Maple, in a web browser.

<!-- <img src="files/images/ipython-notebook-screenshot.jpg" width="800"> -->
<img src="https://jupyter.org/assets/jupyterpreview.png" width="800">

Launch it with the command `jupyter notebook`

in a directory where your notebooks are/will be stored (files with extension *.ipynb); or in a parent directory .

For practical rooms at Université de Montpellier, cf.
http://josephsalmon.eu/enseignement/Montpellier/HLMA310/IntroPython.pdf , page 13


## Variable names


Variable names can contain letters `a-z`, `A-Z`, numbers `0-9`and a few special characters such as `_` they **ALWAYS** must start by a letter. 

By convention, variable names are usually lowercase (rem: an uppercase letter is used for Class names only).

Some variables names are forbidden since they are already defined by Python:

    and, as, assert, break, class, continue, def, del, elif, else, except, 
    exec, finally, for, from, global, if, import, in, is, lambda, not, or,
    pass, print, raise, return, try, while, with, yield



## Numbers

```python
2 + 2 + 1  # a comment 
```


```python
a = 4
print(a)
print(type(a))
```
**Note** int for integer.

```python
int a = 1;  # code C ... leads to an error in Python
```

```python
c = 1.0  # float (floating point number)
print(c)
print(type(c))
```

```python
a = 1.5 + 1j  # complex number
print(a.real)
print(a.imag)
print(1j)
print(a)
print(a + 1j)
print(1j * 1j)
print(type(a))
```

```python
type(1j * 1j)
```

```python
True + False # Boolean number
```

Note: `True` and `False` can usually be perceived as 1 and 0. 


```python
3 < 4  # Boolean
```


```python
1 < 3 < 5
```


```python
3 < 2
```


```python
test = (3 > 4)
print(test)
```


```python
type(test)
```

```python
print(7 * 3.)  # int x float -> float
print(type(7 * 3.))
```

```python
2 ** 10  # exponent, do not use `^` in Python
```


```python
8 % 3  # reminder in the Euclidean division (modulo)
```

**Warning** !


```python
3 / 2  # float by default
```

```python
3 // 2
```

## The standard libraries and its packages

 * Python functions are organized by *modules*
 * Python Standard Library : package collection to access standard functions (low level), such as call to the OS (operating system), file management, string management, web interface, etc.


### References
 
 * The Python Language Reference: https://docs.python.org/3/reference/index.html
 * The Python Standard Library: http://docs.python.org/3/library/

### Using packages

* A package must be *imported* before it can be used:
* Ordering: load the package in the order of complexity (first lower level function as `os`, etc.) then numerical packages (e.g., `scipy`, `numpy`), display ones (`matplotlib`, `seaborn`, etc.)

```python
import math
```

 * The `math` package can now be used :


```python
x = math.cos(2 * math.pi)
print(x)
```

Another way to use a package is to import only the functions that you need:


```python
from math import cos, pi
x = cos(2 * pi)
print(x)
```

**Warning**: NEVER load all functions from a package, there is a risk that you redefine some existing functions without noticing.


```python
from math import *  # NEVER DO THAT, EVER!!!
tanh(1)
```

Instead load the function you need:

```python
from math import tanh
tanh(1)
```

Popular method: use a standard nickname for a package (we will see classical ones: `np, pd, sns, plt, skl,` etc.)


```python
import math as m
print(m.cos(1.))
```

### Inspecting a package

 * Once a package is imported it is possible to list the functions available with `dir`:

```python
import math
print(dir(math))
```

* To access the documentation use `help`

```python
help(math.log)
```

 * In IPython or Jupyter one can also use:

```python
math.log?
```

```python
math.log(10) 
```

```python
math.log(10, 2)
```

```python
math.ceil(2.5)
```

* `help` can be called for modules :


```python
help(math)
```

Note: you can use the previous function to check where is the library on your disk (see at bottom)


 * Useful modules : `os`, `sys`, `math`, etc.

 * For an exhaustive list see :  <http://docs.python.org/3/library/>

---
### <font color='red'> Exercise : log </font>
Write a code that computes the first power of 2 above a given number $n$.

```python
n = 12345
# TODO XXX 
```
---

### Fractions (To read on your own, skipped in course)

```python
import fractions
a = fractions.Fraction(2, 3)
b = fractions.Fraction(1, 2)
print(a + b)
```

* We can use `isinstance` to test variables types :


```python
print(type(a))
print(isinstance(a, fractions.Fraction))
```


```python
a = fractions.Fraction(1, 1)
print(isinstance(a, int))
```

### Type casting (type conversion)


```python
x = 1.5
print(x, type(x))
```


```python
x = int(x)
print(x, type(x))
```


```python
z = complex(x)
print(z, type(z))
```

* We can use `isinstance` to test variables types :


```python
print(type(z))
print(isinstance(z, complex))
print(isinstance(z, type(z)))
```

**Warning:** conversion from `complex` to `float` is ambiguous


```python
x = float(z)
print(x, type(x))
```

## Operators and comparisons

```python
1 + 2, 1 - 2, 1 * 2, 1 / 2  # + - / * integers
```


```python
1.0 + 2.0, 1.0 - 2.0, 1.0 * 2.0, 1.0 / 2.0  # + - / * floats
```

More on the 0.1 + 0.2 craziness: <https://0.30000000000000004.com/>


```python
# Euclidean division
3.0 // 2.0
```


```python
# Warning: use `**`, not `^` as in most languages
2 ** 2
```

* Boolean operators: `and`, `not`, `or`. 


```python
True and False  # see also (1 * 0) % 2 
```

```python
True or False 
```

```python
not False
```

```python
True ^ True  #XOR , see also (1+1) % 2
```

Operations cheat sheet:
<https://docs.python.org/fr/3.9/library/operator.html#mapping-operators-to-functions>

---
### <font color='red'>Exercise : quotes and double quotes</font>
Display with a `for` loop all the possibilities (Boolean tables) for the Boolean operations: *, +, ^ (i.e., and, or, xor).
---


* Comparisons `>`, `<`, `>=` greater or equal, `<=` less or equal, `==` equal (content are the same), `is` object identity.


```python
2 > 1, 2 < 1
```


```python
2 > 2, 2 < 2
```


```python
2 >= 2, 2 <= 2
```


```python
2 != 3  # not equal
```


```python
not 2 == 3  # negation
```

```python
n1 = 600
n2 = 600
n3 = n1
 
print(n1 == n2)
print(n1 is n2)
print(n3 is n1)
```


## Containers

### Strings

```python
s = 'Ciao Ciao!'
# or use " "
s1 = "Ciao Ciao!"
# or use """ """
s2 = """Ciao Ciao!"""
print(s, s1, s2)
print(type(s))
```

---
### <font color='red'>Exercise : quotes and double quotes</font>
Create the following string:
Toto said: "Hello! How's it going?"

```python
# TODO XXX
```

See also string: `\t` (tabulation), `\n` (chariot) , etc.
---


To extract a sub-string between indices `start`  (**included**) `stop` (**excluded**): use the syntax `[start:stop]`



```python
s[0]  # first character
```
**Beware:** indices start at 0!

```python
s[-1]  # last character
```

```python
s[1:5]
```

```python
start, stop = 1, 5
print(s[start:stop])
print(len(s[start:stop]))
```


```python
print(stop - start)
```


```python
print(start)
print(stop)
```

**Remark:** especially for french word (containing é, è, à, ç, etc.), you should check which character encoding system is used. See: unicode, utf8, etc. at <http://sametmax.com/lencoding-en-python-une-bonne-fois-pour-toute/> (fr).

It is possible to omit `start` or `stop`: in this case the default values are 0 or the length of the string respectively.


```python
s[:5]  # 5 first characters
```


```python
s[2:]  # from the third char. to the end
```


```python
print(len(s[5:]))  # len: short for 'length'
print(len(s) - 5)
```


```python
s[-3:]  # 3 last characters
```

It is possible to define a `step` with the syntax `[start: stop: step]` (default value of `step` is 1):


```python
print(s[1::2])
print(s[0::2])
```

This is called **slicing**.
See: <https://docs.python.org/3/library/functions.html?highlight=slice#slice> et <https://docs.python.org/3/library/string.html>

---
### <font color='red'>Exercise : slicing and strings</font>
From the alphabet string, use slicing to generate the string "cfilorux"


```python
import string
alphabet = string.ascii_lowercase
print(alphabet)
```


```python
# XXX
```
---

Some operators may be used to handle strings (this is called **overloading/polymorphism**).


```python
print("aldkfdf" < 'alkfdg') #  lexicographic (dictionary) order
print("zz" + 'z')
print("z" == 'z')
```

#### Display strings

```python
print("str1", "str2", "str3")
```


```python
print("str1", 1.0, False, -1j)  # convert all variables in strings
```


```python
print("str1" + "str2" + "str3") # concatenate ("gluing") with `+` operand
```


```python
print("str1" * 3)  # repeat
```

Strings are classes that have methods to format them.


```python
print("abc, def, ghi".replace(',', ' '))
```

```python
print("ssEslk".upper())
print("kljlj, dsfsdf".capitalize())
print(":".join("Python"))
print(":".join(["Pyt", "hon"]))  # take a list (see list section just below)
print("guru99 career guru99".split(' '))  # return a list 
```

**Important note:** In Python, Strings are immutable. Consider the following code:

```python
x = "Guru99"
y = x.replace("Guru99","Python")
print(x)
print(y)
```

This is because `x.replace("Guru99", "Python")` returns a copy of X with replacements made.You will need to use the following code to observe changes.


```python
x = "Guru99"
x = x.replace("Guru99","Python")
print(x)
```

More information on `strings`:

- <https://mkaz.blog/code/python-string-format-cookbook/>

- <https://docs.python.org/3/library/string.html>


### Floats display

```python
a = 1.0000000002
b = 1.00031e2
c = 136869689
print("val = {}".format(a))
print("val = {}".format(b))

print("val = {0:1.5e}".format(a))
print("val = {0:1.5e}".format(b))

print("val = {0:1.15f}".format(a))

print("val = {:3d}".format(c))
print("val = {:13d}".format(c))
print("val = {:6d}".format(c))
```

---
### <font color='red'> Exercise : $e$ digits</font>
Print the real number $e=\exp(1)$ with 1, 10, 20 and 50 digits (one number by line).  


```python
# TODO XXX
for i in [1, 10, 20]:
    print(f"{math.e:1.{i}f}")
```
---

```python
# More advanced
print("val = {0:1.15f},val2={0:1.{2}f}".format(a, b, 4))

```

New (XXX TODO): f-strings et <https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-digit>

```python
s = "The number {0:s} is approximately {1:1.111}"
print(s.format("pi", math.pi))
```

```python
# Accessing arguments by name:
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
```

More info: <https://docs.python.org/3/tutorial/floatingpoint.html>


### Lists

Lists are similar to `strings` except that can blend any type of object (so a `string` is a kind of `list`)
This is the simplest structure at hand.

A possible syntax to create a list is `[..., ..., ...]` 

```python
l = [1, 2, 3, 4]
print(type(l))
print(l)
```

A slicing example:

```python
print(l[1:3])
print(l[::2])
```

**Warning:** indexing starts at 0!

```python
l[0]
```
**Warning:** pointer addressing!

```python
print("l is :", l)
k = l       # k is a pointer on l, i.e., l and k share the same memory space 
k += [14]   
print("l has been modified :", l)
```
**Question**: Why is the command failing above if you use `k += 14` instead?


```python
k = l.copy()  # enforce copying, l and k point to different memory addresses
k[0] = 15
print(l)
print(k)
```

One can mix types in a single list:

```python
l = [1, 'a', 1.0, 1-1j]
print(l)
```

Lists of lists are possible (e.g., to create trees, etc.):

```python
list_of_list = [1, [2, [3, [4, [5]]]]]
print(list_of_list)
```

or 

```python
tree = [1, [2, 3]]
print(tree)
```

The `range` function generates an enumerator, but you can create a list of integers easily from that.
More details: <https://www.geeksforgeeks.org/python-range-function/>

```python
start, stop, step = 10, 30, 2
print(range(start, stop, step))
print(range(10, 30, 2))
print(list(range(10, 30, 2)))
```

Iterate in reverse order, from n-1 to 0


```python
n = 10
print(range(n-1, -1, -1))
```


```python
range(-10, 10)
```


```python
# convert a string in list
s = "zabcda"
l2 = list(s)
print(l2)
```


```python
# sorting (in french "trier")
l2.sort()
print(l2)
print(l2.sort())
l2.sort(reverse=True)
print(l2)
print(l2[::-1])
```

**Warning:** `l2.sort()` works **in place** and outputs nothing, or rather `None`


#### Append, insert, modify and remove elements in a list


```python
# Create an empty list
l = []  # or use: l = list()

# Append elements on the right with `append`
m = l.append("A")
l.append("d")
l.append("d")

print(m)
print(l)
```

Concatenate lists with "+":


```python
lll = [1, 2, 3]
mmm = [4, 5, 6]
print(lll + mmm)  
```

**Warning:** this is different from `lll.append(mmm)` (try it yourself!)

```python
lll.append(mmm)
print(lll)
```


```python
print(mmm * 3)
```

You can modify a list by assignation (it is then different from `strings`!):


```python
l[1] = "p"
l[2] = "p"
print(l)
```

```python
l[1:3] = ["d", "d"]
print(l)
```

Insert an element with `insert`


```python
l.insert(0, "i")
l.insert(1, "n")
l.insert(2, "s")
l.insert(3, "e")
l.insert(4, "r")
l.insert(5, "t")

print(l)
```

Remove an element by value: `remove`


```python
l.remove("A")
print(l)
```


```python
ll = [1, 2, 3, 2]
print(ll)
ll.remove(2)
print(ll)
```


```python
print(2 in ll)
print(5 in ll)

print(l.index('r'))
print(l.index('t'))
```

Remove an element by indexing: `del`:


```python
del l[7]
del l[6]
print(l)
```

### Map and zip

```python
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha"] 
roll_no = [ 4, 1, 3, 2] 
marks = [ 40, 50, 60, 70] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks) # return iterable
mapped_disp = list(mapped)
print(mapped_disp)
```

```python  
# unzipping values 
name_post, roll_no_post, marks_post = zip(*mapped_disp) 
  
print("The unzipped result: \n",end="") 
# printing initial lists 
print("The name list is : ", end="") 
print(name_post) 
  
print("The roll_no list is : ", end="") 
print(roll_no_post) 
  
print("The marks list is : ", end="") 
print(marks_post) 
```

Use : `help(list)` for more on lists.

```python
help(list)
```

### Tuples

 * *tuples*  are similar to lists but are *immutable* : they cannot be modified once created (so they are close to `strings` in a way). They are often used as output of function (see below).
 
 * You can create them with a command like  `(..., ..., ...)` or simply `..., ...`:


```python
point = (10, 20)
print(point, type(point))
```


```python
point[0]
```

A *tuple* can be unpacked with the following structure :


```python
x, y = point

print("x-coordinate: ", x)
print("y-coordinate: ", y)
```

Yet, you will face an error if you type the following command:

```python
point[0] = 20
```

Usage: mostly output of functions.

### Dictionary

They are similar to your day-to-day dictionary, and use a system of *keys* and *values*: the *key* is the name of the attribute, and the *value* describes the key.

The syntax for dictionaries is: `{key1 : value1, ...}`:


```python
params_bracket = {"parameter1": 1.0,
                  "parameter2": 2.0,
                  "parameter3": 3.0}

# Alternatively:

params_dict = dict(parameter1=1.0,
                   parameter2=2.0,
                   parameter3=3.0)

print(type(params_dict))
print(params_dict)
```

```python
print("p1 =", params_bracket["parameter1"])
print("p2 =", params_bracket["parameter2"])
print("p3 =", params_dict["parameter3"])
```


```python
# Substitutions
params_bracket["parameter1"] = "A"
params_bracket["parameter2"] = "B"

# Add a key with a specific value
params_bracket["parameter4"] = "D"

print("p1 =", params_bracket["parameter1"])
print("p2 =", params_bracket["parameter2"])
print("p3 =", params_bracket["parameter3"])
print("p4 =", params_bracket["parameter4"])
```

Remove a key from the dictionary:

```python
del params_bracket["parameter4"]
print(params_bracket)
```

Test the existence of a key

```python
print("parameter1" in params_bracket)
print("parameter6" in params_bracket)
```

```python
params_bracket["parameter6"]
```

**Note:** you should get used to errors messages. They are helpful, and will help you debug your code.
Here the message raised is clear and explains that the key does not exist, so you cannot access it)


```python
print(params_bracket.items())
print(params_bracket.values())
print(params_bracket.keys())
```

**Note**: you obtained a *view* with the previous syntax.
If you want a list, type the following for instance

```python
print(list(params_bracket.values()))
print([*params_bracket.values()])  #  equivalent
```

## Conditions, `if`/`elif`/`else` and loops

### `if`, `elif`, `else`

**WARNING**: do not forget the symbol ":" at the end of a line with `if`), and `tab` (4 spaces) for indenting: there are not {} or () in Python, only the indentation makes it clear what level of hierarchy you are in.


```python
statement1 = False
statement2 = False

if statement1:
    print("statement1 is True")
elif statement2:
    print("statement2 is True")
else:
    print("statement1 and statement2 are False")
```

**Common errors**

- Forgotten ":" at the end of the line

```python
if statement1
    print("statement1 is True")
```
- No indentation
```python
if statement1:
print("statement1 is True")
```

**Nesting tests**

```python
statement1 = statement2 = True

if statement1:
    if statement2:
        print("both statement1 and statement2 are True")
```

**Common errors with nesting**

- Errors with the tab levels: think about the following two examples

```python
statement1 = True 

if statement1:
    print("printed if statement1 is True")
    print("still inside the 'if' block")
```


```python
statement1 = False

if statement1:
    print("printed if statement1 is True")
print("no more in the 'if' block")
```

## Loops

### `for` loop

**Note**: again use ":" at the end of line


```python
for x in [1, 2, 3]:
    print(x)
```

The `for` loop iterates over elements in the list.
For instance:


```python
for x in range(4): # range starts at 0 and create an iterator (0, 1, 2,..., n-1)
    print(x)
```

**Warning** `range(4)` does not include 4 (get used to that) !!!


```python
for x in range(-3,3):
    print(x)
```

**Warning** `range(-3,3)` does include -3 (get used to that also) !!!


```python
for word in ["calcul", "scientifique", "en", "python"]:
    print(word)
```


```python
for letter in "calcul":
    print(letter)
```

To iterate over a dictionary things are bit different, since there is no natural ordering in Python dictionaries (it is a bit different of good old dictionaries, where the lexicographic order is natural):


**VS Code** tip useful here: `ctrl + d` (select next) / `ctrl + u` (unselect the last) 

```python
print(params_bracket)
for key, value in params_bracket.items():
    print(key, " = ", value)
```

```python
params_bracket.items()
```

```python
for key in params_bracket:
    print(key)
    print(params_bracket[key])
    print('------')
```

```python
# Initialize list of players
players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"] 
  
# Initialize their scores 
scores = [100, 15, 17, 28, 43]  
  
# printing players and scores 
for pl, sc in zip(players, scores): 
    print(f"Player :  {pl}     Score : {sc}")
```

---
### <font color='red'>Exercise : Align display</font>
Can you make the previous loop display the score in an align way? This is a StackOverflow question!
*Hint*: use '<'

---

VERY often, when you iterate over a list (or a similar object) you also need to recover the index associated to its elements. In Python `enumerate` makes it easy to read:


```python
for player_idx, player_name in enumerate(players):
    print("Player index: {0}, Player name: {1}".format(player_idx, player_name))
```

---
### <font color='red'>Exercise : counting letters</font>
Count the number of occurrences of each letter in the string `"HelLo WorLd!!"`.   
The output will be a dictionary `freq_dict` with keys the elements in the string, and as values the number of time they appear. Hence, the solution should be `dict(h=1, e=1, l=3, o=2, w=1, r=1, d=1, !=2)`, without making a difference between lower and upper cases.

**hint**
```python
s = "HelLo WorLd!!"  # use lower() to get lowercase letters.

# XXX TODO
```
---

---
### <font color='red'>Exercise : Caesar cipher </font>

Propose a way to code and decode a message with the Caesar cipher or [Caesar shift](https://en.wikipedia.org/wiki/Caesar_cipher).


```python
code = {'e': 'a', 'l': 'm', 'o': 'e'}
# REM: possibly use +=1 that allow incrementing in place...
s = 'Hello world!'
s_code = ''

# XXX TODO
# solution: s_code = 'Hamme wermd!'

my_inverted_code = {value: key for key, value in code.items()}
s_decoded = ''

# XXX TODO
# solution: s_decoded = 'Hello world!'
```
---

**List comprehension:**

`for` loops:


```python
ll = [x ** 2 for x in range(0,5)]

print(ll)

# This is an alternative to
ll = list()
for x in range(0, 5):
    ll.append(x ** 2)

print(ll)

# And for `caml` fluent users, a map point of view
print(map(lambda x: x ** 2, range(5)))
```

### `while` loop

```python
i = 0
while i < 5:
    print(i)
    i += 1

print("OK, it stopped at i={}".format(i-1))
```

---
### <font color='red'>Exercise: An old $\pi$ approximation</font>
    
Compute an approximation of $\pi$ thanks to the Wallis formula (*hint*: use a `for` loop)

(to visualize TeX in VS Code: install the extension from <https://marketplace.visualstudio.com/items?itemName=goessner.mdmath>)

$$
    \text{Formule de Wallis:}\quad
    \pi = 2 \cdot\prod_{n=1}^{\infty}
    \left({\frac{4 n^{2}}{4 n^{2} - 1}}\right)
$$


More details here:
(fr) <https://fr.wikipedia.org/wiki/Produit_de_Wallis>
(en) <https://en.wikipedia.org/wiki/Wallis_product>


```python
# XXX TODO
```
---

## Functions

A Python function is defined by starting with the keyword `def`, followed by the name of the function, the signature in between `()`, and `:` at the end of the line.

**Examples:**


```python
def func0():
    print("test")
```


```python
func0()
```

**ALWAYS** add docstrings!


```python
def func1(s):
    """Display a string and its length."""
    print(s, "est de longueur", len(s))
```

Now you can leverage the help function:

```python
help(func1)
```

```python
print(func1("test"))
print(func1([1, 2, 3]))
```

In general it is useful to add an **output**, using the `return` keyword:


```python
def square(x):
    """Compute x**2."""
    return x * x
```


```python
print(square(4))
```

It is possible to output several values, and tuples are useful for that:


```python
def powers(x):
    """Compute the first power of x up to x**4."""
    return x * x, x * x * x, x * x * x * x
```


```python
print(powers(3))
x2, x3, x4 = powers(3)
print(x2, x3)
print(type(powers(3)))
out = powers(3)
print(len(out))
print(out[1])
print(out[2])
```


```python
t = (3,)
print(t, type(t))
```


```python
x2, x3, x4 = powers(3)
print(x3)
```

### Arguments by default

It is possible to have optional arguments that are assigned to a fixed values if the user do not provide an alternative:


```python
def myfunc(x, p=2, verbose=False):
    if verbose:
        print("evaluate myfunc with x =", x, "and exponent p =", p)
    return x**p
```

The parameters `verbose` and `p` can now be omitted:


```python
myfunc(5)
```


```python
myfunc(5, 3)
```


```python
myfunc(5, verbose=True)
```

Moreover, if the user provides all the values, they can be provided in any order, check for instance:


```python
myfunc(p=3, verbose=True, x=7)
```

---
### <font color='red'>Exercise: *quicksort*</font>

The [Wikipedia page](http://en.wikipedia.org/wiki/Quicksort)  of the *quicksort* algorithm provides the following code to sort a list:

    function quicksort('array')
       if length('array') <= 1
            return 'array'
       select and remove a pivot value 'pivot' from 'array'
       create empty lists 'less' and 'greater'
       for each 'x' in 'array'
           if 'x' <= 'pivot' then append 'x' to 'less'
           else append 'x' to 'greater'
       return concatenate(quicksort('less'), 'pivot', quicksort('greater'))

Transform this code in valid Python.

**Hints**:

 * recall that the length of a list `l` is given by  `len(l)`
 * two lists can be concatenated with `l1 + l2`
 * `l.pop()` removes the last element of the list `l`

**WARNING**: a list is mutable...

```python
def quicksort(ll):
    # XXX TODO
    return # XXX TODO
```
Test: quicksort([-2, 3, 5, 1, 3]) should output [-2, 1, 3, 3, 5, 1]


A common structure is to have an optional argument, and testing whether it exists or not using `None`:


```python
def spam(arg1=None):
    if arg1 is not None:
        print(arg1)
        # arg1 was specified, do something clever!
```

### Variable number of arguments

The single star `*` unpacks the sequence/collection into positional arguments, so you can do this:


```python
def varargin(*args):
    for i in args: print(i, end=" ")
    print("\n")

varargin(3,4,5)

def multiple_argout(x, y):
    return ((y, x))

print(multiple_argout(1, 2))
```


```python
varargin(multiple_argout(1, 2)) # print a single tuple
```


```python
varargin(*multiple_argout(1, 2)) # print each element separately
```

The double star `**` does the same, only using a dictionary and thus named arguments:


```python
values = { 'x': 1, 'y': 2 }
print(multiple_argout(**values))
varargin(*multiple_argout(**values))
```


```python
def varargin_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, " = ", value)
    print("\n")
    
varargin_kwargs(**values)
varargin_kwargs(values)  # raise an error
```

More to read: https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean-in-a-function-call
