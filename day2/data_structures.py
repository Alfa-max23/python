"""
4 types of data structures
-list
-set
-tuple
-dictionary 
"""

names = list() 
#or
cloud_platforms = ["aws","gcp","azure"]
# print(dir(names))

names.append("Tom")
names.append("Dick")
names.append("Harry")

print(names[0])  
#print(names[5])  ---> this will give error as list index is out of range

print(names)

#iteration in list

for i in cloud_platforms :
    if i == "aws" :
        print("platform is aws")
    else :
        pass    #does nothing, just pass


