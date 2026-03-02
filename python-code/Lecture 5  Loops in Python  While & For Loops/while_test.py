# print number from 1 to 100

# i = 1
# while i <=100:
#     print(i)
#     i += 1
# # print number from 100 to 1

# num = 100
# while num >= 1:
#     print(num)
#     num -= 1

# print the multiplication of table of a number n.

# b = 1
# c = int(input("Enter numbr:"))
# while b <=10:
#     print(c*b)
#     b +=1

# Print the elements of the following  list using loop

# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx +=1

# animal = ["Lion", "Tiger", "Monkey", "Elephant"]
# ani = 0
# while ani < len(animal):
#     print(animal[ani])
#     ani +=1

#search for  a number x in this tuple  using loop

# tup = (1,4,9,16,25,36,49,64,81,100,25)
# id = 0
# x = int(input("Enter Number:"))
# while id < len(tup):
#     if (tup[id] == x):
#         print("Found the number index at", id)
#         break
#     else:
#         print("Finding the numbr........")
#     id +=1
"""
### Break and continue 
Break: used to terminate the loop when encountered.
Continue: terminates execution in the current iteration & continue execution of the loop with the next iteration
"""
# numbs = 1
# while numbs <=5:
#     print(numbs)
#     if(numbs == 4):
#         break
#     numbs += 1
# print("Ends of loops")

i = 0
while i <=10:
    if(i%2 == 0):
        i += 1
        continue #skip
    print(i)
    i += 1