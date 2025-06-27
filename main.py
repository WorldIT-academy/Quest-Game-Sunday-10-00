import colorama 

colorama.init(True)
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
yellow = colorama.Fore.YELLOW
cyan = colorama.Fore.CYAN

while True:
    answer = input(f"Ви прокинулись в лісі, що будете робити? {cyan}(1 - шукати їжу, 2 - знайти укриття)")
    if answer == "1" or answer == "2":
        break
if answer == "1":
    print(f"{yellow}Ви почали шукати їжу")
    while True:
        answer2 = input(f"Ви знайшли гриби, що зробите? {cyan}(1 - зберете їх, 2 - не збиратимите)")
        if answer2 == "1" or answer2 == "2":
            break
    if answer2 == "1":
        print(f"{green}Ви зібрали гриби")
        while True:
            answer4 = input(f"Ви зїли гриб та отруїлісь ваші дії? {cyan}(1 - зїсті ще, 2 - щукати протиотруту)")
            if answer4 == "1" or answer4 == "2":
                break
        if answer4 == "1":
            print(f"{red}Ви померли від отрути")
            
        elif answer4 == "2":
            print(f"{green}Ви знайшли протиотруту та вижили")
            while True:
                answer7 = input(f"Йти далі {cyan}(1 - Так 2 - Ні)")
                if answer7== "1" or answer7 == "2":
                    break
            if answer7 == "1":
                print("Ви вийшли на берег річки, на іншому березі хтось є")
                while True:
                    answer8 = input(f"Що будете робити? {cyan}(1 - Переплисти річку, 2 - Відпочити на березі, 3 - Покликати когось)")
                    if answer8== "1" or answer8 == "2":
                        break
                if answer8 == "1":
                    print(f"{red} Течія була занадто сильна, і вас винесло до водоспаду")
                elif answer8 == "2":
                    print(f"{green}Поки ви спали, поряд пропливав катер. Вас побачили і врятували")
                elif answer8 == "3":
                    print(f"{blue}Незнайомець злякався і утік до лісу")
            elif answer7 == "2":
                print(f"Чому? Вам подобається ліс?.. {red}Ви залишились у лісі на останок життя")
        
    elif answer2 == "2":
        print(f"{red}Ви не зібрали гриби та побачили яблоню ")
        while True:
            answer9 = input(f"Зібрати яблуки? {cyan}(1 - так, 2 - ні)")
            if answer9== "1" or answer9 == "2":
                break
        if answer9 == "1":
            print(f"{yellow}Ви зібрали та зїли ")
        elif answer9 == "2":
            print(f"{red}Ви померли з голоду!!!")
        
elif answer == "2":
    print(f"{blue}Ви знайшли печеру ")
    
    while True:
        answer3 = input(f"Що зробите з печерою? {cyan}(1 - обладнати, 2 -пропустити печеру)")
        if answer3 == "1" or answer3 == "2":
            break
    if answer3 == "1":
        print(f"{yellow}Ви обладнали печеру")
        while True:
            answer6 = input(f"На вас йдуть лосі, що будете робити? {cyan}(1 -сидіти у печері, 2 - йти на зустріч )")
            if answer6 == "1" or answer6 == "2":
                break
        if answer6 == "1":
            print(f"{green}Ви сиділи дуже довго, і вони пішли")
            
        elif answer6 == "2":
            print(f"{red}Ви підійшлі дуже близько до тварин ")
    elif answer3 == "2":
        print(f"{blue}Ви пропустили печеру")
        while True:
            answer5 = input("Ви йшли і вам на зустріч йде чорний чоловік, що будете робити? {cyan}(1 - втекти, 2 - підійти ближче)")
            if answer5 == "1" or answer3 == "2":
                break
        if answer5 == "1":
            print(f"{green}Ви втекли і все впорядку")
            
        elif answer5 == "2":
            print(f"Ви підійшли ближче, і {red}game over")