import actions
#Imports other files

inv = [] #Users Inventory

HP = 0 #Users Health, if it reachs 0, game over

HPmax = 0 #Users max HP

ClassAC = 0 #Stays the same through the game

CurrentAC = 0 #Used to calculate if a computers attack hits

attackBonus = 0 #Used to calculate if a users attack hits

money = 0 #Users money which can buy things in the store room

userCLASS = 0 #Fighter is 1, Wizard is 2, Paladin is 3

userName = '' #Users name

possibleLoot = ['apple', 'magical scroll', 'magical soup', 'torch', 'holy symbol', 'rope', 'silver key', 'potion']#Possible loot to spawn

buyLoot = ['apple', 'magical scroll', 'magical soup', 'torch', 'holy symbol', 'rope', 
'strong sword', 'potion']#Items that can be sold at the store

girlWith = False #Is the girl in the room with the user?

ringWish = False #Will the user return the ring to the woman of the dead man?

chestLoot = ''

scrolls = 3 #There are three scrolls in the lia and when taken, will be none

potions = 3 #There are three potions in the potion-room and when taken, will be none

girlThere = True #Shows that the girl is still there in the room alone

dragonAlive = True #Draogn in room needs to be defeated ONCE

mimicAlive = True #Mimic in room needs to be defeated ONCE

angelAlive = True #Killed only once, if killed at all

deadManAlive = True #The almost dead npc in deadRoom()

treasure = True #Treasure room treasure only appears once

knight = True #The undead knight in cultRoom only exists once

def chestLootPre():
	global chestLoot
	chestLoot = actions.getGroundLoot(100)#spawn loot for chest in chest room, done here so the chest stays empty after raided

# uwu オレンジ今日も食べてみたけどまだ酸っぱくて泣いた