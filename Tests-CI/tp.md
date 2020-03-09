# Unit Tests and integration tests

This lecture what taken from <https://amueller.github.io/COMS4995-s19/slides/aml-02-python-git-testing/#45>

## Tests

Tests are small pieces of code that are written to ensure that a part of a program is working.

### Why tests are useful

It is from the utterly importance to implement tests **during** the development step. It will help you to ensure:

- that code works correctly.
- that changes don’t break anything.
- that bugs are not reintroduced.
- robustness to user errors.
- code is reachable.

### Types of tests

There is different kinds of tests:

1. Unit tests: test if a function does the right thing.
2. Integration tests: test if the system / process does the right thing.
3. Non-regression tests: test if a bug got removed (and will not be reintroduced).

### How to test?

Many coding languages come with their own test framework. In python, we will focus on [`pytest`](http://doc.pytest.org). It is simple though powerful. `pytest` searches for all `test*.py` files and runs all `test*` methods in it. It outputs a nice errors report.

**Exercise:**

1. Install `pytest` with `pip` using the user scheme
2. Test if the command `py.test` is in your PATH (depending on your configuration you will have to add `~/.local/bin` in PATH)

### Example

Let's assume we have the file `inc.py` contains

```python
def inc1(x):
    return x + 1
```

Thence, content of `test_sample.py`

```python
from inc import inc1

# This test will work
def test_inc1():
    assert inc1(3) == 4

# This test will fail
def test_inc2():
    assert inc2(-1) == 4
```

To run these tests:

```bash
$ pytest test_inc.py
```

**Exercise:**

1. Correct the `test_inc2`test.
2. Determine the syntax to run any tests in a directory.
3. Determine the syntax to run only the test called `test_inc1`.

## Code coverage

`pytest` comes with some useful [plugins](https://docs.pytest.org/en/latest/plugins.html). In particular, we will use the coverage report plugin.

A **test coverage** is a measure used to describe the degree to which the source code of a program is executed when a particular test suite runs. A program with high test coverage, measured as a percentage, has had more of its source code executed during testing, which suggests it has a lower chance of containing undetected software bugs compared to a program with low test coverage.

```bash
pip install pytest-cov
```

The documentation can be found at <https://pytest-cov.readthedocs.io/en/latest/>. Source <https://en.wikipedia.org/wiki/Code_coverage>.

**Exercise:**

1. Install the pytest's coverage plugin.
2. Load the `biketrauma` package you can download at <>
3. Add some unit tests to `biketrauma` in a new sub-directory `biketrauma/tests/`.
    - Create a first `test_df()` that test if the Côtes-d'or departement has 459 accidents. And a second `test_df_log()` testing that the log of the number of accident in the departement 92 is close to `7.651120176`.


    - Create a `test_dl()` function that tests the md5sum hash of the downloaded file (a.k.a. `bicycle_db.csv`). It should be "ee8c4e0e7989bc6aac7876d7501bbf4d". You can use this piece of code to compute the md5sum:

```python
import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
```

You should achieve a 92% of code coverage:
```bash
----------- coverage: platform linux, python 3.7.6-final-0 -----------
Name                                    Stmts   Miss  Cover
-----------------------------------------------------------
biketrauma/__init__.py                      4      0   100%
biketrauma/io/Load_db.py                    9      0   100%
biketrauma/io/__init__.py                   3      0   100%
biketrauma/preprocess/__init__.py           0      0   100%
biketrauma/preprocess/get_accident.py       9      0   100%
biketrauma/tests/test_biketrauma.py        21      0   100%
biketrauma/vis/__init__.py                  0      0   100%
biketrauma/vis/plot_location.py             6      4    33%
-----------------------------------------------------------
TOTAL                                      52      4    92%
```

## Continuous integration

Reference: <https://help.github.com/en/actions/building-and-testing-code-with-continuous-integration/setting-up-continuous-integration-using-github-actions>