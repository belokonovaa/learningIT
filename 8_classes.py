#ex.9-1
class Restaurant():
    """модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """инициализирует атрибуты restaurant_name и cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """выводит сообщение о названии ресторана и типе его кухни"""
        print("\nRestaurant's name is " + self.restaurant_name.title() + '.'
              '\nCuisine type of ' + self.restaurant_name.title() + ' is ' +
                self.cuisine_type + '.')

    def open_restaurant(self):
        """выводит сообщение о том, что ресторан открыт"""
        print('Restaurant "' + self.restaurant_name.title() + '" is open!')

#создание экземпляра ресторана
my_restaurant = Restaurant('Avocado Quenn', 'Mediterranean')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#ex.9-2
# создание экземпляров на основе класса
your_restaurant = Restaurant('Onegin cottage', 'European')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

my_mom_restaurant = Restaurant('rock', 'European')
my_mom_restaurant.describe_restaurant()
my_mom_restaurant.open_restaurant()

my_dad_restaurant = Restaurant('1460 Meat story', 'European')
my_dad_restaurant.describe_restaurant()
my_dad_restaurant.open_restaurant()

#ex.9-3
class User():
    """модель пользователя"""

    def __init__(self, first_name, last_name, age, locftion, favorute_song):
        """инициализирует атрибуты описания пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = locftion
        self.favorite_song = favorute_song

    def describe_user(self):
        """выводит информацию о пользователе"""
        print('\nMy name is ' + self.first_name.title() + ' ' +
              self.last_name.title() + '.')
        print('I am ' + str(self.age) + ' years old.')
        print('I live in ' + self.location.title() + '.')
        print('My favorite song is ' + self.favorite_song + '!')

    def greet_user(self):
        """выводит приветствие"""
        print('\nHi, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

anna = User('Anna', 'belokonova', '24',
            'rosov-on-don','Never gonna give your up')
anna.describe_user()
anna.greet_user()

dima = User('dmitriy', 'leonov', '24',
            'White kalitva','Жду чуда')
dima.describe_user()
dima.greet_user()

#ex.9-4
#копия класса ресторана из ex.9-1
class Restaurant():
    """модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """инициализирует атрибуты restaurant_name и cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # новый атрибут - количество обслуженных посетителей
        self.num_served = 0

    def number_served(self):
        """выводит информацию о количестве обслуженных посетителей"""
        print('The number of visitors served is ' + str(self.num_served)
              + '.')

    def set_number_served(self, numbers):
        """устанавливает количество обслуженных посетителей и выводит информацию"""
        self.num_served = numbers
        print('The number of visitors served is ' + str(self.num_served)
              + '.')

    def increment_number_served(self, increment_numbers):
        """увеличивает количество обслуженных посетителей с заданным приращением"""
        self.num_served += increment_numbers
        print('The number of visitors served is ' + str(self.num_served)
              + '.')

rest_1 = Restaurant('Cheese factory', 'European')
# изменение значение нового атрибута - количества обслуженных посетителей
rest_1.num_served = 5
rest_1.number_served()
rest_1.set_number_served(10)
rest_1.increment_number_served(33)
rest_1.increment_number_served(48)

#ex.9-5
# копия класса User из ex.9-3
class User():
    """модель пользователя"""

    def __init__(self, first_name, last_name, age, locftion, favorute_song):
        """инициализирует атрибуты описания пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = locftion
        self.favorite_song = favorute_song
        # добавление нового атрибута с заданным значением
        self.login_attempts = 0

    def number_login_attempts(self):
        """показывает количество попыток входа в систему"""
        print('The number of login attempts is ' + str(self.login_attempts) + '.')

    def increment_login_attempts(self):
        """отображает количество попыток входа в систему в реальном времени.
        При каждой попытке входа показатель увиличивает на 1"""
        self.login_attempts += 1
        print('The number of login attempts is ' + str(self.login_attempts) + '.')

    def reset_login_attempts(self):
        """обнуляет количество попыток входа в систему"""
        self.login_attempts = 0
        print('The number of login attempts is ' + str(self.login_attempts) + ' now.')

olga = User('Olga', 'Skubitskaya', '48', 'Donetsk',
            'White roses')
olga.number_login_attempts()
olga.increment_login_attempts()
olga.increment_login_attempts()
olga.reset_login_attempts()

#ex.9-6
class IceCreamStand(Restaurant):
    """разновидность ресторана - киоск с мороженым"""
    def __init__(self, restaurant_name, cuisine_type):
        """инициализация атрибутов класса родителя (Restaurant)
            и класса потомка (IceCreamStand)"""
        super().__init__(restaurant_name, cuisine_type)
        # добавление нового атрибута - список со вкусами мороженого
        self.flavors = []

    def describe_flavors(self):
        """Создание списка с разновидностью мороженого и его выведение"""
        self.flavors.append('Chocolate')
        self.flavors.append('Strawberry')
        self.flavors.append('Vanilla')
        print('\nOur restaurant "' + self.restaurant_name.title()
              + '" our restaurant has the following ice cream flavors: ')
        for flavor in self.flavors:
            print('- ' + flavor)

my_ice_cream_stand = IceCreamStand('Yammy!', 'Ice Cream')
my_ice_cream_stand.describe_flavors()

#ex.9-7
class Admin(User):
    """разновидность пользователя - администратор"""

    def __init__(self, first_name, last_name, age, locftion, favorute_song):
        """инициализирует атрибуты класса-родителя (User)
        и класса-потомка (Admin)"""
        super().__init__(first_name, last_name, age, locftion, favorute_song)
        # создание нового атрибута - привелегии
        self.privileges = []

    def show_privileges(self):
        """добавляет в новый список привелегии администратора
        и выводит их в отформатированном виде"""
        self.privileges.append("allowed to add messages")
        self.privileges.append("allowed to delete users")
        self.privileges.append("allowed to ban users")
        print("\nAdmin's privileges:")
        for privilege in self.privileges:
            print('- ' + privilege)

sergio = Admin('Sergio', 'Roy', '49',
               'Oktyabrsky','Mirrors')
sergio.show_privileges()

#ex.9-8
class Privileges():
    """ привелегии администратора"""

    def __init__(self):
        """инициализация атрибутов класса"""
        self.privileges = []
    def show_privileges(self):
        """выводит список привелегий администратора"""
        self.privileges.append("allowed to add messages")
        self.privileges.append("allowed to delete users")
        self.privileges.append("allowed to ban users")
        print("\nAdmin has " + str(len(self.privileges)) + " privileges:")
        for privilege in self.privileges:
            print('- ' + privilege)

class Admin(User):
    """разновидность пользователя - администратор"""

    def __init__(self, first_name, last_name, age, locftion, favorute_song):
        """инициализирует атрибуты класса-родителя (User)
        и класса-потомка (Admin)"""
        super().__init__(first_name, last_name, age, locftion, favorute_song)
        #класс Privileges становится атрибутом класса Admin
        self.privileges = Privileges()

elena = Admin('Elena', 'Baranova', '48', 'Aksay',
              'Moscow song')
elena.privileges.show_privileges()

#ex.9-9
class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, milliage):
        """Устанавливает заданное значение на одометре"""
        self.odometer_reading = milliage
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
        print("This car has " + str(self.odometer_reading) + " miles on it.")

class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def update_battery(self):
        """проверяет размер аккумулятора и устанавливает мощность"""
        if self.battery_size != 85:
            self.battery_size = 85
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя и класса-потомка"""
        super().__init__(make, model, year)
        # использует класс Buttery как новый атрибут
        self.battery = Battery()

# создаем экземпляр на основе класса ElectricCar
# с размером аккумулятора по умолчанию
my_car = ElectricCar('A8', 'aidi', '2024')

# вызываем функцию get_range, подтверждающую, что размер аккумулятора
# равен значению по умолчанию
my_car.battery.get_range()

# вызываем функцию update_battery для изменения размера аккумулятора
my_car.battery.update_battery()

# вызываем снова функцию get_range для подтверждения изменения
# размеров аккумулятора
my_car.battery.get_range()


