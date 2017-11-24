#made by aku1997

# create 2 lists
list1 = [1,2,3,4,5,6]
list2 = [1,3,5,6]

# loop for printing only i (the common elements)
# for loop goes through all elements in list2
for i in list1:
	if i in list2: #if condition to only print the elements of list1 that are present in list2
		print(i)