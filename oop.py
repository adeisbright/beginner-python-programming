  class Algebra :
    """
    A class use to represent algebraic operations 
    ...
    Attributes 
    ..........  
    Methods 
    ....... 
    display_arg() 
        prints the argument provided to the constructor 
    """
    def __init__(self , a , b) : 
        """
        Parameters 
        .......... 
        a : int or float 
           The first operand 
        b : int or float 
            The second operand 
        """
        self.a = a 
        self.b = b 
    def display_arg(self) :
        """ Prints the arguments in the constructor """
        print("The arguments are a : {} and b : {}".format(self.a , self.b)) 
# Working with Inheritance in Python   
class Addition(Algebra) :
    def __init__(self , a , b , c) :
        super().__init__(a , b) 
        self.c = c 
    def add(self) :
        print(self.a + self.b + self.c) 
def main() :
    algebraobj = Addition(30 , 40 , 40) 
    algebraobj.add() 
    algebraobj.display_arg()
if __name__ == "__main__" : 
    main()