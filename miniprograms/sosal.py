
otvet = ""
while otvet not in ["да", "Да", "дА", "ДА"]:
    otvet = input("сосал?")
    if otvet not in ["да", "Да", "дА", "ДА"]:
        print("да ну, не верю")
    else:
        break
    

print("правильно;)")