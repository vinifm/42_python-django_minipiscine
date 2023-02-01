def print_numbers():
	file = open("numbers.txt")
	num_list = file.read().split(",")
	for num in num_list:
		print(int(num))

if __name__ == '__main__':
	print_numbers()
