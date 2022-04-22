# Bazi Sang-Kaghaz-Gheychi
# Game Rock(R)-Paper(P)-Scissors(S) ---> RPS
# version 2

print("Sang...")
print("Kaghaz...")
print("Gheychi...")

player1 = input("Player1, make your move: ")
print("Taghalob Nakon! \n\n " * 20)
player2 = input("Player2, make your move: ")

if player1 == player2:
    print("Maghadir mosavi hastand.")
elif player1 == "sang":
    if player2 == "gheychi":
        print("Player 1 wins!")
    elif player2 == "kaghaz":
        print("Player 2 wins!")
elif player1 == "kaghaz":
    if player2 == "gheychi":
        print("Player 2 wins!")
    elif player2 == "sang":
        print("Player 1 wins!")
elif player1 == "gheychi":
    if player2 == "sang":
        print("Player 2 wins!")
    elif player2 == "kaghaz":
        print("Player 1 wins!")
else:
    print("Khatei rokh dadeh ast...")
