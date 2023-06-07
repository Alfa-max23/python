"""
Import library json

-create a dictionary in python
-convert that dicitionary to json

"""

import json

#print(dir(json))

#creating adictionary
ec2 = {
    "name" : "server1",
    "type" : "t2.micro",
    "ami" : "ami-02dfg348gghj"
}

print(ec2) # will print the dicitionary

#print(json.dumps.__doc__) 

txt1 = json.dumps(ec2, indent=4,sort_keys=True)  #indent property will add intent spaces before every keys, sort_key will arrange keys alphabeticaly
print(txt1) #will print json converted format


# in case of nested dictionary

player_dict = {
    "player_details":{"name":"sachin","age":52,"sports":"cricket"},
    "records" : {"matches":600, "century":100},
    "count":10
}

print(player_dict)
json2 = json.dumps(player_dict, indent=4)
print(json2)


