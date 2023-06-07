"""
This script checks if 
My Cloud Environment is amongst following
-AWS
-Azure
-GCP

"""

cloud_env = input("enter your cloud environment : ")
service = input("enter the service :")
print(cloud_env.upper.__doc__)

if cloud_env.lower() == "aws":
    print("you are in AWS")
    if service == "EC2":
        print("you are using ec2")
elif cloud_env.lower() =="azure" :
    print("you are in Azure")
elif cloud_env.lower() == "gcp" :
    print("you are in gcp")
else :
    print("Environments didn't match")

    

