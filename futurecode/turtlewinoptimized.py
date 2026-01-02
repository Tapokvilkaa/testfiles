import turtle
import time
t = turtle.Pen()

def square(px):
    for i in range(3):
        t.forward(px)
        t.right(90)
    t.forward(px)

def square4(pxx):
    for i in range(4):
        square(pxx)

onefour = input("1 квадрат или 4?(1/4) ")
def pixelreg():
    if onefour == "1":
        onepx = input("радиус пикселей: ")
        try:
            onepx = int(onepx)
            square(onepx)  
        except ValueError:
            print("выпей ртути")
            pixelreg()
        except Exception as a:
            if onepx >= 500:
                print("кто мне тут проги ломать любит))0))")
                pixelreg()
    if onefour == "4":
            fourpx = input("радиус пикселей: ")
            try:
             fourpx = int(fourpx)
             square4(fourpx)
            except ValueError:
                print("выпей ртути")
                pixelreg()

pixelreg()
time.sleep(3)

# обернуть в while true цикл, улучшить защиту от иных симболов, добавить колорамуфФЯЯЯЯЯюю
4