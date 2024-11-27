
#module_2_2.py

# "Условная конструкция. Операторы if, elif, else"

while True:                                                            # Выполнять, пока "истина" до break, иначе except.
        try:
            first = int(input('Введите первое целое число: '))
            second  = int(input('Введите второе целое число: '))
            third = int(input('Введите третье целое число: '))
            break                                                     # Если "истина" - то далее  блок 1 (if, elif, else).
        except:                                                       # Если в try ошибка, то print('Нужно ввести ЦЕЛОЕ число')
            print('Нужно ввести ЦЕЛОЕ число')                         # и повторить try.

# блок 1

if first == second == third:                                  #  Если все равны, то "3"
 print('3')
elif first == second or first == third or second == third:    #  Если 2-а из 3-х равны, то "2"
 print('2')
else:                                                         #  Иначе "0"
 print('0')






