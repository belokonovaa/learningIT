#ex.9-13
import random
# импортируем класс OrderedDict для создания словаря
# с сохранением порядка добавления пар «ключ—значение»
from collections import OrderedDict

# создание экземпляра класса OrderedDict,
# который сохраняется в favorite_numbers
favorite_numbers = OrderedDict()

# добавление в словарь новых пар «ключ—значение»
favorite_numbers['Anna'] = '17'
favorite_numbers['Ben'] = '56'
favorite_numbers['Olga'] = '3'
favorite_numbers['Nikita'] = '1'
favorite_numbers['Gleb'] = '88'

# перебор словаря и вывод информации в отформатированном виде
for name, number in favorite_numbers.items():
    print(name.title() + "'s favorite number is " + number + '.')


#ex.9-14
from random import randint

class Die():
    """создает модель 6-гранного кубика"""

    def __init__(self, sides = 6):
        """инициализирует атрибуты класса"""
        self.sides = sides

    def roll_die(self, n):
        """имитация бросков кубика c количеством попыток attempt"""

        for attempt in range(1, 11):
            print('Attempt number ' + str(attempt) + '.')
            number = random.randint(1, self.sides)
            print('Your number on this roll of the dice is ' + str(number) + '!')

# создание экземпляра кубика с количеством сторон по умолчанию
# и имитация броска 10 раз
my_dice = Die()
my_dice.roll_die(10)

# создание экземпляра кубика с 10 сторонами
# и имитация броска 10 раз
your_dice = Die(10)
your_dice.roll_die(10)

# создание экземпляра кубика с 20 сторонами
# и имитация броска 10 раз
mom_dice = Die(20)
mom_dice.roll_die(10)

#ex.9-15
import time

# показывает настоящее время
print("The time is: " + time.ctime())

# показывает время спустя 5 минут
later = time.time() + 300
print("The time later 5 min: " + time.ctime(later))

import datetime
#показывает сегодняшнюю дату
today = datetime.date.today()
print('Today is: ' + str(today))

