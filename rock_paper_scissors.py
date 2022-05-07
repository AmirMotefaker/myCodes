# Code by amotef@gmail.com

# Game Rock(R)-Paper(P)-Scissors(S) ---> RPS

print("Sang...")
print("Kaghaz...")
print("Gheychi...")

player1 = input("Player1, make your move: ")
player2 = input("Player2, make your move: ")

if player1 == "sang" and player2 == "gheychi":
    print("Player 1 wins.")
elif player1 == "sang" and player2 == "kaghaz":
    print("Player 2 wins.")
elif player1 == "kaghaz" and player2 == "sang":
    print("Player 1 wins.")
elif player1 == "kaghaz" and player2 == "gheychi":
    print("Player 2 wins.")
elif player1 == "gheychi" and player2 == "sang":
    print("Player 2 wins.")
elif player1 == "gheychi" and player2 == "kaghaz":
    print("Player 1 wins.")
elif player1 == player2:
    print("har do meghdar barabar ast")
else:
    print("khataei rokh dadeh ast")
