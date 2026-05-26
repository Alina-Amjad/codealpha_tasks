#Stock Portfolio Tracker
dict={}
add=0
while True:
    user_key=input("Enter Stock Name: ").strip()
    user_value=int(input("Enter Investment: "))
    dict[user_key]=user_value
    add_more=input("Enter any key to enter more item else enter N for no: ").strip().lower()
    if add_more=="n":
        break

for value in dict.values():
    add+=value
print("Total Investment : ",add)
with open("file.txt","a") as f:
    f.write("Total Investment:")
    f.write(str(add))
    f.write("\n")
f.close()