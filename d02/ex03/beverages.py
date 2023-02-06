class HotBeverage:
	price = 0.30
	name = "hot beverage"
	desc = "Just some hot water in a cup."

	def description(self):
		return self.desc

	def __str__(self):
		desc = "name : %s\n" % self.name \
			 	+ "price : %.2f\n" % self.price \
				+ "description : %s" % self.description()
		return desc

class Coffee(HotBeverage):
	name = "coffee"
	price = 0.40
	desc = "A coffee, to stay awake."

class Tea(HotBeverage):
	name = "tea"
	price = 0.30
	desc = "Just some hot water in a cup."

class Chocolate(HotBeverage):
	name = "chocolate"
	price = 0.50
	desc = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	name = "cappuccino"
	price = 0.45
	desc = "Un po' di Italia nella sua tazza!"

def test_beverages():
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
	test_beverages()
