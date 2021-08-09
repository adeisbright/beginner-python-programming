#Repetition with the range operator 
for i in range(1 , 10 , 2) :
    print(i) 

c = -20 
d = 5 
#Repetition using while statement
while(c <= 40 ) : 
    f = (9.0/5)*c + 32 
    print("{} degree celcius is equivalent to {:4.2f} Fahrenheit".format(c , f) ) 
    c += d 
print("End of program ")