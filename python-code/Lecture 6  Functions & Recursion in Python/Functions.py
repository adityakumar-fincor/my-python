# # def function_name(a,b):
# #     sum = a+b
# #     print(sum)
# #     return(sum)

# # function_name(10, 20)
# # function_name(30,40)
# # function_name(1, 20)

# # #Function defination
# # def sum(a,b): # parameters
# #     return a+b
# # add = sum(12,28) #function calls; arguments
# # print(add)

# # cites = ["pune", "mumbai", "Delhi"]
# # heros = ["ajay", "boby", "sktiman", "srk"]

# # def print_lenth(list):
# #     print(len(list))

# # print_lenth(cites)
# # print_lenth(heros)

# # def hero_list(list):
# #     for item in list:
# #         print(item, end=" ")

# # hero_list(cites)

# ## Convert USD to INR
# # def converter(usd_value):
# #     inr_value = usd_value * 91.47
# #     print(usd_value, "USD =", inr_value, "INR")

# # doller = int(input("Enter your USD:"))

# # converter(doller)

def check_even_odd(number):
    if number % 2 == 0:
        print   ("This is an Even Number")
    else:
        print("This is a Odd number")

num = int(input("Enter a Number:"))
check_even_odd(num)

