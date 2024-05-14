import random ,time ,os ,emoji

list1=["rock","paper","scissor"]
os.system('cls')
print('\t     ROCK , PAPER & SCISSORS')
print("\n\t\t 1.PLAY    2.QUIT")
choice =input('\n\tEnter number to make a choice: ')
if choice == '1':
    while True:
        os.system('cls')
        print("\t\t\t GAMES ")
        print("\t 1.Rock \t 2.Paper \t 3.Scissors ")
        userchoice=int(input("\n\t Enter the number to make a choice: "))
        if userchoice == 1 :
            choice=list1[userchoice-1]
        elif userchoice == 2:
            choice = list1[userchoice-1]
        elif userchoice == 3:
            choice = list1[userchoice-1]
        else:
            print('Wrong choice.Plz Try Again ')
        comChoice=random.choice(list1)
        if (choice =="paper" and comChoice== "rock") or (choice =="rock" and comChoice =="scissor") or (choice =="scissor" and comChoice =="rock"):
            print(f"\t   You :{choice}  Computer :{comChoice}")
            print('\n\t\t You have won!! 🥳 ')
        elif (choice ==comChoice):
            print()
            print(f"\t   You: {choice}  Computer:{comChoice}")
            print("\n\t\t It's a TIE 😬")
        else :
            print(f"\t   You: {choice}  Computer: {comChoice}")
            print('\n\t\t You have lost 😵‍💫')

        try :
            playChoice=int(input('\nEnter 1 to play again, otherwise quit the game:'))
        except Exception as e:
            print(f'{e} error occurred so exiting...')
            time.sleep(4)
        if playChoice ==1:
            continue
        else:
            break
print(emoji.emojize('\n\t  Thank you for with us playing \U0001f600'))
print('\n\t\tWe are exiting......')
time.sleep(4)