class index:
	def __init__(self, i1 = 0, i2 = 0):
		self.i1 = i1
		self.i2 = i2

	def print_i1i2(self):
		print('i1 = ', self.i1)
		print('i2 = ', self.i2)

	def change_att(self, i1, i2):
		self.i1 = i1
		self.i2 = i2
		#print('i1 = ', self.i1)
		#print('i2 = ', self.i2)

	def sum_i1i2(self):
		return self.i1 + self.i2

	def mult_i1i2(self):
		return self.i1 * self.i2
		

class index_child(index):
	def __init__(self, i1 = 0, i2 = 0, i3 = 0):
		self.i1 = i1
		self.i2 = i2
		self.i3 = i3

	def i3_square(self):
		return self.i3 ** 2

