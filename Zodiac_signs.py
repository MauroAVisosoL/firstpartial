#https://replit.com/join/zmpmlotrhh-mauro-alejandr6

#STEP1
def zodiac():
  day=int(input("Please enter your birth day (number): "))
  month=int(input("Please enter your birth month (number): "))
  if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Your Zodiac sign is: Aquarius")
  elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("Your Zodiac sign is: Pisces")
  elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Your Zodiac sign is: Aries")
  elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Your Zodiac sign is: Taurus")
  elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("Your Zodiac sign is: Gemini")
  elif (month == 6 and day >= 21) or (month == 7 and day <= 22): 
    print("Your Zodiac sign is: Cancer")
  elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print ("Your Zodiac sign is: Leo")
  elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Your Zodiac sign is: Virgo")
  elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Your Zodiac sign is: Libra")
  elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Your Zodiac sign is: Scorpio")
  elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Your Zodiac sign is: Sagittarius")
  elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Your Zodiac sign is: Capricorn")
  else:
    print("Please enter a valid date based on numbers.")


#STEP2
zodiac()
