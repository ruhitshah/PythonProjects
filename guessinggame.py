import random
jackpot = random.randint(1,100)

guess = int(input("Guess an int num:"))

counter=1

while guess != jackpot:
  if guess>jackpot:
    print("Guess a lower num.")

  else:
    print("Guess a higher num.")

  guess = int(input("Guess an int num:"))
  counter+=1

print("Predicted num is correct.")
print("You took",counter,"attempts.")
