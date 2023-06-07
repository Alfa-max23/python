import builtins




cloud_env = ["aws","azure","gcp"]

#if there is error in try block then except block will run
try:
    print(cloud_env[200])  #try changing index value to 0,5,100
except:
    print("exception handled")
finally:
    print("I will execute anyways")

#raise Exception("this is a new exception")

print("this code should run")

try:
    print(cloud_env[200])
    a=10
    b=0
    c=a/b
except ZeroDivisionError as e:
    print("1",e)
except IndexError as e:
    print("2", e)

print(dir(builtins)) #this will list all the builtin errors
