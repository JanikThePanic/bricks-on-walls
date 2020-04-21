import random, actions, rooms, var, art
#Imports other files and random
#Creates what will be global vars that will be used for mobs in a room
hp = 0
ac = 0
monAlive = False
monName = ''

#Genrates a monstor with a max challenge rating between 1 and 100
def genMon(dif):
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName

	monDif = random.randrange(0, dif)

	if monDif < 20: #Easy mobs
		if random.randrange(0,2) == 1:
			monAlive = True
			monName = "goblin"
		else:
			monAlive = True
			monName = "zombie"
	elif monDif < 40: #Meh mobs
		if random.randrange(0,2) == 1:
			monAlive = True
			monName = "troll"
		else:
			monAlive = True
			monName = "orc"
	elif monDif < 60: #Okay, maybe
		print("knight")
	elif monDif < 80: #Damn, a worthy opponent
		print("mindflayer")
	else: #Oh...
		print("dragon")


#Combat system that will ask what you want to do
def combat():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Will ask user if they wish to take action
	userAction = input("\nIt prepares to attack, what do you do?\nType ‘hit’ to attack. Type ‘inv’ to open inventory. Type 'stats' to view stats.\n").lower()

	while hp > 0:#Will repeat until the monster dies, or the user dies, but that would stop this loop indirectly
		print('\033[0;31;48m')#Sets color to red
	
		#Users actions / turn

		while userAction != 'hit' and userAction != 'inv' and userAction != 'stats':
			userAction = input("\nType ‘hit’ to attack. Type ‘inv’ to open inventory. Type 'stats' to view stats.\n").lower()
		
		#If the player chose to open inv
		if userAction == 'inv':
			actions.openInv()
			userAction = ''
	
	#Shows current player stats
		if userAction == "stats":
			print("")
			print("Health Points:", var.HP)
			print("Armour Class:", var.CurrentAC)
			print("Balance:", var.money)
			print("Name:", var.userName)
			#Classes int to strings
			if var.userCLASS == 1:
				print("Class: Fighter")
			elif var.userCLASS == 2:
				print("Class: Wizard")
			else:
				print("Class: Paladin")
			userAction = ''

		#If the player chose to hit
		if userAction == 'hit':
			attack()
			userAction = ''
			#Monsters Turn ONLY IF PLAYER HITS
			if monName == "goblin":
				goblinAtk()
			if monName == "zombie":
				zombieAtk()
			if monName == "troll":
				trollAtk()
			if monName == "orc":
				orcAtk()
			if monName == "mimic":
				mimicAtk()
			if monName == "knight":
				knightAtk()
			if monName == "dragon":
				dragonAtk()
			if monName == "angel":
				angelAtk()

#User attacks something
def attack():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName

	print("\nYou have...")
	for i in range(0, len(var.inv)):
	#Runs thru inv, and lists it with caps on first letter
		temp = var.inv[i]
		temp = temp[0].upper()+temp[1:len(temp)]
		print(temp)

	weapon = input("\nWhat do you wish to attack with?\n").lower()
	while (weapon != 'sword' and weapon != 'strong sword' and weapon != 'staff') or weapon not in var.inv:
		#If they pick something that they dont have
		weapon = input("\nYou don't have that or this item can not be used to attack. Type something else.\n").lower()
	
	#Using DnD combat system
	#Roll 20 sided die to see if you hit
	#Roll d4, d6, d8, or d12 to see the damage if hit

	#Will send a 'hit' function with the weapon name and the die used to determine damage
	if weapon == "sword":
		hit('Sword', 6)
	elif weapon == "strong sword":
		hit('Strong Sword', 8)
	elif weapon == 'staff':
		hit('Staff', 12)


#Checks to see if player hit
def hit(weapon, die):
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName

	print("\nYou attack with your " + str(weapon))
	print("You roll a D20 to hit, and add your Attack Bonus.")
	roll20 = random.randrange(1,21)
	rollHit = roll20 + var.attackBonus
	print("You got a " + str(rollHit))
	#Checks if you hit, roll vs ac of mob
	if rollHit > ac:
		print("You hit!")
		damage(var.attackBonus, die)
	else:
		print("You miss.\n")
		

#For when mobs take damage
#BTW die is single for dice
def damage(attackB, die):
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName

	damage = attackB + random.randrange(1,die+1)
	print("You deal " + str(damage) + " points of damage.\n")
	hp = hp - damage #Sets hp to damaged hp
	if hp <= 0:
		#gives money for winning
		coins = random.randrange(1,6)
		var.money += coins
		#resets mob stuff
		hp = 0
		ac = 0
		monAlive = False
		monName = ''
		print("You have killed the monster and gained " + str(coins) + " coin(s)!\n")


#Calls the intro based on the name
def monIntros(name):
	if name == 'goblin':
		goblinIntro()
	if name == 'zombie':
		zombieIntro()
	if name == 'troll':
		trollIntro()
	if name == 'orc':
		orcIntro()
	if name == 'mimic':
		mimicIntro()
	if name == 'knight':
		knightIntro()
	if name == 'dragon':
		dragonIntro()
	if name == 'angel':
		angelIntro()



#Goblin intro and setup
def goblinIntro():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Sets the monster stats
	hp = 7
	ac = 14
	monAlive = True
	monName = 'goblin'
	#Some roleplay i guess
	print("\nA goblin snarls at you. Seeing a human such as yourself, it is disgusted.")
	combat()


#Goblin attack
def goblinAtk():
	#Goblins chance to hit
	rollHit = random.randrange(1,21) + 2
	#If hits or not
	if rollHit > var.CurrentAC:
		damage = random.randrange(1,7) + 2
		print("The goblin swings his club and hits.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	else:
		print("The goblin swings his club and misses.")


#Zombie intro and setup
def zombieIntro():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Sets the monster stats
	hp = 22
	ac = 8
	monAlive = True
	monName = 'zombie'
	#Some roleplay i guess
	print("\nA zombie awakes, still dead that is. It sees you, a living mortal. Death lights its dark eyes.")
	combat()


#Zombie attack
def zombieAtk():
	#zombies chance to hit
	rollHit = random.randrange(1,21) + 1
	#If hits or not
	if rollHit > var.CurrentAC:
		damage = random.randrange(1,5) + 1
		print("The zombie scratches you.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	else:
		print("The zombie misses to scratch you.")


#troll intro and setup
def trollIntro():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Sets the monster stats
	hp = 25
	ac = 10
	monAlive = True
	monName = 'troll'
	#Some roleplay i guess
	print("\nA mighty troll stands to its full height, which happens to be just over eight feet.")
	combat()


#troll attack
def trollAtk():
	#troll chance to hit
	rollHit = random.randrange(1,21) + 2
	#If hits or not
	if rollHit > var.CurrentAC:
		damage = random.randrange(1,7) + 2
		print("The troll swings his great and mighty club and hits.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	else:
		print("The troll swings his great and mighty club and misses.")


#orc intro and setup
def orcIntro():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Sets the monster stats
	hp = 32
	ac = 9
	monAlive = True
	monName = 'orc'
	#Some roleplay i guess
	print("\nA fat and floppy foot slaps the ground. An orc has awaken, and it’s not happy when awake.")
	combat()


#orc attack
def orcAtk():
	#orc chance to hit
	rollHit = random.randrange(1,21) + 3
	#If hits or not
	if rollHit > var.CurrentAC:
		damage = random.randrange(1,7) + 3
		print("The orc thrusts its meaty fist at you and hits.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	else:
		print("The orc thrusts its meaty fist at you and misses.")


#mimic intro and setup
def mimicIntro():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Sets the monster stats
	hp = 12
	ac = 12
	monAlive = True
	monName = 'mimic'
	#Some roleplay i guess
	print("\nThe mimic opens its mouth to reveal many sharp and bloodthirsty teeth.")
	combat()


#mimic attack
def mimicAtk():
	#mimic chance to hit
	rollHit = random.randrange(1,21) + 4
	#If hits or not
	if rollHit > var.CurrentAC:
		damage = random.randrange(1,7) + 4
		print("The mimic goes for a bite and lands.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	else:
		print("The mimic goes for a bite but misses.")


#knight intro and setup
def knightIntro():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Sets the monster stats
	hp = 20
	ac = 15
	monAlive = True
	monName = 'knight'
	#Some roleplay i guess
	print("\nYou hear the metallic steps behind you. You turn around to see a tall knight in full metal armour")
	combat()


#knight attack
def knightAtk():
	#knight chance to hit
	rollHit = random.randrange(1,21) + 5
	#If hits or not
	if rollHit > var.CurrentAC:
		damage = random.randrange(1,7) + 5
		print("The knight swings his sword and hits.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	else:
		print("The knight swings his sword and misses.")


#dragon intro and setup
def dragonIntro():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Sets the monster stats
	hp = 40
	ac = 10
	monAlive = True
	monName = 'dragon'
	#Some roleplay i guess
	print("\nFire is shot from behind you as you feel the presence of a mighty dragon.")
	combat()


#dragon attack
def dragonAtk():
	#dragon chance to hit
	rollHit = random.randrange(1,21) - 1
	#If hits or not
	if rollHit > var.CurrentAC:
		damage = random.randrange(1,5)
		print("The dragon spits a fireball at you and hits.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	else:
		print("The dragon spits a fireball at you and and misses.")


#angel intro and setup
def angelIntro():
	#Pulls the global monster stats
	global hp 
	global ac
	global monAlive
	global monName
	#Sets the monster stats
	hp = 85
	ac = 5
	monAlive = True
	monName = 'angel'
	#Some roleplay i guess
	print("\nThe angel’s eyes turn white red as a sword made of pure feathers summons in his hand.")
	combat()


#angel attack
def angelAtk():
	#angel chance to hit
	rollHit = random.randrange(1,21) + 2
	#If hits or not
	if rollHit > var.CurrentAC:
		damage = random.randrange(1,5)
		print("The angel swings at you and hits.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	else:
		print("The angel swings at you and misses.")