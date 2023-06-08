"""
This function  will take two numbers and find its sum and difference
"""


def sum_of_two(): # creation of function
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2st Number : "))
    c = a+b
    print("Addition is :", c)

def diff_of_two(): # creation of function
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2st Number : "))
    c = a-b
    print("difference is :", c)

"""
change_case() takes a list as input from user, changes every element of the list to upper case
"""
def change_case():    
    try:
        list = []
        iterator = True

        while iterator:
            element = str(input("input list element, type stop when list is complete adding \n"))
            if element == "stop" or None:
                iterator = False
                print(list)
                break
            list.append(element)       
            
    except:
        print(list)



    finally:
        for i in range(len(list)):
            list[i] = list[i].upper()

        print(list)


def check_list_elements():
    list_of_nos = [1,2,3,4,5,6,7]
    for i in list_of_nos :
        if i%2 == 0 :
            print("even")
        else :
            print("odd")

def check_string_case():
    word = input("enter the word : ")

    if word.islower():
        print("lowercase")
    else :
        word.isupper()
        print("uppercase")

    
    





