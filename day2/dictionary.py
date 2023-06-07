#dictionary
# name = {
#     key1 : value1,
#     key2 : value2
# }

services = {
    "service_name":"EC2",
    "service_cost":"20$",
    "description":"this is aws EC2 instance"
}

print(services["service_name"])
print(services["description"])

#tupple is immutable

#difference between list and a tuple : values of tuple cannot be changes while in list values can be changed
days_of_week = ("sun","mon","tues","wed","thurs","fri","sat")  #this is a tuple 
days_of_the_week_list = ["sun","mon","tues","wed","thurs","fri","sat"] #this is a list
#days_of_week[0] = "sunday" #changing value of starting index but this will give error as thios is a tuple
days_of_the_week_list[0] = "sunday" # value of given index will change in the list
print(days_of_week)
print(days_of_the_week_list[0])