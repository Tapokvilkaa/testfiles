class Person: # создание класса
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

# методы класса
    def show(self): # АБСОЛЮТНО БЛЯТТ ВСЕГДА первый параметр в методах
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    def work(self):
        print(self.name, 'working as a', self.profession)


tapok = Person('Tapok', 'Female', 'student,IT student')

tapok.show()


# источник: https://pynative.com/python-classes-and-objects/
# обьяснение: https://chat.deepseek.com/