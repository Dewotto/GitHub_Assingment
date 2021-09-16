#Main Program File for Module_Test_1
print()
print("Welcome to the module import program!")

import Module_Database

num1 = Module_Database.a
num2 = Module_Database.b
num3 = Module_Database.c
num4 = Module_Database.d
num5 = Module_Database.e

print ("we will now acess the data from the module!")
print (num1, "+", num2, "=", num1 * num2)
print (num3, "+", num4, "+", num5, "=",num3 * num4 *num5)
print ("Magic!!:)")