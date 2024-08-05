#ex.7-1
#испоользование функции input
message = input('What kind of car would you like to buy? ')
print(message.title() + ' is an excellent choice!')

#ex.7-2
#использование функции input с проверкой введенного значения
number = int(input('How many people would you like to order a table for? '))
if number > 8:
    print('Sorry, we have to wait a bit.')
else:
    print('Your table is ready!')

#ex.7-3
#использование функции input с проверкой введенного значения
message = "If you tell me a number, I'll tell you if it's a multiple of 10 or not."
message += '\nPlease tell me the number: '

number = input(message)
if int(number) % 10 == 0:
    print('Your number is a multiple of 10!')
else:
    print('Sorry, your number is not a multiple of 10.')

#простой цикл while с выводом четных чисел
number = 0
while number <= 10:
    print(number)
    number += 2

простой цикл while с выводом нечетных чисел
number = 0
while number <= 9:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

#ex.7-4
# завершение цикла while с использованием команды if
promt = 'Введите дополнения к пицце, и я добавлю их в заказ!'
promt += '\nЕсли все дополнения введены, напишите "выход". '

message = ''
while message != 'выход':
    message = input(promt)

    if message != 'выход':
        print('Дополенение: ' + message + ' добавлено в заказ!')

    else:
        print('Спасибо за заказ!')

#завершение цикла while с использованием флагов True/False
promt = 'Введите дополнения к пицце, и я добавлю их в заказ!'
promt += '\nЕсли все дополнения введены, напишите "выход". '

active = True
while active:
    message = input(promt)

    if message == 'выход':
        active = False
        print('Спасибо за заказ!')
    else:
        print('Дополенение: ' + message + ' добавлено в заказ!')

#завершение цикла while с использованием команды break
promt = 'Введите дополнения к пицце, и я добавлю их в заказ!'
promt += '\nЕсли все дополнения введены, напишите "выход". '

while True:
    message = input(promt)

    if message == 'выход':
        print('Спасибо за заказ!')
        break
    else:
        print('Дополенение: ' + message + ' добавлено в заказ!')

#ex.7-5
# Использование цикла while для получения цены билета в зависимости от возраста
promt = 'Укажите свой возраст и я назову цену билета.'
promt += '\nЕсли хотите прекратить, напишите "выход". '

# Запускаем цикл
while True:
    age = input(promt)

# Прописываем условия
    if age == 'выход':
        print('Приятного просмотра!')
        break

    elif int(age) < 3:
        price = 0
    elif 3 <= int(age) < 12:
        price = 100
    elif int(age) >= 12:
        price = 150

# Выводим результат
    print('Цена билета равна ' + str(price) + ' рублей!')

#ex.7-8
# Начинаем с двух списков: с видами сендвичей
# и пустого списка для хранения приготовленных сендвичей.
sandwich_orders = ['tuna', 'turkey', 'spicy', 'cheese']
finished_sandwiches = []

# Перебираем все элементы первого списка
while sandwich_orders:
    type = sandwich_orders.pop()
    # вывод списка элементов, которые перебрали
    print('Type sandwich: ' + type)
    # добавление элементов первого списка во второй
    finished_sandwiches.append(type)

# вывод элементов второго списка (приготовленных сендвичей)
print('\nFinished_sandwiches: ')
for sandwich in finished_sandwiches:
    print('I made a ' + sandwich + '-sandwich!')

#ex.7-8
# Удаление повторяющихся значений из списка
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'turkey', 'spicy',
                   'pastrami', 'cheese']

# Вывод в терминал первоначального списка
print(sandwich_orders)

# Создание цикла для удаления повторяющегося элемента
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Вывод измененного списка
print(sandwich_orders)

# ex.7-10
# Создаем пустой словарь для сохранения значений, вводимых пользователем
response = {}

# Создаем цикл для получения ответа пользователей и сохраняем их в словарь
while True:
    name = input('What is your name? ')
    city = input('Which city would you like to visit? ')

    response[name] = city

# Спрашиваем о необходимости продолжения опроса
    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat.lower() == 'no':
        print('Thank you for your answer!')
        break

# Выводим результаты опроса
print('\nResults:')
for name, city in response.items():
    print(name.title().strip() + ' dreams of going to '
          + city.title().strip() + '!')