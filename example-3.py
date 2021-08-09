from covid19model import Covid19Model 
class Covid19Analysis(Covid19Model) :
    def __init__(self) :
        pass  
    def computeTotals(self) :
        totalcases = 0 
        totaldeaths = 0 
        totalrecovered = 0 
        for city in self.city_and_cases.keys() :
            totalcases += self.city_and_cases[city]["Cases"]
            totaldeaths += self.city_and_cases[city]["Death"]
            totalrecovered += self.city_and_cases[city]["Recovered"]
        print("Total Cases : {} , Total Death : {} , Total Recovered : {}" 
        .format(totalcases , totaldeaths , totalrecovered))  
     

    def lagosinfection(self) : 
        lagos_population = self.city_and_cases["Lagos"]["Population"]
        infected_persons = self.city_and_cases["Lagos"]["Cases"]
        percentage_infected = (infected_persons/lagos_population)*100 
        print("The percentage of Lagos population that is infected : {:3.3f}%".format(percentage_infected))
    def leastmortalityrate(self) : 
        for city in self.city_and_cases.keys() :
            cases = self.city_and_cases[city]["Cases"]
            death = self.city_and_cases[city]["Death"]
            mortalityrate = death/cases 
    #def caseranking(self) :
    #def citydetail(self) : 
def main() :
    main = Covid19Analysis() 
    main.lagosinfection()
    main.computeTotals()
    #main.leastmortalityrate()
if __name__ == "__main__" : 
   main()