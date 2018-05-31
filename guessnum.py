from random import randint
from pickle import load, dump

# Load user preferences
try:
	with open(r"\guessnum.pref", "rb") as pref_file:
		prefs = load(pref_file)
		max_tries = prefs["max_tries"]
		max_number = prefs["max_number"]
	print("User preferences loaded!")
except:	
	max_tries = int(input("How many guesses you want? "))
	max_number = int(input("How many numbers you want to guess from: 1-"))

	# Save user preferences
	with open(r"\guessnum.pref", "wb") as pref_file:
		dump({"max_tries" : max_tries, "max_number" : max_number}, pref_file)
	
	print("User preferences saved!")

tries = max_tries
number = randint(1, max_number)
guess = 0

print("Ok, you have %d tries to guess a number from 1-%d!\n\n" % (tries, max_number))

def crazyMode():
	for x in range(randint(1, max_number), randint(1, max_number)):
		print("Is it... ", x)
		if x == number:
			return x
	return 0

while guess != number:
	guess = input("Is it... ")

	if guess:
		guess = int(guess)
		
		if guess == 32767:
			guess = crazyMode()
		
		tries -= 1

		if guess == number:
			print("Hoooorrraaay! You guessed it right!")
			break
		elif guess < number:
			print("It's bigger...\n")
		elif guess > number:
			print("It's not so big.\n")

		if tries > 0:
			print(tries, "guess(es) remaining!\n")
			if tries == 1:
				print("Last try!!!!\n")
		elif tries == 0:
			print("Sorry, you didn't get it in", max_tries, "guesses, the number was", number)
			break
	else:
		print("Hey! That's not a number!\n")


print("Thanks for playing!")
