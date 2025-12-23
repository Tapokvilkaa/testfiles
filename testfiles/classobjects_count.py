class Tapokcnt:
    count = 0
    def __init__(self, name, kanadetomosusora,):
        self.name = name
        self.kanadetomosusora = kanadetomosusora
        Tapokcnt.count += 1

    def show(self):
        print(self.name, self.kanadetomosusora)
    
    def num(self):
        print(Tapokcnt.count)


tapok = Tapokcnt("tapok", "what")
tapok.show()
tapok.num()

tapook = Tapokcnt("tapook", "whaat")
tapook.show()
tapook.num()