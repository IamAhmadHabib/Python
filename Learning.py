# # MDCAT AGGREGATE CALCULATOR
# name = input("Enter your Name.")

# a = input("Enter your Matric Marks.")
# matric = int(a)

# b = input("Enter your FSC marks.")
# fsc = int(b) 

# c = input("Enter your MDCAT score.")
# mdcat = int(c)

# total = 1100  #Total marks of fsc and matric
# totall = 200  #Total marks of MDCAT 

# matric_formula = ((matric/total)*100)*0.1 
# fsc_formula = ((fsc/total)*100)*0.4
# mdcat_formula = ((mdcat/totall)*100)*0.5
# total_aggregate = matric_formula + fsc_formula + mdcat_formula
# print ((f"{name} your total aggregate is {total_aggregate}"))



# SWAP 
# a = input("Enter 1st Number")
# b = input("Enter 2nd Number")
# a , b = b , a #SWAP FUNCTION
# print ((f"Your numbers will be swaped {a},{b}")  )

# NESTED LOOP is a loop which contains outer loop and inner loop
# for______:                      Outer Loop Rows
#     for_______:                 Inner Loop Coloums
#         statement(s)            Inner Loop
# statement(s)                    Outer Loop

# a = int(input("Enter a row"))
# for i in range(a):
#     for j in range(1,10,2):
#     # print(i)
#         print(j, end="")
#     print()


# a = int(input("Enter any number"))
# for i in range (1, a+1):
#     for j in range (i):
#         print(a, end=" ")
#     print()
        
# row = int(input("Enter no of rows"))
# for i in range(1, row+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
        

# a = int(input("Enter no of rows:"))
# for i in range (1, a+1):
#     for j in range(i, 0,-1):
#         print(j , end=" ")
#     print()

# Question # 01

# a = input("Enter a String : ")
# a = a.lower()
# if (a [:]) == (a [::-1]) :
#     print(f"{a} is a Palindrome.")
# else:                                                         
#     print(f"{a} is not a Palindrome.")  




# Question # 02  
# Part C
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for i in range(1,6):                        #ROW    (RIGHT)
#     for j in range(i):                      #COLUMN (DOWN)
#             print(i, end=" ")                     
#     print()
           
# Part B
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range (1,6):
    for j in range (i): 
        print(j+1, end=" ")  
    print()
                  
# Part A
# 1	
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# a = 1
# for i in range(1,6):
#     for j in range(i):
#         print(a, end=" ")
#         a += 1
#     print()
    

# In the first iteration of the outer loop, 'i' is 1. a. Starting the inner loop 'for _ in range(i):'. Since 'i' is 1, the inner loop will only iterate once. b. In the first iteration of the inner loop, we print the value of 'a' (which is 1) and add 1 to 'a'. The value of 'a' after this iteration is 2. c. Ending the inner loop as there are no more iterations left. d. Printing a newline character to start a new line for the next iteration of the outer loop.
# The outer loop now moves to the second iteration, where 'i' is 2. a. Starting the inner loop 'for _ in range(i):'. Since 'i' is 2, the inner loop will iterate twice. b. In the first iteration of the inner loop, we print the value of 'a' (which is 2) and add 1 to 'a'. The value of 'a' after this iteration is 3. c. In the second iteration of the inner loop, we print the value of 'a' (which is 3) and add 1 to 'a'. The value of 'a' after this iteration is 4. d. Ending the inner loop as there are no more iterations left. e. Printing a newline character to start a new line for the next iteration of the outer loop.    


# Part D
# *
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# a = "*"
# for i in range (1,6):
#     for j in  range(i):
#             print (a, end =" " )
#     print() 
 
# for k in  range(4,0,-1):
#     for l in range (k): 
#         print(a, end = " ")
#     print()

 
 
#  Question # 04
# import random

# a = random.randint(1,5)  
# while True:
#     b = int(input("Guess a secret number between 1 and 5:"))  
#     if b == a :
#         print ("Congratulations! You guessed the right number.")
#         break
#     else:
#         if b>a:
#             print("Wrong Guess! Please Try Again" )
#         else:
#             print("Wrong Guess! Please Try Again")


# a = int(input("Enter a Number:"))  
# def square ():
#     a = int(input("Enter a Number:"))
#     print("The Square of the number will be : ",a ** 2)
#     if a>0:
#         True 
#     while True:
#         square ()
#     else:
#         print("Exitted")



                                 
# def greet(name="Ahmad",Subject="Python",dept="BCT"): # Default Parameters
#     print(f"Hi, {name}")
#     print(f"Are you from {dept} department.")
#     print(f"Do you study {Subject}?")
# greet("John","IT","DS")
# greet("John","DS","IT")                         #Positional Arguments
# greet(Subject="Math",name="Ahmad",dept="BBA")   #Keyword Arguments (Bad Practice)
# greet()

# LAB TASK 1

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# operation = str(input("Enter the operation you want to use."))

# def calculator (a,b,operation):
#     if operation == "addition":
#         return a + b
#     elif operation == "subtraction":
#         return a - b
#     elif operation == "multiplication":
#         return a * b
#     elif operation == "division":
#         return a / b
# print(calculator(a,b,operation))
        

# LAB TASK 2
# a = int (input("Enter 1st number:"))
# b = int (input("Enter 2nd number:"))
# c = int (input("Enter 3rd number:"))   
# d = int (input("Enter 4th number:"))

# def largest_number(a,b,c,d):
#     print("The largest number is :", max(a,b,c,d))
# largest_number(a,b,c,d)

# LAB TASK 3  Fibonacci Series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 

# def fibonacci(n):
#     a, b = 0, 1
#     result = []
#     while len(result) < n:
#         result.append(a)
#         a, b = b, a + b
#     return result


# a = int(input("Enter the number: "))
# fibonacci_sequence = fibonacci(a)
# print("Fibonacci sequence of length", a, ":")
# print(fibonacci_sequence)


# Q1:

# a = int(input("Enter the length of triangle: "))
# b = int(input("Enter the width of triangle: "))
# c = float(1/2)
# d = a*b
# area = c*d
# print("The area of the right angled triangle is: ", area)

# # Q2: 
# a = input("Enter Email: ")
# b = input("Enter Password: ")
# email = "abc@gmail.com"
# password = "abc"
# if a == email and b != password:
#     print("Invalid Password")
# elif a != email and b == password:
#     print("Invalid Email")
# elif a != email and b != password:
#     print("Invalid Email and Password")
# else:
#     print("User Logged in!")
    
# Q3:
# a = int(input("Enter Year: "))
# if a % 4 == 0:
#     print("It is a Leap Year! Tada")
# else:
#     print("It is not a Leap Year!")

# Q4:

# a = input("Enter anything: ")
# b = "Z"
# c = (b[0] + a[1:] )
# print(c)

# Q5:
 
# a = input("Enter a String: ")
# print(a[::2])
    
# Q6:
# a = input("Enter a string: ")
# b = input("Enter another string: ")
# c = (b[:2] + a[2:])
# d = (a[:2] + b[2:])
# print(c, " ", d)

# Q7:
# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# while True:
#     number = int(input("Enter a number: "))
#     if is_prime(number):
#         print(f"{number} is a prime number.")
#         break
#     else:
#         print(f"{number} is not a prime number. Please try again.")



# Q8:
    #     1
    #     1
    #    121
    #   12421   
    #  1248421    
    
# rows = 5  # Number of rows in the triangle

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j * i, end="")  # Print the number without newline
#     print()  # Print a newline after each row

 
# Q9:

# a = 1
# n = 1
# while a<=8:
#     while n<=10:
#         b = a*n
#         print(f"{a}*{n}", "=", b)
#         n += 1
#     print()    
#     a +=1
#     n = 1    
    
# Q10:
# num_rows = int(input("Enter the number of rows: "))

# # Initialize the triangle with the first row
# triangle = [[1]]

# # Generate subsequent rows using nested loops
# for _ in range(1, num_rows):
#     row = [1]
#     for i in range(1, len(triangle[-1])):
#         row.append(triangle[-1][i - 1] + triangle[-1][i])
#     row.append(1)
#     triangle.append(row)

# # Print the triangle with proper spacing
# for row in triangle:
#     print(" " * (num_rows - len(row)), *row)



# Q12: Write a function that takes in params for different shape measurements and returns the area of that shape depending upon those measurements and the type of shape. If the type of shape is not specified it should by default calculate the area of a rectangle. It should be able to calculate the area of square, rectangle, circle, and triangle.

# a = input("Enter Shape to calculate area: ")
# a = a.lower()
# b = input("Enter Length: ")
# c = input("Enter Width: ")
# d = input("Enter radius: ")
# if a == "square":
#     b = int(b)
#     area1 = b*b
#     print("The Area of Square is: ", area1)
# elif a == "rectangle":
#     b = int(b)
#     c = int(c)
#     area2 = b*c 
#     print("The Area of Rectangle is: ", area2)
# elif a == "circle":
#     d = int(d)
#     import math
#     area3 = math.pi * d * d     # Another Method without using import: area3 = (3.14*d*d)
#     print("The Area of Circle is: ", area3)
# elif a == "triangle":
#     b = int(b)
#     c = int(c)
#     area4 = (0.5*b*c)
#     print("The Area of Triangle is: ", area4)
# else:
#     b = int(b)
#     c = int(c)
#     area = b*c
#     print("The Area of Rectangle is: ",area )
    

# Q7:
# 4388576018402626
# 0123456789 10 11 12 13 14 15
# 4388576018 4  0  2  6  2  6
# a = (input("Enter a credit card number: "))
# a = a[::-1]
# a = [int(x) for x in a]

# for i in range(1,len(a),2):
#     a[i] *= 2
#     if a[i] > 9:
#         a[i] = a[i] % 10 + 1
# total = sum(a)

# if total % 10 == 0:
#     print("Credit Card is Valid")
# else:
#     print("Credit Card is Invalid")














