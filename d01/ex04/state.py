import sys

def display_state(capital):
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

	if capital not in capital_cities.values():
		print("Unknown capital city")
		return
	for key, val in capital_cities.items():
		if capital == val:
			state_abbr = key
	for key, val in states.items():
		if state_abbr == val:
			print(key)

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		quit
	else:
		display_state(sys.argv[1])
