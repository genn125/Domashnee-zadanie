
#module_1.py

# Дополнительная практика : "Средний балл"

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorting = sorted(students)                         # Сортировка по алфавиту студентов

average_grades = {}                                   # Средние оценкИ, Создание пустого словаря

for i in range(len(sorting)):                             # диапазон по колличеству студентов
    student = list(sorting)[i]                              #Преобразует последовательность в список


    average_grade = sum(grades[i]) / len(grades[i])             # Средняя оценкА
    average_grades[student] = average_grade

print(average_grades)
