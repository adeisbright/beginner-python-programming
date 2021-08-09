def solution(num) : 
    multiples_of_3or5 = []
    for i in range(num) :
        if (i%5 == 0 or i%3 == 0) : 
            multiples_of_3or5.append(i) 
    return sum(multiples_of_3or5) 

print(solution(10)) 

#def to_camel_case(str) :
#indexing is used for getting a single character from a string 
name = "Sammy Shark!" 
indexing_neg = name[-4] 
indexing_pos = name[7] #The last item is at index -1 
print(indexing_neg) 

#we use slicing to get a range of characters - 
sliceFromStart = name[1 : 8: 2] #string[start:countfromstart:step] 
usingNegative = name[-4 : -1] 
get_all = name[::-1]
print(sliceFromStart) 
print(usingNegative) 
print(get_all) 

# List Comprehension - A way to create list based on existing list instead of using for loop 
mimic = [char + "o" for char in name] #[expression for var in list] 
num = [x*x for x in range(10) if x%2 == 0 if x%4 == 0] 
obj = ["Even" if x%2 == 0 else "Odd" for x in range(10)]
print(mimic) 
print(num)
print(obj)