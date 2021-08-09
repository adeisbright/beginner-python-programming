# Functional Programming in Python 
# Function with no parameter 
def say_hi() : 
    """ Prints Hi to the standard output device """
    print("Hi")
# A function is invoked when it is called 
say_hi() # will print Hi in the terminal 
# Function with positional parameters 
def add(a , b) :
    """ 
        Returns the result of adding two numbers 
    """ 
    return a + b 
print(add(3  , 4)) 
# Functions with default arguments 
def multiply(x , y = 4) : 
    result = x*y 
    return result 
print(multiply(2)) 

# Function that can accept variable number of arguments
def addmany(*args) :
    sum = 0 
    try :
        if (len(args) != 0) : 
            for i in args :
                sum += i  
            print(sum)
        else :
            raise Exception("Please , enter numbers to add") 
    except (Exception) as error :
        print(error)

addmany(2 , 3 , 4) 
