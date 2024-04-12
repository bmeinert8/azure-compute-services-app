def cloud_optimized():
    print("Excellent! Your application is already cloud optimized.")
    third_choice = input("Do you require HPC workload? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
    if third_choice == "1":
        print("Excellent! You should consider using Azure Batch.")
    else:
        print("Ok, you do not require HPC workload.")
        x_choice = input("Are you using Spring Boot apps? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
        if x_choice == "1":
            print("Great! You should consider using Azure Spring Apps.")
        else:
            print("Ok, you are not using Spring Boot apps.")
            fourth_choice = input("Do you require an event-driven workload with short lived processes? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
            if fourth_choice == "1":
                print("Great! You should consider using Azure Functions.")
            else :
                print("Ok, you do not require an event driven workload.")
                fifth_choice = input("Do you require a managed web hosting platform and features? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                if fifth_choice == "1":
                    print("Wonderful! You should consider using Azure App Service.")
                else:
                    print("Ok, you do not require a managed web hosting platform and features.")
                    sixth_choice = input("Do you need full-fledged orchistration? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                    if sixth_choice == "2":
                        print("Great! You should consider using Azure Container Instances.")
                    else:
                        print("Ok, wonderful. You do require full-fledged orchistration.")
                        seventh_choice = input("Do you require a managed service? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                        if seventh_choice == "2":
                            print("Since you do not require a managed service, you should consider your own orchestration implementation on Azure Virtual Machines such as: \n 1. VMware Tanzu on Azure VM \n 2. Kubernetes on Azure VM \n 3. OpenShift on Azure VM")
                        else:
                            print("Ok, you do require a managed service.")
                            eigth_choice = input("Are you familiar with Service Fabric or older .NET Framework? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                            if eigth_choice == "1":
                                print("Great! You should consider using Azure Service Fabric.")
                            else:
                                print("Ok, you are not familiar.")
                                nineth_choice = input("Are you using Red Hat Openshift? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                                if nineth_choice == "1":
                                    print("Great! You should consider using Azure Red Hat OpenShift.")
                                else:
                                    print("Alright, you are not using Red Hat Openshift.")
                                    tenth_choice = input("Do you need access to Kubernetes API? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                                    if tenth_choice == "1":
                                        print("Great! You should consider using Azure Kubernetes Service. (AKS)")
                                    else:
                                        print("Ok, You do not need access to Kubernetes API.")
                                        print("Based on your responses, you should consider using Azure Container Apps.")
                                        input("Press Enter to exit...")
                                        exit()                            


def containerized_app():
    print("Great! Lets get started with containerizing your application.")
    x_choice = input("Are you using Spring Boot apps? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
    if x_choice == "1":
        print("Great! You should consider using Azure Spring Apps.")
    else:
        print("Ok, you are not using Spring Boot apps.")
        fourth_choice = input("Do you require an event-driven workload with short lived processes? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
        if fourth_choice == "1":
            print("Great! You should consider using Azure Functions.")
        else:
            print("Ok, you do not require an event driven workload.")
            fifth_choice = input("Do you require a managed web hosting platform and features? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
            if fifth_choice == "1":
                    print("Wonderful! You should consider using Azure App Service.")
            else:
                print("Ok, you do not require a managed web hosting platform and features.")
                sixth_choice = input("Do you need full-fledged orchistration? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                if sixth_choice == "2":
                    print("Great! You should consider using Azure Container Instances.")
                else:
                    print("Ok, wonderful. You do require full-fledged orchistration.")
                    seventh_choice = input("Do you require a managed service? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                    if seventh_choice == "2":
                        print("Since you do not require a managed service, you should consider your own orchestration implementation on Azure Virtual Machines such as: \n 1. VMware Tanzu on Azure VM \n 2. Kubernetes on Azure VM \n 3. OpenShift on Azure VM")
                    else:
                        print("Ok, you do require a managed service.")
                        eigth_choice = input("Are you familiar with Service Fabric or older .NET Framework? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                        if eigth_choice == "1":
                            print("Great! You should consider using Azure Service Fabric.")
                        else:
                            print("Ok, you are not familiar.")
                            nineth_choice = input("Are you using Red Hat Openshift? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                            if nineth_choice == "1":
                                print("Great! You should consider using Azure Red Hat OpenShift.")
                            else:
                                print("Alright, you are not using Red Hat Openshift.")
                                tenth_choice = input("Do you need access to Kubernetes API? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                                if tenth_choice == "1":
                                    print("Great! You should consider using Azure Kubernetes Service. (AKS)")
                                else:
                                    print("Ok, You do not need access to Kubernetes API.")
                                    print("Based on your responses, you should consider using Azure Container Apps.")
                                    input("Press Enter to exit...")
                                    exit()                            
    

print("Welcome to the Azure compute services decicsion helper. Lets get started!")
input("Press Enter to continue...")
first_choice = input("Are you looking to build new or migrate an existing application? Please type 1 or 2 to select one of the following options: \n 1. Build new \n 2. Migrate  \n")
if first_choice == "1":
    print("Perfect! Lets get started with building a new application.")
    second_choice = input("Do you require full control over the infrastructure? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
    if second_choice == "1":
        print("Great! You should consider using Azure Virtual Machines.")
    else:
        print("Ok, you do not require full controll over the infrastructure.")
        third_choice = input("Do you require HPC workload? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
        if third_choice == "1":
            print("Excellent! You should consider using Azure Batch.")
        else:
            print("Ok, you do not require HPC workload.")
            x_choice = input("Are you using Spring Boot apps? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
            if x_choice == "1":
                print("Great! You should consider using Azure Spring Apps.")
            else:
                print("Ok, you are not using Spring Boot apps.")
                fourth_choice = input("Do you require an event-driven workload with short lived processes? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                if fourth_choice == "1":
                    print("Great! You should consider using Azure Functions.")
                else :
                    print("Ok, you do not require an event driven workload.")
                    fifth_choice = input("Do you require a managed web hosting platform and features? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                    if fifth_choice == "1":
                        print("Wonderful! You should consider using Azure App Service.")
                    else:
                        print("Ok, you do not require a managed web hosting platform and features.")
                        sixth_choice = input("Do you need full-fledged orchistration? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                        if sixth_choice == "2":
                            print("Great! You should consider using Azure Container Instances.")
                        else:
                            print("Ok, wonderful. You do require full-fledged orchistration.")
                            seventh_choice = input("Do you require a managed service? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                            if seventh_choice == "2":
                                print("Since you do not require a managed service, you should consider your own orchestration implementation on Azure Virtual Machines such as: \n 1. VMware Tanzu on Azure VM \n 2. Kubernetes on Azure VM \n 3. OpenShift on Azure VM")
                            else:
                                print("Ok, you do require a managed service.")
                                eigth_choice = input("Are you familiar with Service Fabric or older .NET Framework? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                                if eigth_choice == "1":
                                    print("Great! You should consider using Azure Service Fabric.")
                                else:
                                    print("Ok, you are not familiar.")
                                    nineth_choice = input("Are you using Red Hat Openshift? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                                    if nineth_choice == "1":
                                        print("Great! You should consider using Azure Red Hat OpenShift.")
                                    else:
                                        print("Alright, you are not using Red Hat Openshift.")
                                        tenth_choice = input("Do you need access to Kubernetes API? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
                                        if tenth_choice == "1":
                                            print("Great! You should consider using Azure Kubernetes Service. (AKS)")
                                        else:
                                            print("Ok, You do not need access to Kubernetes API.")
                                            print("Based on your responses, you should consider using Azure Container Apps.")
                                            input("Press Enter to exit...")
                                            exit()                            
else:
    print("Great! Lets get started with migrating an existing application.")
    eleventh_choice = input("Is your application already cloud optimized? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
    if eleventh_choice == "1":
        cloud_optimized()
    else:
        print("Ok, your application is not cloud optimized. So you will be doing an lift and shift migration.")
        twelveth_choice = input("Can your application be Containerized? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
        if twelveth_choice == "1":
            print("Perfect! We can containerize this application.")
            containerized_app()
        else:
            print("Ok, you cannot containerize this application.")
            thirteenth_choice = input("Is this a COTS app? Please type 1 or 2 to select one of the following options: \n 1. Yes \n 2. No \n")
            if thirteenth_choice == "1":
                print("Great! You should consider using Azure VMs.")
            else:
                print("Ok, this is not a CTOS app.")
                print("Based on your responses, you should consider using either Azure App Service or Azure Spring Apps.")
                input("Press Enter to exit...")
                exit()
