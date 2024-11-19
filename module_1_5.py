
# module_1_5.py

# Практика: "Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = 'вывести на экран', 2, int
print(immutable_var)

#immutable_var [1] = 'ghbdtn'
# кортеж нельзя изменить

mutable_list = ['вывести на экран', 2, int]
print(mutable_list)

mutable_list [1] = 'заменить 2й элемент'
print(mutable_list)
mutable_list.extend (['что-то добавить'])
print(mutable_list)











