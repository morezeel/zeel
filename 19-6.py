print("==== Built-in Function In Python ====>")

numbers = [4 , 8 , 6 , 7 , 3]
numbers = (4 , 8 , 6 , 7 , 3)
numbers = {4 , 8 , 6 , 7 , 3}
numbers = {"1":4 , "2":8 , "3":6 , "4":7 , "5":3}
numbers = {}

print(type(numbers))

print(len(numbers))

if len(numbers) == 0:
    print("list is empty!!!")
else:
    print("list is available!!")

# min() and max() function

numbers = [4 , 8 , 6 , 7 ,3]

print ("max number : " , max(numbers))
print ("min number : " , min(numbers))

# sum() functions

numbers = [4 , 8 , 6 , 7 , 3]

print("some of numbers: " , sum(numbers))

print("<==== Nagative Float Number Operation ====>")

num = float(input("Enter a nagative float number: "))

# abs() function

print("absolute value: " , abs(num))

# pow() function

print("raised to power 3: " , pow(num , 3))

# round() function

print("round of value" , round(num))

# sort and Reverse a List 

print("<=== Sort and Reverse a List ===>")

user_list = list(map(int , input("Enter Number seperatred by Space : ").split()))

print("user list: " , user_list)

print("sorted user list: " , sorted(user_list))

print("sorted user list: " , sorted(user_list , reverse=True))

print("sorted user list: " , list(reversed(user_list)))

import random

print("<=== Random list and its analysis ===>")

random_list = random.sample(range(1 , 100) , 10)

print("Random List: ", random_list)













