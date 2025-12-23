result = 5 + 10 # сложение
print(result, type(result))

result2 = 10 - 5 # вычитание 
print(result2, type(result2))

result3 = 5 * 5 # умножение
print(result3, type(result3))

result7 = 5 ** 3 # возвожение в степень
print(result7, type(result7))

# ДЕЛЕНИЕ:
result4 = 5 / 2 # деление вернёт float
print(result4, type(result4))

result5 = 5 // 2 # деление вернёт int
print(result5, type(result5))

result6 = 5 % 2 # деление вернёт int(остаток)
print(result6, type(result6))

# так же, это всё работает и в строке:
print(5 + 10)
print(10 - 5)
print(5 * 5)
print(5 ** 3)
print(5 / 2)
print(5 // 2)
print(5 % 2)

#
num1 = -142 # само число
print(abs(num1)) # возврощает число

# переменные можно спокойно перезаписывать
tapok = 14
print(tapok)

tapok = "vilka"
print(tapok)

# переназначение типа данных:
# str - str()
# int - int()
# float - float()
# bool - bool()

tapok2 = 17
tapok2 = str(tapok2)
tapok3 = float(tapok2)
print(tapok2,(type(tapok2)))
print(tapok3, (type(tapok3)))

tapok4 = int(input("Введите число "))
tapok5 = int(input("Введите второе число "))
print(tapok4 + tapok5, ",Ёё, так можно калькулятор написать то")
print("Hello World!")