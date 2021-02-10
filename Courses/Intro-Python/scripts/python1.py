import math

x = math.cos(2 * math.pi)
print(x)

from math import cos, pi
x = cos(2 * pi)
print(x)

from math import *  # NEVER DO THAT, EVER!!!
tanh(1)

from math import tanh
tanh(1)

import math as m
print(m.cos(1.))

import math
print(dir(math))

#math.log?

math.log(10) 

math.log(10, 2)

math.ceil(2.5)

import fractions
a = fractions.Fraction(2, 3)
b = fractions.Fraction(1, 2)
print(a + b)

print(type(a))
print(isinstance(a, fractions.Fraction))

a = fractions.Fraction(1, 1)
print(isinstance(a, int))

x = 1.5
print(x, type(x))

x = int(x)
print(x, type(x))

z = complex(x)
print(z, type(z))

print(type(z))
print(isinstance(z, complex))
print(isinstance(z, type(z)))

#x = float(z)
#print(x, type(x))

1 + 2, 1 - 2, 1 * 2, 1 / 2 # + - / * integers

1.0 + 2.0, 1.0 - 2.0, 1.0 * 2.0, 1.0 / 2.0 # + - / * floats

3.0 // 2.0 # Euclidean division

# Warning: use `**`, not `^` as in most languages
2 ** 2

n1 = 600
n2 = 600
n3 = n1
 
print(n1 == n2)
print(n1 is n2)
print(n3 is n1)

s = 'Ciao Ciao!'
# or use " "
s1 = "Ciao Ciao!"
# or use """ """
s2 = """Ciao Ciao!"""
print(s, s1, s2)
print(type(s))

s[0]  # first character
s[-1]  # last character
s[1:5]

start, stop = 1, 5
print(s[start:stop])
print(len(s[start:stop]))

print(stop - start)

print(start)
print(stop)

s[:5]  # 5 first characters
s[2:]  # from the third char. to the end
print(len(s[5:]))  # len: short for 'length'
print(len(s) - 5)
s[-3:]  # 3 last characters

print(s[1::2])
print(s[0::2])

import string
alphabet = string.ascii_lowercase
print(alphabet)

print("aldkfdf" < 'alkfdg') #  lexicographic (dictionary) order
print("zz" + 'z')
print("z" == 'z')

print("str1", "str2", "str3")

print("str1", 1.0, False, -1j)  # convert all variables in strings

print("str1" + "str2" + "str3") # concatenate ("gluing") with `+` operand

print("str1" * 3)  # repeat

print("abc, def, ghi".replace(',', ' '))

print("ssEslk".upper())
print("kljlj, dsfsdf".capitalize())
print(":".join("Python"))
print(":".join(["Pyt", "hon"]))  # take a list (see list section just below)
print("guru99 career guru99".split(' '))  # return a list 

x = "Guru99"
y = x.replace("Guru99","Python")
print(x)
print(y)

x = "Guru99"
x = x.replace("Guru99","Python")
print(x)

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

for i in [1, 10, 20]:
    print(f"{math.e:1.{i}f}")

# More advanced
print("val = {0:1.15f},val2={0:1.{2}f}".format(a, b, 4))

s = "The number {0:s} is approximately {1:1.111}"
print(s.format("pi", math.pi))

# Accessing arguments by name:
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'

l = [1, 2, 3, 4]
print(type(l))
print(l)

print(l[1:3])
print(l[::2])

l[0]

print("l is :", l)
k = l       # k is a pointer on l, i.e., l and k share the same memory space 
k += [14]   
print("l has been modified :", l)

k = l.copy()  # enforce copying, l and k point to different memory addresses
k[0] = 15
print(l)
print(k)

l = [1, 'a', 1.0, 1-1j]
print(l)

list_of_list = [1, [2, [3, [4, [5]]]]]
print(list_of_list)

tree = [1, [2, 3]]
print(tree)

start, stop, step = 10, 30, 2
print(range(start, stop, step))
print(range(10, 30, 2))
print(list(range(10, 30, 2)))

n = 10
print(range(n-1, -1, -1))

range(-10, 10)

# convert a string in list
s = "zabcda"
l2 = list(s)
print(l2)

# sorting (in french "trier")
l2.sort()
print(l2)
print(l2.sort())
l2.sort(reverse=True)
print(l2)
print(l2[::-1])

# Create an empty list
l = []  # or use: l = list()

# Append elements on the right with `append`
m = l.append("A")
l.append("d")
l.append("d")

print(m)
print(l)

lll = [1, 2, 3]
mmm = [4, 5, 6]
print(lll + mmm)

lll.append(mmm)
print(lll)

print(mmm * 3)

l[1] = "p"
l[2] = "p"
print(l)

l[1:3] = ["d", "d"]
print(l)

l.insert(0, "i")
l.insert(1, "n")
l.insert(2, "s")
l.insert(3, "e")
l.insert(4, "r")
l.insert(5, "t")

print(l)

l.remove("A")
print(l)

ll = [1, 2, 3, 2]
print(ll)
ll.remove(2)
print(ll)

print(2 in ll)
print(5 in ll)

print(l.index('r'))
print(l.index('t'))

del l[7]
del l[6]
print(l)

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha"] 
roll_no = [ 4, 1, 3, 2] 
marks = [ 40, 50, 60, 70] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks) # return iterable
mapped_disp = list(mapped)
print(mapped_disp)

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

point = (10, 20)
print(point, type(point))

point[0]

x, y = point

print("x-coordinate: ", x)
print("y-coordinate: ", y)

#point[0] = 20

params_bracket = {"parameter1": 1.0,
                  "parameter2": 2.0,
                  "parameter3": 3.0}

# Alternatively:

params_dict = dict(parameter1=1.0,
                   parameter2=2.0,
                   parameter3=3.0)

print(type(params_dict))
print(params_dict)

print("p1 =", params_bracket["parameter1"])
print("p2 =", params_bracket["parameter2"])
print("p3 =", params_dict["parameter3"])

# Substitutions
params_bracket["parameter1"] = "A"
params_bracket["parameter2"] = "B"

# Add a key with a specific value
params_bracket["parameter4"] = "D"

print("p1 =", params_bracket["parameter1"])
print("p2 =", params_bracket["parameter2"])
print("p3 =", params_bracket["parameter3"])
print("p4 =", params_bracket["parameter4"])

del params_bracket["parameter4"]
print(params_bracket)

print("parameter1" in params_bracket)
print("parameter6" in params_bracket)

#params_bracket["parameter6"]

print(params_bracket.items())
print(params_bracket.values())
print(params_bracket.keys())

print(list(params_bracket.values()))
print([*params_bracket.values()])  #  equivalent

statement1 = False
statement2 = False

if statement1:
    print("statement1 is True")
elif statement2:
    print("statement2 is True")
else:
    print("statement1 and statement2 are False")

if statement1:
    print("statement1 is True")

statement1 = statement2 = True

if statement1:
    if statement2:
        print("both statement1 and statement2 are True")

statement1 = True 

if statement1:
    print("printed if statement1 is True")
    print("still inside the 'if' block")


statement1 = False

if statement1:
    print("printed if statement1 is True")
print("no more in the 'if' block")

for x in [1, 2, 3]:
    print(x)

for x in range(4): # range starts at 0 and create an iterator (0, 1, 2,..., n-1)
    print(x)

for x in range(-3,3):
    print(x)

for word in ["calcul", "scientifique", "en", "python"]:
    print(word)

for letter in "calcul":
    print(letter)

print(params_bracket)
for key, value in params_bracket.items():
    print(key, " = ", value)

params_bracket.items()

for key in params_bracket:
    print(key)
    print(params_bracket[key])
    print('------')

# Initialize list of players
players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"] 
  
# Initialize their scores 
scores = [100, 15, 17, 28, 43]  
  
# printing players and scores 
for pl, sc in zip(players, scores): 
    print(f"Player :  {pl}     Score : {sc}")


for player_idx, player_name in enumerate(players):
    print("Player index: {0}, Player name: {1}".format(player_idx, player_name))

import copy
s = "HelLo WorLd!!"  # use lower() to get lowercase letters.

code = {'e': 'a', 'l': 'm', 'o': 'e'}
# REM: possibly use +=1 that allow incrementing in place...
s = 'Hello world!'

def cesar(s,code):
    s_code = s
    for (k,v) in zip(code.keys(),code.values()):
        s_code = s_code.replace(k,v)
        print(s_code)
    return(s_code)
sc = cesar(s,code)
print(sc)

my_inverted_code = {value: key for key, value in code.items()}
print(cesar(sc,my_inverted_code))
          

#s_code = ''

# XXX TODO
# solution: s_code = 'Hamme wermd!'

#s_decoded = ''

# XXX TODO
# solution: s_decoded = 'Hello world!'

ll = [x ** 2 for x in range(0,5)]

print(ll)

# This is an alternative to
ll = list()
for x in range(0, 5):
    ll.append(x ** 2)

print(ll)

# And for  `caml` fluent users, a map point of view
print(map(lambda x: x ** 2, range(5)))

i = 0
while i < 5:
    print(i)
    i += 1

print("OK, it stopped at i={}".format(i-1))

def func0():
    print("test")

func0()

def func1(s):
    """Display a string and its length."""
    print(s, "est de longueur", len(s))

print(func1("test"))
print(func1([1, 2, 3]))

def square(x):
    """Compute x**2."""
    return x * x

print(square(4))

def powers(x):
    """Compute the first power of x up to x**4."""
    return x * x, x * x * x, x * x * x * x

print(powers(3))
x2, x3, x4 = powers(3)
print(x2, x3)
print(type(powers(3)))
out = powers(3)
print(len(out))
print(out[1])
print(out[2])

t = (3,)
print(t, type(t))
x2, x3, x4 = powers(3)
print(x3)

def myfunc(x, p=2, verbose=False):
    if verbose:
        print("evaluate myfunc with x =", x, "and exponent p =", p)
    return x**p

myfunc(5)
myfunc(5, 3)
myfunc(5, verbose=True)

myfunc(p=3, verbose=True, x=7)

def quicksort(ll):
    # XXX TODO
    return # XXX TODO

def spam(arg1=None):
    if arg1 is not None:
        print(arg1)
        # arg1 was specified, do something clever!

def varargin(*args):
    for i in args: print(i, end=" ")
    print("\n")

varargin(3,4,5)

def multiple_argout(x, y):
    return ((y, x))

print(multiple_argout(1, 2))
varargin(multiple_argout(1, 2)) # print a single tuple
varargin(*multiple_argout(1, 2)) # print each element separately

values = { 'x': 1, 'y': 2 }
print(multiple_argout(**values))
varargin(*multiple_argout(**values))
def varargin_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, " = ", value)
    print("\n")
    
varargin_kwargs(**values)
#varargin_kwargs(values)  # raise an error