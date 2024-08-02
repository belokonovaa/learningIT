#ex.3-1
friends = ['Marina', 'inga', 'Katrin ']
print(friends[0])
print(friends[1].title())
print(friends[2].lstrip())

#ex.3-2
friends = ['Marina', 'Inga', 'Katrin']
message = ' Have a nice day!'
print('\nHi, ' + friends[0] + '!' + message)
print('Hi, ' + friends[1] + '!' + message)
print('Hi, ' + friends[2] + '!' + message)

#ex.3-3
cars = ['Audi', 'Mercedes', 'Kia']
print('\nI want to buy a car ' + cars[0] + '.')
print('I want to buy a car ' + cars[1] + '.')
print('I want to buy a car ' + cars[2] + '.')

#ex.3-4
guests = ['Valery', 'Marya', 'Dmitriy']
print('\n' + guests[0].title() + ', I want to unvite you to lunch.')
print(guests[1].title() + ', I want to unvite you to lunch.')
print(guests[2].title() + ', I want to unvite you to lunch.')

#ex.3-5
guests = ['Valery', 'Marya', 'Dmitriy']
#один из гостей не смог прийти
missing_guest = guests[1]
print('\nUnfortunately, ' + missing_guest + ' will not be able to come.')

#замена гостя
guests[1] = 'Alina'
print('\nNew invitations:')
print(guests[0].title() + ', I want to unvite you to lunch.')
print(guests[1].title() + ', I want to unvite you to lunch.')
print(guests[2].title() + ', I want to unvite you to lunch.')

#ex.3-6
guests = ['Valery', 'alina', 'Dmitriy']
#добавление новых гостей в список
print('\nI have some new guests!')
guests.insert(0, 'Olga')
guests.insert(2, 'Elena')
guests.append('Sergio')
#приглашение новых гостей
print('Now I want to invite ' + str(len(guests)) + ' guests to lunch!')
print(guests[0].title() + ', I want to unvite you to lunch.')
print(guests[1].title() + ', I want to unvite you to lunch.')
print(guests[2].title() + ', I want to unvite you to lunch.')
print(guests[3].title() + ', I want to unvite you to lunch.')
print(guests[4].title() + ', I want to unvite you to lunch.')
print(guests[5].title() + ', I want to unvite you to lunch.')

#ex.3-7
#отмена приглашения для некоторых гостей
print('\nI invite only 2 guests to lunch.')
guest = guests.pop()
print(guest.title() + ', I am so sorry.')
guest = guests.pop()
print(guest.title() + ', I am so sorry.')
guest = guests.pop()
print(guest.title() + ', I am so sorry.')
guest = guests.pop()
print(guest.title() + ', I am so sorry.')

print('\n' + guests[0] + ' and ' + guests[-1] + ' I am waiting for you for '
                                                'lunch!')

#удаление всех гостей из списка
del guests[0]
del guests[0]

#вывод пустого списка
print(guests)

#ex.3-8
countries = ['France', 'USA', 'Canada', 'Australia', 'Germany']
print(countries)
#временная сортировка списка по алфавиту
print(sorted(countries))
print(countries)

#временная сортировка списка в обратном алфавитном порядке
print(sorted(countries, reverse=True))
print(countries)

#постоянная сортировка списка в обратном направлении
countries.reverse()
print(countries)

#постоянная сортировка списка по алфавиту
countries.sort()
print(countries)

#постоянная сортировка списка в обратном алфавитном порядке
countries.sort(reverse=True)
print(countries)

#ex.3-9
countries = ['France', 'USA', 'Canada', 'Australia', 'Germany']
print('\nThere are ' + str(len(countries)) + ' countries!\n')

#ex.3-10
cities = ['Vologda', 'Moscow', 'Aksay']

#замена элемента в списке
cities[1] = 'Tomsk'
print(cities)

#добавление элемента в конец списка
cities.append('Kirov')
print(cities)

#добавление элемента по указанному индексу
cities.insert(0, 'Rostov-on-Don')
print(cities)

#удаление элементов списка
del cities[3]
print(cities)

cities.pop()
print(cities)

cities.pop(1)
print(cities)

cities.remove('Tomsk')
print(cities)

cities.append('Kirov')
cities.append('Aksay')
cities.append('Vologda')
cities.append('Tomsk')
print(cities)

#упорядочение списка
#сортировка по алфавиту
cities.sort()
print(cities)

#сортировка в обратном алфавитном порядке
cities.sort(reverse=True)
print(cities)

#временная сортировка по алфавиту
print(sorted(cities))
print(cities)

#сортировка в обратном направлении
cities.reverse()
print()

#подсчет элементов списка
print(len(cities))
