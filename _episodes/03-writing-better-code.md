---
title: "Writing Better Code"
teaching: 70
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---
FIXME

## Naming Variables

The careful selection of names is very important to understanding. Cryptic names of components, modules, classes, functions, arguments, exceptions and variables can lead to confusion about the role that these components play.

Good naming is fundamental to good design, because source code represents the most detailed version of our design. Compare and contrast the ease with which the following statements can be understood:

~~~
out(p(f(v), 2) + 1)

print(power(fibonacci(argument), 2) + 1)
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

The reader should be able to understand a single function or method from its code and its comments, and should not have to look elsewhere in the code for clarification. It can be easy to get lost in code, and others  will not have the same knowledge of our project or code as we do.

The kind of things that need to be commented are:

- Why certain design or implementation decisions were adopted, especially in cases where the decision may seem counter-intuitive
- The names of any algorithms or design patterns that have been implemented
- The expected format of input files or database schemas

There are some restrictions. Comments that simply restate what the code does are redundant. Comments must be accurate, because an incorrect comment causes more confusion than no comment at all.



### Docstrings

If the first thing in a function is a string that isn't assigned to a variable, that string is attached to the function as its documentation, e.g.:

~~~
FIXME
~~~
{: .language-python}


A string like this is called a docstring. We don't need to use triple quotes when we write one, but if we do, we can break the string across multiple lines. This also applies to modules

> ## Improved Commenting for our Functions
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
> >     Arguments:
> >     fahr -- the temperature in Fahrenheit
> >     """
> >     celsius = ((fahr - 32) * (5/9))
> >     return celsius
> >
> > def fahr_to_kelvin(fahr):
> >     """Convert Fahrenheight to Kelvin.
> >
> >     Uses standard Fahrenheit to Kelvin formula
> >
> >     Arguments:
> >     fahr -- the temperature in Fahrenheit
> >     """
> >     kelvin = fahr_to_celsius(fahr) + 273.15
> >     return kelvin
> > ~~~
> > {: .language-python}
> {: .solution}

{% include links.md %}