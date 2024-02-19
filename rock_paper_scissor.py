import random

play = False               
wins, losses, ties = 0,0,0 #score tracking of User
w, l = 0,0                 #score tracking of Computer
names = {'R':'Rock', 'P':'Paper','S':'Scissors'}

# while loop till the user doesn't Quit the game
while play == False: 
    choice = input("Please choose your next move('R' for rock, 'P' for paper and 'S' for scissors) or 'Q' to quit the game: ")
    computer_choice = random.choice(['R','P','S'])
    if choice == computer_choice:
        print(f"Your choice: {names[choice]}")
        print(f"Computer's choice: {names[computer_choice]}")
        print("It is a Tie")
        ties += 1
    elif choice != 'R' and choice != 'S' and choice != 'P' and choice!= 'Q':
        print("Please enter correct choice")
    elif choice == 'Q':
            print("Thank you for playing!!")
            play = True
    else: #all rock paper scissor choices
        print(f"Your choice: {names[choice]}")
        print(f"Computer's choice: {names[computer_choice]}")
        if choice =='R' and computer_choice == 'S':
            print("Yayy!! You won!")
            wins += 1
            l += 1
        elif choice == 'R' and computer_choice == 'P':
            print("Oh Noo!! You lost!")
            losses += 1
            w += 1
        elif choice == 'S' and computer_choice == 'R':
            print("Oh Noo!! You lost!")
            losses += 1
            w += 1
        elif choice == 'S' and computer_choice == 'P':
            print("Yayy!! You win!")
            wins += 1
            l += 1
        elif choice == 'P' and computer_choice == 'R':
            print("Yayy!! You win!")
            wins += 1
            l += 1
        elif choice == 'P' and computer_choice == 'S':
            print("Oh Noo!! You lost!")
            losses += 1
            w += 1
        else:
            pass

    #showing game status
    print(f"Your Status: {wins} Wins, {losses} Losses, {ties} Ties")
    print(f"Computer's Status: {w} Wins, {l} Losses, {ties} Ties")
        

    