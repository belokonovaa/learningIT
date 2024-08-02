#ex.5-1
#проверка условий
city = 'Tokyo'
print("Is city == 'Tokyo'? I predict True.")
print(city == 'Tokyo')
city = 'Moscow'
print("Is city == 'Tokyo'? I predict False.")
print(city == 'Tokyo')
city = 'Kemerovo'
print("Is city == 'Moscow'? I predict False.")
print(city == 'Moscow')
print("Is city == 'Kemerovo'? I predict True.")
print(city == 'Kemerovo')

#ex.5-2
#проверка равенства строк
string = 'I love Python!'
if string == 'I love Python!':
    print('I really love Python too!')

#проверка неравенства строк
string = 'I love C++'
if string != 'I love Python!':
    print('Why do not you love Python? ')

#проверка с использованием функции lower()
name = 'Anna'
if name.lower() == 'anna':
    print('Sorry, this name is occupied.')
else:
    print('This name is free!')

name = 'DmItrY'
if name.lower() == 'anna':
    print('Sorry, this name is occupied.')
else:
    print('This name is free!')

# числовые проверки равенства и неравенства
age = 18
if age == 18:
    print("Congratulations! You're an adult.")

answer = 24
if answer != 55:
    print('Your answer is uncorrect.')

# условий «больше» и «меньше»
age = 34
if age > 18:
    print("You're an adult.")

age = 5
if age < 18:
    print("You're a child.")

# условий «больше или равно» и условий «меньше или равно»
money = 1000
if money >= 1000:
    print('You can go on vacation!')

money = 975
if money <= 1000:
    print('Sorry, you can not go on vacation.')

#проверка с ключевым словом and и or
age = 21
money = 19437
if (age >= 18) and (money >= 1000):
    print("You can go on a journey by yourself!")

age = 6
money = 74
if (age <= 18) and (money <= 1000):
    print("You can only travel with your parents.")

#проверка вхождения элемента в список или его отсуствия
name = ['Anna', 'Maria', 'Daria', 'Victoria']
print('Anna' in name)
print('Elena' in name)

#ex.5-3
alien_color = 'red'
if alien_color == 'green':
    print("You've earned 5 points!")

alien_color = 'green'
if alien_color == 'green':
    print("You've earned 5 points!")

#ex.5-4
alien_color = 'yellow'
if alien_color == 'green':
    print("You've earned 5 points!")
else:
    print("You've earned 10 points!")

#ex.5-5
alien_color = 'red'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15
print("You've earned " + str(point) + " points!")

#ex.5-6
age = 34
if age < 2:
    message = 'a baby'
elif age >=2 and age < 4:
    message = 'a kid'
elif age >=4 and age < 13:
    message = 'a child'
elif age >= 13 and age < 20:
    message = 'a teenager'
elif age >= 20 and age < 65:
    message = 'an adult'
elif age >= 65:
    message = 'an elderly man'
print('You are ' + message + '.')

#ex.5-7
favorite_fruits = ['banana', 'Kiwi', 'WaTermelon', 'Apple', 'PeAch']
#сделать весь список в одинаковом формате
favorite_fruits = [x.title() for x in favorite_fruits]
if 'Banana' in favorite_fruits:
    print('You love a Banana!')
if "Watermelon" in favorite_fruits:
    print('You love a Watermelon!')
if "Strawberry" in favorite_fruits:
    print('Do you love a strawberry?')
if "Cherry" in favorite_fruits:
    print('Do you love a cherry?')
if 'Peach' in favorite_fruits:
    print('You love a peach!')

#ex.5-8
names = ['anna', 'Maria', 'Admin', 'Daria', 'Victoria']
for name in names:
    if name.lower() == 'admin':
        print('Hello ' + name.title() + ', would you like to see a status '
                                        'report?')
    else:
        print('Hello ' + name.title() + ', thank you for logging in again!')

#ex.5-9
names = []
if names:
    for name in names:
        print('Hi, ' + name.title() + '!')
else:
    print('We need to find some users!')

#ex.5-10
current_users = ['Anna', 'Maria', 'Elena', 'Daria', 'Victoria']
current_users = [x.lower() for x in current_users]
new_users = ['ANNA', 'Olga', 'Ksenia', 'Natalia', 'daria']

for name in new_users:
    if name.lower() in current_users:
        print('Please choose a different name.')
    else:
        print('Name is free!')

#ex.5-11
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        addition = 'st'
    elif number == 2:
        addition = 'nd'
    elif number == 3:
        addition = 'rd'
    else:
        addition = 'th'
    print(str(number) + addition)
