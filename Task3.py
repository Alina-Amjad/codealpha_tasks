#moving same
import os
import shutil
source_file=os.getcwd()
destination_file=os.path.join(source_file,"images")
os.mkdirs("./images", exist_ok=True)
for file in os.listdir(source_file):
    if file.lower().endswith(".jpg"):
        full_path=os.path.join(source_file, file)
        shutil.move(full_path,destination_file)
print("ALL JPG Moved")

#email
import re
emails=[]
for file in os.listdir(source_file):
    if file.endswith(".txt"):
        with open("file","r") as f:
            content=f.read()
            found=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',content)
            emails.extend(found)
print("Emails Found: ")
print(emails)
