import random, actions, rooms, var, art, monsters
#Imports other files and random


#THIS is the starting room, with no combat, just 3 doors, maybe loot, and a simple intro
def room_of_bricks():
	posLoot = "" #Makes local ground loot
	print('\033[0;36;48m')#Sets text collor to cyan

	posLoot = actions.getGroundLoot(75)#Will MAYBE spawn loot
	groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
	#Makes a drawing with or without loot
	if groundLoot != "":
		art.startRoom(True)
	else:
		art.startRoom(False)

	#Intro
	print("\nThe room is empty. Looking around, you see three doors. Door A seems to be a simple wooden door. Door B gives the vibe of treasure to behold. Lastly, door C looks as if it holds the knowledge of millions.\n")
	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(3)
	print('\033[0;37;48m')#Default Color
	#Calls next room
	if nextDoor == 'a':
		room_of_goblin()
	elif nextDoor == 'b':
		chest_room()
	elif nextDoor == 'c':
		library()



#One of the three rooms from the start, this room has a goblin and a golden key which will open the tresure room
def room_of_goblin():
	print('\033[0;36;48m')#Sets text collor to cyan
	posLoot = 'golden key'
	groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot

	goblin = random.randrange(1,101)#Most likly spawns a goblin
	if goblin <= 90:
		monsters.monAlive = True
		monsters.monName = "goblin"
	else:
		monsters.monAlive = False

	#Makes a drawing with or without loot and with maybe the goblin
	if groundLoot != "":
		art.goblinRoom(True, monsters.monAlive)
	else:
		art.goblinRoom(False, monsters.monAlive)

	if monsters.monAlive:
		print("\nThe room is cold, " + var.userName + ". As you enter, you notice the hideous creature in the corner. You shake in fear as you notice that it is armed. You fight begins.\n")
		print('\033[0;31;48m')#Sets color to red
		monsters.goblinIntro()
		print('\033[0;37;48m')#Default Color
	else:
		print("\nThe room is cold, " + var.userName + ". As you enter, there is nothing. Nothing alive or dead. Lucky you, I suppose.\n")

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(3)
	print('\033[0;37;48m')#Default Color

	if nextDoor == 'a':#Store needs key, so if the user doesnt have it /shrug
		if 'silver key' not in var.inv:
			print("You need a silver key to go here.")
			nextDoor = actions.pickDoorsKey("タイガ", "b", "c", "タイガ")#Will ask for b or c
		else:
			storeRoom()

	if nextDoor == 'b':
		mimicRoom()
	if nextDoor == 'c':
		room_of_bricks()



#One of the three rooms from the start, simple room with a meh mob and a chest
def chest_room():
	print('\033[0;36;48m')#Sets text colour to cyan
	posLoot = ''

	mob = random.randrange(1,101)#Most likly spawns a mob
	if mob <= 80:
		monsters.genMon(40)
	else:
		monsters.monAlive = False

	#Makes a drawing with chest and maybe mob
	art.chestRoom(monsters.monAlive)

	if monsters.monAlive:
		print("\nFear rushes. Just like you rushed to your senses when you saw the monster in the room, and additionally the chest there too.\n")
		print('\033[0;31;48m')#Sets color to red
		monsters.monIntros(monsters.monName)#Will spawn the monster needed
		print('\033[0;37;48m')#Default Color
	else:
		print("\nYou seem to have a sense that something is there. Right you were, a chest lies in the middle of the room.\n")

	actions.chest(var.chestLoot)#Gives the player a chance to open the chest

	actions.stdActions(posLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(2)
	print('\033[0;37;48m')#Default Color
	if nextDoor == 'a':
		trapRoom()
	elif nextDoor == 'b':
		room_of_bricks()


#Store room, player here can buy a better sword
def storeRoom():
	print('\033[0;36;48m')#Sets text collor to cyan
	posLoot = "" #Makes local ground loot so when actions are send, there is nothing to pickup

	art.store() #Draw the store
	print("So far, this room seems the most welcoming yet. At the end of the room, there is what seems to be a magically automated items shop.")

	selling = random.choice(var.buyLoot)#Puts random item on sale
	price = 0
	#Sets prices for items
	#Will also randomize the price just a little
	if selling == 'apple':
		price = 5 + random.randrange(-3, 6)
	elif selling == 'magical scroll':
		price = 7 + random.randrange(-3, 6)
	elif selling == 'magical soup':
		price = 7 + random.randrange(-3, 6)
	elif selling == 'torch':
		price = 5 + random.randrange(-3, 6)
	elif selling == 'holy symbol':
		price = 30 + random.randrange(-3, 6)
	elif selling == 'rope':
		price = 7 + random.randrange(-3, 6)
	elif selling == 'strong sword':
		price = 12 + random.randrange(-3, 6)
	elif selling == 'potion':
		price = 7 + random.randrange(-3, 6)
	#Makes offer
	print('\033[0;34;48m')#Sets text collor to blue
	print("The store magically greets you, and offers you (a/an) " + selling + " for the price of " + str(price) + " coins.\n")
	#Asks
	buy = input("Do you wish to make the purchase? Yes or No?\n").lower()
	while buy != 'yes' and buy != 'no': #yes or no, no maybe
		buy = actions.line()
	#If say yes we have to check their bal
	if buy == "yes":
		if var.money >= price:
			var.inv.append(selling)
			var.money = var.money - price
			print("You have purchased (a/an) "+ selling +".\n")
		else:
			print("You can't afford that!\n")
	
	#Back to std actions
	print('\033[0;37;48m')#Default Color
	actions.stdActions(posLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(3)
	print('\033[0;37;48m')#Default Color

	if nextDoor == 'a':
		girlRoom()
	if nextDoor == 'b':
		potionRoom()
	if nextDoor == 'c':
		room_of_goblin()


#Library room, under start, and cotians many scrolls, but has a meh mob
def library():

	mob = random.randrange(1,100)#Most likly spawns a mob
	if mob <= 80:
		monsters.genMon(40)
	else:
		monsters.monAlive = False

	print('\033[0;36;48m')#Sets text collor to cyan

	#Does the scroll thing
	if var.scrolls == 0:
		#If there are no scrolls left
		posLoot = actions.getGroundLoot(75)#Will MAYBE spawn loot
		groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
		#Makes drawing with no scrolls, maybe loot, and maybe mon
		if groundLoot != "":
			art.lia(False, True, monsters.monAlive)
		else:
			art.lia(False, False, monsters.monAlive)

	else:
		#If there scrolls left
		art.lia(True, False, monsters.monAlive)
		groundLoot = ""
		#Makes drawing with Scrolls and maybe mon
		print("There seem to be three scrolls you can pickup.")
		pick = input("Do you wish to take them?\n").lower()
		#Will keep asking
		while pick != 'yes' and pick != 'no': #yes or no, no maybe
			pick = actions.line()
		#If yes or no
		if pick == 'yes':
			print("\nYou have picked up three scrolls.\n")
			var.inv.append('magical scroll')
			var.inv.append('magical scroll')
			var.inv.append('magical scroll')
			var.scrolls = 0
		
	#Room desc
	print("The room seems to be an ancient library of some sort. Maybe of a great wizard.\n")
		
	#Combat if needed
	if monsters.monAlive:
		print('\033[0;31;48m')#Sets color to red
		monsters.monIntros(monsters.monName)#Will spawn the monster needed
	
	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(4)
	print('\033[0;37;48m')#Default Color
	if nextDoor == 'a':
		room_of_bricks()
	elif nextDoor == 'b':
		cultRoom()
	elif nextDoor == 'c':
		lavaRoom()
	elif nextDoor == 'd':
		dragon()


#Potion room, cotians many potions, but has a meh mob
def potionRoom():

	mob = random.randrange(1,100)#Most likly spawns a mob
	if mob <= 80:
		monsters.genMon(40)
	else:
		monsters.monAlive = False

	print('\033[0;36;48m')#Sets text collor to cyan

	#Does the potion thing
	if var.potions == 0:
		#If there are no potions left
		posLoot = actions.getGroundLoot(75)#Will MAYBE spawn loot
		groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
		#Makes drawing with no scrolls, maybe loot, and maybe mon
		if groundLoot != "":
			art.pos(False, True, monsters.monAlive)
		else:
			art.pos(False, False, monsters.monAlive)

	else:
		#If there potions left
		art.pos(True, False, monsters.monAlive)
		groundLoot = ""
		#Makes drawing with potions and maybe mon
		print("There seem to be three potions you can pickup.")
		pick = input("Do you wish to take them?\n").lower()
		#Will keep asking
		while pick != 'yes' and pick != 'no': #yes or no, no maybe
			pick = actions.line()
		#If yes or no
		if pick == 'yes':
			print("\nYou have picked up three potions.\n")
			var.inv.append('potion')
			var.inv.append('potion')
			var.inv.append('potion')
			var.potions = 0
		
	#Room desc
	print("The room seems to be an ancient potionary of some sort. Maybe of a great brewer.\n")
		
	#Combat if needed
	if monsters.monAlive:
		print('\033[0;31;48m')#Sets color to red
		monsters.monIntros(monsters.monName)#Will spawn the monster needed
	
	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(2)
	print('\033[0;37;48m')#Default Color

	if nextDoor == 'a':#Store needs key, so if the user doesnt have it /shrug
		if 'silver key' not in var.inv:
			print("You need a silver key to go here.")
			nextDoor = actions.pickDoorsKey("タイガ", "b", "タイガ", "タイガ")#Will ask for b
		else:
			storeRoom()

	if nextDoor == 'b':
		trapRoom()


#Trap room below potions and above chest room. Arrows will be shot and there's a chance the player will be shot taking some damage
def trapRoom():
	print('\033[0;36;48m')#Sets text collor to cyan
	posLoot = actions.getGroundLoot(100)
	groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
	#Draws map with or without loot
	if groundLoot != "":
		art.trapRoom(True)
	else:
		art.trapRoom(False)

	print("\nThis room... It doesn't feel right. It looks like a thin hallway.\n")

	#Will calculate if the arrow hits
	arrowHit = random.randrange(1,21)+2
	print("You were right to think so.")
	print("An arrow shoots out of the wall.")
	if arrowHit >= 15:
		print("Thankfully, you were able to dodge it.")
	else:
		print("The arrow penetrates your skin.")
		damage = random.randrange(1,7)
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)
	
	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(2)
	print('\033[0;37;48m')#Default Color

	if nextDoor == 'a':
		potionRoom()
	if nextDoor == 'b':
		chest_room()


#Room with girl crying, lost in the underground
def girlRoom():
	print('\033[0;36;48m')#Sets text collor to cyan
	#Gen Loot
	posLoot = actions.getGroundLoot(80)#Will MAYBE spawn loot
	groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
	#Makes var for drawing with or without loot
	if groundLoot != "":
		loot = True
	else:
		loot = False

	#If girl still there
	if var.girlThere:
		#Draw girl and maybe loot
		art.girlRoom(loot, True)
		print("As you enter the room, you think of how sad and cold it would be to cry here. That is when you hear the crying of a girl in the corner. You realize you are not the only one with the trapped fate of this dungeon of rooms.\n")
		#Does the user wish to take her?
		take = input("Do you wish to take her with you in hopes of her being free? Yes or No?\n").lower()
		#Will keep asking
		while take != 'yes' and take != 'no': #yes or no, no maybe
			take = actions.line()
		if take == 'yes':
			var.girlThere = False
			print("You take the girl, together you will find freedom.")
	else:
		art.girlRoom(loot, False)
		print("The room is cold.\n")

	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(2)
	print('\033[0;37;48m')#Default Color

	if nextDoor == 'a':#Store needs key, so if the user doesnt have it /shrug
		if 'silver key' not in var.inv:
			print("You need a silver key to go here.")
			nextDoor = actions.pickDoorsKey("タイガ", "b", "タイガ", "タイガ")#Will ask for b
		else:
			storeRoom()

	if nextDoor == 'b':
		mimicRoom()


#Room with mimic that looks like a chest
def mimicRoom():
	print('\033[0;36;48m')#Sets text collor to cyan
	#Gen Loot
	posLoot = actions.getGroundLoot(80)#Will MAYBE spawn loot
	groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
	#Makes var for drawing with or without loot
	if groundLoot != "":
		loot = True
	else:
		loot = False

	#If mimic still there
	if var.mimicAlive:
		#Draw "chest" and maybe loot
		art.mimicRoom(loot, True)
		print("The room warms you as you see another chest. What joy!\n")
		#Does the user wish to open the 'chest'?
		take = input("Do you wish to open the chest?\n").lower()
		#Will keep asking
		while take != 'yes' and take != 'no': #yes or no, no maybe
			take = actions.line()
		if take == 'yes':
			print('\033[0;31;48m')#Sets color to red
			var.mimicAlive = False
			print("DECEPTION! Thou was no chest, but a mimic, the works of a devil!")
			monsters.monAlive = True
			monsters.monName = "mimic"
			monsters.monIntros(monsters.monName)#Will spawn the mimic
			
	else:
		art.mimicRoom(loot, False)
		print("Cold sweat runs down you as you no longer see what you once thought to be a chest.\n")

	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(3)
	print('\033[0;37;48m')#Default Color
	if nextDoor == 'a':
		girlRoom()
	elif nextDoor == 'b':
		room_of_goblin()
	elif nextDoor == 'c':
		deadRoom()


#Room with dead party members, and one is just barly alive and asks you to give a ring to his daughter, you can steal the ring and get coins, or be nice and try dilver the ring
def deadRoom():
	print('\033[0;36;48m')#Sets text collor to cyan
	#Gen Loot
	posLoot = actions.getGroundLoot(50)#Will MAYBE spawn loot
	groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
	#Makes var for drawing with or without loot
	if groundLoot != "":
		loot = True
	else:
		loot = False

	#If man is still there
	if var.deadManAlive:
		#Man will give ring
		#Draw man and maybe loot
		art.deadRoom(loot, True)
		print('Amoung corpses, a man, almost dead, reaches his hand to you.\n“Please, take this ring to my daughter as you leave. I beg you, make my dying wish come true.”')
		#To take or not to take
		take = input("Do you take the ring? Yes or no?\n").lower()
		while take != 'yes' and take != 'no': #yes or no, no maybe
			take = actions.line()
		if take == 'yes':
			#Coins or dyying wish?
			moral = input(var.userName + ", you can fulfil the man’s wish, or lie to him and turn the ring into 20 coins. Coins or Wish?\n").lower()
			while moral != 'coins' and moral != 'wish': #coins or wish, pick m8
				moral = actions.line()
			#Gain or wish
			if moral == 'coins':
				var.money += 25
				print("You gain 25 coins.")
			else:
				print("You smile a honest person's smile.")

		print("The man’s body falls dead, never to see the light again.")

	#No man
	else:
		#Draws maybe loot and no man
		art.deadRoom(loot, False)
		
	#Cant happen again
	var.deadManAlive = False
	print("The corpses of a party lie. Dead. Never to stand again.")

	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(2)
	print('\033[0;37;48m')#Default Color
	if nextDoor == 'a':
		mimicRoom()
	elif nextDoor == 'b':
		cultRoom()


#Cult Room, there is a undead Knight doing some jazz with a davids star and all, idk, prob some magic, anyway, he will fight you, unless you are a paladin, then he will kill himself for richs to give yo you. cuz you know, that what you do when you worship someone
def cultRoom():
	print('\033[0;36;48m')#Sets text collor to cyan
	#Gen Loot
	posLoot = actions.getGroundLoot(80)#Will MAYBE spawn loot
	groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
	#Makes var for drawing with or without loot
	if groundLoot != "":
		loot = True
	else:
		loot = False

	#Intro
	print("\nThe room has a magical vibe. On the ground, you can make out Davids star drawn with what seems to be dried blood. To your shock, you also notice a goats head sticking out from the opposing wall.\n")

	#If knight alive
	if var.knight:
		#Draws room with maybe loot and yes knight
		art.cultRoom(loot, True)
		#If paladin, the knight will kill himself
		if var.userCLASS == 3:
			print("You hear the metallic steps behind you.\nAs you turn around, a sword of an undead knight is swinging down at you.\nMidway, the knight stops, realizing you are a paladin.\nHe gets on his knees and begs for forgiveness.\nBefore you have a chance to say anything, the knight casts a spell on himself, turning himself into 25 coins as forgiveness.")
			var.money += 25
			var.knight = False
		#Else he will fight to the death
		else:
			var.knight = False
			monsters.monAlive = True
			monsters.monName = "knight"
			monsters.monIntros(monsters.monName)#Will spawn the knight

	#No knight drawing, and maybe loot
	else:
		art.cultRoom(loot, False)

	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(3)
	print('\033[0;37;48m')#Default Color
	if nextDoor == 'a':
		deadRoom()
	elif nextDoor == 'b':
		library()
	elif nextDoor == 'c':
		dragon()


#I expect many will die here, "some of you will die but that's a sacrifice i'm willing to make" ~Lord Farquad something from shrek. anyhow, there is a very strong dragon here
def dragon():
	print('\033[0;36;48m')#Sets text collor to cyan
	#Gen Loot
	posLoot = actions.getGroundLoot(80)#Will MAYBE spawn loot
	groundLoot = actions.tellUserOfLoot(posLoot)#Checks if user can see loot
	#Makes var for drawing with or without loot
	if groundLoot != "":
		loot = True
	else:
		loot = False

	#Intro
	print("\nThe room is warm, which is odd seeing how the rest of the rooms seemed deathly cold.\n")

	#If dragon alive
	if var.dragonAlive:
		#Draws room with maybe loot and yes dragon
		art.dragonRoom(loot, True)
		art.dragon()
		#Will only happen once, and fight begins
		var.dragonAlive = False
		monsters.monAlive = True
		monsters.monName = "dragon"
		monsters.monIntros(monsters.monName)#Will spawn the dragon

	#No dragon drawing, and maybe loot
	else:
		art.dragonRoom(loot, False)

	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(3)
	print('\033[0;37;48m')#Default Color
	if nextDoor == 'a':
		library()
	elif nextDoor == 'b':
		cultRoom()
	elif nextDoor == 'c':
		lastRoom()


#Lava room, to go anywhere, the player will have to jump, and if fails will lose some hp, if player has a rope, chances of success are higher
def lavaRoom():
	print('\033[0;36;48m')#Sets text collor to cyan
	#intro
	art.lavaRoom()
	print("\nThe room is filled with lava. One-step and you’re testing your luck with a jump. That said, if you have a rope, your chances increase.\n")
	#There is no loot
	groundLoot = ''

	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave
	
	nextDoor = actions.pickDoor(3)

	#Now, the user shall jump, if thos fails, damage shall acour
	#Math
	chance = 12 + random.randrange(-2,3)
	playerChance = random.randrange(1,21)
	if 'rope' in var.inv:
		playerChance += 5
	if playerChance >= chance:
		print("You jump to the door and succeed.")
		if 'rope' in var.inv:
			print("Your rope came in useful.")
	else:
		damage = random.randrange(1,7)
		print("You jump to the door and fail.")
		print("Damage Dealt:", damage)
		actions.loseHP(damage)
		print("Current HP:", var.HP)

	if nextDoor == 'b':#Store needs key, so if the user doesnt have it /shrug
		if 'golden key' not in var.inv:
			print("You need a golden key to go here.")
			nextDoor = actions.pickDoorsKey("a", "タイガ", "c", "タイガ")#Will ask for other door
		else:
			treasure()

	if nextDoor == 'a':
		library()

	if nextDoor == 'c':
		lastRoom()


#A room with just one door that holds treasure for the user
def treasure():

	mob = random.randrange(1,100)#Most likly spawns a mob
	if mob <= 80:
		monsters.genMon(40)
	else:
		monsters.monAlive = False

	print('\033[0;36;48m')#Sets text collor to cyan

	#Does the treasure thing
	if var.treasure:
		#If there is treasure left
		art.tr(True, monsters.monAlive)
		groundLoot = ""
		#Makes drawing with treasure and maybe mon
		print("The room is scattered with gold coins!")
		pick = input("Do you wish to take them?\n").lower()
		#Will keep asking
		while pick != 'yes' and pick != 'no': #yes or no, no maybe
			pick = actions.line()
		#If yes or no
		if pick == 'yes':
			print("\nYou have gained 50 coins.\n")
			var.money += 50
			var.treasure = False

	else:
		print("The room reminds you of riches.")
		#If there are no potions left
		groundLoot = ""
		#Makes drawing with no treasure, and maybe mon
		art.tr(False, monsters.monAlive)
		
	#Combat if needed
	if monsters.monAlive:
		print('\033[0;31;48m')#Sets color to red
		monsters.monIntros(monsters.monName)#Will spawn the monster needed
	
	print('\033[0;37;48m')#Default Color

	actions.stdActions(groundLoot)
	#Asks the user standard Actions, what they want to do in the room, and this repeats until they choose to leave

	#After they have chosen door, they will be asked what door they wish to go into
	nextDoor = actions.pickDoor(1)
	print('\033[0;37;48m')#Default Color

	if nextDoor == 'a':
		lavaRoom()


#This is the final room, the journy of mozart comes to an end as steins gate is found. There shall be an angle, which only attacks if the user wishs to hit it
def lastRoom():
	groundLoot = "" #Makes local ground loot
	print('\033[0;36;48m')#Sets text collor to cyan

	#Makes a drawing of room
	#Angel there no matter what, as you either die or finish the game
	art.lastRoom()
	#Draws an angel
	art.angel()
	
	#Room intro
	print("You see the light above you. There is a ladder leading to the forever free and open world. Your escape from this nauseating and enclosed space. One thing stands in front of you. An angel looks deep into your eyes with a blank face, unmoving.")

	#Attack or not
	maybe = input("\nDo you wish to attack the angel?\n").lower()
	while maybe != 'yes' and maybe != 'no': #live or die, pick m8
		maybe = actions.line()
	#If so, the angel attacks aswell andtheres combat
	if maybe == "yes":
		print("You have chosen death, says the angel.\n")
		monsters.monAlive = True
		monsters.monName = "angel"
		monsters.monIntros(monsters.monName)#Will spawn the monster needed aka angel of DEATH

		print('\033[0;36;48m')#Sets text collor to cyan

	#If no, he lives peacefully
	elif maybe == "no":
		print("\nYou walk past the angel peacefully.\n")

	#Story
	print("You make your way up the ladder. After everything you’ve been thru, it’s all becoming worth it.")
	#If girl with user, a nice happy ever after
	if var.girlThere == False:
		print("The girl you rescued will live a happy life. She ends up marrying a boy she meets at a village, they have two kids, and you watch as their lives come to a happy ever after.")
	print("\nYou've done it.\n")

	#credits and again?
	print('\033[0;37;48m')#Default Color
	print("\n\n\nCredits\n\n\nJanik\nJohn Titor\nHououin Kyouma\nOkabe Rintarou\nKurisu Makise\nTaiga\nArima Kousei\nMai-San\n2Channel\n5Channel\nAll of CERN\nAnd you dear player.")
	
	again = input("\nType 'enter' to play again.\n").lower()
	while again != "enter":
	 again = input("\nType 'enter' to play again.\n").lower()
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
	import main
	main.start_game()
#The End