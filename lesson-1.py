#! number

print(2 + 2)
print(2 - 2)
print(2 * 2)
print(17 / 3)

print(17 // 3)  # округляет к меньшей
print(17 % 3)  # выводит остаток (2)

print(5 ** 2)  # степень (5 * 5)

width = 5
height = 5.45
print(width + height)

print(round(height, 1))  # round округление до нулевых значений

#! string

print('spam eggs')  # single quotes

print('doesn\'t')  # use \' to escape the single quote...

print("doesn't")  # ...or use double quotes instead

print('"Yes," they said.')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

# Если вы не хотите, чтобы символы с предисловием \интерпретировались как специальные символы,
# вы можете использовать необработанные строки , добавив rперед первой кавычкой:

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# Строковые литералы могут занимать несколько строк. Один из способов — использовать тройные кавычки: """..."""или '''...'''.
# Концы строк автоматически включаются в строку, но этого можно избежать, добавив \в конце строки символ . Следующий пример:

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Строки можно объединять (склеивать) с помощью +оператора и повторять с помощью *:
# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

# Два или более строковых литерала (т.е. заключенные в кавычки) рядом друг с другом автоматически объединяются.
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# Строки могут быть проиндексированы (подписаны), при этом первый символ имеет индекс 0.
# Отдельного типа символов нет; символ — это просто строка размера один:

word = 'Python'
print(word[0])  # character in position 0

print(word[5])  # character in position 5

# Индексы также могут быть отрицательными числами, чтобы начать отсчет справа:

word[-1]  # last character

word[-2]  # second-last character

word[-6]

# В дополнение к индексации также поддерживается нарезка .
# В то время как индексация используется для получения отдельных символов,
# нарезка позволяет получить подстроку:

word[0:2]  # characters from position 0 (included) to 2 (excluded)

word[2:5]  # characters from position 2 (included) to 5 (excluded)

# Индексы срезов имеют полезные значения по умолчанию;
# пропущенный первый индекс по умолчанию равен нулю,
# пропущенный второй индекс по умолчанию равен размеру разрезаемой строки

word[:2]   # character from the beginning to position 2 (excluded)

word[4:]   # characters from position 4 (included) to the end

word[-2:]  # characters from the second-last (included) to the end

# Строки Python нельзя изменить — они неизменяемы . Следовательно, присваивание индексированной позиции в строке приводит к ошибке:
# Если вам нужна другая строка, вы должны создать новую:

'J' + word[1:]

word[:2] + 'py'


#! СПИСКИ

squares = [1, 4, 9, 16, 25]  # СПИСОК

# Все операции над срезами возвращают новый список, содержащий запрошенные элементы. Это означает, что следующий фрагмент возвращает неглубокую копию списка:
squares[:]
#[1, 4, 9, 16, 25]


# Списки также поддерживают такие операции, как конкатенация:
squares + [36, 49, 64, 81, 100]

# В отличие от строк, которые являются неизменяемыми , списки являются изменяемым типом, т.е. их содержимое можно изменить:

cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!

cubes[3] = 64  # replace the wrong value
print(cubes) #[1, 8, 27, 64, 125]

#Вы также можете добавлять новые элементы в конец списка, используя append() метод (позже мы увидим больше о методах):

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
#[1, 8, 27, 64, 125, 216, 343]

#Также возможно назначение слайсов, и это может даже изменить размер списка или полностью очистить его:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
#['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
#['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
print(letters)
#['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
#[]

#Встроенная функция len()также применяется к спискам: определяет количесво жлементов в массиве

letters = ['a', 'b', 'c', 'd']
print(len(letters))
#4

#Возможно вложение списков (создание списков, содержащих другие списки), например:

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
#[['a', 'b', 'c'], [1, 2, 3]]
x[0]
#['a', 'b', 'c']
x[0][1]
#'b'