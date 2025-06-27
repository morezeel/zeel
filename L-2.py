# 1. Print your name

print("Hello , my name is Zeel ")

# #  2. Ask Name and Print

name = input("What is your name : ")
print("Nice to meet you, " , name)

# #  3. sum of two number 

a = 10
b = 20 

sum = a + b

print("The sum of", a, "and", b, "is", sum)

#  4. simple calculator

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("addition : " , a + b)
print("subtraction : " , a - b)
print("multiplication : " , a * b)
print("divion : " , a / b)

#  5. sandwich maker

bread = input("Choose Your bread (white/brown)")
filling = input("Choose your filling (cheese/jan/potato/banana)")

print("Here you silly sandwich: ")
print("[" + bread + " bread " + filling + "  rainbow silly sandwich " + " ]")

#  6. rock , paper and scissors game

import random

chocies = ["rock" , "paper" , "scissors"]
computer = random.choice(chocies)
player = input("choose rock , paper and scissors: ")

if player == computer:
    print("It's a tie!!!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You win!!!")
else:
     print("computer win......")














