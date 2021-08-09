# This program reads users detail from a file and works with some standard library 
import os 
from math import pi 
import shutil 
class Error(Exception) : 
    pass 
class BindingError(Error) : 
    def __init__(self , name , message) : 
        self.name = name 
        self.message = message 

class Example4 :
    program_name = "Brighto" #class variable is shared by all objects 
    def __init__(self , user_name , user_age):
        self.user_name = user_name #instance variable 
        self.user_age  = user_age 
    def sayHi(self):
        print("Hello , {}".format(self.user_name))
    def save_name(self) : 
        try : 
            print(Example4.program_name) 
            # with open("hello.txt" , "a+" , encoding="utf-8") as f: 
            #     f.write("\n" + self.user_name) 
            #     print(f.readline())
            raise BindingError("BindingError" , "The static variable was not accessed properly")
        except (IndexError , IOError , NameError) as error : 
            print(error)
        except BindingError as error: 
            print(error)
        finally : 
            print("The last thing standing is {}".format(pi)) 
if __name__ == "__main__":
    start = Example4("Adeleke" , 26) 
    start.sayHi() 
    start.save_name() 
    print(start.program_name)