
###=================================List========================================
marks = [10.3, 87.5, 12, 20, 99]
print(marks)
print(marks[3])
print(marks[2])
print(type(marks))
print(len(marks))
##==================================================================================
student = ["karan", 99, 17, "chandigarh"]
print(student)
print(student[0])
print(type(student))
##===================================================================================
#mutable list

name = ["Roshan", "Aditya", "Vinay"]
print(name)
name[0] = "Rohit"
print(name)
##================================List Method=================================================
#append
list = [2,1,3]
list.append(4)
print(list)

#sort
A = ["a","c","b","f","e","d"]
#append
A.append("Z")
#list reverse 
A.reverse()
print("reverse list =",A)
#sort
A.sort()
print("Sort list =", A)
#sorts reverse
A.sort(reverse=True)
print("descending =",A)
#list insert
num = [12,44,55]
print(num)
num.insert(3,5)
print(num)
