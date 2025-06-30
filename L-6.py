#  1. Types of Loops in Python

#  for loop

# for i in range(3):
#     print("For Loop :" , i)

# for i in range(2 , 5):
#     print(i)

# for i in range(2 , 5 , 1):
#      print(i)

# range (start , stop , step)

#  while loop 

#  logic

    #     i += 1 [ i = 0 + 1 ] + 1
    #     i += 1 [ i = 1 + 1 ] + 2

i = 0
while i <= 10:
    print("While loop:" , i)
    i += 1

#  Nested Loop

for i in range(1 , 4):
    for j in range(1 , 4):
        print(j)
    print()

