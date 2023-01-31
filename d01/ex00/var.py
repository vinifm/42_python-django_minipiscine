def my_var():
	var1 = 42
	print(f"{var1} has a type {type(var1)}")

	var2 = 42.0
	print(f"{var2} has a type {type(var2)}")

	var3 = False
	print(f"{var3} has a type {type(var3)}")

	var4 = [0, 1, 2]
	print(f"{var4} has a type {type(var4)}")

	var5 = (0, 1, 2)
	print(f"{var5} has a type {type(var5)}")

	var6 = {"apple", "banana", "tangerine"}
	print(f"{var6} has a type {type(var6)}")

	var7 = {"Name": "Vini", "Loves to": "sleep"}
	print(f"{var7} has a type {type(var7)}")

	var8 = "I'm running out of types"
	print(f"{var8} has a type {type(var8)}")

	var9 = type(var8)
	print(f"{var9} has a type {type(var9)}")

if __name__ == '__main__':
	my_var()
