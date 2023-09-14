#STEP 1
def name():
  print("Welcome you average dumb student")
  print("You give me three grades (from 01 to 100), I tell you your average.")
  print("Tell me, what was your first grade?")
  first = input()
  print("Mmmmmmkay...")
  print("And what was your second grade?")
  second = input()
  print("Mmmmmmmmmmmmriiiight...")
  print("Finally, and the third one?")
  third = input()
  print("Mmmmmhhhmmm...")
  print("Let me see, let me see...")
  result = (int(first)+int(second)+int(third))/3
  print("Your average grade would be:", result, ". Mkay?")
  if result > 70:
    print("Lucky you, you aren't failing.")
  else:
    print("Uufff, you failed... Special needs schools are still available!")
#STEP 2
name()
