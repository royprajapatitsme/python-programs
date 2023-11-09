import random
import math

user1 = str(input("Enter first user name:- "))
 
user2 = str(input("Enter seconds user name:- "))


 
# generating random number between
x = random.randint(user1, user2)
print("\n\tYou've only ",
       round(math.log(user2 - user1 + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(user2 - user1 + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = str(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(user2 - user1 + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
