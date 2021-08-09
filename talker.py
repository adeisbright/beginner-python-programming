from sys import argv 

script , user_name = argv 

print("Hello {} , I am your AI girlfriend".format(user_name)) 
location = input("Tell me about your location") 

print("{} lives in {}".format(user_name , location))