import re 
word = "What do we do to grow" 
test = re.findall(r"\w+" , word) 
split = re.split(r"\s" , word) 
li = ["guru99 get" , " guru give" , "guru selenium"]
print(test , split)  
for elem in li :
    z = re.match("(g\w+)\W(g\w+)" , elem) 
    if z :
        print((z.groups()))
pattern  = re.compile(r"^[a-zA-Z]{4,}") 
name  = "Adeleke" 
check  = pattern.match(name) 
print(check.groups())
