#ex.4-1
#формирование списка
pizzas = ['Vegetarian', 'Shrimp', 'Chili pepper', 'Mashrooms']
for pizza in pizzas:
    print(pizza)

#формирование списка и конечного сообщения
for pizza in pizzas:
    print('I like ' + pizza + ' pizza!')
print('I really love pizza!')

#формирование и сортировка списка
pets = ['dogs', 'cats', 'hedgehogs', 'hamsters']
pets.sort()
for pet in pets:
    print('I think that ' + pet.title() + ' are the most favorite animal in '
                                          'the world!')

#ex.4-3
#вывод чисел от 1 до 20
for value in range(1,21):
    print(value)

#ex.4-5
#перебор чисел в созданном списке, поиск мин, макс числа и суммы чисел
values = []
for value in range(1, 101):
    values.append(value)
print(min(values))
print(max(values))
print(sum(values))
#или
values = list(range(1,101))
print(min(values))
print(max(values))
print(sum(values))
#или
values = [value for value in range(1, 101)]
print(min(values))
print(max(values))
print(sum(values))

#ex.4-6
#создание списка нечетных чисел
odd_numbers = list(range(1,21,2))
print(odd_numbers)

#ex.4-7
#список чисел, кратный 3
numbers = []
for number in range(3,31,3):
    numbers.append(number)
print(numbers)

#ex.4-8
#список кубов целых чисел от 1 до 10
numbers = list(range(1,11))
for number in numbers:
    print(number**2)
#или
numbers = [number**2 for number in range(1,11)]
print(numbers)

#ex,4-10
#создание срезов в начале, середине, конце списка
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print('The first three items in the list are:' + str(letters[:3]))
print('Three items from the middle of the list are:' + str(letters[2:5]))
print('The last three items in the list are:' + str(letters[-3:])) #или [4:]

#ex.4-11
#копирование списка через срез
my_pizzas = ['Vegetarian', 'Shrimp', 'Chili pepper', 'Mashrooms']
freind_pizzas = my_pizzas[:]

my_pizzas.append('Pepperoni')
freind_pizzas.append('Hawaiian')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print('- ' + pizza)

print('My friend’s favorite pizzas are:')
for pizza in freind_pizzas:
    print('- ' + pizza)

#ex.4-13
#проверка невозможности изменения элементов кортежа
menu = ('Tomato soup', 'Chips', 'BBQ ribs', 'Garlic bread', 'Fruit platter')
print('\n\tOur restaurant has:')
for dish in menu:
    print(dish)

new_menu = ('Onion soup', 'Chips', 'BBQ ribs', 'Garlic bread', 'Fish platter')
print('\n\tOur restaurant has new menu:')
for dish in new_menu:
    print(dish)
