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
		return
	for key, val in states.items():
		if state == key:
			state_abbr = val
	for key, val in capital_cities.items():
		if state_abbr == key:
			return val

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
		return
	for key, val in capital_cities.items():
		if capital == val:
			state_abbr = key
	for key, val in states.items():
		if state_abbr == val:
			return key

def is_capital(capital):
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	if capital in capital_cities.values():
		return True
	return False

def is_state(state):
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}

	if state in states.keys():
		return True
	return False

def display_cities_and_states(str):
	raw_list = str.split(",")

	# remove whitespaces, turns everything lowercase and capitalize first letters
	for index in range(len(raw_list)):
		raw_list[index] = raw_list[index].strip().casefold().title()
	raw_list.remove('')

	for city_state in raw_list:
		if is_capital(city_state):
			state = display_state(city_state)
			print(f"{city_state} is the capital of {state}")
		elif is_state(city_state):
			capital = display_capital(city_state)
			print(f"{capital} is the capital of {city_state}")
		else:
			print(f"{city_state} is neither a capital city nor a state")

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		quit
	else:
		display_cities_and_states(sys.argv[1])
