# HMMA 238

(Almost) everything you need to know as an applied mathematician concerning coding and system admin.

## Teachers

- Joseph Salmon : joseph.salmon@umontpellier.fr,
- Benjamin Charlier : benjamin.charlier@umontpellier.fr
- Florent Bascou : florent.bascou@umontpellier.fr

## Office hours

 Thursday 18h-19h, ___appointment by email only___.

## Web page

<https://github.com/bcharlier/HMMA238>
<https://github.com/HMMA238-2021/>

## Prerequisite

Students are expected to know basic notions of probabilities, optimization, linear algebra and statistics.

## Course description

This course focuses on discovering good coding practices (the language used being Python, but some element of bash and git will also be useful) for professional coding.
A special focus on data processing and visualization will be at the heart of the course.
We will mostly focus on basic programming concepts, as well as on discovering the Python scientific libraries, including ```numpy, scipy, pandas, matplotlib, seaborn```.
Beyond `pandas` ninja skills, we will also introduce modern practices for coders : (unitary) tests, version control, documentation generation, etc.

## Grading

### Project (60% of the final grade)

- Projects will be by predefined (at random) groups of 3.

- Expected work : a ```github``` repository where the work is available. A precise description will be given with the subjects.
The ```github``` repository will contain at least a (markdown) Readme file introducing your work. All the code will be placed in a directory called */Code*, a tex/pdf or `jupyter notebook`  will be put in a */Report* directory and your final beamer/power point presentation (in an open source format) will be set in `/Beamer` directory.
The later will be a short presentation of the work that will be orally presented during 15mn in front of a jury.

- Due date (mid-term project snapshot) : TBD. This will include the creation of a ```github``` repository, a short description on how the work is split and a detailed work program for the second part of the project.

- Due date (final project) : Week 16. The ```github``` repository should be completed before this date (nothing pushed later will be taken into account).

**Warning:** the project repository must show a balanced contribution between group members and intra-group grades variation could be made to reflect issues on the intra-group workload balance.

### Practical / Homework (25% of the final grade)

- A small challenge based on a real dataset. This will be a personal work.

- Due date : Week 13.

### Tests (15% of the final grade)

- Thre short tests of 15 min each (on moodle). This will be a personal work.
- Due date : Week 6, 9 and 12.

## Bonus

1 supplementary point on the final grade of the course can be obtained for contributions improving the course material (Practicaks, Readme, etc...) under the following constraints :

- only .5 point is given for a contribution,
- only the first contribution proposed on a theme is rewarded (no point given for followers!),
- documented pull-requests (PR) are expected : details are expected to help judging what the proposition improves/corrects,
- for typos at least 5 corrections are expected to receive .5 point. The corrections should be gathered in **single PR**.
- each student can only get 1 point maximum through bonuses.

## (Tentative) Course schedule

1. BC : (20/01) [intro to linux essentials and command line tools: bash, regexp, grep, find, rename](Bash/),

2. BC : (21/01) [python virtual env: Anaconda](Venv/), [Python virtual environment](Venv/), [IDE: VScode](IDE/),

3. BC : (27/01) [git: a first introduction, `github`, ssh key creation, various git commands, conflict, pull request](Git/)

4. JS : (28/01) [coding : algorithms, modules, basic types, functions, loops](Intro-Python/) [coding : list, dictionary, tuples, if statement and loops, exceptions](Intro-Python/)

5. BC : (03/02) [hands on git](Git/), [classes (`__init__`, `__call__`, etc...), operator overloading, files handling](Intro-Python/)

6. JS : (04/02) [`numpy` : basics on matrices (arrays), slicing, simple linear algebra, masking; `matplotlib`: first plots](Numpy-Matplotlib/)

7. BC : (10/02) [Create a Python Module](Python-modules/)

8. JS : (11/02) [`numpy` : casting, concatenation, `imshow`, `meshgrid`, casting, copy](Numpy-Matplotlib/);  [`scipy`: EDO, Interpolation, Optimize](Scipy/)

9. JS : (17/02) [`scipy`: Images/channel, FFT](Scipy/), [Pandas: missing data](Pandas/)

10. JS : (18/02) [Pandas: first steps](Pandas/)

11. BC : (03/03) [Create a Python Module](Python-modules/), [unit tests](Tests-CI/)

12. JS : (04/03) [Pandas: more on that](Pandas/)

13. BC : (10/03) [unit test](Tests-CI/)

14. BC : (17/03) [Documentation with Sphinx](Docs/)

15. JS : (18/03) [Sparse Matrices and graphs and memory](TempsMemoire/)

16. BC : (31/03) pytorch? 

17. JS : (01/04) [Numba](Numba/)

18. JS : (08/04) [Statsmodels](Statsmodels/)

19. JS : (19/04) Oral examination

20. BC : (20/04) Oral examination

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
- Exceptions to move from main -> specific notebook;

## Utils

Some useful extensions:

```bash
conda install -c conda-forge jupyter_contrib_nbextensions
conda install -c conda-forge nbstripout
```
