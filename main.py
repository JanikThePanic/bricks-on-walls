import actions, rooms, var, art, monsters
#Imports other files

#The main loop used to start the game, and will be called again for replay
def start_game():

	#ASCII Art for title
	art.title()
	#Confirms that the user wants to play
	userIN = input("\nType 'Enter' to begin the adventure.\n").lower()
	
#Will not accept anything but 'enter'
	while userIN != "enter":
		print('\033[0;31;48m')#Sets text color to red
		userIN = input("\nI didn't get that. Please type 'Enter' to begin.\n").lower()
		print('\033[0;37;48m')#Default Color

	#Will ask for class, name and then will start the first room	
	actions.getClass()
	actions.getUserName()
	#Game Intro
	print("\nWell, "+var.userName +", you awaken in a cold and moist cobble dungeon. You do not remember living beforehand, and now you see it as your sole purpose to escape the maze of dungeons and see the surface once again.")
	#First room of the dungeon
	rooms.room_of_bricks()

#Will set preGame loot for chest
var.chestLootPre()
#Starts game
start_game()