from local_lib.path import Path
import sys

def write_to_file():
	path = Path()
	direc = path.abspath() + '/hello'
	path.mkdir_p(direc, 0o777)
	print(direc)
	# with open('direc/file.txt') as file:
	# 	file.write("Hello world!")

if __name__ == '__main__':
	write_to_file()
