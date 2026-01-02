class Person: # создание класса

    school_name = "Ceip Jose Esquiel" # переменная класса, общая для всех его обьектов

    def __init__(self, name, sex, profession): # __init__ - конструктор, метод автоматически вызывающиейся при создании нового обьекта
        # self(или любое другое название) - ссылка на наш будущий обьект
        # всё остальное - обычные параметры
        # : для создания блока метода, я не знаю зачем но надо
        self.name = name
    #   |     |   |   |
    #   |     |   |   значение из параметра
    #   |     |   оператор присваивания
    #   |     имя атрибута
    #   ссылка на обьект
        # так же со всеми остальными ниже
        self.sex = sex
        self.profession = profession

    def show(self): # АБСОЛЮТНО БЛЯТТ ВСЕГДА self(или зависит от названия) первый рпараметр в методах
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    def work(self):
        print(self.name, 'working as a', self.profession)


tapok = Person('Tapok', 'Female', 'student,IT student') 
tapok.show() # всегда ставь скобки после этого, не повторяй моих ошибок

tapok.sex = "Non-Binary" # изменили в обьекте(я не небинар это пример)

Person.school_name = "CEIP Jose esquivel" # изменили в классе

tapok.school_name = "ABC" # изменили только для одного обьекта

print(tapok.school_name) # покажет ABC(т.е. эта переменная только для этого обьекта)
print(Person.school_name) # покажет CEIP Jose esquivel(т.е это переменная класса)

# !!ВАЖНАЯ ИНФА!! когда мы меняем переменную класса только для обьекта, оно не меняет значеие переменной для него, а создаёт новую которая затемняет переменную класса для этого обьекта
# что бы удалить переменную затемнающию переменную класса и вернуть переменную класса нужно:
del tapok.school_name

print(tapok.school_name) # снова будет CEIP Jose esquivel
# источник: https://pynative.com/python-classes-and-objects/
# обьяснение: https://chat.deepseek.com/
# обращение к себе в будуйщем читающей это:
# пожалуйста используй двойные скобки, это просто пример