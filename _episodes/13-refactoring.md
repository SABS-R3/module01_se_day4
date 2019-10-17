---
title: "Refactoring"
teaching: 30
exercises: 30
questions:
- "What is refactoring?"
- "How should I structure code to separate functionality?"
- "How can I separate configuration from code?"
objectives:
- "Use modules to separate functionality from the main flow of a program"
- "Use type annotations to describe the behaviour of a function"
- "Use configuration files to separate configuration from code"
keypoints:
- "Python uses modules to separate code out of the main file"
- "Storing configuration data outside of the code makes it easier for others to use your software"
- "Type annotations may be used to provide extra description about the behaviour of a function"
---

## Refactoring

> ## Refactoring
> > Code refactoring is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve nonfunctional attributes of the software. Advantages include improved code readability and reduced complexity; these can improve source-code maintainability and create a more expressive internal architecture or object model to improve extensibility.
> >
> > -- Wikipedia - Code refactoring
{: .callout}

While most IDEs provide some support for automated refactoring, this tends not to work so well with dynamically typed languages like Python.
When refactoring a statically typed language, it is easy for the IDE to recognise that one use of a variable, function or class is the same as another, since any use of the same identifier across multiple files must have been explicitly identified (by e.g. including the header files).
Dynamic languages, like Python, do not have this requirement, so it is much more difficult to check that an identifier refers to the same object.

## Modules

So far we've been structuring our code within a single file, but what happens when this file gets too long to manage easily?

As we've seen with Numpy and a few other bits from the Python standard library, in Python we're able to separate out code into a **library** and **import** it into the main part of our program.
Some equivalent of this is possible in most programming languages (e.g. `#include` in C++ after the linker has run).

Once again, we'll use the temperature conversion code to illustrate this:

~~~
# file: conversions.py

def fahr_to_celsius(fahr):
    """Convert Fahrenheit to Celsius.

    Uses standard Fahrenheit to Celsius formula.

    :param fahr: float temperature in Fahrenheit
    :returns: float temperature in Celsius
    """
    celsius = ((fahr - 32) * (5/9))
    return celsius

def fahr_to_kelvin(fahr):
    """Convert Fahrenheight to Kelvin.

    Uses standard Fahrenheit to Kelvin formula, making use of fahr_to_celsius function.

    :param fahr: float temperature in Fahrenheit
    :returns: float temperature in Kelvin
    """
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin
~~~
{: .language-python}

~~~
# file: climate_analysis.py

import conversions

print(conversions.fahr_to_celsius(32), 'C')
print(conversions.fahr_to_kelvin(32), 'K')
~~~
{: .language-python}

~~~
0 C
273.15 K
~~~
{: .output}

### Packages

As well as modules, we also have **packages** as a way of structuring our Python files.
A Python package is really just a directory with a set of modules in it, but with a special Python file `__init__.py`
This special file usually doesn't need to contain anything, but if it exists within a directory, Python will treat that directory as a package of modules.

To put our temperature conversion code in a package:

~~~
mkdir conversions
mv conversions.py conversions/temperature.py
~~~
{: .language-bash}

~~~
# file: climate_analysis.py

from conversions import temperature

print(temperature.fahr_to_celsius(32), 'C')
print(temperature.fahr_to_kelvin(32), 'K')
~~~
{: .language-python}

~~~
0 C
273.15 K
~~~
{: .output}

If we wish to, we can shorten this a little bit by adding to our package's `__init__.py`:

~~~
# file: __init__.py

from temperature import fahr_to_celsius, fahr_to_kelvin
~~~
{: .language-python}

So now we can use these functions directly from the package:

~~~
# file: climate_analysis.py

import conversions

print(conversions.fahr_to_celsius(32), 'C')
print(conversions.fahr_to_kelvin(32), 'K')
~~~
{: .language-python}

~~~
0 C
273.15 K
~~~
{: .output}

> ## Packaging Academics
>
> The Academics model is something that could be used as part of a much larger piece of software to help manage academic staff and their publications, such as a Current Research Information System (CRIS).
> But, to do that we're going to need it in a suitable form - a Python package...
>
> Take the Academics model (just the reusable class definitions) and turn it into a Python package named `academics` to be used from a script:
>
> ~~~
> from academics import Academic
>
> academics = [Academic(name) for name in ['Alice', 'Bob', 'Carol', 'David']]
> alice = academics[0]
> bob = academics[1]
> alice.add_staff(bob)
>
> alice.write_paper('A science paper')
> bob.write_paper('Another science paper')
>
> print(alice.all_papers)
> ~~~
> {: .language-python}
>
> ~~~
> ['A science paper', 'Another science paper']
> ~~~
> {: .output}

## Type Annotations

When talking about type systems in different programming languages, there are two distinctions to be made.

The first is whether the language is **staticly typed** or **dynamically typed**.
In statically typed languages, each variable must have a type, usually set when it is defined - C++ is a statically typed language:

~~~
int count = 0;
const double x = 10.;
~~~
{: .language-cpp}

In contrast, a dynamically typed language like Python, does not need / allow variables to have a type defined as the variable may hold multiple values of multiple different types over its lifetime:

~~~
count = 0
x = 10.

count = 'Hello World!'
x = print
~~~
{: .language-python}

The second axis is whether the language is **strongly typed** or **weakly typed**.
Strongly typed languages do not allow the type of a value (not the variable, but the value it holds) to be converted without an explicit cast, whereas weakly typed languages do.

In addition to this, the type system in Python is often referred to as **duck typing**, after the duck test "if it walks like a duck and it quacks like a duck, it's a duck".
This means that the type of an object in most cases does not actually matter, but rather the important thing is that the object 

Type annotations are a slightly devisive topic within the Python community, with some people claiming they increase the clarity of code, while others claim that they undermine one of the main benefits of Python's dynamic typing.
Both of these viewpoints are to some degree true, so before using type annotations it is important to consider whether they are a net benefit to your code.

Type annotations make Python functions (and classes, etc.) look a little more like C++ functions.
Function parameters are annotated with a colon followed by the type, while return values are annotated with an arrow then the type after the function parentheses.

~~~
def fahr_to_celsius(fahr: float) -> float:
    """Convert Fahrenheit to Celsius.

    Uses standard Fahrenheit to Celsius formula.

    :param fahr: float temperature in Fahrenheit
    :returns: float temperature in Celsius
    """
    celsius = ((fahr - 32) * (5/9))
    return celsius

def fahr_to_kelvin(fahr: float) -> float:
    """Convert Fahrenheight to Kelvin.

    Uses standard Fahrenheit to Kelvin formula, making use of fahr_to_celsius function.

    :param fahr: float temperature in Fahrenheit
    :returns: float temperature in Kelvin
    """
    kelvin = fahr_to_celsius(fahr) + 273.15
    return kelvin
~~~
{: .language-python}

One of the advantages of an IDE like PyCharm is support for things like type annotations.
If you try to use an annotated function with arguments of a different type, we should see a highlighted complaint.

To see how type annotations actually behave in practice, lets write another, very simple, function:

~~~
def add_floats(a: float, b: float) -> float:
    return a + b

print(add_floats(1, 2))
print(add_floats('Hello', 'World!'))
~~~
{: .language-python}

~~~
3
HelloWorld!
~~~
{: .output}

As we can see, although PyCharm tells us that we're using the function incorrectly when we call it with two strings instead of floats, the function does actually work.
This is because type annotations in Python aren't quite like they are in a statically typed language.
The type annotations we provide are not used to perform checking at runtime, but are an indicator that tools can use to inform us of potential errors.

## Configuration Files

Remember back when we were looking at the procedural paradigm, before we knew about classes, and we used a nested data structure to represent our academics?

~~~
academics = [
    {
        'name': 'Alice',
        'papers': [
            {
                'title': 'My science paper',
            },
            {
                'title': 'My other science paper',
            }
        ]
    },
    {
        'name': 'Bob',
        'papers': [
            {
                'title': 'Bob writes about science',
        ]
    }
]
~~~
{: .language-python}

Well, it just so happens that this data structure is almost exactly a **JSON** file.
JavaScript Object Notation (JSON) is a very common format for handling config files and other complex data structures, which has libraries for processing it in almost all programming languages.

In Python the `json` library is part of the standard library, so we don't need to worry about installing anything extra.

Unfortunately we don't have time to cover this properly, but as usual, the Python documentation is a useful resource.
See [JSON library](https://docs.python.org/3.7/library/json.html).

> ## Obfuscating Pi
>
> In the `code` directory of this lesson are two programs which need linting, one in Python (`pi.py`) and one in C++ (`pi.cpp`).
> Copy both of these programs and use the appropriate linters to help reformat the code.
>
> To run `pylint` on a Python file use:
>
> ~~~
> pylint pi.py
> ~~~
> {: .language-bash}
>
> To run `cpplint` on a C++ file use:
>
> ~~~
> cpplint pi.cpp
> ~~~
> {: .language-bash}
>
> Before you make any changes to the code, make sure you run it and make a note of the output - when refactoring it's important that you don't change the behaviour of the code.
> Later in the course we'll cover proper software testing, so we can automate these checks, but for now we'll have to check manually.
> Though this code relies on random numbers, we've set a fixed random seed so that the behaviour is predictable to make testing easier.
>
> Once you've fixed all of the style issues, try using some of the techniques we've discussed in this session (modules and type annotations) to make further improvements to the code.
> The focus here is on improving reusability and reliability.
>
{: .challenge}

{% include links.md %}

