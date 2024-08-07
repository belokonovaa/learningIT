#ex.8-1
# самая простая функция
def display_message():
    """Выводит похвалу"""
    print('Wow! You are already learning the functions! \nWell done!')

display_message()

#ex. 8-2
# функция с одним параметром
def favorite_book(name):
    """выводит информацию о любимой книге"""
    print('One of my favorite books is ' + name.title() + '!')

favorite_book('Alice in Wonderland')

#ex. 8-3
#вызов функции с позиционными и именованными аргументами
def make_shirt(size, text):
    """выводит информацию о заказанной футболке - размер и текст"""
    print('You ordered a ' + size.title() + '-size shirt with text: "' + text +
          '".')
make_shirt('s', 'Hello, World!')
make_shirt(text='Never gonna give you up!', size='m')

#ex.8-4
#вызов функции с аргументами по умолчанию
def make_shirt(size = 'L', text = 'I love Python!'):
    """выводит информацию о заказанной футболке - размер и текст"""
    print('You ordered a ' + size.upper() + '-size shirt with text: "' + text +
          '".')

make_shirt()
make_shirt(size='s')
make_shirt(text='You will succeed!')
make_shirt(size='xxl', text='blablabla')
make_shirt('s', 'hi')

#ex.8-5
#
def describe_city(city, country = 'Russia'):
    """выводит внесенные данные в отформатированном виде: город в страна"""
    # условие для правильного отображения информации
    if country.lower() == 'usa':
        print(city.title().strip() + ' is in ' + country.upper() + '.')
    else:
        print(city.title().strip() + ' is in ' + country.title() + '.')

describe_city('Moscow')
describe_city('st.petersburg')
describe_city('new york ', 'USA')

#ex.8-6
# функция с возвращаемым значением
def city_country(city, country):
    """возвращает данные в отформатированном виде: город-страна"""
    full_info = city.title() + ' - ' + country.title()
    return full_info

new_info = city_country('moscow', 'russia')
print(new_info)
new_info = city_country('berlin', 'germany')
print(new_info)
new_info = city_country('paris', 'france')
print(new_info)

#ex.8-7
# функция, использующая в качестве возвращаемого значения словарь
def make_album(musician, album, tracks = ''):
    """ возвращает словарь с информацией об исполнителе, его альбоме
        и, при наличии, количества треков в альбоме"""
    musician = musician.title().strip()
    album = album.title().strip()
    info = {'musician': musician, 'album': album}
    #при наличии количества треков в альбоме добавляет новую пару
    #ключ-значение в словарь
    if tracks:
        info['tracks'] = tracks
    return info

new_info = make_album('Lana del rey', 'blue banisters')
print(new_info)
new_info = make_album(' драгни', 'не валяй дурака', tracks='10')
print(new_info)
new_info = make_album('pizza', 'кухня')
print(new_info)

#ex.8-8
#использование функции с циклом while
def make_album(musician, album):
    """ возвращает в словарь отформатированные данные об исполнителе
        и его альбоме"""
    musician = musician.title().strip()
    album = album.title().strip()
    info = {'musician' : musician, 'album' : album}
    return info

while True:
    # запрашивает у пользователя информацию о его любимом музыканте и альбоме
    print("\nPlease tell me about your favotite musician and his album:")
    print("(enter 'q' at any time to quit)")

    musician = input('What is your favorite musician? ')
    if musician == 'q':
        break

    album = input('What is your favorite album? ')
    if album == 'q':
        break

    # выводит информацию в виде словаря
    records = make_album(musician, album)
    print(records)

#ex.8-9
# создаем список фокусников
magicians = ['Anna', 'Vitaliy', 'Gennadiy', 'Julia']

def show_madician(lists):
    """ перебирает все имена фокусников и добавляет приветствие"""
    for magician in magicians:
        print('Hi, ' + magician.title() + '!')

show_madician(magicians)

#ex.8-10
# вызов функции из функции

# создаем список фокусников
magicians = ['Anna', 'Vitaliy', 'Gennadiy', 'Julia']
def make_great(lists):
    """добавляет к каждому имени фокусника приставку -great
        и выводит приветствие """
    for i in range(len(lists)):
        lists[i] = 'Great-' + lists[i]
    show_madician(lists)

make_great(magicians)

#ex.8-11
# создаем список фокусников
magicians = ['Anna', 'Vitaliy', 'Gennadiy', 'Julia']
def make_great_2(lists):
    """добавляет к имени приставку Great и выводит список фокусников"""
    for i in range(len(lists)):
        lists[i] = 'Great-' + lists[i]
    print(lists)
    # возвращаем изменный список и сохраняем его в новом списке,
    # для подтверждения, что исходный список не изменился
    return lists
    new_lists = lists
    print(new_lists)

# передаем функции копию списка
make_great_2(magicians[:])
# подтверждаем, что исходный список не изменился
print(magicians)

#ex.8-12
# создание функции с произвольным набором аргументов
def make_sandwich(*toppings):
    """перебирает все дополнения к пицце и выводит их в отформатированном виде"""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print('- ' + topping)

make_sandwich('bread', 'ham', 'cheese')
make_sandwich('pepper', 'tomato', 'chips', 'pesto')
make_sandwich('tomato', 'cheese')

#ex.8-13
# использование произвольного набора именованных аргументов
def build_profile(first, last, **user_info):
    """строит словарь с информацией о пользователе"""
    person = {}
    person['first name'] = first
    person['last name'] = last
    for key, value in user_info.items():
        person[key] = value
    return person

anna = build_profile('Anna', 'Belokonova', location = 'Selmash')

print(anna)

