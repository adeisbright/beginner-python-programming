# Making Python modules and generating useful functions

def sum_numbers(a , b = 4) :
    """
        Description 
          
        Parameters 
        .......... 
        a : int or float 
           The first operand 
        b : int or float 
            The second operand 
        Return 
          
    """
    return a + b


#Working with string
my_str = "\t Hello, Adeleke! \n When will you visit ?"
name = "adeleke     "
print("The {} has {} at the beginning".format(my_str , name[2::-2]))
# print(name.capitalize() , name.islower() , name.isupper() , name.isalnum() , name.isalpha() , name.isdecimal())
# print(name.join("!-!"))
# print(len(name))
# print(name.lstrip())
# print(name.rjust(20 , "*"))
# print(name.strip())
# print(name.split(" " ,name.count("a")))
# print(name.split()[0])
# print(name.replace("a" , "b"))
# print(name.find("e" , 2 , 4))
# print(name.endswith(" "))
# print(name.startswith("a" , 2 , 4))
num = 22.456544
print("Testing string formating with {:*^15.2f}".format(num))
if __name__ == "__main__" : 
   #main()
   print(sum_numbers(3))

