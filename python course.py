# A Good Programmer
# 1) Should know how to comment code properly
# 2) Should know which data structure should be used when
#



# AGE CALCULATOR
# a = input("What year were you born?")
# b = int(a) # We have to convert a into integer because it converts into string 
# c = 2023-b
# print ("Your age is {}".format(c) ) 

# PASSWROD CHECKER
# username = input("Enter Username")
# password = input("Enter your password")
# password_length = len(password)
# hidden_password = "*" * password_length 
# print((f"Hi {username}. Your password {hidden_password} is {password_length} characters Long."))

# LISTS
# daraz = ["mobiles", "groceries" , "Pens", "Mobile Covers" ]

# print (daraz [0])
# daraz [0] = "laptops"
# daraz_new = daraz [:] #[:] this sign is very important because if we dont use it then it simply copies the same
# daraz_new [1] = "Earbuds"
# daraz_new [0] = "mobiles"
# daraaaaz = daraz_new

# print (daraz) 
# print (daraaaaz)

# MATRIX
# matrix = [ [1,2,3],
#            [1,3,4,],
#            [1,5,6,7],
#          ]
# print(matrix [1][2])
 
# list = [1,2,3,45,346,361,142,311]
# a = list.reverse()
# print(a) #It gives output as none which means it does not create a new list but instead modifies the existing list 

# RANGE
# print(list(range(1,101)))

# JOIN
# a = "??"
# b = a.join([ "Why", "are", "you", "doing this"] )
# print(b)

# LIST UNPACKING is used to separate only the desired portion of the list while undesired portion remains in the list.

# a,b,c, *other, d= [1,2,3,4,5,6,7,8,9]

# print(a)
# print(b)  
# print(c)
# print(other)
# print (d)

# DICTIONERES/HASH TABLE/MAP
# {} we use these brackets to denote the dictioneries 
# key : value 
# In dictionary we can assign any variable with any data type 
# Keys should be immutable 
# Keys can be any data type like string,integer,bool,tuple but not list as lists are mutable.
# Most of the time keys are strings

# CASE 1
# dictionary = {
#     "a" : 23,
#     "b" : 47,
#     "u" : 213 
# }
# print(dictionary["u"])
# print(dictionary)

# CASE 2
# dict = {
#     "A": [12,12,53,46,46],
#     "B": "Ahmad has a cat",
#     "C": False
# }
# print(dict["A"][2])
# print(dict)

# print(dict["A"][2])   We can also do this in list like below

# list = [ {
#     "A": [12,12,53,46,46],
#     "B": "Ahmad has a cat",
#     "C": False},
        
#         {
#             "D":"He is single",
#             "E":["Bulshit",1,235,133]
#         }
#  ]

# print(list[0]["A"][2])
# print(list[1]["E"][3])

# Difference between list and Dict
# List has order while dict dont have order.
# List contains elements of same datatype while dict contain element of different datatypes.
# Dict holds more information than lists

# .get() function
# is used in dict to give no error but instead return none if there is nothing in the dict which we are trying to print 

# dict = {
#     1 : 321,
#     "A": "asfjkbsd",
#     True: (1,2,3),
# }


# print(dict.get(21,345)) # the value after comma will assign the key a value if it is not present before in a dict and if the key is already present then it will ignore it.

# print("A" in dict)
# print("Ahmad" in dict)
 
# We can create a dict by some other method like below

# user = dict(name="Muhammad Ahmad", age= 42)
# print(user)

# DICTIONARY METHODS 

user = {
    "A": [12,12,53,46,46],
    "Bahamas": "Ahmad has a cat",
    "C": False
       }
    
print("Bahamas" in user.keys())
print("Bahamas" in user.values())

        


