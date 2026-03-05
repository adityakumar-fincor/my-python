# del keyword = used to delete object properties or object itself
"""
del s1.name
del s1
"""

class student:
    def __init__(self, name):
        self.name = name

s1 = student("Dipika")
print(s1.name)
del s1

## Private(like) attributes & methods
"""
coceptual implementation in python
private attributes & methods are meant to be used only within the class and are not accessible from outside the class
"""

class account:
    def __init__(self, account_no, account_pass):
        self.account_no = account_no
        self.__account_pass = account_pass
acc1 = account("1234", "abcd")
print(acc1.account_no, acc1.__account_pass)