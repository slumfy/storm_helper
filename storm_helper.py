import cards
import sys
import json
from player import player
from player import mana


def setup_initial_state(initial_state):
	f = open(initial_state)
	data = json.load(f)
	json_str = json.dumps(data)
	print(json_str)
	initial_mana = mana(data['player']['mana']['red'],
	data['player']['mana']['blue'],
	data['player']['mana']['black'],
	data['player']['mana']['green'],
	data['player']['mana']['white'],
	data['player']['mana']['generic'])
	initial_player = player(initial_mana)
	f.close()
	return initial_player


def main():
	player_status = setup_initial_state(sys.argv[1])
	player_status.print_player_info()


if __name__ == "__main__" :
	main()
