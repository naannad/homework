"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""
# input("Введите количество студентов:")

# students = int(input())
# for i in range(students):
#     ask = input("Сколько языков Вы знаете?")

students = int(input("Введите количество студентов:"))
lst = []
while students != 0:
       ask = int(input("Сколько студентов знают языки:"))
       for i in range(ask):
              ask1 = input("Какие языки Вы знаете:")
              lst.append(ask1)
       students -= ask

       print(len(lst), "-", lst)
       lst = []