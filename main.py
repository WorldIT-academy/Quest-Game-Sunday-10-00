import colorama 

colorama.init(True)
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE

while True:
    answer = input("ви прокинулись в лісі, що зробите? (1 - збирати їжу, 2 - знайти укриття)")
    if answer == "1" or answer == "2":
        break
if answer == "1":
    print("ви почали збирати їжу")
    while True:
        answer2 = input("ви знайшли гриб, що зробите? (1 - зібрати їх, 2 - не зібрати)")
        if answer2 == "1" or answer2 == "2":
            break
    if answer2 == "1":
        print("ви зібрали гриби")
        while True:
            answer4 = input("ви зїлі гриб та отруїлісь ващі дії? (1 - зїсті ще 2 - щукати противояд)")
            if answer4 == "1" or answer4 == "2":
                break
        if answer4 == "1":
            print("ві померлі від отрути")
            
        elif answer4 == "2":
            print("ви знайшли противояд та вижили")
            while True:
                answer7 = input("Йти далі (1 - Так 2 - Ні)")
                if answer7== "1" or answer7 == "2":
                    break
            if answer7 == "1":
                print("")
                
            elif answer7 == "2":
                print(" ")
        
    elif answer2 == "2":
        print(" ви не зібрали гриби")
        
elif answer == "2":
    print("ви знайшли печеру ")
    
    while True:
        answer3 = input("Що зробите з печерою? (1 - обладнати, 2 -пропустити печеру)")
        if answer3 == "1" or answer3 == "2":
            break
    if answer3 == "1":
        print("ви обладнали печеру")
        while True:
            answer6 = input("на вас йдуть лоси (1 -сидіти у печері, 2 - йти на зустріч )")
            if answer6 == "1" or answer6 == "2":
                break
        if answer6 == "1":
            print("ви сиділи занадто довго")
            
        elif answer6 == "2":
            print("ви підійшлі дуже блізько до тварин ")
    elif answer3 == "2":
        print("ви пропустили печеру")
        while True:
            answer5 = input("ви йшли і вам на зустріч іде чорній чоловік, (1-втекти, 2-підійти ближче)")
            if answer5 == "1" or answer3 == "2":
                break
        if answer5 == "1":
            print("ви втекли і все впорядку")
            
        elif answer5 == "2":
            print("ви підійшли ближче і game ower")