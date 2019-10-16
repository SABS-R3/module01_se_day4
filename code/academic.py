 #!/usr/bin/env python3

class Paper:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Academic(Person):
    def __init__(self, name):
        super().__init__(name)
        self.papers = []
        self.staff = []

    def write_paper(self, title):
        new_paper = Paper(title)

        self.papers.append(new_paper)
        return new_paper

    def add_staff(self, academic):
        if academic not in self.staff:
            self.staff.append(academic)

    @property
    def all_papers(self):
        papers = list(self.papers)
        for staff in self.staff:
            papers = papers + staff.all_papers

        return papers


if __name__ == "__main__":
    academics = [Academic(name) for name in ['Alice', 'Bob', 'Carol', 'David']]
    alice = academics[0]
    bob = academics[1]
    alice.add_staff(bob)

    alice.write_paper('A science paper')
    bob.write_paper('Another science paper')

    print(alice.all_papers)
