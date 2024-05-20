# Задание "Средний бал"
#Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":

#На вход даны следующие даннные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # множество
# списки содержат оценки по алфавитному порядку учеников во множестве
my_set = list(students)  # преобразование множества в список
my_set.sort()   # сортировка в алфаыитном порядке
print(my_set)
print(grades)
one = sum(grades[0]) / len(grades[0]) # расчет среднего балла для учеников
two = sum(grades[1]) / len(grades[1])
three = sum(grades[2]) / len(grades[2])
four = sum(grades[3]) / len(grades[3])
five = sum(grades[4]) / len(grades[4])
dict = {my_set[0]: one, my_set[1] : two,  my_set[2] : three,  my_set[3] : four,  my_set[4] : five}
print(dict)



