#https://replit.com/join/jbaohzmhta-mauro-alejandr6

#STEP1
def GAME():
  import random
  print("Welcome to Mexico City RPG")
  print("You are a traveler in Mexico City")
  print("Select your character first:")
  print("1. El Vitor")
  print("2. El Albertano")
  print("3. El Chapulín Colorado")
  print("Enter the number of your chosen character:")
  character = input()
  if character == "1":
    print("You are El Vitor")
    character_selec = "Vitor"
  elif character == "2":
    print("You are El Albertano")
    character_selec = "Albertano"
  elif character == "3":
    print("You are El Chapulín Colorado")
    character_selec = "Chapulín Colorado"
  else:
    print("Input unrecognizable, restart.")

  print("You are traveling in a metro in Mexico City, a pickpocket gets behind you.")
  print("Quick,", character_selec, ",what do you do?")
  print("1.Fight" , "2.Steal" , "3.Run")
  choice = input()
  if choice == "1":
    result_one = ['You win the fight +4', 'You lose the fight -3']
    print(random.choice(result_one))
  elif choice == "2":
    result_two = ['You steal the money easily +2', 'He notices and shoots you -3']
    print(random.choice(result_two))
  elif choice == "3":
    print("Seriously? In a metro you tried to run away? -5")
  else: 
    print("Input unrecognizable, restart.")
    
  print("You are stuck in the traffic,", character_selec, ", what do you do?")
  print("1. Wait" , "2. Honk the horn" , "3. Get out of the car and walk")
  choice_two = input()
  if choice_two == "1":
    result_two_one = ['Nothing happened. -2', 'People moved +3']
    print(random.choice(result_two_one))
  elif choice_two == "2":
    result_two_two = ['You honk the horn, nobody notices. -2', 'People moved +3']
    print(random.choice(result_two_two))
  elif choice_two == "3":
    result_two_thre = ['You walk but a car runs over you. -6','You run and succeed. +5']
    print(random.choice(result_two_thre))
  else:
    print("Input unrecognizable, restart.")

  print("You have reached the end of this RPG, count your points and play again!")
#STEP2
GAME()

#END
