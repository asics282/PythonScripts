# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Введите день недели: "))
if (day == 6 or day == 7):
    print("День недели", day," является выходным")
elif day in range(1,6):
    print("День недели", day," является рабочим")
else:
    print ("В неделе всего 7 дней. Введите корректную цифру")