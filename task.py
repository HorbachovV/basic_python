# reverse string
def reverse_string(string):
    return string[::-1]

print(reverse_string('володимир'))

# character count
def count_characters(string):
    character_count = {}
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

print(count_characters('володимир')) 

#subscriber function
subscribers = [
  {'name': 'Vova', 'age': 33},
  {'name': 'Ira', 'age': 23},
  {'name': 'Oleg', 'age': 43},
  {'name': 'Olia', 'age': 31},
  {'name': 'Julia', 'age': 29},
]

def helloSubscribers(lis):
    if len(lis) >= 40:
        print('Hello dear subscribers')
    else:
        print('No')

helloSubscribers(subscribers)


#square list number

def square_arr(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]
    return arr

numbers = [1, 2, 3, 4, 5, 6]
print(square_arr(numbers))


#add addjective
friends = [
  {
    "name": 'Joe',
    "gender": 'Male'
  },
  {
    "name": 'Fibi',
    "gender": 'Female'
  },
  {
    "name": 'Ros',
    "gender": 'Male'
  },
  {
    "name": 'Monica',
    "gender": 'Female'
  },
  {
    "name": 'Rachel',
    "gender": 'Female'
  },
  {
    "name": 'Chandler',
    "gender": 'Male'
  },
]

def add_ajective(list):
    for person in list:
        if person['gender'] == 'Male':
           person['name'] += ' is handsome'
        else:
           person['name'] += ' is beatiful'
    return list

print(add_ajective(friends))


# string check
def str_check(string):
    if string[::-1] == string:
        return True
    else:
        return False
    
print(str_check('ABBA'))


# list comprehension
print([x for x in range(1, 10, 2)])


# lambda sorted dict
dct = {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1}

new_dict = sorted(dct.items(), key= lambda x: x[1])

print(new_dict)