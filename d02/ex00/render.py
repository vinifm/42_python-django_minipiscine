import sys, os, re

def create_dictionary():
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

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		print("error: wrong number of arguments", file = sys.stderr)
		exit(1)
	file_name = sys.argv[1]
	if (not file_name.endswith(".template")):
		print("error: bad file extension", file = sys.stderr)
		exit(1)
	elif not os.path.isfile(file_name):
		print("error: file not found", file = sys.stderr)
		exit(1)
	settings_dic = create_dictionary()
	render_template(file_name, settings_dic)
