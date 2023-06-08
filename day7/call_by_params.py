def check_environment(list_of_env, test_env):
    output = []
    for env in list_of_env :
        if env.lower() == "aws":
            output.append("you are in aws")
        elif env.lower() == "azure":
            output.append("you are in azure")
        else :
            output.append("you are in gcp")
    
    return output

# op = check_environment(["AWS", "Azure"])
#print(op)