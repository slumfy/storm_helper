class mana:
	red		= 0
	blue	= 0
	black	= 0
	green 	= 0
	white 	= 0
	generic	= 0

	def __init__(self, red, blue, black, green, white, generic):
		self.red = red
		self.blue = blue
		self.black = black
		self.green = green
		self.white = white
		self.generic = generic

	def print_mana(self):
		print("### MANA : ###")
		print("RED : " + str(self.red))
		print("BLUE : " + str(self.blue))
		print("BLACK : " + str(self.black))
		print("GREEN : " + str(self.green))
		print("WHITE : " + str(self.white))
		print("GENERIC : " + str(self.generic))
		print("############\n")


class player:
	storm_count = 0

	def __init__(self,mana):
		self.mana = mana


	def print_player_info(self):
		print("storm_count : " + str(self.storm_count))
		self.mana.print_mana()