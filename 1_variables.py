#ex.2-3
name = 'Anna'
message = 'Hello' + ',' + ' ' + name + '!' + ' ' + 'How are you today?'
print(message)

#ex.2-4
name_1 = ' dima'
name_2 = 'aLIna '
message = ('Hello' + ',' + ' ' + name_2.title().strip() + '!' + ' ' +
           'How are you today?')
print(message)

#ex.2-5
print('Michel de Montaigne' + ' ' + 'said: ' + '"The mind consists not '
        'only in knowledge, but also in the ability to apply knowledge '
        'in practice"' + '.')

#ex.2-6
author = ' Michel de Montaigne'
phrase = ('The mind consists not only in knowledge, but also in the ability '
          'to apply knowledge in practice')
message = author.strip() + ' ' + 'said: ' + '"' + phrase + '"' + '.'
print(message)

#ex.2-7
name_1 = 'Amina '
#приводит переменную к нужному виду
name_1 = name_1.title().strip()
name_2 = ' GeOrgia'
name_2 = name_2.title().strip()
name_3 = 'oStin'
name_3 = name_3.title().strip()
print('Names:' + '\n\t' + name_1 + ',' + '\n\t' + name_2 + ',' + '\n\t' +
      name_3 + '.')

print('\nNames: \n\tOlga, \n\tSergio, \n\tVladimir.')

#ex.2-8
#математические операции, результатом которых является число 8
print(1+7)
print(2*4)
print(64/8)
print(23-15)

#ex.2-9
favorite_number = 17
print('My favorite number is ' + str(favorite_number) + '!')

#ex.2-11
#принципы написания кода
import this

