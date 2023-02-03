class HotBeverage:
	price = 0.3043894389
	name = "hot beverage"

	def description(self):
		return "Just some hot water in a cup."

	def __str__(self):
		desc = "name : %s\n" % self.name \
			 	+ "price : %.2f\n" % self.price \
				+ "description : %s" % self.description()
		return desc

class Coffee(HotBeverage):
	name = "coffee"
	price = 0.40

	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	name = "tea"
	price = 0.30

	def description(self):
		return "Just some hot water in a cup."

class Chocolate(HotBeverage):
	name = "chocolate"
	price = 0.50

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	name = "cappuccino"
	price = 0.45

	def description(self):
		return "Un po' di Italia nella sua tazza!"

def test():
	beverage = HotBeverage()
	coffee = Coffee()
	tea = Tea()
	chocolate = Chocolate()
	cappuccino = Cappuccino()

	print(f"\n{beverage}")
	print(f"\n{coffee}")
	print(f"\n{tea}")
	print(f"\n{chocolate}")
	print(f"\n{cappuccino}\n")

if __name__ == '__main__':
	test()
