#УРОК 2

name = "Tapok" # str - строка
age = 11 # int - целое число
avg = 7.5 # float - ???
leha = True # bool - логический тип данных
# переменные не могут начинатся с цифры или специального знака

print(name)
print(type(name)) # <class 'str'>

print(age)
print(type(age)) # <class 'int'>

print(avg)
print(type(avg)) # <class 'float'>

print(leha)
print(type(leha)) # <class 'bool'>

print(type(11))
print(type("tapok"))
# функция type может использоватся как и на переменных, так и на текстах

name2 = input("Введите текст: ")
print("Ваш текст: ",name2)
print("Тип данных: ",type(name2))
