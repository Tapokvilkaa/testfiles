import time
import colorama
import sys

#(".", end="\r")
#ime.sleep(0.8)
#rint(" " * 50 + "\r", end="") 


name = input("Введи своё имя чтобы я знала как тебя звать: ")
print("КТО ТО УЖЕ ДЕЛАЛ НОВЕЛЛУ В КОМАНДНОЙ СТРОКЕ??")

yagandon = ""
while yagandon not in ["1", "2", "3"]:  
    yagandon = input("1 - да, 2 - нет, 3 - возможно: ")
    if yagandon not in ["1", "2", "3"]:
        print("Напиши нормальный ответ, пожалуйста!")  

if yagandon == "1":
    print("ну..")
    time.sleep(0.2)
    print(".")
    time.sleep(0.2)
    print("..")
    time.sleep(0.2)
    print("...")
    time.sleep(0.2)
    print("...зато я это вполне сама придумала!")
    time.sleep(0.2)
    print("И Я ЭТО СДЕЛАЮ!!")
    time.sleep(2)
    print("...если мне хватит сил и терпения")
    time.sleep(2)
    print("...и если мне не придёт в голову другая безумная идея во время изучения пайтона")

elif yagandon == "2":
    print("ЗНАЧИТ Я БУДУ ПЕРВОЙ!!")
    time.sleep(2)
    print("...если мне хватит сил и терпения")
    time.sleep(2)
    print("...и если мне не придёт в голову другая безумная идея во время изучения пайтона")

elif yagandon == "3":
    print("...очень информативный ответ, ",name ,".")
    time.sleep(2)
    print("НО Я ЭТО ВСЁ РАВНО СДЕЛАЮ!!!")
    time.sleep(2)
    print("...если мне хватит сил и терпения")
    time.sleep(2)
    print("...и если мне не придёт в голову другая безумная идея во время изучения пайтона")

time.sleep(1)

print("в любом случае пожелай мне удачи! Пока, ",name , "!")
print("завтра доделаю, да ждёт меня програмирование")
time.sleep(5)

    