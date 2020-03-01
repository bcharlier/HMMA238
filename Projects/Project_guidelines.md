# Project guidelines

## Grading

The final project represents 70% of the final grade for the course. The due date is **April 20 (23h59)**.
The `github` repository should be completed before this date (nothing pushed later will be taken into account).

The project's grade (out of 20 points) will be decomposed as follows:

- 15 points for the code/notebook

- 5 points for the final defense.

Projects will be by predefined (at random) groups of 2 or 3. The list will be available on Moodle.

Moreover 10% of the final grade will be given for the milestone.

### Milestone

The milestone is due on **March 22 (23h59)** and will represent 10% of the final grade.
It will consist of the following elements:

- the `github` repository prepared with the structure described below.

- at least a creation and a branch merged in the `github` history.

- a `readme.md` file with the elements described below.

- a `work_organization.md` file describing in details the repartition of the task expected for the whole project between the team members.

- a test function that will allow you to test the (main) functions you will create for the project.

## Elements expected

- The ultimate goal is to provide a Python module that can be imported with `pip` and containing your work.
A description of the procedure will be needed (imagine you are addressing to a user not aware of your package).

- The project is stored on a `github` repository.

- You have to choose a name for your project. Hereafter, it is denoted by `my_module_name`.

- It should contain all the aspects described below.

### Project structure

- All the code will be placed in a sub-directory called `/my_module_name`.

- A `jupyter notebook` file  will be put in a `/report` sub-directory synthesizing the most interesting results you found, showing images/movies/widgets of interest.

- A presentation (in an open source format: like beamer with tex or LibreOffice Impress) will be put in a `/beamer` directory. The later will be a short presentation of the work that will be orally presented during 15mn in front of a jury.

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
