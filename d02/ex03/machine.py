import random
from beverages import *

class CoffeeMachine:

	def __init__(self):
		self.broken_counter = 0

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90
		desc = "An empty cup?! Gimme my money back"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.broken_counter = 0
		print("The machine has been repaired")

	def serve(self, beverage):
		if self.broken_counter == 10:
			raise self.BrokenMachineException()
		self.broken_counter += 1
		return random.choice([beverage, self.EmptyCup()])

def test_machine():
	machine = CoffeeMachine()
	drinks = [Coffee(), Tea(), Chocolate(), Cappuccino()]
	for i in range(22):
		print("order number:", i)
		try:
			print(machine.serve(random.choice(drinks)))
		except machine.BrokenMachineException:
			machine.repair()
		print()

if __name__ == '__main__':
	test_machine()
