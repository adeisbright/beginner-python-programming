""" 
    Program : Working with string and string method 
"""    
# How to create a string 
name = "adeleke" 
# Methods of string 
# print the name in uppercase 
print(name.upper()) # You can use name.lower() to do the reverse operation 
# returns True if the string is made of numeric characters 
numeric_string = "345666666"
print("numeric_string".isnumeric()) # other methods include istitle() , isalpha , isalnum , isnumeric , count(x) , find(n) 
print(name.find("A")) # Returns the first index of the character if present or -1 if absent
first_3_characters = name[0:3] 
word_bank = "This is our word bank not the world bank" 
# Let the user enter a character then count how many times it occurs 
user_input = input("Enter a charater to count how many times it occurs in our bank:  ") 
try :
    if (word_bank.find(user_input)) :
        print("The character {} occurs {:^2d} times in our bank".format(user_input , word_bank.count(user_input))) 
    else :
        print("The character you provided is not in our bank")
except (ValueError) as error :
    print("Please  , enter a valid English character")
print(first_3_characters)
reversed_name  = name[::-1] 
print(reversed_name)

#String formatting 
time = 23.94999999
print("{:*^10s} smiles for {:2.2f} hours every day ".format(name.upper(),time))
