guess_list=["hi","hello","bye","goodbye","hurrah"]
print(len(set(guess_list[0])))
i=0
guess=0
correct=0
while i<len(guess_list):
    word=guess_list[i]
    print(word)
    string=""
    while True:
        user=input("Enter Your Choice: ").strip().lower()
        if user in set(guess_list[i]):
            string+=user
            print("correct")
            if len(string)==len(set(guess_list[i])):
                print("Guessed Right")
                break
        else:
            if guess==6:
                print("Chances Finished")
                break
            print("Wrong")
            guess+=1
    if  guess==6:
        break
    i+=1    

    
        
