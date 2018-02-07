user = ["arun", "prasanna", "maddy", "arunprasanna"]
sathyam = 100

while True :
    print("welcome to ticket rec seystem")
    ip = input("enter the user name to login : ").strip().lower()
    if ip in user:
        print (("hello {}" ).format(ip))
        total = int (input("how many tickets you would like to book"))
        if total < sathyam :
            print ("your ticket has been booked")
            sathyam = sathyam - total
        else :
            print("booing is full sorry ")
    else :
        print("user name dose not exit in list whould you like to add ?")
        add = input("Enter Y or N to continue ").strip().lower()
        if add == 'y':
            user.append(ip)
            print (user)

