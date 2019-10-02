---
title: "Writing Better Code"
teaching: 20
exercises: 50
questions:
- "How can I make my code more readable and understandable?"
objectives:
- "Explain the benefits of making your code more readable."
- "Rename variables, functions and methods to be more descriptive."
- "Use comments to describe code behaviour where needed."
- "Use docstrings to specifically describe the behaviour functions, methods, and modules."
keypoints:
- "Always assume that someone else will read your code at a later date, including yourself."
- "Rename variables, functions and methods to add context to make your code more readable."
- "Add comments to explain *why* something was done in a certain way if not obvious."
- "Refrain from adding code comments that just restate what code clearly already does."
- "Use docstrings contained within `\"\"\"` at the start of functions, methods and modules to explain behaviour and input/output parameters."
- "Python Enhancement Proposals (or PEPs) describe a recommended convention or specification for how to do something in Python."
---

Executable code is for machines, whilst source code is for humans. Generally speaking, code is write once, read many. So we should ensure our code is readable and understandable by both others and also ourselves when we come back to it later. Let's look at a few key ways we can do this in our code, using Python as an example language, then look at using these techniques to improve our Managing Academics and Numpy/Matplotlib code we wrote earlier.

## Naming Things

The careful selection of names is very important to understanding. Cryptic names of components, modules, classes, functions, arguments, exceptions and variables can lead to confusion about the role that these components play.

Good naming is fundamental to good design, because source code represents the most detailed version of our design. Compare and contrast the ease with which the following statements can be understood:

~~~
out(p(f(v), 2) + 1)

print(process(fibonacci(argument), 2) + 1)
~~~
{: .language-python}

There are common naming recommendations:

- Modules, components and classes are typically *nouns* (e.g. Molecule, BlackHole, DNASequence)
- Functions and methods are typically *verbs* (e.g. spliceGeneSequence, calculateOrbit)
- Boolean functions and methods are typically expressed as *questions about properties* (e.g. isStable, running, containsAtom)


## Documenting your Code

### Comments

Source code tells the reader what the code does. Comments allow us to provide the reader with additional information - it's always a good idea to keep others in mind when writing code.

A good rule of thumb is to assume that someone will **always** read your code at a later date, and this includes a future version of yourself. It can be easy to forget why you did something a particular way in six months time.

The reader should be able to understand a single function or method from its code and its comments, and should not have to look elsewhere in the code for clarification. It can be easy to get lost in code, and others will not have the same knowledge of our project or code as we do.

The kind of things that need to be commented are:

- Why certain design or implementation decisions were adopted, especially in cases where the decision may seem counter-intuitive
- The names of any algorithms or design patterns that have been implemented
- The expected format of input files or database schemas

There are some restrictions. Comments that simply restate what the code does are redundant, and comments must be accurate, because an incorrect comment causes more confusion than no comment at all.


### Docstrings

If the first thing in a function is a string that isn't assigned to a variable, that string is attached to the function as its documentation, e.g.:

~~~
def fibonacci(n):
  """Calculate the Fibonacci number of the given integer.

  If the input value n <= 0 then 0 is assumed.

  :param n: integer
  :returns: fibonacci number
  """
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
~~~
{: .language-python}

Note here we are also explicitly documenting our input variables and what is returned by the function. Along with a helpful description of what the function does, this information can act as a *contract* for readers to understand what to expect in terms of behaviour when using the function, as well as how to use it.

A comment string like this is called a *docstring*. We don't need to use triple quotes when we write one, but if we do, we can break the string across multiple lines. This also applies to Python modules, which are essentially files of Python functions, and methods within classes.

> ## Python PEP 257 - recommendations for docstrings
>
> Python Enhancement Proposals (PEP for short) are design documents for the Python community, typically specifications or conventions for how to do something in Python, a description of a new feature in Python, etc. PEP 257 deals with docstring conventions to standardise how they are used. In PEP 257, for example, on the subject of module-level docstrings:
>
> ~~~
> The docstring for a module should generally list the classes, exceptions and functions (and any other objects) that are exported by the module, with a one-line summary of each. (These summaries generally give less detail than the summary line in the object's docstring.) The docstring for a package (i.e., the docstring of the package's __init__.py module) should also list the modules and subpackages exported by the package.
> ~~~
>
> There are many other PEPs, and we'll be looking into another of these which defines conventions for Python coding style later.
{: .callout}

So at the beginning of a module file we can just add a docstring explaining the nature of a module. For example, if `fibonacci()` was included in a module with other functions, our module could have at the start of it:

~~~
"""A module for generating numerical sequences of numbers that occur in nature.

Functions:
  fibonacci - returns the Fibonacci number for a given integer
  golden_ratio - returns the golden ratio number to a given Fibonacci iteration
  ...
"""
...
~~~
{: .language-python}

We'll be revisiting module-level docstrings later.

A number of different docstring formats exist:

- reST - based on reStructuredText. This is probably more prevalent nowadays, and is used by default in PyCharm
- Epytext - historically based on a format of docstrings used for Java, in their javadoc documentation
- Google - they have their own format
- numpydoc - recommended by Numpy, based on the Google format, quite verbose

The format we're using here for our examples is reST.

> ## Improved Commenting for our Temperature Functions
>
> Take a look back at the temperature functions we wrote earlier in the course:
>
> ~~~
> def fahr_to_cels(fahr):
>     # Convert temperature in Fahrenheit to Celsius
>     cels = (fahr + 32) * (5 / 9)
>     return cels
>
> def fahr_to_kelv(fahr):
>     # Convert temperature in Fahrenheit to Kelvin
>     cels = fahr_to_cels(fahr)
>     kelv = cels + 273.15
>     return kelv
> ~~~
> {: .language-python}
>
> Turn each of these comments into Python docstrings that explain briefly what the function does, its arguments, and what the function returns.
>
> > ## Solution
> > ~~~
> > def fahr_to_celsius(fahr):
> >     """Convert Fahrenheit to Celsius.
> >
> >     Uses standard Fahrenheit to Celsius formula
> >
> >     :param fahr: float temperature in Fahrenheit
> >     :returns: float temperature in Celsius
> >     """
> >     celsius = ((fahr - 32) * (5/9))
> >     return celsius
> >
> > def fahr_to_kelvin(fahr):
> >     """Convert Fahrenheight to Kelvin.
> >
> >     Uses standard Fahrenheit to Kelvin formula
> >
> >     :param fahr: float temperature in Fahrenheit
> >     :returns: float temperature in Kelvin
> >     """
> >     kelvin = fahr_to_celsius(fahr) + 273.15
> >     return kelvin
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Improving our Managing Academics and Data Analysis Codes
>
> After writing code and getting it to work, it's a good habit to reflect on what you've written and see if it's readability can be improved.
> See if you can improve your Managing Academics code you wrote in both the object oriented and recursive paradigms, and your Numpy/Matplotlib code, by doing the following:
>
> - Rename your variables, functions, and methods to be more descriptive appropriate to their context.
> - Add comments and docstrings to describe behaviour.
>
> Discuss and compare your improvements to each of these codes with someone next to you. Based on your discussions, can you further improve your code in the above ways?
{: .challenge}

Commenting and adding docstrings to code is important to describe how our code behaves. Another approach to improve the readability and understandability of our code is *refactoring*, a process where we change the code itself, which we've touched on with renaming. There are other ways we can refactor our code by addressing issues with control flow and modularity, which we'll look at later.

{% include links.md %}