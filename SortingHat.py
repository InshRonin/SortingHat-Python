
# Write code below 💖
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Welcome to the Sorting Hat of Hogwartz")

print()
questionOne = int(input("Q1 Do you like Dawn or Dusk?\n"
"1) Dawn\n"
"2) Dusk\n"
"Select one option:"))
if questionOne == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif questionOne == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

print()
questionTwo = int(input("Q2 When I'm dead, I want people to remember me as:\n"
    "1) The Good\n"
    "2) The Great\n"
    "3) The Wise\n"
    "4) The Bold\n"
"Select one option:"))
if questionTwo == 1 :
  Hufflepuff += 2
elif questionTwo == 2:
  Slytherin += 2
elif questionTwo == 3:
  Ravenclaw += 2
elif questionTwo == 4:
  Gryffindor += 2
else:
  print("Wrong input.")
  
print()
questionThree = int(input("Q3 Which kind of instrument most pleases your ear?\n"
    "1) The violin\n"
    "2) The trumpet\n"
    "3) The piano\n"
    "4) The drum\n"
"Select one option:"))
if questionThree == 1:
  Slytherin  += 4
elif questionThree == 2:
  Hufflepuff  += 4
elif questionThree == 3:
  Ravenclaw += 4
elif questionThree == 4:
  Gryffindor += 4
else:
  print("Wrong input.")
  
print()
print(f"Slytherin Score: {Slytherin}")
print(f"Hufflepuff Score: {Hufflepuff}")
print(f"Ravenclaw Score: {Ravenclaw}")
print(f"Gryffindor Score: {Gryffindor}")

print()
maxScore = max(Slytherin,Hufflepuff,Ravenclaw,Gryffindor)
if maxScore == Slytherin:
    print("Congrats! You are selected for Slytherin")
elif maxScore == Hufflepuff:
    print("Congrats! You are selected for Hufflepuff")
elif maxScore == Ravenclaw:
    print("Congrats! You are selected for Ravenclaw")
elif maxScore == Gryffindor:
    print("Congrats! You are selected for Gryffindor")
else:
    print("You made erros in the input. Please Retry Again")