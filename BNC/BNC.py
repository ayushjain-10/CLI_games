from random import randint

roles = ["Bear", "Ninja", "Cowboy"]

# get random no.
computer = roles[randint(0,2)]

player = False

while player == False:
    player = input("Bear, Ninja, or Cowboy? > ")

    # conditional statement used to compare roles
    if computer == player:
      print("DRAW!")
    elif computer == "Cowboy":
      if player == "Bear":
        print("You lose!", computer, "shoots", player)
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
    elif computer == "Bear":
      if player == "Cowboy":
        print("You win!", player, "shoots", computer)
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
      if player == "Cowboy":
        print("You lose!", computer, "defeats", player)
      else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)

    play_again = input("Do you want to play again? (type yes or no) ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break