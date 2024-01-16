Name = input("Please enter your name:\n")
print("Hello " + Name)

Age = input("Please enter your age:\n")
print(Name +" is " + Age + " years old")

if(int(Age) >= 18):
    print(Name + " is an adult")
else:
    print(Name + " is still a child")

if(Name == "Ahmed"):
    if(int(Age) == 18):
        print("Literally me")
    else:
        print("L age")
elif(int(Age) == 18):
    if(Name != "Ahmed"):
        print("L name")
else:
    print("L everything")
    