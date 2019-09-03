% Best Practices in Developing Software
% SSI

## Agenda: Day 4

## SSI - Some Experiences

## Barriers to Writing Good Code

- Research goals take precedence
- Feels like no progress being made
- Bewildering array of practices - which ones?

## "Technical Debt"

*"Reflects the implied cost of additional rework caused by choosing an easy or limited solution now instead of using a better approach that would take longer."*

## "Technical Debt"

- Like financial debt -  gathers 'interest' over time
- Tech. debt paid off in maintenance
- If not addressed, software becomes unable to evolve
- Many applications just replaced due to prohibitive maintenance costs

Moral: deal with maintenance *early* and *often*

## Importance of Maintainability

The IEEE Standard Glossary of Software Engineering Terminology defines maintainability as:

*"The ease with which a software system or component can be modified to correct faults, improve performance or other attributes, or adapt to a changed environment."*

## What is Maintainable Software?

Helps you to:

- Fix bugs without introducing new ones
- Add new features, without introducing new bugs
- Make a fix that prevents a bug from re-occurring
- Make changes to support new environments, operating systems or tools
- Bring new developers on board your project
- Improve usability
- Increase performance

## Benefits of Maintainability

In general:

- Reduces technical debt
- Makes you more productive
- Much easier to collaborate around software

## "Disposable" Code?

Writing code to prove a concept or perform quick calculation, discard it.

But:
- Are you sure you (or others) will never use it again?
- Small maintainability investments now = easier to pick up later
    + An 'insurance policy' against future use

## General Hints and Tips

- Always assume code will be used by others
    + A future version of yourself!
- Prevention is better (and cheaper) than cure
- Remember code generally write once, read many
- Strike balance between practice adoption and research progress
