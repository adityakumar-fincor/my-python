# info = {
#     "name" : "aditya",
#     "surname" : "Kumar"
# }
# print(info)
# print(type(info))

student = {
    "name" : "Aditya",
    "subject" : {
        "math" : 90,
        "eng" : 99,
        "phy" : 95
    }
}

print(student["subject"]["math"])
print(student)
print(student["subject"])
print(student["name"])

#dictionary Methods
#myDict.key() "return all key"

print(student.keys())
print(len(student))

#myDict.values # return all value
print(student.values())
print(student.items())
print(list(student.items()))
print(student.get("name2"))
print(student["name"])


a = "aditya"
