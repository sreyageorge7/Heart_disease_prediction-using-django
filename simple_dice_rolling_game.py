while True:
    choice = input('ROLL THE DICE?(y/n): ').lower()
    if choice == 'y':
      import random
      dice1 = random.randint(1, 6)
      dice2 = random.randint(1, 6)
      print(f"{dice1},{dice2}")
    elif choice == 'n':
          print("thanks for playing")
          break
    else:
          print("Invalid input. Please enter 'y' or 'n'")