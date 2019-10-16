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
- pycodestyle (formerly known as pep8)
- pylint

As well as checking for adherence to a style guide, many linters also attempt to identify suspicious parts of the code which may indicate an error has been made.
One example of this is checking that there are no unused or undefined variables - an unused or undefined variable may be the result of a typo.
Because of this, the process of linting is particularly important for languages which are not typically compiled, such as Python.
Some of the benefits of linting, such as checking for undefined variables, happen at compile time when using a compiled language such as C++.

Since the Python linters `pycodestyle` (formerly `pep8`) and `pylint` are not part of the standard Anaconda distribution, we're going to have to install them outselves.
In Python, we have access to a package manager

~~~
pip install --user pycodestyle pylint
~~~
{: .language-bash}

## Building Documentation with Sphinx

<!-- Demo, not practical -->

> ## Action Stations (Again)!
> This time we're going to look at a particularly good example of a software project.
>
> Imagine that your collaborators have now asked you to contribute to one of their projects.
> They've sent you a link to the repository in GitHub and want you to familiarise yourself with the code before you begin making your changes.
>
> Again in groups of 4 or 5, look at the repository for the [Requests library](https://github.com/psf/requests).
> Examine the contents of the repository (code, documentation, other assets) and as a group discuss what has been done to make it easier to make use of this project, both as a user and as a developer wanting to contribute.
> Make a list of things which have been done to make it easier for people to use, install, maintain, extend and generally collaborate, with this software.
> Is there anything missing that you would find useful?
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

