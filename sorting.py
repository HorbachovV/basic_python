def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # міняємо місцями
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([5, 3, 8, 4, 2]))  # [2, 3, 4, 5, 8]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([10, 20, 30, 40], 30))  # 2

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))  # 3

numbers = [10, 5, 20, 1]

sorted_numbers = sorted(numbers)  # створює новий список
print(sorted_numbers)  # [1, 5, 10, 20]

numbers.sort()  # змінює список "на місці"
print(numbers)  # [1, 5, 10, 20]


words = ["banana", "apple", "cherry"]

sorted_words = sorted(words)
print(sorted_words)  # ['apple', 'banana', 'cherry']


users = [
    {"name": "Anna", "age": 25},
    {"name": "John", "age": 30},
    {"name": "Mike", "age": 20}
]

# Сортування по віку
sorted_by_age = sorted(users, key=lambda x: x["age"])

print(sorted_by_age)
# [{'name': 'Mike', 'age': 20}, {'name': 'Anna', 'age': 25}, {'name': 'John', 'age': 30}]
