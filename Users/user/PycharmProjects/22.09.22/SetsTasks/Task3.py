"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)

mn1 = set()
mn2 = set()
mn3 = set()

for i in newspaper:
    mn1.add(i)

for i in magazine:
    mn2.add(i)

for i in both:
    mn3.add(i)


print(len((mn1 | mn2) - mn3))