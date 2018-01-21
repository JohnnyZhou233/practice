class Mobilephone(object):
	def __init__(self, brands, types, price):
		self.brands = brands
		self.types = types
		self.price = price

	def get_introduction(self):
		return self.brands + " " + self.types
	
	def get_intro(self):
	message = "The price is"
	return message

brands = "Apple"
types = "Iphone"
price = "8999"	