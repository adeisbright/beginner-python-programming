import os 
try :
    with open("hello.txt"  , "r+"  , encoding = "utf-8") as f : 
        names = ["Adeleke" , "Bright" , "Philo" , "IP" , "Lord IP" , "SP" , "Senator" , "Aboy" , "Ipenko"] 
        """for name in names : 
            f.write(name +"\n")
        """
        for line in f :
            print(line)
         #a , w+ , b readline . readlines 
finally :
    f.close() 

print(os.getcwd()) #returns the current working directory 

#newdir  = os.mkdir("dele") #creates a new directory dele 
#cd = os.chdir(r"C:\Users\Metges\Desktop\node-app") os.remove(filename) os.rmdir(dir)
direc = os.listdir() # creates an array of files in that directory 
for i in direc : 
    print(i) 
#ren  = os.rename("projects" , "projectile") #renames a file to a new name
# import shutil 
# remove_dir = shutil.rmtree("projectile") #deletes a file 
boo_list = [2  , {} , []] 
print(all(boo_list))
