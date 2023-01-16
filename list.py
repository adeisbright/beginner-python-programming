""" 
    Program : Working with List in Python
"""  
my_list = [1 , 3 , 2 , 4] 
another_list = ["a" , "b" , "c" , "d" , "e" , "f"] 
sliced_list = another_list[2:5] # Include all element from index 2 to the index 5(but not included) . The element at index 5 is exclusive that is not included
item_0 = my_list[0] # A list can be sliced and can also be indexed
del my_list[2]
print(item_0)
for x in my_list :
    print(x) 
m = max(my_list) 
print(m)
scores = [2 , 4 , 10 , 2 , 4] 
average  = sum(scores)//len(scores) 
print("The average score is {}".format(average) , scores.count(4) ) 
#Reverse the list 
scores.reverse() #You cannot print out rev 
print(scores)
scores.sort()
scores.append(30)
three_count = scores.count(3) 
index_of_4 = scores.index(4) 
extension = scores.extend([2 , 19]) 
scores.insert(0 , 99) 
scores.remove(4) #Removes the first occurence of 4 
comotAgain = scores.pop(0) #Removes an element at this index
print(scores , three_count , index_of_4 ) 
