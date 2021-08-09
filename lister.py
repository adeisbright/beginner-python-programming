def filter(list) : 
    """
        Description 
           Returns element from a list that meets a certain condition 
        Parameter 
        ......... 
           list : A list of elements whether number or any data
    """ 
    return list 
students = ["John" , "Musa" , "Peter"] 
scores  = [1 , 2, 3] 
prime_of_3 = []
for score in scores :  
    if (score > 1) :
        prime_of_3.append(score) 
scores.extend(prime_of_3) 

print(scores.sort())
