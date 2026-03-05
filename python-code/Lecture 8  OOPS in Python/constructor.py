class student:
#this is default constructors
    def __init__(self):
        pass

#this is parameterized constructors
    college_name = "Amity" #class atributes
    name = "Rohit"
    def __init__(self, name, marks):
        self.name = name #object attriutes
        self.marks = marks
        print("adding new student in database...")
    def welcome(self):
        print("Welcome student", self.name)
    def get_marks(self):
        return self.marks
## Methods ===> Methods are functions that belongs to objects.
s1 = student("Aditya", 98)
s1.welcome()
print(s1.name, s1.marks) #Aditya
print(s1.name)
print(s1.get_marks())
s2 = student("Dipika", 99)
print(s2.name, s2.marks) #Dipika
print(student.college_name)

### class attributes and instance attributes


