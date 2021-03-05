# HMMA 238

(Almost) everything you need to know as an applied mathematician / statistician concerning coding and system administration.

## Teachers

- Joseph Salmon : joseph.salmon@umontpellier.fr,
- Benjamin Charlier : benjamin.charlier@umontpellier.fr
- Florent Bascou : florent.bascou@umontpellier.fr

with the help of many students including:
- Amelie Vernay
- ...

## Web page

<https://github.com/bcharlier/HMMA238>

<https://github.com/HMMA238-2021/>

## Prerequisite

Students are expected to know basic notions of probabilities, optimization, linear algebra and statistics for this course.
Some rudiments on coding is also expected (if, for, while, functions) but not mandatory.

## Course description

This course focuses on discovering good coding practices (the language used being Python, but some element of bash and git will also be useful) for professional coding.
A special focus on data processing and visualization will be at the heart of the course.
We will mostly focus on basic programming concepts, as well as on discovering the Python scientific libraries, including ```numpy, scipy, pandas, matplotlib, seaborn```.
Beyond `pandas` ninja skills, we will also introduce modern practices for coders : (unitary) tests, version control, documentation generation, etc.


## (Tentative) Course schedule

1. BC : (20/01) [Introduction to linux essentials and command line tools: bash](Courses/Bash/),

2. BC : (21/01) [Introduction to linux essentials and command line tools: regexp, grep, find, rename](Courses/Bash/),

3. BC : (27/01) [IDE: VScode](Courses/IDE/), [Python virtual env: Anaconda](Courses/Venv/), [Python virtual environment](Courses/Venv/), [Git: a first introduction, `github`, ssh key creation, various git commands, conflict, pull request](Courses/Git/); see also [Bonus/](Bonus/)

4. JS : (28/01) [Coding : algorithms, modules, basic types, functions, loops](Courses/Intro-Python/) [coding : list, dictionary, tuples, if statement and loops, exceptions](Courses/Intro-Python/)

5. BC : (03/02) [hands on git](Courses/Git/)

6. JS : (04/02) [`numpy` : basics on matrices (arrays), slicing, simple linear algebra, masking; `matplotlib`: first plots](Courses/Numpy-Matplotlib/)

7. BC : (10/02) [Some git again](Courses/Git/), 

8. JS : (11/02) [`numpy` : casting, concatenation](Courses/Numpy-Matplotlib/);

9. JS : (17/02) [`numpy` / `matplotlib`: `imshow`, `meshgrid`, copy](Courses/Numpy-Matplotlib/);

10. JS : (18/02) [`scipy`: EDO, Interpolation, Optimize](Courses/Scipy/)

11. BC : (03/03) [classes (`__init__`, `__call__`, etc...), operator overloading, files handling](Courses/Classes_n_Exceptions/), [Create a Python Module](Courses/Python-modules/)

12. JS : (04/03) [`scipy`: Images/channel](Courses/Scipy/), [Pandas: first steps / missing data](Courses/Pandas/)

13. BC : (10/03) [Create a Python Module](Courses/Python-modules/), [unit tests](Courses/Tests-CI/)

14. BC : (17/03) [Documentation with Sphinx](Docs/)

15. JS : (18/03) [Sparse matrices, graphs and memory](Courses/TempsMemoire/)

16. BC : (31/03) pytorch?

17. JS : (01/04) [Numba](Courses/Numba/)

18. JS : (08/04) [Statsmodels](Courses/Statsmodels/)

19. JS-BC : (19/04) Oral examination

20. JS-BC : (20/04) Oral examination

## Grading

### Challenge (25% of the final grade)

- A small challenge based on a real datasets. This will be a personal work, and includes an aesthetic part and prediction part.

- Due date : 23:59 Thursday, April 1st.

- More information on the challenge is available at [Challenge 2020-2021](Challenge/2020-2021)

### Tests (15% of the final grade)
Three short tests of 15 min each (on Moodle). This will be a personal work.

- Quiz 1 (**Week 6**)
- Quiz 2 (**Week 10**)
- Quiz 3 (**Week 12**)

### Project (60% of the final grade)

**Warning:** the precise details of the projects might evolve before the allocation phase, and a precise grid will be given in the project section.

**Warning:** the project repository must show a balanced contribution between group members and intra-group grades variation could be made to reflect issues on the intra-group workload balance.


## Bonus

**1 supplementary point** on the final grade of the course can be obtained for contributions improving the course material (practicals, Readme, etc.).
See the [Bonus](Bonus/) section for more details on how to proceed.


## Books and other resources

The resources for the course are available on the present `github` repository. Additional elementary elements (**in French**) on Python are available in the course [HLMA310](http://josephsalmon.eu/HLMA310.html) and the associated lectures notes [IntroPython.pdf](http://josephsalmon.eu/enseignement/Montpellier/HLMA310/IntroPython.pdf).

### Additional resources

- (General) : [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)
- (Data Science) : J. Van DerPlas, *Python Data Science Handbook, With Application to Understanding Data*, 2016<https://jakevdp.github.io/PythonDataScienceHandbook/>
- (General) Skiena, *The algorithm design manual*, 1998
- (General) Courant et al. , *Informatique pour tous en classes préparatoires aux grandes écoles : Manuel d'algorithmique et programmation structurée avec Python*,
2013, (french)
- (General/data science) Guttag, *Introduction to Computation and Programming*,
2016

    Associated videos: <http://jakevdp.githubio/blog/2017/03/03/reproducible-data-analysis-in-jupyter/>

- (Code and style) Boswell et Foucher, *The Art of Readable Code*, 2011
- (Scientific computing tools for Python) <http://www.scipy-lectures.org/>
- (Visualization) <http://openclimatedata.net/>


## Oldies (for jupyter notebook extensions)

Some useful extensions:

```bash
conda install -c conda-forge jupyter_contrib_nbextensions
conda install -c conda-forge nbstripout
```
