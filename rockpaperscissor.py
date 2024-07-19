import random
print("winning rules of the game ROCK PAPER SCISSORS are:\n"
      +"Rock vs Paper -> Paper wins\n"
      +"Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissor wins\n ")
while True:
    print("Enter your choice \n 1 - Rock\n 2-Paper\n 3-Scissors\n")
    choice = int(input("Enter your choice"))
    while choice > 3 or choice < 1:
        choice = int(input(" Enter a valid choice:"))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2 :
        choice_name == 'Paper'
    else:
        choice_name == 'Scissors'
    print('user choice is \n',choice_name)
    print('Now its Computers Turn...')
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is \n",comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)
    if choice == comp_choice:
        print('Its a Draw',end="")
        result = "DRAW"
    if choice == 1 and comp_choice == 2:
        print('paper wins =>',end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>',end="")
        result = 'Paper'
    if choice == 1 and comp_choice == 3:
        print('Rock wins =>\n',end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
         print('Rock wins =>\n',end="")
         result = 'Rock'
    if choice == 2 and comp_choice == 3:
         print('Scissors wins =>\n',end="")
         result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>\n',end="")
        result = 'Scissors'
    if result == 'Draw':
        print("<== Its a tie==>")
    if result == choice_name:
        print("<== user ==>")
    else:
        print("<==Computer wins==>")
    print("do u want to play again?")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing")               