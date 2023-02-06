class Intern:
	def __init__(self, name = "My name? I'm nobody, an intern, I have no name."):
		self.Name = name

	def __str__(self):
		''' String representation of the object '''
		return self.Name

	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("I'm just an intern, I can't do that...")

	def make_coffee(self):
		return self.Coffee()

def test():
	nobody = Intern()
	mark = Intern("Mark")

	print()
	print(f"nobody's name: {nobody}")
	print(f"mark's name: {mark}\n")

	print("- Mark, make me coffee!")
	print(mark.make_coffee())

	# print("- Intern, work!")
	# print(nobody.work())

	try:
		print("\n- Intern, work!")
		print(nobody.work())
	except:
		print("\nIntern was fired.")

if __name__ == '__main__':
	test()
