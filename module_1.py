
#module_1.py

# Дополнительная практика : "Средний балл"

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorting = sorted(students)                         # Сортировать студентов

average_grades = {}                                   # "Средние оценкИ", Создать пустой словарь

for i in range(len(sorting)):                            # i присвоить диапазон (range) по количеству (len) сортированных студентов (sorting)

    studddent = sorting[i]                                   # studddent присвоить элемент списка sorting с номером, равным значению переменной i

    average_grades[studddent] = sum(grades[i]) / len(grades[i])  #  Заполнить пустой словарь "Средние оценкИ"

print(average_grades)

# Иногда, при очень частом изменении в программе, результат давал ТОЛЬКО {'Steve': 4.8}, приходилось откатывать
