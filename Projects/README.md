# Project guidelines

- Work by groups of 4 students, assigned at random (list on the Moodle website).
- Nature of the project for the year 2020-2021 : [here](2021/)

## Timing
- **Mid-term** project snapshot: Due date **Week 12** (before Friday March 26, 23:59). This will include the creation of a ```github``` repository (README.md, etc.), a short description on how the work is split and a detailed work program for the project including how the task are attributed (coding).

- Due date (final project) : **Week 16 (TBA)**. The ```github``` repository should be completed before this date (nothing pushed later will be taken into account). The oral presentation should be recorded before Monday 19.


## Elements expected /  Grading


### Summary

|General |Details|Points (out of 20)|
|-----|--------------|----------------|
|**Mid-term**|Git / branches|2.5             |
|     |Task affectation|1               |
|**Core project : Code / Repo/ etc.**|Science Technical Problem Resolution|2.5             |
|     |Readme Comments  Pep8|1               |
|     |Unit Tests CI Deploy : wheel|2               |
|     |Class (1 class min)|0.5             |
|     |Reproducibility  Dataset loading|1               |
|     |Graphical aspects : Widgets, film, 3D, etc.|2.5             |
|     |Time efficiency Memory efficiency|1               |
|     |Documentation |2.5             |
|**Oral** |Beamer (structure, spelling)|1.5             |
|     |Clarity / lively presentation / Rhythm / Show |2               |
| **Total**| | 20|


### Details

- The ultimate goal is to provide a Python module that can be imported with `pip` and containing your work.
A description of the procedure will be needed (imagine you are addressing to a user not aware of your package).
Last year project are available in the sub-folder `2020` and a good example of what we expect is <https://github.com/tanglef/chaoseverywhere>.

- The project must be stored on a `github` repository.

- You have to choose a name for your project. Hereafter, it is denoted by `my_module_name`.

- It should contain all the aspects described below.

### Science
Solve (even partially) the problem raised in your project description.


### Project structure

- All the code will be placed in a sub-directory called `/my_module_name` (choosing your module name accordingly).

- A `jupyter notebook` file  will be put in a `/report` sub-directory synthesizing the most interesting results you found, showing images/movies/widgets of interest.

- A presentation (in an open source format: like Beamer with TeX or LibreOffice Impress) will be put in a `/beamer` directory. The later will be a short presentation of the work that will be orally presented during 15mn in front of a jury.

- A documentation (using `sphinx`) will be stored in a `/doc` sub-directory.

### Git aspects

- a (markdown) `readme.md` file introducing your work and the team member (first/last name + email).

- A `.gitignore` that prevent garbage files to be included in your project.

- equilibrated commits in two branches should be done (*e.g.,* in development branch and the master one), and merged for the milestone day.

### Object programming aspects

- you should code at least one `Python` class.

### Dataset(s)

- The data used should be available in a way that the end user do not need to perform a manual download of any kind.

### Graphical aspects

The repository will contain code of the following nature:

- a code producing a movie (either an animated gif or an avi file) with at least 200 frames created. The frames should also be stored images by images in a `temp/` directory not versioned on `github` but created on the fly.

- a widget must be proposed in the `jupyter notebook`

- histograms/kde plots illustrating the data created must also be provided.

### Time/memory evaluation

- A full study of the time and memory footprint of the code produced will be provided.

- At least one sparse matrix should be used along the project in a meaningful way (e.g., consider the `scipy.sparse.csc_matrix` module).

### Documentation

- Documentation should be added correctly for the functions written. Please use `sphinx`.

### Test and CI

- Provide unitary tests to check that the function you proposed satisfies the requirement you target.
- Implement a Continuous Integration solution with `github` that run your unitary test at each commit.

### Deploy

- It should be possible to package your Python module using `wheel` (i.e., you need to provide a `setup.py`,  file).
