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