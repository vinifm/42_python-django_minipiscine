import sys, os

def create_dictionary():
	'''
	Returns a dictionary from the settings.py file
	'''
	with open("settings.py", "r") as settings_file:
		dic_list = []
		for line in settings_file:
			dic_list.append([(x.strip(" \n\"")) for x in line.split('=', 1)])
	return dict(dic_list)

def render_template(file_name, dic):
	'''
	Creates an html file replacing the patterns in a .template file with the values defined in settings.py
	'''
	with open(file_name) as file:
		content = file.read()
		for key, val in dic.items():
			content = content.replace("{%s}" % key, val)
		with open(os.path.splitext(file_name)[0] + ".html", "w") as new_file:
			new_file.write(content)

def	check_arg_num():
	if (len(sys.argv) != 2):
		raise Exception("Wrong number of arguments")

def	check_file_extension(file_name):
	if (not file_name.endswith(".template")):
		raise Exception("Bad file extension")

def	check_file_path(file_name):
	if not os.path.isfile(file_name):
		raise Exception("file not found")

if __name__ == '__main__':
	check_arg_num()
	file_name = sys.argv[1]
	check_file_extension(file_name)
	check_file_path(file_name)
	render_template(file_name, create_dictionary())
