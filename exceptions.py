
# Exceptions  in Python are a special type of objects that occur during program execution when an unexpected event occurs that interrupts the normal flow of execution. These can be syntax errors, logical errors, or interactions with external systems (for example, a missing file).

# try except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Ділення на нуль неможливе!")


try:
    int('abc')
except ValueError:
    print("Не можна перетворити рядок 'abc' на число!")


my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Індекс поза межами списку!")


try:
    with open('nonexistent_file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("Файл не знайдено!")


try:
    2 + "hello"
except TypeError:
    print("Не можна додавати число і рядок!")

class MyCustomError(Exception):
    pass


try:
    raise MyCustomError("Це моя власна помилка")
except MyCustomError as e:
    print(e)


try:
    x = int(input("Введіть число: "))
except ValueError:
    print("Ви ввели не число!")
else:
    print("Ви ввели число:", x)


try:
    with open('my_file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("Файл не знайдено!")
finally:
    print("Блок finally завжди виконується")


# raise
# finally

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Ділення на нуль неможливе!")
    return x / y

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)



def read_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        print("Файл не знайдено!")
    finally:
        print("Блок finally завжди виконується")

try:
    content = read_file("nonexistent_file.txt")
    print(content)
except FileNotFoundError:
    print("Обробка помилки")


def process_data(data):
    try:
        # Обробка даних
        result = int(data) / 2
        return result
    except ValueError:
        raise ValueError("Невірний формат даних!")
    finally:
        print("Завершено обробку даних")

try:
    data = input("Введіть число: ")
    result = process_data(data)
    print("Результат:", result)
except ValueError as e:
    print("Помилка:", e)