# у меня сложилось  впечатление, что в варианте 3-1
# именнованные параметры. Изменила на позиционные в моем разумении
num_1 = int(input("Введите делимое: "))
num_2 = int(input("Введите делитель: "))

def division(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print("На ноль делить нельзя")

print(division())