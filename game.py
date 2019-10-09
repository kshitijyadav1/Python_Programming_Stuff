#! python3
def game_title():
	print("Escape from cave terror!")
def play():
	gpc = get_player_command() # gpc
	if gpc == 'n':
		print("Go North")
	elif gpc == 'e':
		print("Go East")
	elif gpc == 'w':
		print("Go West")
	elif gpc == 's':
		print("Go South")
	else:
		print("Invalid direction")
		
def get_player_command():
	return str(input("Action: ")).lower()
	
game_title()
for i in range(4):
	play()
	