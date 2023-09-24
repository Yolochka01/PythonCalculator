zn_1 = int(input("Введите первое число "))
znak = input("Введите операцию ")
zn_2 = int(input("Введите второе число "))
if znak == '+':
    print(zn_1 + zn_2)
elif znak == '-':
    print(zn_1 - zn_2)
elif znak == '/':
    print(zn_1 / zn_2)
elif znak == '*':
    print(zn_1 * zn_2)
elif znak == "**":
    print(zn_1 ** zn_2)
elif znak == "//":
    print(zn_1 // zn_2)
else:
    print("Вы ввели не то число или операцию")