#STEP 1
def name():
  print("Welcome to the cotton fields. Tell me how you would like me to call you.")
  variable = input()
  print("Hello my new favorite slave: ",variable)
  print("Give me today´s temperature in Celsius")
  number = input()
  result = int(number)*(9/5)+32
  print("Today's temperature in farenheit is",result,",man.")
  result = int(number)+273.15
  print("And in Kelvin it would be:", result,"man")
  print("Anything else you need?", variable,"?")
  variable = input()
  if variable == "yes":
    print("Nuh Huh, you're the slave here go hug a tree.")
  if variable == "no":
    print("Great, now stop bodering.")
    
  else:
    print("Do you even know how to speak properly you bastard????")
#STEP 2
name()
