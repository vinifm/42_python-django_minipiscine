def my_var():
	var_list = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]
	for var in var_list:
		print(f"{var} has a type {type(var)}")

if __name__ == '__main__':
	my_var()
