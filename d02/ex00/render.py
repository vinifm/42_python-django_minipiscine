import sys, os, re

def render_template():
	'''Creates an html file replacing the patterns in a .template file with the values defined in settings.py'''
	pass

if __name__ == '__main__':
	if (len(sys.argv) != 2 or not sys.argv[1].endswith(".template")):
		exit(1)
	try:
		open(sys.argv[1])
	except FileNotFoundError:
		exit(1)
	render_template()
