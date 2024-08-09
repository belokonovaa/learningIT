#ex.10-1
# вывод содержимого файла
file = ' '
with open (file) as file:
    contents = file.read()
    print(contents)

# вывод содержимого файла с перебором строк
file = ' '
with open (file) as file:
    for line in file:
        print(line.rstrip())

# вывод содержимого файла с созданием списка строк
file = ' '
with open (file) as file:
    lines = file.readlines()

# использование списка строк после закрытия файла
for index, line in enumerate(lines):
    print(str(index + 1) + '. ' + line.strip())


#ex.10-2
# замена слова в строке читаемого файла
file_name = 'python.txt'
with open(file_name) as file:
    for index, line in enumerate(file):
        new_line = line.replace('Python', 'C')
        print(str(index + 1) + '. ' + new_line.strip())

#ex.10-3 and 10-4
# запись имен пользователей в новый файл
with open('guest.txt', 'a') as file_of_name:
    while True:
        message = 'What is your name?'
        message += '\nIf you want to stop, enter "q" '
        name = input(message)

        if name == 'q':
            break
        else:
            print('Hi, ' + name.title() + '!')
            file_of_name.write(name.title() + '\n')

#ex.10-5
# запись ответов пользователей в отдельный текстовый файл
with open('user_answers', 'a') as file:
    promt = 'Why do you like to programming?'
    promt += '\nIf you want to stop, enter "q" '
    while True:
        answer = input(promt)

        if answer == 'q':
            break
        else:
            print('Wow! It is great!')
            file.write(answer + '\n')


#10-6 and 10-7
# сложение чисел, введенных пользователем
message = "Tell me 2 numbers and I'll add them up"
message += '\nIf you want to stop, enter "q" '
print(message)

while True:
        first_number = input('First number: ')
        if first_number == 'q':
            break

        second_number = input('Second number: ')
        if second_number == 'q':
            break

        # выведение подсказки, если пользователь указал не числа, а строки
        try:
            answer = int(first_number) + int(second_number)
        except ValueError:
            print('Please tell me a number!')
        else:
            print('Answer: ' + str(answer))

#10-8
def read_file(name_of_file, names):
    """читает файл и выводит клички животных в отформатированном виде
        при отсутствии файла выводит сообщениеб,
        что такого файла не существует"""

    try:
        with open(name_of_file) as file:
            print(names.title() + ': ')
            for name in file:
                print('- ' + name.title().strip())
    except FileNotFoundError:
        print('Sorry, this file is missing.')

read_file('dogs.txt', 'Dogs')
read_file('cats.txt', 'Cats')

#10-10
def count_words(file, word):
    """подсчитывает количество заданного слова в выбранном файле"""
    try:
        with open(file) as file:
            for line in file:
                count_word = line.count(word)
            print('The word "' + word + '" appears in the book '
                  + str(count_word) + ' times!')
    except FileNotFoundError:
        pass

count_words('pride.txt', 'the')
