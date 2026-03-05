class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0 
        for value in self.marks:
            sum += value
        print("Hi", self.name, "Your avg score is:", sum/3)
s1 = student("Aditya Kumar", [99,98,97])
print(s1.name, s1.marks)
s1.get_avg()

#Q2

class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

acc1 = account(10000, 123456789)
print(acc1.balance,"\n",acc1.account_no)