# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# append

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)    # Output: [1, 2, 3, 4]

# extend

my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)    # Output: [1, 2, 3, 4, 5, 6]

# insert

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)    # Output: [1, 4, 2, 3]

# remove

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)    # Output: [1, 3, 2]

# pop

my_list = [1, 2, 3]
popped = my_list.pop(1)
print(popped)     # Output: 2
print(my_list)    # Output: [1, 3]

# index

my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)      # Output: 1

# count

my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)      # Output: 2

# sort

my_list = [3, 2, 1]
my_list.sort()
print(my_list)    # Output: [1, 2, 3]

# reverse

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)    # Output: [3, 2, 1]


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1]) # banana
print(thislist[-1]) # mango
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
mylist = thislist.copy()
print(mylist)

# loop list
for x in thislist:
  print(x)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# List comprehension
some_list = [x * 2 for x in range(10) ]
print(some_list) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]