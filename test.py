#This is a test python file

def sorting_hat():
    name = input("Hello! Enter your first name: ")
    if name == "Harry":
        print("You're a wizard, Harry!")
    elif name == "Jacob":
        print("You aren't a wizard, Jacob.")
    elif len(name) < 5:
        print("Hufflepuff!!")
    elif "t" in name:
        print("Gryffindor!!")
    elif 5 <= len(name) < 7:
        print("Slytherin!!")
    else:
         print("Ravenclaw!")

while True:
    sorting_hat()
