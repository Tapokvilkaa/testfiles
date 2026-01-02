import random
rr = random.random()  # случайное число от 0.0 до 1.0
print(rr)

ra = random.randint(-1, 5)  # случайное ЦЕЛОЕ число в диапозоне чисел в скобках
print(ra)

ru = random.uniform(-1, 5)  # случайное дробное число в диапозоне чисел в скобках
print(ru)

rc = random.choice(["я гандон", "я не гандон"])  # случайный элемент из списка 
print(rc)

rcs = random.choices(["я гандон", "я не гандон"]) # возвращает случайный элемент(ы) из списка как список(даже если элемент 1)
print(rcs)
#   choices так же имеет ещё несколько параметров:
#   |- weights -- вероятности для каждово элемента
#   |- cum_weights -- пока что сама хз
#   |- k -- количество выбраных элементов(по умолчянию 1)

abcdictlol = ["A", "B", "C"]
random.shuffle(abcdictlol)  # перемешивает список 
print(abcdictlol)

