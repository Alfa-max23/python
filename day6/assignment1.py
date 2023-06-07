"""
Input a list of numbers from user i.e take integrer inputs and append list

find smallest and second smallest number from the list

"""
#creating an empty list
numlist = []
#number of elements as input
n = int(input("Enter number of elements: "))


#iterating till the range to add elements in list
for i in range(0,n):
    
    element = int(input("Enter element : "))
    #adding element to the list
    numlist.append(element)

#print(numlist)

min1 = float('inf')
min2 = float('inf')


for i in range(n):
    
    if numlist[i] < min1:
       min1, min2 = numlist[i], min1
    elif numlist[i] < min2 :
        min2 = numlist[i]

print(numlist)
print(min1,min2)
#numlist.sort()    sorts the list
# print(dir(list))
# print(numlist.count.__doc__)


        




