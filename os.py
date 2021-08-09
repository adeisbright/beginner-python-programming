import re 
word = "What do we do to grow" 
test = re.findall(r"\w+" , word)
print(test)