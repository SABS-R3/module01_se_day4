---
title: "Community Practices"
teaching: 40
exercises: 40
questions:
- "Why should I follow community standards?"
- "What community standards exist for Python and C++?"
- "How can I make sure I'm following these standards?"
- "How should I document my projects?"
objectives:
- "Understand the benefits of following community conventions and standards"
- "Use existing tools to validate that your code conforms to community standards"
- "Learn how to make software projects shareable under an Open Source license"
- "Use existing tools to turn docstrings into documentation"
keypoints:
- "Community standards make it easier for developers to join an existing project"
- "Linters are tools used to ensure code conforms to community standards"
---

## Community Practices

### Why Docstrings?

~~~
def fibonacci(n):
    """Calculate the Fibonacci number of the given integer.

    A recursive implementation of Fibonacci.

    :param n: integer
    :raises ValueError: raised if n is less than zero
    :returns: fibonacci number
    """
    if n < 0:
        raise ValueError('Fibonacci is not defined for N < 0')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
~~~
{: .language-python}

~~~
help(fibonacci)
~~~
{: .language-python}

### Building Documentation with Sphinx

One of the most important things you can do to make it easier for others to use or extend your code is to provide documentation.
We've seen docstrings already, but wouldn't it be great if you could take the docstrings you've written and turn it into documentation that you can publish online with your code?

Sphinx lets us do exactly that, but it is a little tricky to get set up properly:

~~~
pip install --user sphinx
cd code
mkdir docs
cd docs
sphinx-quickstart
~~~
{: .language-bash}

The Sphinx quickstart tool provides us with sensible default values, but we need to do a little bit of customisation to `config.py`:

~~~
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'code'
copyright = '2019, Alice'
author = 'Alice'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
~~~
{: .language-python}

Once we've made these changes to the configuration, we need to tell Sphinx which Python files we want it to get docstrings from.
In practice we would create a new documentation page for each module, but for the sake of simplicity, we'll add our module to the main page of the documentation for now.
To the file `index.rst` we need to add:

~~~
# file: index.rst

.. automodule:: temperature
   :members:
~~~

Now, we should be ready to build our documentation:

~~~
make html
~~~
{: .language-bash}

To view our documentation, we have two options.
The simplest option is to use PyCharm to open the HTML files in our web browser - right click on `index.html` and select 'open with browser'.
Secondly, we can use a basic web server that's built in to Python to view it:

~~~
cd _build/html
python -m http.server
~~~
{: .language-bash}

The in a web browser navigate to `http://localhost:8000` and you should see the same documentation page.

When writing documentation for a real project, there are a few useful websites such as [ReadTheDocs](https://readthedocs.org/) which allow us to host our documentation online for free - for open source projects.

### Style Guides & Linting

As we have discussed this morning, one of the most important things we can do to make sure our code is accessible to others is to make sure that it is cleanly formatted and uses sensible, descriptive names.
In order to help us format our code, we generally follow guidelines known as **style guides**.
A style guide is a set of conventions that we agree upon with our colleagues, to ensure that everyone contributing to the same project is producing code which looks similar.

While a group of developers may choose the write and agree upon a new style guide unique to each project, in practice many programming languages or problem domains have a single style guide or set of style guides which is adopted almost universally.
For C++, popular style guides include the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) and the [JSF C++ Coding Standards](http://www.stroustrup.com/JSF-AV-rules.pdf).
The [C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines) are an extensive reference intended more for the creators of software engineering tools, but may be worth having a look at.
In Python, although we do have a choice of style guides available, the [**PEP8**](https://www.python.org/dev/peps/pep-0008/) style guide is used in almost all cases.

As you will have noticed by now, one of the differences between writing Python in Jupyter notebooks and writing Python in PyCharm is that with PyCharm we get recommendations for formatting our code.
The recommendations made by PyCharm are mostly taken from the PEP8 style guide.

Many tools, known as **linters**, exist to validate your code against particular community standards, but the main two to be aware of for Python are:
- `pycodestyle` (formerly known as `pep8`)
- `pylint`

We'll also have a look at `cpplint` for C++ which validates your code against the Google C++ style guide.

As well as checking for adherence to a style guide, many linters also attempt to identify suspicious parts of the code which may indicate an error has been made.
One example of this is checking that there are no unused or undefined variables - an unused or undefined variable may be the result of a typo.
Because of this, the process of linting is particularly important for languages which are not typically compiled, such as Python.
Some of the benefits of linting, such as checking for undefined variables, happen at compile time when using a compiled language such as C++, but some of the other checks are still useful when using compiled languages.

Since the Python linters `pycodestyle` (formerly `pep8`) and `pylint` are not part of the standard Anaconda distribution, we're going to have to install them outselves.
The C++ linter `cpplint` is actually written in Python, so we'll install that as well.
Most programming languages you're likely to use (C++ is an exception) come with a package manager that you can use to install dependencies.
In Python, the package manager is called `pip`:

~~~
pip install --user pycodestyle pylint cpplint
~~~
{: .language-bash}

When using `pip` we can install packages globally, or for only our user account - we'll install it just for our user account, since that won't interfere with anyone else if we're using a shared computer.

We'll come back to linting this afternoon when we look at refactoring...

### Licensing

Software licensing can be a whole topic in itself, so we'll just summarise here.
Your institution's Intellectual Property (IP) team will be able to offer specific guidance that fits the way your institution thinks about software.

In IP law, software is considered a creative work of literature, so any code you write automatically has copyright protection applied.
This copyright will usually belong to the institution that employs you, but this may be different for PhD students.
If you need to check, this should be included in your employment / studentship contract.

Since software is automatically under copyright, without a license no one may:
- copy it
- distribute it
- modify it
- extend it
- use it (unclear - this has not been properly tested in court yet)

Fundamentally there are two kinds of license, **Open Source** licenses and **Proprietary** licenses, which serve slightly different purposes.

Proprietary licenses are designed to pass on limited rights to end users, and are most suitable if you want to commercialise your software.
They tend to be customised to suit the requirements of the software and the institution to which it belongs - again your institutions IP team will be able to help here.

Open Source licenses are designed more to protect the rights of end users - they specifically grant permission to make modifications and redistribute the software to others.
There are three particularly notable Open Source licenses:
- BSD
- MIT
- GPL


### Version Control

We should mention version control here, as this is a very important aspect of collaborative software development - but we won't cover it properly, since that's coming up later in the course.
Version control allows you to track the history of all changes to your software - including being able to manage multiple people collaborating on the same files.

That's enough for now, we'll be seeing much more about it soon.


> ## Action Stations (Again)!
> This time we're going to look at a generally good example of a real software project.
>
> Imagine that your collaborators have now asked you to contribute to one of their projects.
> They've sent you a link to the repository in GitHub and want you to familiarise yourself with the code before you begin making your changes.
>
> Again in small groups, look at the repository for the [Requests library](https://github.com/psf/requests).
> Examine the contents of the repository (code, documentation, other assets) and as a group discuss what has been done to make it easier to make use of this project, both as a user and as a developer wanting to contribute.
> Make a list of things which have been done to make it easier for people to use, install, maintain, extend and generally collaborate, with this software.
> Is there anything missing that you would find useful?
>
> Make notes on your findings, and then briefly report back the top three things to the class.
> For a maximum of three minutes, for each of the three issues you found (i.e. a minute each), report back the following:
>
> 1. A few sentences description of what you've found
> 2. A few sentences on how this benefits users of developers of the software
>
> > ## Solution
> > #### Repository itself
> > - Repo name is the name of the project
> > - Documentation is extensive and clearly written
> > - Specific guidance on how to contribute to the project
> > - Project is clearly licensed
> > - Many tests - which are run automatically with every change (Continuous Integration)
> > - GitHub Issues and Pull Request functionality is being used well
> >
> > #### README.md
> > - Has a simple code example
> > - Has a list of features
> > - Shows how to install the software
> > - Has links to further documentation
> >
> > #### Code
> > - Code will structured (though we haven't taught you about structuring projects yet)
> > - No redundant files
> > - Docstrings used extensively
> > - Well commented where docstrings are not sufficient
> > - Many class, function and variable names are descriptive
> > - Follows a consistent style
> >
> > #### Bad
> > - Commit messages generally not descriptive
> > - Master branch code not fully working with all supported versions of Python (Python 2.7 tests failing)
> {: .solution}
{: .challenge}


{% include links.md %}

