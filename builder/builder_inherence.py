# one of the things that you might have noticed as we looked at the builder facets and the idea of
# combining builders is that we were directly violating the open closed principle, because whenever you
# have a new sub builder, you have to add it to the builder.

# So there is an alternative approach to this entire story, and the approach is to simply use inheritance.
# Whenever you need to build up additional information you inherit from a builder that you've already got.
class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self) -> str:
        return (
            f"{self.name} born on {self.date_of_birth} " + f"works as {self.position}"
        )

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonBirthDateBuilder()
me = pb.called("Dmitri").works_as_a("Quant").born("1/1/1980").build()
print(me)
