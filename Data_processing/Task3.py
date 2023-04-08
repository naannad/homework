"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""
def print_temperature(temperatures):
    for temperature in temperatures:
        print("Сегодня", temperature, "градусов")

temperatures = [17, 19, 20, 22, 18]
print_temperature(temperatures)