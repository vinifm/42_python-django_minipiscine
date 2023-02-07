#!/usr/bin/python3


class Text(str):
	"""
	A Text class to represent a text you could use with your HTML elements.

	Because directly using str class was too mainstream.
	"""

	def __str__(self):
		text = super().__str__().replace('<', '&lt;')
		text = text.replace('>', '&gt;')
		text = text.replace('>', '&gt;')
		text = text.replace('"', '&quot;')
		text = text.replace('\n', '\n<br />\n')
		return text


class Elem:
	"""
	Elem will permit us to represent our HTML elements.
	"""
	[...]

	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
		"""
		A builder taking in parameter the element's name, HTML attributes and type (simple or double tags).
		"""
		self.tag = tag
		self.attr = attr
		self.tag_type = tag_type
		self.content = []
		if content:
			self.add_content(content)
		# if content == '':
		# 	raise Elem.ValidationError
		# elif content == None:
		# 	self.content = ''
		# elif isinstance(content, Elem):
		# 	self.content = [content]
		# else:
		# 	self.content = content

	def __str__(self):
		"""
		The __str__() method will permit us to make a plain HTML representation of our elements. Make sure it renders everything (tag, attributes, embedded elements...).
		"""
		result = ''
		if self.tag_type == 'double':
			result = f'<{self.tag}>'
			[...]
			# put content into result
			result += self.__make_content()
			result += f'</{self.tag}>'
		elif self.tag_type == 'simple':
			[...]
		return result

	def __make_attr(self):
		"""
		Here is a function to render our elements attributes.
		"""
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result

	def __make_content(self):
		"""
		Here is a method to render the content, including embedded elements.
		"""
		if len(self.content) == 0:
			return ''
		result = '\n'
		for elem in self.content:
			for line in str(elem).split('\n'):
				result += '  ' + line + '\n'
		return result

	class ValidationError(Exception):
		pass

	def add_content(self, content):
		if not Elem.check_type(content):
			raise Elem.ValidationError
		if type(content) == list:
			self.content += [elem for elem in content if elem != Text('')]
		elif content != Text(''):
			self.content.append(content)

	@staticmethod
	def check_type(content):
		"""
		Is this object a HTML-compatible Text instance or a Elem, or even a
		list of both?
		"""
		return (isinstance(content, Elem) or type(content) == Text or
				(type(content) == list and all([type(elem) == Text or
												isinstance(elem, Elem)
												for elem in content])))


if __name__ == '__main__':
	[...]
