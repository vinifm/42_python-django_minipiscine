def my_var():
	var_list = [42, 42.0, False, [1, 2, 3], (0, 1, 2), {"apple", "banana", "tangerine"},
				{"Name": "Vini", "Loves to": "sleep"}, "I'm running out of types", type(42)]
	for var in var_list:
		print(f"{var} has a type {type(var)}")

if __name__ == '__main__':
	my_var()
