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