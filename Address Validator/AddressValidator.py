def addressVal(address):
    if "@" not in address or "." not in address:
        return False
    
    dot = address.find(".")
    at = address.find("@")

    #'@' should come before last '.'
    if at<1 or dot<at+2 or dot == len(address) -1:
        return False

    return True

print("This program will decide if your input is a valid email address")
while(True):
    print("A valid email address needs an '@' symbol and a '.'")
    x = input("Input your email address(type 'exit' to quit): ")
    
    if x.lower() == "exit":
        break
    
    if addressVal(x):
        print("Valid")
    else:
        print("Invalid")