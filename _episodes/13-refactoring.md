---
title: "Refactoring"
teaching: 0
exercises: 0
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

Refactoring is the process of making changes to our code, without affecting its behaviour.

> ## Refactoring
> > Code refactoring is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve nonfunctional attributes of the software. Advantages include improved code readability and reduced complexity; these can improve source-code maintainability and create a more expressive internal architecture or object model to improve extensibility.
> >
> > -- Wikipedia - Code refactoring
{: .callout}

> ## Refactoring Support in IDEs
> While most IDEs provide some support for automated refactoring, this tends not to work so well with dynamically typed languages like Python.
> When refactoring a statically typed language, it is easy for the IDE to recognise that one use of a variable, function or class is the same as another, since any use of the same identifier across multiple files must have been explicitly identified (by e.g. including the header files).
> Dynamic languages, like Python, do not have this requirement, so it is much more difficult to check that an identifier refers to the same object.

## Modules

So far we've been structuring our code within a single file, but what happens when this file gets too long to manage easily?

As we've seen with Numpy, in Python we're able to separate out code into a **library** and **import** it into the main part of our program.
This is possible in most programming languages (including C++, as we've seen yesterday)

## Type Annotations

The type system in Python is often referred to as **duck typing**, after the duck test "if it walks like a duck and it quacks like a duck, it's a duck".
This means that the type of an object in most cases does not actually matter, but rather the important thing is that the object 

Type annotations are a slightly devisive topic within the Python community, with some people claiming the increase the clarity of code, while others claim that they undermine one of the main benefits of Python's dynamic typing.
Both of these viewpoints are to some degree true, so before using type annotations it is important to consider whether they are a net benefit to your code.

{% include links.md %}

