"""
   Programme : FizzBuzz 
   Description : This program uses the modulo operator and conditional statement 
                to check if a number is divisible by 3 , 5 , or both.
                If the number is divisible by 3 and 5  , the program will print fizzbuzz
                Else if the number is divisible by 3 , the program will print Fizz
                Else if the number is divible by 5 , the program will print buzz 
                Else the program will print  the number instead of Fizzbuzz , fizz , or buzz
   Author      : Adeleke Bright 
   Company     : ACE AFRICA 
   Last Modified : 31-03-2020"
""" 
for i in range(1 , 30) : 
    if ( i%3 and i%5 == 0) : 
        print("FizzBuzz") 
    elif (i%3 == 0) : 
        print("Fizz")  
    elif (i%5 == 0) :
        print("Buzz")
    else :
        print(i) 
