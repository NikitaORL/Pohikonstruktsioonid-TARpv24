from random import randint
from os import system

Player1Score = []
Player2Score = []
Nimi = str(input("Palun sisestage oma nimi: "))
print(f"Tere {Nimi}, täna hakkate mängima kivi, paber, käärid mängu!")
print("Teie vastane on robot")
system('cls')


while True:
    while True:
        try:
            
            player_choice = int(input("""Valige:
[1 - Kivi]
[2 - Käärid]
[3 - Paber]
> """))
            if player_choice not in [1, 2, 3]:
                print("Palun vali ainult 1, 2 ja 3!")
                continue
            break
        except ValueError:
            print("Sisestage kehtiv number (1, 2 või 3).")

    robot_choice = randint(1, 3)
    print(f"Robot valis: {robot_choice}")


    if player_choice == robot_choice:
        print("Viik!")
    elif (player_choice == 1 and robot_choice == 2) or (player_choice == 2 and robot_choice == 3) or (player_choice == 3 and robot_choice == 1):
        print(f"Õnnitleme, {Nimi}, sa võitsid!")
        Player1Score.append(1)
    else:
        print("Robot võitis!")
        Player2Score.append(1)

    
    print(f"\nSkorid: {Nimi}: {len(Player1Score)} | Robot: {len(Player2Score)}\n")

    
    while True:
        play_again = input("Kas soovite mängida veel? (jah/ei): ").lower()
        if play_again == "jah":
            system('cls')  
            break 
        elif play_again == "ei":
            print("Mäng on lõppenud!")
            print(f"Lõpptulemus: {Nimi}: {len(Player1Score)} | Robot: {len(Player2Score)}")
            
            break
        else:
            print("Palun sisestage 'jah' või 'ei'.")

    
    if play_again == "ei":
        break
