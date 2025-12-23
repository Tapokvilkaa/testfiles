import colorama

while True:
    user_input = input("Введите число (или 'стоп' для выхода): ")
    
    if user_input.lower() == 'стоп':
        print(colorama.Fore.GREEN + "Выход из программы. Пока!" + colorama.Style.RESET_ALL)
        break
    

    try:
        number = int(user_input)
    except ValueError:
        print(colorama.Style.BRIGHT + colorama.Fore.RED + "Ошибка! Пожалуйста, введите целое число или 'стоп'." + colorama.Style.RESET_ALL)
        continue
    
    
    if number % 2 == 0:
        print(colorama.Style.DIM + colorama.Fore.BLUE + f"Число {number} чётное!" + colorama.Style.RESET_ALL)
    else:
        print(colorama.Style.DIM + colorama.Fore.RED + f"Число {number} нечётное!" + colorama.Style.RESET_ALL)