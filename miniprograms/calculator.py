while True:
    num1 = input("введи первое число или стоп что бы выйти")
    if num1.lower() == "стоп":
        break

    try:
        num1 = float(num1)
    except ValueError:
        print("ну ты еблан что ли")
        continue

    num2 = input("введи второе число или стоп что бы выйти")
    if num2.lower() == "стоп":
        break

    try:
        num2 = float(num2)
    except ValueError:
        print("выкинь клавиатуру в окно пж")
        continue

    opr = input("введи операцию(+,-,*,/) ну или стоп для выхода")
    if opr.lower() == "стоп":
        break
    elif opr == "+":
        print(num1 + num2)
    elif opr == "-":
        print(num1 - num2)
    elif opr == "*":
        print(num1 * num2)
    elif opr == "/":
        if num2 == 0:
            print("ты долбаёб?")
            continue
        print(num1 / num2)
    else:
        print("ты умрёшь и тд.")
        continue
     
        



    
    

    

# opr = input("введи операцию(+,-,*,\) ну или стоп для выхода")
# if opr == "стоп".lower():
#     break
# elif opr == ""

    