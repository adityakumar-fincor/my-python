#class method = A class method is bound to the class & receive the class as an implicit first argument.
#Note static method can't access or modify class state & generally for utility.

class person:
    name = "anonymous"

    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = person()
p1.changename("Dipika")
print(p1.name)
print(person.name)