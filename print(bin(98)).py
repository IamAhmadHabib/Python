# ALL THE CODES AND FUNCTIONS I AM LEARNING

# .format 
# Name = input ("Full Name")
# Age = input ( "Age" )
# Class = input ( "Class" )
# print("Hi {}.You are {} years old. And you are in {}".format(Name,Age,Class))

# AUGMENTED ASSIGNMENT OPERATOR
# ahmad = -10.7
# ahmad += 2
# print  (ahmad)

# TYPECASTING 
# str1 = "Hello"
# We can't simply add string and integers. We have to change them into same type 
# str2 = str(20)    
# str3 = str1 + str2
# print(str3)

# SLICING FUNCTION
# str1 = "HELLO, WORLD!"
# print(str1[5:10:2])
# print(str1[:13:3])
# print(str1[::-1]) REVERSE
# print(str1[::].title() )

# FIND FUNCTION 
# find(start,end,)
# If there are two same characters then it will tell which is first. If there is no charcter then it will give output of -1
# print(str1.find("L",0,13) )

# COUNT FUNCTION will tell how many times a charcter comes. If there is no character in the string then it will give 0 output
# print(str1.count("L"))

# STRIP FUNCTION is used to eliminate spaces
# JOIN FUNCTION is used to join anything we want with any string
# str2 = "-"
# print (str2 .join(str1))

# Number to OCTAL
# b = 1098
# print (oct(b))

# Number to HEXA
# a = 1289
# print(hex(a))

# REPLACE FUNCTION
# a = "Ahmad"
# print (a.replace("A", "D"))


# LISTS
# Lists are mutable
# In Lists we can store strings, integers as well
# In lists we can make multiple lists and can be nested like list = [[1,2,3]
# [2,4,6]
# [9,8,7]
# ]
# In lists we have index 012 by commas like below
      # -5  -4   -3   -2  -1
# list = [20, 50, 100, 300, 55]
      #  0   1   2    3    4
# print (list[2])
# print (list[-1])
# print (list[n-1])
# print (list[-n])
# print (list[])

# APPEND FUNCTION IS USED TO ADD VALUES
# EXTEND FUNCTION IS USED TO ADD MORE THAN 1 VALUE AT THE END
# INSERT FUNCTION IS USED TO ADD NEW VALUES IN CENTER AND SHIFTS THE PREVIOUS VALUES TO THE NEXT
# list.append(1000)
# print(list)
# list.insert(0,5)
# print(list)
# list.extend([900,950])
# print(list)

# COUNT FUNCTION IS USED TO TELL HOW MANY VALUES ARE USED OF SAME THING, IF THERE IS NO VALUE THEN IT WILL RETURN 0
# print(list.count(55))
# print(list.count(1000))

# SORT FUNCTION IS USED TO SORT VALUES INTO ASCENDING OR DESCENDING ORDERS
# list.sort() ASCENDING
# print(list)
# list.sort(reverse = True)   DESCENDING
# print(list)

# SORTED FUNCTION
# sorted = sorted(list) 
# print(sorted , "SORTED LISTED")
# print(list , "ORIGINAL LIST" )



