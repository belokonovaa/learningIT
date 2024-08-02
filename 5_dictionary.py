#ex.6-1
#информация о человеке
person = {
    'first_name' : 'Anna',
    'last_name' : 'Belokonova',
    'age' : '24',
    'city' : 'Rostov-on-Don',
    }

print('Your first name is ' + person['first_name'].title() + '.')
print('Your last name is ' + person['last_name'].title() + '.')
print('Your age is ' + str(person['age']) + '.')
print('Tour city is ' + person['city'] + '.')

#ex.6-2
#информация о любимых числах друзей
nums = {
    'Anna' : '17',
    'Ben' : '56',
    'Olga' : '3',
    'Nikita' : '0',
    'Gleb' : '88',
    }

print("Anna's favorite numbers is " + str(nums['Anna']) + '!')
print("Ben's favorite numbers is " + str(nums['Ben']) + '!')
print("Olga's favorite numbers is " + str(nums['Olga']) + '!')
print("Nikita's favorite numbers is " + str(nums['Nikita']) + '!')
print("Gleb's favorite numbers is " + str(nums['Gleb']) + '!')

#ex.6-3
#создание глоссария с новыми терминами
glossary = {
    'Список' : 'последовательность элементов, следующая в определенном порядке',
    'Конкатенация' : 'операция соединения двух или более строк в одну',
    'Словарь' : 'совокупность пар «ключ—значение»',
    }

print('\nMy glossary:')
print('\tСписок' + ' - это ' + glossary['Список'] + '.')
print('\tСловарь' + ' - это ' + glossary['Словарь'] + '.')
print('\tКонкатенация' + ' - это ' + glossary['Конкатенация'] + '.')

#ex.6-4
#перебор глоссария и вывод терминов в отформатированном виде
for key, value in glossary.items():
    print(key.title() + ' - это ' + value + '.')

#ex.6-5
#информация о реках и городах. Перебор словаря
info = {
    'St.Petersburg' : 'Neva',
    'Moscow' : 'Moscow-river',
    'Rostov-on-Don': 'Don'
    }

for city, river in info.items():
    print('The ' + river.title() + ' runs through ' + city.title() + '.')

print('\nCities:')
for city in info.keys():
    print('\t- ' + city.title())

print('\nRivers:')
for river in info.values():
    print('\t- ' + river.title())

#ex.6-6
#информаиця о любимых языках программирования. Вывод в терминал в соотвествии с
#правилами русского языка(ед/мн число)
names = ['jen', 'sarah', 'anna', 'elza', 'edward', 'phil']
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
    }

for name in names:
    if name in favorite_languages:
        print('Hi, ' + name.title() + '!' + ' Thank you for your answer!' +
              ' I know, that your favorite language is ' +
              favorite_languages[name].title() + '!')
    else:
        print('Hi, ' + name.title() + '!' + ' What is your favorite language?')

#ex.6-7
#создание списка со словарями
person_1 = {
    'first_name' : 'Anna',
    'last_name' : 'Belokonova',
    'age' : '24',
    'city' : 'Rostov-on-Don',
    }

person_2 = {
    'first_name' : 'Elena',
    'last_name' : 'Baranova',
    'age' : '48',
    'city' : 'Aksay',
    }

person_3 = {
    'first_name' : 'Dmitriy',
    'last_name' : 'Leonov',
    'age' : '24',
    'city' : 'White Kalitva',
    }

people = [person_1, person_2, person_3]

for person in people:
    full_name = person['first_name'] + ' ' +  person['last_name']
    print('\nFull name: ' + full_name + '\nAge: ' + str(person['age'])
          + '\nCity: ' + person['city'])

#ex.6-8
pet_1 = {
    'name' : 'Barsik',
    'type' : 'cat',
    'owner' : 'Anna'
    }

pet_2 = {
    'name' : 'Borya',
    'type' : 'dog',
    'owner' : 'vladimir'
    }

pet_3 = {
    'name' : 'kyzya',
    'type' : 'Hamster',
    'owner' : 'Alina'
    }

pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print('\nThe most beloved ' + pet['owner'].title() + "'s pet is " +
          pet['type'].lower() + '.' + '\nThe ' + pet['type'].lower() +
          "'s name is " + pet['name'].title() + '!')

#ex.6-9
#создание словаря со списками
favorite_countries = {
    'Anna' : ['USA', 'Canada', 'Great Britian'],
    'Olga' : ['brazil'],
    'Sergio' : ['Poland', 'New Zeland'],
}

for name, countries in favorite_countries.items():
    if len(countries) == 1:
        print('\nThe most favorite ' + name.title() + "'s country is:")
        for country in countries:
            print('- ' + country.title())
    else:
        print('\nThe most favorite ' + name.title() + "'s countries are:")
        for country in countries:
            print('- ' + country.title())

#ex.6-10
nums = {
    'Anna' : ['17', '3'],
    'Ben' : ['56', '41'],
    'Olga' : '3',
    'Nikita' : '0',
    'Gleb' : ['88', '97', '102'],
    }

for name, numbers in nums.items():
    if len(numbers) == 1:
        print('\nThe luckiest number for ' + name.title() + ':')
        for number in numbers:
            print('- ' + number)
    if len(numbers) > 1:
        print('\nThe luckiest numbers for ' + name.title() + ':')
        for number in numbers:
            print('- ' + number)

#ex.6-11
#создание словаря со словарями
cities = {
    'Moscow': {'country': 'Russia',
               'population' : '13 149 803',
               'date of foundation' : '1147'},
    'Rostov-on-Don' : {'country': 'Russia',
                       'population' : '1 142 162',
                       'date of foundation' : '1749'},
    'St.Petersburg' : {'country': 'Russia',
                       'population' : '5 597 763',
                       'date of foundation' : '1703'},
    'Kemerovo' : {'country': 'Russia',
                  'population' : '544 600',
                  'date of foundation' : '1701'}
    }

for city, info in cities.items():
    print('\nThe ' + city.title() + ' is located in ' + info['country'] + '.'
          + ' It was founded in ' + str(info['date of foundation']) + '.'
          + " It's population is " + str(info['population']) + '.')