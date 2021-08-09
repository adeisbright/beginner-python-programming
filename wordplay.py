"""
    Program : Random Sentence Generator 
    Description : The program will generate a unique sentence whenever the program runs
    Instructor : Adeleke Bright for ACE AFRICA(www.aceafrica.net)
"""
from random import randint 
class RandomPhrase :
    
    nouns = ["Adeleke" , "ACE AFRICA" , "PYTHON" , "Django" , "Gaming"] 
    modifiers = ["Beautifully" , "is" , "Affordable and" , "may"] 
    verb = ("Sings" , "Learn" , "Heals" , "Lambast") 

    def __init__(self) :
        self.n = RandomPhrase.nouns 
        self.m  = RandomPhrase.modifiers
        self.v  = RandomPhrase.verb 
    def play(self) :
        """ returns a unique sentence for the user"""
        your_word = "{} {} {}" 
        return your_word.format(self.n[randint(0 , len(self.n) - 1)] , 
        self.m[randint(0 , len(self.m) - 1)] , self.v[randint(0 , len(self.v) - 1)]) 

def main() :
    word_play = RandomPhrase() 
    print(word_play.play())

if __name__ == "__main__" : 
    main()