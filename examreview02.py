#STEP 1
def name():
  print("Welcome to KFC, we have three things in our menu:")
  print("Chicken Tenders: 4.00 / Fried Wings: 5.00 / Popcorn Nuggets 3.00")
  print("Tell me, option 1, 2 or 3?")
  option = input()
  if option == "1":
    number = 4.00
  if option == "2":
    number = 5.00
  if option == "3":
    number = 3.00
  print("Discount cupon? How much discount does it give you?")
  discount = input()
  substraction = 100-int(discount)
  result = (int(number)/100)*substraction
  print("You need to pay:", result,"Have a nice day.")
#STEP 2
name()
