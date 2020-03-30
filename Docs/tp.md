# Documentation with Sphinx

## reStructuredText

### Introduction

Sphinx is an  extension of [reStructuredText](https://docutils.sourceforge.io/rst.html). reStructuredText (RST, ReST, or reST) is a file format for textual data used primarily in the Python programming language community for technical documentation.

It is part of the [`Docutils`](https://docutils.sourceforge.io/) project of the Python Doc-SIG (Documentation Special Interest Group), aimed at creating a set of tools for Python similar to Javadoc for Java or Plain Old Documentation (pod) for Perl. `Docutils` can extract comments and information from Python programs, and format them into various forms of program documentation.

In this sense, reStructuredText is a lightweight markup language designed to be both:

1. processable by documentation-processing software such as `Docutils`,
2. easily readable by human programmers who are reading and writing Python source code.

Reference: <https://en.wikipedia.org/wiki/ReStructuredText>, <https://en.wikipedia.org/wiki/Comparison_of_document-markup_languages> and <https://en.wikipedia.org/wiki/Comparison_of_documentation_generators>

### Syntax

A ReST file is a plain text file with a `.rst` extension. Alike Markdown (`.md`) it allows to easily write formatted text.

#### Headers

```rst
Section Header
==============

Subsection Header
-----------------
```

#### Lists

```rst
- A bullet list item
- Second item

  - A sub item

- Spacing between items creates separate lists

- Third item

1) An enumerated list item

2) Second item

   a) Sub item that goes on at length and thus needs
      to be wrapped. Note the indentation that must
      match the beginning of the text, not the
      enumerator.

      i) List items can even include

         paragraph breaks.

3) Third item

#) Another enumerated list item

#) Second item
```

#### Images

```rst

.. image:: /path/to/image.jpg
   :height: 100
   :width: 200
   :scale: 50
   :align: center
   :alt: ordinateur

   Caption text rendered below the image...
```

#### Named links and anonymous links

A sentence with links to \`Wikipedia\`_ and the \`Linux kernel archive\`_.

```rst
.. _Wikipedia: https://www.wikipedia.org/
.. _Linux kernel archive: https://www.kernel.org/
```

Another sentence with an \`anonymous link to the Python website\`__.

```rst
__ https://www.python.org/
```

N.B.: named links and anonymous links are enclosed in grave accents (`), and not in apostrophes (').

N.B.: it is possible to create references to label linked to an image, a section, in the `.rst` file etc...

#### Literal blocks

```rst
::

  some literal text

This may also be used inline at the end of a paragraph, like so::
```

  some more literal text

```rst
.. code:: python

   print("A literal block directive explicitly marked as python code")
```

## Set up the doc

Reference: this part is mainly from the Sphinx documentation <http://www.sphinx-doc.org/en/stable/>.

The documentation is usually located in a `docs` or `doc` folder located at the root of a project. For instance in the `biketrauma` module we have:

```bash
packaging_tutorial/
    biketrauma/
        __init__.py
        data/
        vis/
        io
        tests/
    doc/
    setup.py
    .gitignore
```

In the Sphinx terminology, this `doc` folder is called the [source directory](http://www.sphinx-doc.org/en/stable/glossary.html#term-source-directory). It contains:

1. a configuration file `conf.py` with all the information needed to read the sources and build the doc. By building, I mean the process of generating the doc (usually in `html`, `pdf`, etc...) from the ReST files.
2. a directory structure containing `.md` or `.rst` files with the doc.

To help you, Sphinx comes with a script called `sphinx-quickstart` that sets up a source directory and creates a default `conf.py` with the most useful configuration values from a few questions it asks you. To use this, run:

```bash
$ sphinx-quickstart
```

Answer each question asked. Be sure to say **yes** to the `autodoc` extension, as we will use this later. There is also an automatic “API documentation” generator called `sphinx-apidoc`; see [`sphinx-apidoc`](http://www.sphinx-doc.org/en/stable/man/sphinx-apidoc.html) for details.

**Exercise:** Set up the documentation for `biketrauma`

1. Install the sphinx package with pip
2. Create a `doc` folder and `cd` into it
3. Launch `sphix-quickstart`.

## Defining documentation structure

Let’s assume you’ve run `sphinx-quickstart`. It created a source directory with `conf.py` and a master document, `index.rst` (if you accepted the defaults).

The main function of the master document is to serve as a welcome page, and to contain the root of the “table of contents tree” (or `toctree`). This is one of the main things that Sphinx adds to reStructuredText, a way to connect multiple files to a single hierarchy of documents.

The `toctree` directive initially is empty, and looks like so:

```rst
.. toctree::
   :maxdepth: 2
```

You add documents listing them in the content of the directive:

```rst
.. toctree::
   :maxdepth: 2

   usage/installation
   usage/quickstart
   ...
```

This is exactly how the `toctree` for this documentation looks. The documents to include are given as document names, which in short means that you leave off the file name extension and use forward slashes (/) as directory separators.

**Exercise:**

1. Update the `index.rst`: by adding an image located at <https://aenkg.info/img/a167ed14c4655893357e586ec3d6704f.jpg> just below the title of the page
2. Install the `read_the_doc` theme as explained [here](https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html#via-python-package). Interested people can read <http://www.sphinx-doc.org/en/stable/theming.html>.
3. Create the corresponding directory and files in order to add a, 
     - A `Installation` section with few sentences a code snippet that explain how to install `biketrauma`
     - A `Documentation` section with subsections `io` and `visu` each one containing a title and few lines of text.

## Building the doc

During the configuration of Sphinx, a text file called `MakeFile` has been created: In software development, `Make` is a build automation tool that automatically builds executable programs and libraries from source code by reading files called `Makefiles` which specify how to derive the target program. 

Reference: <https://en.wikipedia.org/wiki/Make_(software)>

```bash
$ make html
```

Then to access the web pages created:

```bash
$ firefox _build/html/index.html
```

N.B.: there is also a [sphinx-build](http://www.sphinx-doc.org/en/stable/man/sphinx-build.html) tool that can help you to build without make.

**Exercise:**

1. list all the `target` defined in the `Makefiles`
2. Build your doc and visualize it with a navigator

## API doc (autodoc)

When documenting Python code, it is common to put a lot of documentation in the source files, in documentation strings. Sphinx supports the inclusion of [`docstrings`](https://www.python.org/dev/peps/pep-0257/) from your modules with an extension (an extension is a Python module that provides additional features for Sphinx projects) called `autodoc`.

In order to use `autodoc`, you need to activate it in `conf.py` by putting the string `'sphinx.ext.autodoc'` into the list assigned to the extensions config value. Then, you have a few additional directives at your disposal.

For example, to document the function `io.open()`, reading its signature and docstring from the source file, you’d write this:

```rst
.. autofunction:: io.open
```

You can also document whole classes or even modules automatically, using member options for the auto directives, like

```rst
.. automodule:: io
   :members:
```

`autodoc` needs to import your modules in order to extract the docstrings. Therefore, you must add the appropriate path to `sys.path` in your `conf.py`.

**Exercise:**

1. Write a docstring for the class `biketrauma.io.Load_db` and the function `plot_location`
2. Integrate these documentations in a section called `API` in the sphinx toctree.

## Sphinx-Gallery

TODO!