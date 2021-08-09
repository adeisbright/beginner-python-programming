"""
   Program     : AUTOMATED CGPA PROCESSOR 
   Description : This program will help any organization involved 
                 in grading to efficiently rank students using any criteria 
    Requirements : 
        1.0 Compute Final CGPA 
        2.0 Rank Students from descending to ascending and vice versa  
        3.0 Capable of selecting the best cgpa for any student
"""
students = [
    {"name" : "Adeleke Bright" , "matric_number" : "U2001/3010005" , "gpas" : [4.56 , 3.87 , 4.42 , 5.0]} , 
    {"name" : "Ibekwe Chukwudi" , "matric_number" : "U2001/3010008" , "gpas" : [3.56 , 4.12 , 4.92 , 4.85]} , 
    {"name" : "Benjamin Rukevwe" , "matric_number" : "U2001/3010009" , "gpas" : [5.00 , 4.77 , 4.35 , 3.9]}
]   
#*args non keyworded list of arguments 
#**kwargs keyworded list of arguments 
#*splat operator is like spread operator in python
def sum(values) : 
    #How can the function work with rest paramters ? 
    # How to verify that something is an array 
    """ Returns the sum of a sequence """ 
    total = 0 
    for x in values :
        total += x 
    return total 
for student  in students : #Use list comprehension or zip to achieve this effect
    CGPA = sum(student["gpas"])/len(student["gpas"]) #Return it to two decimal places 
    # How to attach the cgpa to the current student after computation 
    student["cggpa"] = CGPA 
    student.update("name" , "Adeleke") 
    #if ( i == 0) :student.update("name" , "Adeleke") 
    print(CGPA) 
print(students)
print(17.85/4) 

#pop() delete and returns the value of the key specified 
#popitem() removes and return an arbitrary element(key , value) pair from the dictionary 
# clear() empties the dictionary 
#get() access the value in a key 
#str() returns a printable str 
#keys() , items() , values() , has_key() , type() returns the type of data or variable cmp()

