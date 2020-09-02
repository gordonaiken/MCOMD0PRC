# Hello World

print("Hello, World!")


# Second Program

name = input("What is your name?")
print ("Hello " + name)
print ("What are we going to learn today")
table = int(input("Which times table? "))
if table < 13:
    for i in range(1,13):
        print (str(i) + " times " + str(table) + " is " + str(table*i))
else:
    print("This is too hard for today")


# Tip Calculator

import math

total = float(input("What is the bill (in £)? "))

numPayers = int(input("How many are paying? "))
approx_tip = total /100 * 10
ind_contrib = approx_tip / numPayers
ind_tip = math.floor(ind_contrib + 0.5)
print ("Each person should tip £"+ str(ind_tip))
