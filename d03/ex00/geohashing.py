from antigravity import geohash
import sys

def	check_coordinates():
	try:
		lat, long = float(sys.argv[1].strip(",")), float(sys.argv[2].strip(","))
	except ValueError as error:
		print(error)
		exit(1)
	if not -90 < lat < 90:
		raise Exception("Invalid latitude")
	if not -180 < long < 180:
		raise Exception("Invalid longitude")
	return lat, long

def	check_datedow(datedow):
	if not datedow.replace("-", "").replace(".", "").isnumeric():
		raise Exception("Invalid date-dow opening string")

def	calc_geohash(lat, long):
	datedow = sys.argv[3].encode('utf-8')
	geohash(lat, long, datedow)

if __name__ == '__main__':
	lat, long = check_coordinates()
	check_datedow(sys.argv[3])
	calc_geohash(lat, long)
