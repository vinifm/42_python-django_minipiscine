import random
from beverages import *

class CoffeeMachine:

	def __init__(self):
		pass

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90
		desc = "An empty cup?! Gimme my money back"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		pass

	def serve(self, beverage):
		'''
		Returns
		'''
		return random.choice([beverage, self.EmptyCup()])

def test_machine():
	machine = CoffeeMachine()
	print(machine.serve(Tea()))

if __name__ == '__main__':
	test_machine()
