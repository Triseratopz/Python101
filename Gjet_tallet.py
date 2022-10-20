import random
	
randomTall = random.randint(1, 20)

#Variabel som holder telling på hvor mange gjettinger vi gjort.
numberOfGuesses = 1

#Variabel som holder styr på hvis loopen ska kjøre eller ikke.
isRunning = True

print ("Gjett på et tall mellom 1 og 20")

guess =input("Hvilket nummer gjeter du: ")


while isRunning:

	# Sjekker hvis vi har noen gjettinger igjen
	if numberOfGuesses != 5: 
	
		# Sjekke hvis brukerern har gjettet riktig tall
		if int(guess) == randomTall:
			
			print ("Du gjettet riktig")
			# Bryter loopen ved at sette isRunning til false.
			isRunning = False
		
		# Sjekker hvis brukeren gjettet for lavt
		elif int(guess) < randomTall:
		
			numberOfGuesses += 1
			# Gir hint om at brukeren gjettet for lavt og ber om en ny gjetting.
			print ("Du gjettet for lavt")
			guess = input("Gjett igjen: ")	

		# Sjekker hvis brukeren gjettet for høyt.
		elif int(guess) > randomTall:
			
			numberOfGuesses += 1
			# Gir hint om at brukeren gjettet for høyt og ber om en ny gjetting.
			print ("Du gjettet for høyt")
			guess = input("Gjett igjen: ")			

	# Hvis vi ikke har noen mere gjettinger igjen så printer vi ut GAME OVER
	# og bryter loopen ved å sette isRunning til false.
	else:
	
		print ("DU har gjettet feil for mange ganger")
		print ("GAME OVER")
		isRunning = False