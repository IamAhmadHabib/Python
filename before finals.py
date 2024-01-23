# a = [10 ,11 ,101] 
# if a[0] == a[1] == a[2]:
#     print(3) 
# elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
#     print(2)
# else:
#     print(0)



# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# twin_primes = []

# for num in range(3, 100):
#     if is_prime(num) and is_prime(num + 2):
#         twin_primes.append((num, num + 2))

# for pair in twin_primes:
#     print(pair)
    

# def isAnagram(s1,s2):
    
#     if sorted(s1) == sorted(s2):
#         print( "It is Anagram")
#     else:
#         print( "It is not Anagram")

        
# s1 = input("Enter 1st one: ")
# s2 = input("Enter 2nd one: ")    
# s1 = s1.lower()
# s2 = s2.lower()        

# isAnagram(s1,s2)


# def merge(list1, list2):
#     mergedList = []

#     while list1 and list2:
#         if list1[0] < list2[0]:
#             mergedList.append(list1.pop(0))
#         else:
#             mergedList.append(list2.pop(0))

#     while list1:
#         mergedList.append(list1.pop(0))

#     while list2:
#         mergedList.append(list2.pop(0))

#     return mergedList






# user = input("Enter you string: ")
# vowels = "aeiouAEIOU"
# def vowel_count(user):
#   number_of_vowels = 0
#   for x in user:
#     if x in vowels:
#       number_of_vowels+=1
#   return number_of_vowels
# def consents_count(user):
#   number_of_consents = 0
#   for x in user:
#     if x not in vowels:
#       number_of_consents+=1
#   return number_of_consents
# print("Number of vowels are: " ,vowel_count(user))
# print("Number of consents are: " ,consents_count(user))


a = int(input("Enter the value of a:"))
for i in range (1,a):
    i *=i
    print(i)
 

