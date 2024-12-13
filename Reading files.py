fileName = 'Guest.txt'
with open(fileName) as file_Object:
    content=file_Object.read()
    if not content:
        with open(fileName,'a') as file_Object:
            file_Object.write("these are the guests in our Hotel\n")

print("Welcome to our Hotel")

if(input("will you be checking into a room(y/n)")=='y'):
    name=input("What name would you be checking in under\n")
    print(f"Enjoy your stay,{name}")

    with open(fileName,'a') as file_Object:
        file_Object.write(f"{name}\n")


