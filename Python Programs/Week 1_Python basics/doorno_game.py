s=input("Enter any word: ")
count=len(s)
if count%2==0:
    print("LEVEL 1 - GUESS SAFE DOOR NO")
    comp_no=count/2
    chance = 1
    while chance<=3:
        user_no=int(input("Guess which door no is safe to go next ? :"))
        if user_no==comp_no:
            print("Hurray!....You've guess the safe door")
            break
        else:
            print(f"Oops, youve guessed wrong....youve {3-chance} chance")
            chance+=1
else:
    print("Youre lucky enough to go")
