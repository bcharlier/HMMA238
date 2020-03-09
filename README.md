# HMMA 238

(Almost) everything you need to know as a applied mathematician concerning coding and system admin.

## Teachers

- Joseph Salmon : joseph.salmon@umontpellier.fr,
- Benjamin Charlier : benjamin.charlier@umontpellier.fr

## Office hours

 Thursday 18h-19h, ___appointment by email only___.

## Web page

<https://github.com/bcharlier/HMMA238>

## Prerequisite

Students are expected to know basic notions of probabilities, optimization, linear algebra and statistics.

## Course description

This course focuses on discovering good coding practices (the language used being Python, but some element of bash and git will also be useful) for professional coding.
A special focus on data processing and visualization will be at the heart of the course.
We will mostly focus on basic programming concepts, as well as on discovering the Python scientific libraries, including ```numpy, scipy, pandas, matplotlib, seaborn```.
Beyond Pandas skills, we will also introduce modern practices for coders : (unitary) tests, version control, documentation generation, etc.

## Grading

### Project (70% of the final grade)

- Projects will be by predefined (at random) groups of 2 or 3.
- The list will be available soon (TODO)
- Expected work : a ```github``` repository where the work is available A precise description will be given with the subjects.
The ```github``` repository will contain at least a (markdown) Readme file introducing your work. All the code will be placed in a directory called */Code*, a tex/pdf or `jupyter notebook`  will be put in a */Report* directory and your final beamer/power point presentation (in an open source format) will be set in `/Beamer` directory.
The later will be a short presentation of the work that will be orally presented during 15mn in front of a jury.

- Due date : April 20.
The ```github``` repository should be completed before this date (nothing pushed later will be taken into account).

**Warning:** the project repository must show a balanced contribution between group members and intra-group grades variation could be made to reflect issues on the intra-group workload balance.

### Mid-term project snapshot (10% of the final grade)

- This will include the creation of a ```github``` repository, a short description on how the work is split and a detailed work program for the second part of the project.
- Due date : March (TBD)

### Practical / Homework (20% of the final grade)

- This is a classical homework, where a ```jupyter notebook``` will be graded. This will be a personal work.
- Due date : March (TBD)

## (Tentative) Course schedule

1. BC : (22/01) [coding : algorithms, modules, basic types, functions, loops](Intro-Python/)
2. JS : (23/01) [coding : list, dictionary, tuples, if statement and loops, exceptions](Intro-Python/)
3. BC : (29/01) [classes (`__init__`, `__call__`, etc...), operator overloading, files handling](Intro-Python/), [git: a first introduction](Git/)
4. JS : (30/01) [`numpy` : basics on matrices (arrays), slicing, simple linear algebra, masking; `matplotlib`: first plots](Numpy-Matplotlib/)
5. BC : (05/02) [`github`, ssh key creation, various git commands, conflict, pull request](Git/)
6. JS : (06/02) [`numpy` : casting, concatenation, `imshow`, `meshgrid`, casting, copy](Numpy-Matplotlib/);  [`scipy`: EDO, Interpolation, Optimize](Scipy/)
7. BC : (12/02) [hands on git](Git/), [intro to linux essentials and command line tools](Bash) 
8. JS : (13/02) [`scipy`: Images/channel, FFT](Scipy/), [Pandas: missing data](Pandas/)
9. BC : (26/02) [bash, regexp, grep, find, rename](Bash/), [Python virtual environment](Venv/)
10. JS : (27/02) [Pandas: first steps](Pandas/)

11. BC : (04/03) [Python virtual env: Anaconda](Venv/), [IDE: VScode](IDE/), [Create a Python Module](Python-modules/)

12. JS : (05/03) [Pandas: more on that](Pandas/)

13. BC : (11/03) [Create a Python Module](Python-modules/), [unit tests](Tests-CI/)

14. BC : (18/03)

15. JS : (19/03)

16. JS : (26/03)

17. BC : (31/03) (1.5h course only)

18. JS : (02/04)

19. JS+BC : (21/04) Oral examination

20. JS+BC : (28/04) Oral examination

## Bonus

2 supplementary points on the final grade of the course can be obtained for contributions improving the course material (notebooks, Readme, etc.) under the following constraints :

- only 1 point is given for a contribution,
- only the first contribution proposed on a theme is rewarded (no point given for followers...),
- documented pull-requests are expected : details are expected to help judging what the proposition improves/corrects,
- for typos at least 5 corrections are expected to receive 1 point,
- each student can only get 2 points maximum through bonuses.

## Books and other resources

The main resource for the course is available on the present `github` repository, with additional elements available in the file [IntroPython.pdf](http://josephsalmon.eu/enseignement/Montpellier/HLMA310/IntroPython.pdf).

### Additional resources

- (General) Skiena, *The algorithm design manual*, 1998
- (General) Courant et al. , *Informatique pour tous en classes préparatoires aux grandes écoles : Manuel d'algorithmique et programmation structurée avec Python*,
2013, (french)
- (General/data science) Guttag, *Introduction to Computation and Programming*,
2016
- (Data Science) : J. Van DerPlas, *Python Data Science Handbook, With Application to Understanding Data*, 2016
<https://jakevdp.github.io/PythonDataScienceHandbook/>
- (Code and style) Boswell et Foucher, *The Art of Readable Code*, 2011
- (Python) <http://www.scipy-lectures.org/>
- (Visualization) <http://openclimatedata.net/>

## TODOS (for teachers only)

- change language (FR->EN) for all notebooks
- possibly set a shared file for graphics
- Un-merge ```numpy/matplotlib``` notebooks
- SparseMatrix notebook might be split with element put in ```numba```???

## Utils

Some useful extensions:

```bash
conda install -c conda-forge jupyter_contrib_nbextensions
conda install -c conda-forge nbstripout
```
