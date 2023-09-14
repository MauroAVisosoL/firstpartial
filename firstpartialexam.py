#STEP 1
def name():
  print("Temperature Machine, Vibration Machine & Thermal Shock Machine bought")
  print("Temperate Machine: 15,000")
  print("Vibration Machine: 20,000")
  print("Thermal Shock Machine: 16,000")
  print("It would be a total of 51000")
  number = 51000
  print("What´s the percentage of your discount cuppon?")
  discount = input()
  substraction = 100-int(discount)
  result = (int(number)/100)*substraction
  print("You need to pay:", result,"Have a nice day.")
  yen = int(result)*8.37
  dollar = int(result)*0.057
  print("Dollar:",dollar,"Japanese Yen:",yen,"Have a nice day")
#STEP 2
name()
