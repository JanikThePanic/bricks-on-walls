import random, actions, rooms, var, art, monsters
#Imports other files and random

#Colors http://ozzmaker.com/add-colour-to-text-in-python/

#Title and credits
def title():
	

	print('\033[0;34;48m')#Sets text collor to blue
	print(" _ \n|_) __ o  _  |  _     _ __    | | _  |  |  _  \n|_) |  | (_  |<_>    (_)| |   |^|(_| |  | _>")

	print('\033[0;37;48m')#Default Color
	print("\nBricks on Walls\nBy Janik Abdullayev")


def pickup(loot):#Art for pickups
	if loot == "apple":#Art for apple
		print("\n  ,--./,-.\n / #      \\\n |        |\n \        /\n  `._,._,'")
	elif loot == "magical soup":#Art for soup
		print("\n      _..-------.._\n    .' .-._.-._.-. '.\n    \\'--.._____..--'/\n     \\    Soup!    /\n      '._________.'")


def yum():#Makes a YUM! for when you eat something
	print("__     ___    _ __  __ _ \n\\ \\   / / |  | |  \\/  | |\n \\ \\_/ /| |  | | \\  / | |\n  \\   / | |  | | |\/| | |\n   | |  | |__| | |  | |_|\n   |_|   \\____/|_|  |_(_)\n")


def death():#Death to the living
	print('\033[0;31;48m')#Sets text color to red

	print("__     ______  _    _   _____ _____ ______ _____  \n\\ \\   / / __ \\| |  | | |  __ \\_   _|  ____|  __ \\ \n \\ \\_/ / |  | | |  | | | |  | || | | |__  | |  | |\n  \\   /| |  | | |  | | | |  | || | |  __| | |  | |\n   | | | |__| | |__| | | |__| || |_| |____| |__| |\n   |_|  \\____/ \\____/  |_____/_____|______|_____/")
	
	print('\033[0;37;48m')#Default Color


def startRoom(lootBool):#Draws the room, and will write loot if loot is seen
	print("#"*3+"\033[0;31;48mA\033[0;36;48m"+"#"*9)
	print("#"+" "*11+"#")
	if lootBool:
		print("#"+" "*4+"\033[0;31;48mLoot\033[0;36;48m"+" "*3+"#")
	else:
		print("#"+" "*11+"#")
	print("#"+" "*11+"\033[0;31;48mB\033[0;36;48m")
	for i in range(0,3):
		print("#"+" "*11+"#")
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")
	print("#"+" "*11+"#")
	print("#"*5+"\033[0;31;48mC\033[0;36;48m"+"#"*7)


def goblinRoom(lootBool, monBool):#Draws goblin room, given maybe loot, and maybe monster
	print("#"*6+"\033[0;31;48mA\033[0;36;48m"+"#"*6)
	print("#"+" "*11+"#")

	#Maybe draw loot
	if lootBool:
		print("#"+" "*4+"\033[0;31;48mLoot\033[0;36;48m"+" "*3+"#")
	else:
		print("#"+" "*11+"#")

	print("#"+" "*11+"#")
	#Maybe draw Monster
	if monBool:
		print("\033[0;31;48mB\033[0;36;48m"+" "*2+"\033[0;31;48mGoblin\033[0;36;48m"+" "*3+"#")
	else:
		print("\033[0;31;48mB\033[0;36;48m"+" "*11+"#")

	for i in range(0,2):
		print("#"+" "*11+"#")
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")
	print("#"+" "*11+"#")
	print("#"*5+"\033[0;31;48mC\033[0;36;48m"+"#"*7)


def chestRoom(monBool):#Draws chest room, given maybe loot, and maybe monster
	print("#"*6+"\033[0;31;48mA\033[0;36;48m"+"#"*6)
	print("#"+" "*11+"#")

	#chest
	print("#"+" "*3+"\033[0;31;48mChest\033[0;36;48m"+" "*3+"#")

	print("#"+" "*11+"#")
	#Maybe draw Monster
	if monBool:
		print("\033[0;31;48mB\033[0;36;48m"+" "*2+"\033[0;31;48m"+monsters.monName[0].upper()+monsters.monName[1:len(monsters.monName)]+"\033[0;36;48m"+" "*3+"#")
	else:
		print("\033[0;31;48mB\033[0;36;48m"+" "*11+"#")

	for i in range(0,2):
		print("#"+" "*11+"#")
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")
	print("#"+" "*11+"#")
	print("#"*13)


def store():#Draws the store
	print("#"*13)
	print("#  |Store|  #")
	print("#  -------  #")
	for i in range(0,2):
		print("#"+" "*11+"#")
	print("\033[0;31;48mA\033[0;36;48m"+" "*11+"\033[0;31;48mB\033[0;36;48m")
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")
	for i in range(0,2):
		print("#"+" "*11+"#")
	print("#"*6+"\033[0;31;48mC\033[0;36;48m"+"#"*6)


def lia(scrolls, loot, mon):#Draws the library. maybe scroll, maybe loot, maybe mon
	#Draws with scrolls and maybe mon
	print("#"*6+"\033[0;31;48mA\033[0;36;48m"+"#"*6) #1
	print("#"+" "*11+"#")#2
	#Scroll or loot
	if scrolls:#3
		print("#"+" "*2+"\033[0;31;48mScrolls\033[0;36;48m"+" "*2+"#")
	else:
		#Loot or not
		if loot:
			print("#"+" "*4+"\033[0;31;48mLoot\033[0;36;48m"+" "*3+"#")
		else:
			print("#"+" "*11+"#")
	#if mob
	if mon:#4
		nameLen = 10 - len(monsters.monName)
		print("#"+" "+"\033[0;31;48m" + monsters.monName + "\033[0;36;48m"+" "*nameLen+"#")
			
	print("\033[0;31;48mB\033[0;36;48m"+" "*11+"\033[0;31;48mC\033[0;36;48m")#5
	print("#"+" "*11+"#")#6
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")#7
	print("#"+" "*11+"#")#8
	print("#"*6+"\033[0;31;48mD\033[0;36;48m"+"#"*6)


def pos(pos, loot, mon):#Draws the potion room. maybe potions, maybe loot, maybe mon
	#Draws with potions and maybe mon
	print("#"*13) #1
	print("#"+" "*11+"#")#2
	#potions or loot
	if pos:#3
		print("#"+" "*2+"\033[0;31;48mPotions\033[0;36;48m"+" "*2+"#")
	else:
		#Loot or not
		if loot:
			print("#"+" "*4+"\033[0;31;48mLoot\033[0;36;48m"+" "*3+"#")
		else:
			print("#"+" "*11+"#")
	#if mob
	if mon:#4
		nameLen = 10 - len(monsters.monName)
		print("#"+" "+"\033[0;31;48m" + monsters.monName + "\033[0;36;48m"+" "*nameLen+"#")
			
	print("\033[0;31;48mA\033[0;36;48m" + " "*11+"#")#5
	print("#"+" "*11+"#")#6
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")#7
	print("#"+" "*11+"#")#8
	print("#"*6+"\033[0;31;48mB\033[0;36;48m"+"#"*6)


#Draws trap room with or without loot
def trapRoom(loot):
	print('#'*4 + "\033[0;31;48mA\033[0;36;48m" + '#'*3)
	for i in range(0,2):
		print("#"+" "*6+"#")
	#Loot or not
	if loot:
		print("#"+" "+"\033[0;31;48mLoot\033[0;36;48m"+" "+"#")
	else:
		print("#"+" "*6+"#")
	#Big spaces to make illustion of hallway with arrows shooting from walls
	for i in range(0,3):
		print("#"+" "*6+"#")
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "+"#")
	for i in range(0,2):
		print("#"+" "*6+"#")
	print('#'*3 + "\033[0;31;48mB\033[0;36;48m" + '#'*4)


#Girl room drawing with maybe girl and maybe loot
def girlRoom(loot, girl):
	print('#'*9)
	print('#'+' '*7+'#')
	#if girl there
	if girl:
		print("# \033[0;31;48mGirl\033[0;36;48m  #")
	else:
		print('#'+' '*7+'#')
	print('#'+' '*7+'\033[0;31;48mA\033[0;36;48m')
	#If loot there
	if loot:
		print("# \033[0;31;48mLoot\033[0;36;48m  #")
	else:
		print('#'+' '*7+'#')
	print('#'+' '*7+'#')
	print("#  \033[0;31;48mYou\033[0;36;48m  #")
	print('#'+' '*7+'#')
	print("####\033[0;31;48mB\033[0;36;48m####")


#Mimic room drawing with maybe 'chest' and maybe loot
def mimicRoom(loot, mimic):
	print('#'*4 + "\033[0;31;48mA\033[0;36;48m" + '#'*4)
	print('#'+' '*7+'#')
	#if mimic there
	if mimic:
		print("# \033[0;31;48mChest\033[0;36;48m #")
	else:
		print('#'+' '*7+'#')
	print('#'+' '*7+'\033[0;31;48mB\033[0;36;48m')
	#If loot there
	if loot:
		print("# \033[0;31;48mLoot\033[0;36;48m  #")
	else:
		print('#'+' '*7+'#')
	print('#'+' '*7+'#')
	print('#'+' '*7+'#')
	print('#'+' '*7+'#')
	print("#  \033[0;31;48mYou\033[0;36;48m  #")
	print('#'+' '*7+'#')
	print("####\033[0;31;48mC\033[0;36;48m####")

	
#Draws dead party's room
def deadRoom(loot, men):
	print("#"*6+"\033[0;31;48mA\033[0;36;48m"+"#"*6)
	print("#"+" "*11+"#")

	#Maybe draw loot
	if loot:
		print("#"+" "*4+"\033[0;31;48mLoot\033[0;36;48m"+" "*3+"#")
	else:
		print("#"+" "*11+"#")

	print("#"+" "*11+"#")
	#Maybe draw man
	if men:
		print("#"+" "*4+"\033[0;31;48mMen\033[0;36;48m"+" "*4+"#")
	else:
		print("#"+" "*11+"#")

	for i in range(0,2):
		print("#"+" "*11+"#")
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")
	print("#"+" "*11+"#")
	print("#"*5+"\033[0;31;48mB\033[0;36;48m"+"#"*7)

	
#draws Cult room
def cultRoom(loot, knight):
	print("#"*6+"\033[0;31;48mA\033[0;36;48m"+"#"*6)
	print("#"+" "*11+"#")

	#Maybe draw loot
	if loot:
		print("#"+" "*4+"\033[0;31;48mLoot\033[0;36;48m"+" "*3+"#")
	else:
		print("#"+" "*11+"#")

	print("#"+" "*11+"#")
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"\033[0;31;48mB\033[0;36;48m")
	print("#"+" "*11+"#")

	#Maybe draw knight
	if knight:
		print("#"+" "*2+"\033[0;31;48mKnight\033[0;36;48m"+" "*3+"#")
	else:
		print("#"+" "*11+"#")

	for i in range(0,1):
		print("#"+" "*11+"#")
	print("#"+" "*11+"#")
	print("#"*5+"\033[0;31;48mC\033[0;36;48m"+"#"*7)

	
#draws dragon room
def dragonRoom(loot, d):
	print("#"*6+"\033[0;31;48mA\033[0;36;48m"+"#"*6)
	print("#"+" "*11+"#")

	#Maybe draw loot
	if loot:
		print("#"+" "*4+"\033[0;31;48mLoot\033[0;36;48m"+" "*3+"#")
	else:
		print("#"+" "*11+"#")

	print("#"+" "*11+"#")
	print("\033[0;31;48mB\033[0;36;48m"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"\033[0;31;48mC\033[0;36;48m")
	print("#"+" "*11+"#")

	#Maybe draw dragon
	if d:
		print("#"+" "*2+"\033[0;31;48mDragon\033[0;36;48m"+" "*3+"#")
	else:
		print("#"+" "*11+"#")

	for i in range(0,1):
		print("#"+" "*11+"#")
	print("#"+" "*11+"#")
	print("#"*6+"#"*7)


#Draws lava Room
def lavaRoom():
	print("#"*15)
	print("#" + ' '*13 + '#')
	print("#" + ' '*13 + "\033[0;31;48mB\033[0;36;48m")
	for i in range (0,2):
		print("#" + ' '*13 + '#')
	print("\033[0;31;48mA     LAVA   \033[0;36;48m #")
	for i in range (0,2):
		print("#" + ' '*13 + '#')
	print("#\033[0;31;48m" + '    You      ' +"C\033[0;36;48m")
	print("#" + ' '*13 + '#')
	print("#"*15)


#Draws the potion room. maybe potions, maybe loot, maybe mon
def tr(tr, mon):
	print("#"*13) #1
	print("#"+" "*11+"#")#2
	#treasure?
	if tr:#3
		print("#"+" "*1+"\033[0;31;48mTreasure\033[0;36;48m"+" "*2+"#")
	else:
		print("#"+" "*11+"#")
	#if mob
	if mon:#4
		nameLen = 10 - len(monsters.monName)
		print("#"+" "+"\033[0;31;48m" + monsters.monName + "\033[0;36;48m"+" "*nameLen+"#")
	print("#"+" "*11+"#")#6
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")#7
	print("#"+" "*11+"#")#8
	print("#"*6+"\033[0;31;48mA\033[0;36;48m"+"#"*6)


def lastRoom():#Draws the room, and will write loot if loot is seen
	print("#"*3+"\033[0;31;48mA\033[0;36;48m"+"#"*9)
	print("#"+" "*11+"#")
	print("#"+" "*2+"\033[0;31;48mLadder\033[0;36;48m"+" "*3+"#")
	print("\033[0;31;48mB\033[0;36;48m"+" "*11+"#")
	for i in range(0,2):
		print("#"+" "*11+"#")
	print("#"+" "*2+"\033[0;31;48mAngle\033[0;36;48m"+" "*4+"#")
	print("#"+" "*11+"#")
	print("#"+" "*2+"\033[0;31;48mYou\033[0;36;48m"+" "*6+"#")
	print("#"+" "*11+"#")
	print("#"*6+"#"*7)


#Draws a dragon
def dragon():
	print("             __                  __\n            ( _)                ( _)\n           / / \\\\              / /\\_\\_\n          / /   \\\\            / / | \\ \\\n         / /     \\\\          / /  |\\ \\ \\\n        /  /   ,  \\ ,       / /   /|  \\ \\\n       /  /    |\\_ /|      / /   / \\   \\_\\\n      /  /  |\\/ _ '_| \\   / /   /  \    \\\\\n     |  /   |/  0 \\0\\    / |    |    \\    \\\\\n     |    |\\|      \\_\\_ /  /    |     \\    \\\\\n     |  | |/    \\.\\ o\\o)  /      \\     |    \\\\\n     \\    |     /\\\\`v-v  /        |    |     \\\\\n      | \\/    /_| \\\\_|  /      \n      | \\    \\\\\n      | |    /__/_ `-` /   _____  |    |  \\    \\\\\n      \\|    [__]  \\_/  |_________  \\   |   \\    ()\n       /    [___] (    \\         \\  |\\ |   |   //\n      |    [___]                  |\\| \|   /  |/\n     /|    [____]                  \\  |/\\ / / ||\n    (  \\   [____ /     ) _\\      \\  \\    \\| | ||\n     \\  \\  [_____|    / /     __/    \\   / / //\n     |   \\ [_____/   / /        \\    |   \\/ //\n     |   /  '----|   /=\\____   _/    |   / //\n  __ /  /        |  /   ___/  _/\\    \  | ||\n (/-(/-\\)       /   \\  (/\\/\\)/  |    /  | /\n               (/\\/\\)           /   /   //\n                      _________/   /    /\n                     \\____________/    (")


#Draws angel
def angel():
	print(".                                       ,\n)).               -===-               ,((\n))).                                 ,(((\n))))).            .:::.           ,((((((\n))))))))).        :. .:        ,(((((((('\n`))))))))))).     : - :    ,((((((((((((\n ))))))))))))))))_:' ':_((((((((((((((('\n `)))))))))))).-' \\___/ '-._(((((((((((\n  `))))_._.-' __)(     )(_  '-._._(((('\n   `))'---)___)))'\\_ _/'((((__(---'(('\n     `))))))))))))|' '|(((((((((((('\n       `)))))))))/'   '\\((((((((('\n         `)))))))|     |((((((('\n          `))))))|     |(((((('\n                /'     '\\\n               /'       '\\\n              /'         '\\\n             /'           '\\\n             '---..___..---'")