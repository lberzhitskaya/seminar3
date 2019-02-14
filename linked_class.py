from linked_list import MyList, ListNode
from myclass import index

class Set:
	def __init__(self):
		self.my_set = MyList()
		
	def length(self):
		return self.my_set.__len__()
		
	def contains(self, item):
		return self.my_set.__contains__(item)
				
		
	def add(self, item):
		nd =  ListNode(item)
		self.my_set.add(nd)
		
	def remove(self, item):
		self.my_set.remove(item)
		
	def iterator(self):
		return self.my_set.__iter__()
		
	def equals(self, other_set):
		if type(other_set) is not Set:
			print("Unsuitable object type!")
			return ""
			
		if self.length() != other_set.length():
			return False

		set1 = other_set.iterator()		
		for elem in set1:
			if not self.my_set.__contains__(elem):
				return False
		return True
		
	
	def difference(self, other_set):
		if type(other_set) is not Set:
			print("Unsuitable object type!")
			return ""
			
		result_set = Set()
		it = self.iterator()
		for item in it:
			if not other_set.contains(item):
				result_set.add(item)

		return result_set
		
		
	def issubsetof(self, other_set):
		if type(other_set) is not Set:
			print("Unsuitable object type!")
			return ""
			
		if self.length() > other_set.length():
			return False
			

		for item in self.my_set:
			if not other_set.contains(item):
				return False
	
		return True
		
	
			
		
		
