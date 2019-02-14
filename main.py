from linked_list import MyList, ListNode
from linked_class import Set
from myclass import index

i1 = index(1, 2)
i2 = index()
i3 = index(1, 1)
i4 = index(1, 3)
i5 = index(0, 1)

index_set_1 = Set()
index_set_2 = Set()

index_set_1.add(i1)
index_set_1.add(i2)
index_set_1.add(i4)
index_set_1.add(i5)


index_set_2.add(i5)
index_set_2.add(i1)
index_set_2.add(i2)
index_set_2.add(i3)
#lst = MyList()

#nd = ListNode(1)
#lst.add(nd)
#nd = ListNode(2)
#lst.add(nd)
#nd = ListNode(3)
#lst.add(nd)
#lst.remove(2)
#lst.remove(1)



print("Checking equality of sets 'index_set_1'  и  'index_set_2':")
print(index_set_1.equals(index_set_2))

new_set = index_set_2.difference(index_set_1)
it = new_set.iterator()
print("Difference of two sets:")
for elem in it:
	elem.print_i1i2()
	print("")

print(index_set_1.issubsetof(index_set_2))
print(index_set_2.issubsetof(index_set_1))
