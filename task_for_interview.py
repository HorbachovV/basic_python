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

def squareList(some_list):
    for item in some_list:
        item *= item
    return item

my_list = [1, 2, 3, 4, 5, 6]

print(squareList(my_list))