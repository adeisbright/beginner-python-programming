"""
    Program : States and Capital in Nigeria with user prompt
    Description : This program uses Object Oriented Programming  , functional programming , exception handling , program structure ,etc
    Developer : Adeleke Bright 
    Last modified : 26-03-2020 
    Company       : ACE AFRICA (www.aceafrica.net)
""" 
class NigerianStates : 
    # states_and_lga is a static variable holding the Eastern States 
    states_and_lga = {
        "Abia" : {
            "capital" : "Umuahia" , 
            "lgas"     : [{"name" : "Aba North" ,  "headquarter" : "Eziama Urata" , } , {"name" : "Abia South" , 
                "headquarter" : "Aba" } , {"name" : "Arochukwu" , "headquarter" : "Aro Okigboa" 
            }]
        } , 
        "Anambra" : {
            "capital" : "Awka" , 
            "lgas"     : [{"name" : "Idemili South " , "headquarter" : "Ojoto"
            }]
        }
    } 
    def get_lga(self) : 
        """Prints the lga in the user provided state"""
        user_guess = input("Please , enter a state in Eastern Nigeria : ")
        try :
            if user_guess in NigerianStates.states_and_lga.keys() :
                print(NigerianStates.states_and_lga[user_guess]["lgas"]) 
            else : 
                raise Exception("This state is not available")
        except Exception as error: 
            print(error)

def main() : 
    states = NigerianStates()       
    states.get_lga()   
# Run the programme only if it contains code generated in this file 
if __name__ == "__main__" : 
    main()
