class Math :
    def __init__(self , *args):
        self.numbers = args 
    def sum(self) : 
        try :
            total = 0 
            for x in self.numbers : 
                total += x 
            print(type(self.numbers)) 
            return total 
        except (IndexError , IOError , NameError , ValueError) as error : 
            return error

    def toJaden(self , string) :
        
if __name__ == "__main__" : 
    sum = Math(2 , 3 , 4 , "a") 
    print(sum.sum()) 

