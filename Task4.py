replies=["Hi!","I'm fine, Thanks","Goodbye!"]
user=input("Enter Message: ").strip().lower()
if user=="hello":
    print(replies[0])
elif user=="how are you":
    print(replies[1])
elif user=="bye":
    print(replies[2])
else:
    print("Invalid Message")