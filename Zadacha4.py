# Задача 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

q = int(input("Введите номер четверти координат (от 1 до 4): "))
if q == 1:
    print(f'Диапозон точек для {q}-ой четверти: (X > 0, Y > 0)')
elif q == 2:
    print(f'Диапозон точек для {q}-ой четверти: (X < 0, Y > 0)')
elif q == 3:
    print(f'Диапозон точек для {q}-ой четверти: (X < 0, Y < 0)')
elif q == 4:
    print(f'Диапозон точек {q}-ой четверти: (X > 0, Y < 0)')
else: 
    print("Введено некорректное значение четверти")