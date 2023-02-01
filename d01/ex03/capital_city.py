import sys

def display_capital(state):
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}

	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	if state not in states.keys():
		print("Unknown state")
		return
	for key, val in states.items():
		if state == key:
			state_abbr = val
	for key, val in capital_cities.items():
		if state_abbr == key:
			print(val)

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		quit
	else:
		display_capital(sys.argv[1])
