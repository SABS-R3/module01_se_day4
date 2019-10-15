% Best Practices in Developing Software
% SSI

## Barriers to Writing Good Code

- Research goals take precedence
- Feels like no progress being made
- Bewildering array of practices - which ones?

## "Technical Debt"

*"Reflects the implied cost of additional rework caused by choosing an easy or limited solution now instead of using a better approach that would take longer."*

## "Technical Debt"

- Like financial debt - gathers 'interest' over time
- Tech. debt paid off in maintenance
- If not addressed, software becomes unable to evolve
- Many applications just replaced due to prohibitive maintenance costs

Moral: deal with maintenance *early* and *often*

## Benefits of Maintainability

Improving maintainability reduces technical debt.
In general maintainable code allows you to more easily:

- Add new features, without introducing bugs
- Fix a bug, without introducing new ones
- Improve performance or usability
- Make changes to support new environments
- Be more productive
- Collaborate around software
- *Verify your code w.r.t. the science!*

## Importance of Maintainability

The IEEE Standard Glossary of Software Engineering Terminology defines maintainability as:

*"The ease with which a software system or component can be modified to correct faults, improve performance or other attributes, or adapt to a changed environment."*

## Why else is Maintainability Desirable?

What if:

- A developer with key skills falls ill or leaves the team?
- Development is restarted following a funding hiatus?
- New team members are brought on board?

"Software archaeology" is *hard!*

## "Disposable" Code?

Writing code to prove a concept or perform quick calculation, discard it.

But:

- Are you sure you (or others) will never use it again?
- Small maintainability investments now = easier to pick up later
    + An 'insurance policy' against future use

## General Hints and Tips

- Be critical of code you develop and make use of.
- Always assume code will be used by others
    + A future version of yourself!
- Prevention is better (and cheaper) than cure
- Remember code generally write once, read many
- Strike balance between practice adoption and research progress
