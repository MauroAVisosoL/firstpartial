#https://replit.com/join/sfjljqwpvh-mauro-alejandr6

#STEP1
def DIET():
  print("Welcome to the brand new *HEALTHY DIET CALCULATOR* \n")
  print("Please fill the following data as it is asked.")
  age=int(input("Age of the patient: \n"))
  weight=int(input("Weight of the patient (Kilograms): \n"))
  height=float(input("Height of the patient (Meters with decimal): \n"))
  print("Level of physical activity: \n 1) Sedentary. - 2) Moderate. - 3) Active. (Please type 1, 2 or 3")
  activity=input()
  
  #Criteria 1 & 2:
  if age <= 18:
    print(" \n We reccomend a high carbohydrate diet.")
  elif 18 < age <= 30:
    print(" \n We recommend a high protein and lower carbohydrate diet.")
    if 18 <= age <= 30 and activity == "1" or "2":
      print("n You need aerobic exercises.")
  elif 30 < age < 35:
    print(" \n We recommend a high protein and lower carbohydrate diet.")
    if 30 < age <= 35 and activity == "1" or "2":
      print("...")
  elif age >= 35:
    print(" \n We reccomend a low sugar diet.")
  else:
    print(" \n There seems to be an unrecognizable input, please check your answers and start again.")
    
  #Criteria 3:
  squared_height = float(height)**2
  BMI = int(weight)/float(squared_height)
  if BMI <= 18 and activity == "1":
    print("\n Your BMI is:", BMI,", you need to consult a nutritionist and increase your physical activity.")
  elif 18 < BMI <= 25 and activity == "2":
    print("\n Your BMI is:", BMI,", you are in good condition.")
  elif BMI > 25 and activity == "1":
    print("\n Your BMI is:", BMI,", you need to consult a nutritionist, increase physical activity, and reduce your weight.")
  
#STEP2
DIET()
