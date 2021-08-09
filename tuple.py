tup  = fruits = ("Mango" , "Orange" , "Apple") 
# help(fruits) will return helps on how to use tup 
# A tuple is an immutable data structure . That is why we cannot use many methods on it 
# For the purpse of mutating its state
print(len(tup) , tup.index("Mango") , tup.count("Apple")) 
# tup.clear() clears everything 
dict = {
	"name" : "Adeleke Bright" ,
	"hobbies" : ["Cycling" , "Football" , "Gaming" , "Comedy" , "Dancing"] ,
	"career" : "Software Enginnering" ,
	"age" : 26 ,
	"address" : {
		"country ": "Nigeria" ,
		"state" : "Lagos" ,
		"lga" : "Kosofe" ,
		"street" : "36 Doyin Omololu street , Alapere-Ketu"
	}
} 
copy_dict = dict.copy() # Purely copies a dictionary. This is a clone 
# dict.clear() clears the dictionary 
#print(dict , copy_dict ) 
name = dict.get("name") 
print(name) 
for i in dict.keys() :
    print(i) 
for i in dict.values() : 
    print(i) 
for i in dict.items() : 
    print(i)
dict.update("name" : "John")
print(dict)