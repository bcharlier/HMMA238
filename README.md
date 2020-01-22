HMMA 238
========


# Teachers

- Joseph Salmon : joseph.salmon@umontpellier.fr,
- Benjamin Charlier : benjamin.charlier@umontpellier.fr

# Office hours

 Thursday 18h-19h, ___appointment by email only___.

# Webpage

https://github.com/bcharlier/HMMA238

# Prerequisite

Student are expected to know basic notions of probabilities, optimization, linear algebra and statistics.

# Course description
This course focuses on using coding practices (the language used being Python, but some element of bash and git will also be useful) for professional coding practices.
A special focus on data processing and visualization will be enforced.
We will focus on mostly on basic programming concepts, as well as discovering the Python scientific libraries, including ```numpy, scipy, pandas, matplotlib, seaborn```.
Beyond Pandas skills, we will also introduce modern practices for coders : (unitary) tests, version control, documentation generation, etc.


# Grading
## Project (70% of the final grade)

- Projects will be by predefined (at random) groups of 2 or 3.
- The list will be available soon (TODO)
- Expected work : a ```github``` repository where the work is available A precise description will be given with the subjects.
The ```github``` repository will consist of a (markdown) readme file as introduction, all the code in a directory called code, as well as a short summary of the proposed work in tex/pdf.
A short presentation of the work will be asked (using beamer for instance) of about 15mn.
Grades could be modified to reflect issues on the workload balance.
-  Due date : April 20.
The ```github``` repository should be completed before this date (nothing pushed later will be taken into account).

**Warning** : the project repository must show a balanced contribution between group members.

## Mid-term project snapshot (10% of the final grade)
- This will include the creation of the ```github``` repository how the work is split and a detailed program for the second part of the project.
- Due date : March (TBD)

## Practical / Homework (20% of the final grade)
- This is a classical homework, where a ```jupyter notebook``` will be graded. This will be a personal work.

- Due date : March (TBD)

# (Tentative) Course schedule

1. BC : (22/01) [coding : algorithms, modules, functions, objects, variables, vectors, tables, lists, dictionaries, conditions, loops (in-line, enumerate, zip, kwarg, *, tuple, future import)](Intro-Python/)
Code styling elements : pep8 / IDE/ VSCode, jupyter notebook / jupyter lab. IDE (completion with TAB, snippet)
2. JS : (23/01)
Python follow-up + ```mumpy / matplotlib``` (np.allclose, type : float, vectorization operation by line/columns) --- Elements for practice : numerical instabilities, conditioning,
simple visualizations, elementary statistics.
3. BC : (29/01)
Installation : ```conda / pip```, Development stack / problems of software development. Markdown.
Additional reading :
https://rr-france.github.io/bookrr/booksprintrr.pdf
4. JS : (30/01)
Images / videos / signal / widget / (optional : Altair).
TP : sinusoids
5. BC : (05/02)
git et github
6. JS : (06/02)
```pytest``` and tests, Debugging : ```ipdb```, CI : continuous architecture / code interdependently of the OS Travis as example link :
 https://rachelcarmena.github.io/2018/
12/12/how-to-teach-git.html
 https://amueller.github.io/COMS4995-s19/
slides/aml-02-python-git-testing/#1
7. BC : (12/02)
```bash``` / regex (```rename, find, grep```) : Create / delete / clean dataframe / simple analysis
(e.g. on cars, imdb, etc.)
8. JS : (13/02)
```pandas / seaborn```
9. BC : (26/02)
```pandas / seaborn```
10. JS : (27/02)
```statsmodels```
11. BC : (04/03)
Classes /constructors/ ```__init__``` / ```__call__``` / Practical : TBD ; ```sklearn``` (OLS, etc.).
Functions->classes (example : a=np.array([3,2]) and command a.sum() instead of
np.sum(a))
12. JS : (05/03)
graph ```networkx```/ ```igraph``` / sparse/full matrices
13. BC : (11/03) ```pytorch``` / ```autograd``` / formal calculation
14. BC : (18/03)
15. JS : (19/03) time / memory efficiency, compilation "just in time" (```numba```), profiling
Documentation : ```sphinx``` / ```doxygen```
16. JS : (26/03)
17. BC : (31/03) (1.5h course only)
18. JS : (02/04)
19. JS+BC : (21/04) Oral examination
20. JS+BC : (28/04) Oral examination



# Bonus
2 supplementary points on the final grade of the course can be obtained for contributions improving the course material (notebooks, readme, etc.) under the following constraints :
- only 1 point is given for a contribution
- only the first contribution proposed on a theme is rewarded (no point given for follo-
wers...)
- documented pull-requests are expected : details are expected to help judging what the proposition improves/corrects
- for typos at leas 5 corrections are expected to get 1 point
- each student can only get 2 points maximum through bonuses.



# Books and other resources


The main resource for the course is available on the present github repository, with additional elements presented in the file [IntroPython.pdf](http://josephsalmon.eu/enseignement/Montpellier/HLMA310/IntroPython.pdf).

## Additional resources:

- (General) Skiena, *The algorithm design manual*, 1998
- (General) Courant et al. , *Informatique pour tous en classes préparatoires aux grandes écoles : Manuel d'algorithmique et programmation structurée avec Python*,
2013, (french)
- (General/data science) Guttag, *Introduction to Computation and Programming*,
2016
- (Data Science) : J. Van DerPlas, *Python Data Science Handbook, With Application to Understanding Data*, 2016
https://jakevdp.github.io/PythonDataScienceHandbook/
- (Code and style) Boswell et Foucher, *The Art of Readable Code*, 2011
- (Python) http://www.scipy-lectures.org/
- (Visualization) http://openclimatedata.net/


# TODOS (for teachers only):

- change language (FR->EN) for all notebooks

- possibly set a shared file for graphics

- Un-merge ```numpy/matplotlib``` notebooks

- SparseMatrix notebook might be split with element put in ```numba```???


