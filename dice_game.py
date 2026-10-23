import random

while True:
  choice = input("Roll the dice? (yes/no): ")
  if choice == "yes":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f"You rolled a {die1} and {die2}")
  elif choice == "no":
    print("Game over.")
    break
  else:
    print("Invalid option.")