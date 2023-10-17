#https://replit.com/join/cspiorcqeq-mauro-alejandr6

#STEP1
def FEDEX():
  print("*WELCOME TO FEDEX SHOPPING COMPANY*")
  price=int(input("Please enter the price of the item you want to buy: \n"))
  print("Do you have a membership card? (Yes/No)")
  member = input()
  if price >= 100 and member == "Yes":
    discount_one = (int(price)/100)*85
    print("The total price is:", discount_one,", due to price being over 100 and membership card.")
  elif price >= 100 and member == "No":
    discount_two = (int(price)/100)*90
    print("The total price is:", discount_two,", due to price being over 100 and no membership card.")
  elif price < 100 and member == "Yes":
    discount_three = (int(price)/100)*95
    print("The total price is:", discount_three,", due to price being under 100 and membership card.")
  elif price < 100 and member == "No":
    discount_four = (int(price)/100)*100
    print("The total price is:", discount_four,", due to price being under 100 and no membership card.")
  else:
    print("Please check your data, there seems to be something wrong")
#STEP2
FEDEX()
