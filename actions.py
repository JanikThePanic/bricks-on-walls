import random, actions, rooms, var, art, monsters
#Imports other files and random

#Keeps asking the user what class they want to be
def getClass():
	#Sets color of text
	#Will pose question and no accept anything but givin options
	print('\033[0;32;48m')
	var.userCLASS = input("\nWhat class do you wish to be? Fighter, Wizard or Paladin? Fighters do more damage. Wizards get a magical staff. Paladins are the knights of god.\n").lower()

	while var.userCLASS != "fighter" and var.userCLASS != "wizard" and  var.userCLASS != "paladin":
		print('\033[0;31;48m')#Sets text collor to red
		var.userCLASS = input("\nI didn't get that. Do you wish to be a Fighter, Wizard or Paladin?\n").lower()
		print('\033[0;37;48m')#Default Color

	#Puts classes into an int for eaiser future checking
	if var.userCLASS == "fighter":
		var.userCLASS = int(1)
	elif var.userCLASS == "wizard":
		var.userCLASS = int(2)
	elif var.userCLASS == "paladin":
		var.userCLASS = int(3)
	#Starts the game set-up and gives the player starter gear
	print('\033[0;37;48m')
	setPreGame(var.userCLASS)


#Starter gear and class stats
def setPreGame(userClass):
	if userClass == 1: #If fighter, strong but non magic
		var.ClassAC = 12
		var.HPmax = 22
		var.attackBonus = 4
		var.inv.append("sword")
		var.inv.append("apple")
		var.inv.append("magical soup")
		var.inv.append("magical soup")
		var.money = 25
		var.CurrentAC = var.ClassAC + 3
		var.HP = var.HPmax
	elif userClass == 2: #If wizard, weak, but magical
		var.ClassAC = 10
		var.HPmax = 16
		var.attackBonus = 1
		var.inv.append("torch")
		var.inv.append("magical soup")
		var.inv.append("staff")
		var.inv.append("magical scroll")
		var.inv.append("magical scroll")
		var.inv.append("potion")
		var.money = 15
		var.CurrentAC = var.ClassAC
		var.HP = var.HPmax
	elif userClass == 3: #Paladin is a mix
		var.ClassAC = 11
		var.HPmax = 19
		var.attackBonus = 3
		var.inv.append("sword")
		var.inv.append("magical soup")
		var.inv.append("apple")
		var.inv.append("holy symbol")
		var.inv.append("potion")
		var.inv.append("potion")
		var.money = 20
		var.CurrentAC = var.ClassAC + 2
		var.HP = var.HPmax


#Default line for if thats not an option
def line():
	print('\033[0;31;48m')#Sets text collor to red
	return input("\nSorry, I did't get that.\n").lower()
	print('\033[0;37;48m')#Default Color


#Gets User's name. Not cap sens so user can have user like xX_uSeR_Xx
def getUserName():
	var.userName = input("\nWhat would your name happen to be?\n")


#Randomly chooses to generate loot, and then randomly picks the loot
def getGroundLoot(chance):
	#Provided with chance varible
	if random.random() <= chance:
		return random.choice(var.possibleLoot)
	else:
		return ''


#Will determain if the user can see the loot
def tellUserOfLoot(loot):
	bonous = 0
	#Can see better if they have a torch
	if "torch" in var.inv:
		bonous = 15
	if random.randrange(1,101) <= (75+bonous):
		#If player can see the loot
		print("\nOn the ground, you see (a/an) " + loot + ".\n")
		return loot
	else:
		#If not
		print("\nThe ground seems empty as far as you can tell.\n")
		return ''


#Gives user actions to do, until they choose to leave aka "door"
def stdActions(loot):
	#Gives standard actions and what they do
	userAction = input("\nThere are some actions you can perform. Type ‘inv’ to access inventory, type ‘pickup’ to pick up items that have been revealed, type ‘stats’ to view your stats and type ‘door’ to go to a specific door.\n").lower()
	lootStat = loot #This is done so loot can't re pickuped

	#Will repeat untill they choose to leave
	while userAction != "door":
		if userAction == "inv":
			#If inv, will open inventory, and run the inv function
			openInv()

		elif userAction == "pickup":
			#Picks up loot, and sets it to nothing so it cant be repicked up
			print('\033[0;35;48m')#Sets text color to some pinky red thingy
			pickup(lootStat)
			lootStat = ""
			print('\033[0;37;48m')#Default Color

		elif userAction == "stats":#Shows current player stats
			print("") #New line
			print("Health Points:", var.HP) #Health
			print("Armour Class:", var.CurrentAC) #AC aka defence
			print("Balance:", var.money) #Money
			print("Name:", var.userName) #Name
			if var.userCLASS == 1: #Class
				print("Class: Fighter")
			elif var.userCLASS == 2:
				print("Class: Wizard")
			else:
				print("Class: Paladin")

		#Poses the question of next action
		print('\033[0;31;48m')#Sets text color to red
		userAction = input("Inv, pickup, stats, or door?\n").lower()
		print('\033[0;37;48m')#Default Color


#When chest is opened
def chest(loot):
	userIn = input("Do you wish to open the chest in the room? Yes or no?\n").lower()#Will ask
	while userIn != 'yes' and userIn != 'no':
		userIn = line()#and again

	if userIn == "yes":
		if loot != '': #If not empty
			print("You open the chest.")
			pickup(loot)
			var.chestLoot = ''
		else: #If empty
			print("The chest is empty.\n")


#If player picks something up
def pickup(loot):
	#If its nothing, then theirs nothing
	if loot == '':
		print("There's nothing to pick up.\n")
	else:
		#Some items have some art
		art.pickup(loot)
		#Gives them the line and adds the item to their inventory
		print("You have picked up (a/an) " + loot + ".\n")
		var.inv.append(loot)


#Opens INVENTORY
def openInv():
	print("\033[0;32;48m") #Sets colour
	print("OPENED INVENTORY\n") #Formatting
	print("You currently have...")
	#Runs thru inv, and lists it with caps on first letter
	var.inv = sorted(var.inv)
	for i in range(0, len(var.inv)):
		temp = var.inv[i]
		temp = temp[0].upper()+temp[1:len(temp)]
		print(temp)

	#Asks what the user wants to do, and gives option to exit
	userIn = input("\nType ‘use’ to use something you have. Type ‘exit’ to exit inventory.\n").lower()
	while userIn != "use" and userIn != "exit":#Will ask again if option not met
		userIn = line() #Will not accept anything but the posed options

	if userIn == "use": #If user wants to use an item
		print("\033[0;32;48m")
		toUse = input("\nWhich item do you wish to use?\n").lower()

		while toUse not in var.inv:
			toUse = input("\nYou don't have that. What do you wish to use?\n").lower()
			#Repeats till user gives item they have

		useItem(toUse)#Sends the usage item to the USE function
	
	if userIn == "exit": #Exits inv if they want to exit
		return


#Use of all items
def useItem(item):
	#Function for using items
	#Will maybe do some art, remove the item, then do the items thing, and return

	if item == "apple":#Use of apple
		art.yum()
		var.inv.remove(item)
		gainHP(2)
		print("\nYou gained back 2HP, and are at "+str(var.HP) + ".")
		return
	if item == "magical soup":#Use of soup
		soupTime()
	if item == "potion":#Use of potion
		potionTime()
		return
	if item == "sword":#Explains sword
		print("\nThis item can only be used during combat.\n")
		return
	if item == "strong sword":#Explains strong sword
		print("\nThis item can only be used during combat.\n")
		return
	if item == "staff":#Explains staff
		print("\nThis item can only be used during combat.\n")
		return
	if item == "armour":#Uses armour
		var.inv.remove("armour")
		var.CurrentAC += 1
		print("\nYou have put on armour, your AC is now " + str(var.CurrentAC) + ".\n")
		return
	if item == "torch":#Explains torch
		print("\nThis item allows you to see better and is already held.\n")
		return
	if item == "magical scroll":#Uses scroll
		scrollTime()
		return
	if item == "holy symbol":#Explains symbol
		print("\nThis item will give you a second life, and can't be used right now.\n")
		return
	if item == "rope":#Explains rope
		print("\nThis item can only be used in certain rooms.\n")
		return
	if item == "golden key":#Explains gkey
		print("\nThis item will open golden locks.\n")
		return
	if item == "silver key":#Explains skey
		print("\nThis item will open silver locks.\n")
		return

	else:#Anything else
		print("\nThat item can't be used, or is automatically equiped.\n")
		return


#For when HP is added and doesn't go over the max
def gainHP(HPadded):
	var.HP += HPadded
	if var.HP > var.HPmax:
		var.HP = var.HPmax


#For when HP is taken away and checks for death
def loseHP(HPlost):
	var.HP = var.HP - HPlost
	#If dead
	if var.HP <= 0:
		if "holy symbol" in var.inv:
			#If they have a holy symbol, they live again with little hp
			var.HP = random.randrange(1,5)
			var.inv.remove("holy symbol")
			print("You have died, but thankfully your Holy Symbol has saved you. Your HP is now " + str(var.HP) + ".\n")
		else:
			#If they dont, well sucks
			art.death()
			#Tells how girl is not there forever
			if var.girlThere == False:
				print("The girl you also took with you is now left for the eating of the " + monsters.monName)
			#Asks if the user wishes to play again
			again = input("Type 'enter' to play again.\n").lower()
			while again != "enter":
				 again = input("Type 'enter' to play again.\n").lower()
			#Resets varibles
			var.inv.clear()
			monsters.hp = 0
			monsters.ac = 0
			monsters.monAlive = False
			monsters.monName = ''
			monsters.dragonAlive = True
			monsters.angelAlive = TrueClassAC = 0 #Stays the same through the game
			var.CurrentAC = 0 #Used to calculate if a computers attack hits
			var.attackBonus = 0 #Used to calculate if a users attack hits
			var.money = 0 #Users money which can buy things in the store room
			var.userCLASS = 0 #Fighter is 1, Wizard is 2, Paladin is 3
			var.userName = '' #Users name
			var.girlWith = False #Is the girl in the room with the user?
			var.ringWish = False #Will the user return the ring to the woman of the dead man?
			var.chestLoot = ''
			var.scrolls = 3 #There are three scrolls in the lia and when taken, will be none
			var.potions = 3 #There are three potions in the potion-room and when taken, will be none
			var.girlThere = True #Shows that the girl is still there in the room alone
			var.dragonAlive = True #Draogn in room needs to be defeated ONCE
			var.mimicAlive = True #Mimic in room needs to be defeated ONCE
			var.angelAlive = True #Killed only once, if killed at all
			var.deadManAlive = True #The almost dead npc in deadRoom()
			var.knight = True #The undead knight in cultRoom only exists once
			var.treasure = True #Treasure room treasure only appears once
			#Imports main, and starts the start function
			import main
			main.start_game()


#Soup has random effects
def soupTime():
	var.inv.remove("magical soup")
	effect = random.randrange(0,3)
	art.yum()

	if effect == 0:#Healing effect
		gainHP(10000)
		print("\nYou ate a soup of healing ability, your HP is now " + str(var.HP) + ".\n")
	if effect == 1:#Poison
		print("\nYou have poisoned yourself")
		loseHP(random.randrange(1,9))
		print("Your HP is now " + str(var.HP) + ".\n")
	if effect == 2:#AC boost
		var.CurrentAC += 1
		print("\nYour immune system has gotten stronger, your AC is now " + str(var.CurrentAC) + ".\n")


#Potion has random effects
def potionTime():
	var.inv.remove("potion")
	effect = random.randrange(0,3)
	art.yum()

	if effect == 0:#Healing effect
		gainHP(10000)
		print("\nYou drank a potion of healing ability, your HP is now " + str(var.HP) + ".\n")
	if effect == 1:#Poison
		print("\nYou have poisoned yourself")
		loseHP(random.randrange(1,9))
		print("Your HP is now " + str(var.HP) + ".\n")
	if effect == 2:#AC boost
		var.CurrentAC += 1
		print("\nYour immune system has gotten stronger, your AC is now " + str(var.CurrentAC) + ".\n")


#Scroll has random effects
def scrollTime():
	print('\033[0;36;48m')#Sets text collor to cyan
	var.inv.remove("magical scroll")
	effect = random.randrange(0,3)

	if effect == 0:#Summons loot
		loot = random.choice(var.possibleLoot)
		var.inv.append(loot)
		print("\nThe scroll hovers and burns to summon (a/an) " + loot + ", which is added to your inventory.\n")
	if effect == 1:#Richs
		temp = random.randrange(2,10)
		var.money += temp
		print("\nYour scroll flashes, and in its place you find " + str(temp) + " coins.\n")
	if effect == 2:#Kill the dead
		if monsters.monAlive:
			monsters.hp = 1
			print("\nThe scroll mocks the beast to a critical point.\n")
		else:
			print("\nThe scroll vanished, with no effect that you can see.\n")
	
	print('\033[0;37;48m')#Default Color


#Door needs to be picked but some have key
def pickDoorsKey(a,b,c,d):
	print('\033[0;33;48m')#Sets text color to yellow

	userIn = ""
	userIn = input("What door do you wish to go into?\n").lower()
	while userIn != a and userIn != b and userIn != c and userIn != d:
		userIn = input("\nThat door either does not exist, or is locked. Pick another.\n").lower()
	return userIn


#Will be called once the player needs to pick a door, the function requires the amount of doors to choose from
def pickDoor(doors):
	print('\033[0;33;48m')#Sets text color to yellow

	userIn = ""
	#I was too lazy to use dictonaries, so i just made a if and while for doors from 1 to 4

	if doors == 1: #Incase of 1 door
		userIn = input("\nThere is only a door A. Type the letter of the door you wish to enter.\n").lower()
		while userIn != 'a':
			userIn = input("\nSorry. There is only Door A. Type the letter A.\n").lower()
		return 'a'

	if doors == 2: #Incase of 2 doors
		userIn = input("\nThere is Door A and Door B. Type the letter of the door you wish to enter.\n").lower()
		while userIn != 'a' and userIn != 'b':
			userIn = input("\nSorry. There is only Door A and Door B. Type the letter after 'Door'.\n").lower()
		if userIn == 'a':
			return 'a'
		else:
			return 'b'

	if doors == 3: #Incase of 3 doors
		userIn = input("\nThere is Door A, Door B and Door C. Type the letter of the door you wish to enter.\n").lower()
		while userIn != 'a' and userIn != 'b' and userIn != 'c':
			userIn = input("\nSorry. There is only Door A, Door B and Door C. Type the letter after 'Door'.\n").lower()
		if userIn == 'a':
			return 'a'
		elif userIn == 'b':
			return 'b'
		else:
			return 'c'

	if doors == 4: #Incase of 4 doors
		userIn = input("\nThere is Door A, Door B, Door C and Door D. Type the letter of the door you wish to enter.\n").lower()
		while userIn != 'a' and userIn != 'b' and userIn == 'c' and userIn == 'd':
			userIn = input("\nSorry. There is only Door A, Door B, Door C and Door D. Type the letter after 'Door'.\n").lower()
		if userIn == 'a':
			return 'a'
		elif userIn == 'b':
			return 'b'
		elif userIn == 'c':
			return 'c'
		else:
			return 'd'

	print('\033[0;37;48m')#Default Color