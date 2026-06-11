x = 0
while x<1:
    x+=1
    import time 
    time.sleep(1)
    print("Мини игра: Чётное- Нечётное")
    time.sleep(1)
    print("Меню!!!!")
    time.sleep(1)
    print("Привет! Это игра Чётное - Нечётное! Выбери сложность!")
    time.sleep(1)
    print("====================================================")
    time.sleep(1)
    print("1-Легкая")
    time.sleep(1)
    print("2-Средняя")
    time.sleep(1)
    print("3-Сложная")
    time.sleep(1)
    print("4-Экстремальная")
    time.sleep(1)
    print("5-Выход")
    time.sleep(1)
    player = int(input("Ваш выбор: "))
    time.sleep(1)
    print("=========================")

if player == 5:
    time.sleep(1)
    print("Вы вышли из игры! Пока!")
    quit()

elif player == 1:
    import random 
    phrases = ("Хорошее число!","Ты мастер!","Имба!","Идеально","У вас хороший вкус!")
    time.sleep(1)

    time.sleep(1)
    print("Привет! Это игра Чётное - нечётное, правила тут простые: пиши любое число, а я тебе скажу его чётность. Тебе будут даваться баллы за это, если наберешь 10 баллов, выиграешь. Удачи! И помни, у тебя только 3 попытки.")
    print("Сложность - легкая")
    print("=====================================================================")
    score = 0
    y = 0
    while y<3:  

        try:
            time.sleep(1)
            play = int(input("Напиши свое число! Твое число: "))
    
            play2 = int(play)
        except:
            print("Ты ввел не число! Ничего страшного! Раунд перезапускается!")
            continue

        if play%2 == 0:

            time.sleep(1)
            print("Прекрасно!! Это чётное число!")
            time.sleep(1)
            print(random.choice(phrases))
        else:
            time.sleep(1)
            print("Хорошо! Это нечётное число")
            time.sleep(1)
            print(random.choice(phrases))

        points = random.randint(1,5)   
        score += points  
        y+=1 
        time.sleep(1)
        print("Ты получил",points,"очков-(а)! Так держать!")
        time.sleep(1)
        print("У тебя сейчас",score,"очков-(а)! Молодец!")

        time.sleep(1)
        ld = input("Продолжить? Да или нет?")
        if ld == "да":
            time.sleep(1)
            print("продолжаем!")
            time.sleep(1)
            print("=========================")

            time.sleep(1)
            print("Раунд",y + 1,"/ 3")
        elif ld == "нет":
            time.sleep(1)
            print("Игра завершена! Пока!")
            time.sleep(1)
            print("Ты накопил",score,"баллов!")
            quit() 

    if ld == "да":
        time.sleep(1)
        print("Сейчас у тебя",score,"очков-(а)")
        time.sleep(1)
        print("Итоги:")
        if score >= 10:
            time.sleep(1)
            print("Молодец!!!! Ты выиграл! Победа твоя!")
        elif score >8 and score <10:
            time.sleep(1)
            print("Ты почти выиграл!")
        else:
            time.sleep(1)
            print("К сожалению ты проиграл. Попробуй еще раз!")
            import sys
            sys.exit()

elif player == 2:
    import random 
    phrases = ("Хм..Интересно","Хороший выбор!","Думаю это очевидно!","Идеально","Прекрасный выбор!")
    time.sleep(1)

    time.sleep(1)
    print("Привет! Это игра Чётное - нечётное, правила тут простые: пиши любое число, а я тебе скажу его чётность. Тебе будут даваться баллы за это, если наберешь 20 баллов, выиграешь. Удачи! И помни, у тебя только 5 попыток.")
    print("Сложность - средняя")
    print("=====================================================================")
    score = 0
    i = 0
    while i<5:
   
        try:
            time.sleep(1)
            play = int(input("Напиши свое число! Твое число: "))
    
            play2 = int(play)
        except:
            print("Ты ввел не число! Ничего страшного! Раунд перезапускается!")
            continue

        if play%2 == 0:

            time.sleep(1)
            print("Ого, это чётное число!")
            time.sleep(1)
            print(random.choice(phrases))
        else:
            time.sleep(1)
            print("Кажетcя это нечётное число!")
            time.sleep(1)
            print(random.choice(phrases))

        points = random.randint(1,5)   
        score += points  
        i+=1 
        time.sleep(1)
        print("Ты получил",points,"очков-(а)! Так держать!")
        time.sleep(1)
        print("У тебя сейчас",score,"очков-(а)! Молодец!")

        time.sleep(1)
        ld = input("Продолжить? Да или нет?")
        if ld == "да":
            time.sleep(1)
            print("продолжаем!")
            time.sleep(1)
            print("=========================")

            time.sleep(1)
            print("Раунд",i + 1,"/ 5")
        elif ld == "нет":
            time.sleep(1)
            print("Игра завершена! Пока!")
            time.sleep(1)
            print("Ты накопил",score,"баллов!")
            quit()

    if ld == "да":
        time.sleep(1)
        print("Сейчас у тебя",score,"очков-(а)")
        time.sleep(1)
        print("Итоги:")
        if score >= 20:
            time.sleep(1)
            print("Молодец!!!! Ты выиграл! Победа твоя!")
        elif score >15 and score <20:
            time.sleep(1)
            print("Ты почти выиграл!")
        else:
            time.sleep(1)
            print("К сожалению ты проиграл. Попробуй еще раз!")
            import sys
            sys.exit()

elif player == 3:
    import random 
    phrases = ("Вот это ты везунчик!","Ого!","Интересно!","Идеально","Имбулька!")
    time.sleep(1)

    time.sleep(1)
    print("Привет! Это игра Чётное - нечётное, правила тут простые: пиши любое число, а я тебе скажу его чётность. Тебе будут даваться баллы за это, если наберешь 46 баллов, выиграешь. Удачи! И помни, у тебя только 10 попыток.")
    print("Сложность - сложная")
    score = 0
    a = 0
    while a<10:
   
        try:
            time.sleep(1)
            play = int(input("Напиши свое число! Твое число: "))
    
            play2 = int(play)
        except:
            print("Ты ввел не число! Ничего страшного! Раунд перезапускается!")
            continue

        if play%2 == 0:

            time.sleep(1)
            print("Скажу: это чётное число!")
            time.sleep(1)
            print(random.choice(phrases))
        else:
            time.sleep(1)
            print("Это это нечётное число!")
            time.sleep(1)
            print(random.choice(phrases))

        points = random.randint(1,6)   
        score += points  
        a+=1 
        time.sleep(1)
        print("Ты получил",points,"очков-(а)! Так держать!")
        time.sleep(1)
        print("У тебя сейчас",score,"очков-(а)! Молодец!")

        time.sleep(1)
        ld = input("Продолжить? Да или нет?")
        if ld == "да":
            time.sleep(1)
            print("продолжаем!")
            time.sleep(1)
            print("=========================")

            time.sleep(1)
            print("Раунд",a + 1,"/ 10")
        elif ld == "нет":
            time.sleep(1)
            print("Игра завершена! Пока!")
            time.sleep(1)
            print("Ты накопил",score,"баллов!")
            quit()

    if ld == "да":
        time.sleep(1)
        print("Сейчас у тебя",score,"очков-(а)")
        time.sleep(1)
        print("Итоги:")
        if score >= 46:
            time.sleep(1)
            print("Молодец!!!! Ты выиграл! Победа твоя!")
        elif score >36 and score <46:
            time.sleep(1)
            print("Ты почти выиграл!")
        else:
            time.sleep(1)
            print("К сожалению ты проиграл. Попробуй еще раз!")
            import sys
            sys.exit()

elif player == 4:
    import random 
    phrases = ("Какое ваше любимое число?","Вы правда мастер!","Желаю вам выиграть!","Прекрасно!","У вас хороший выбор!")
    time.sleep(1)

    time.sleep(1)
    print("Привет! Это игра Чётное - нечётное, правила тут простые: пиши любое число, а я тебе скажу его чётность. Тебе будут даваться баллы за это, если наберешь 70 баллов, выиграешь. Удачи! И помни, у тебя только 15 попыток.")
    print("Сложность - экстремальная")
    score = 0
    b = 0
    while b<15:
   
        try:
            time.sleep(1)
            play = int(input("Напиши свое число! Твое число: "))
    
            play2 = int(play)
        except:
            print("Ты ввел не число! Ничего страшного! Раунд перезапускается!")
            continue

        if play%2 == 0:

            time.sleep(1)
            print("Ты загадал чётное число!")
            time.sleep(1)
            print(random.choice(phrases))
        else:
            time.sleep(1)
            print("Это нечётное число!")
            time.sleep(1)
            print(random.choice(phrases))

        points = random.randint(1,7)   
        score += points  
        b+=1 
        time.sleep(1)
        print("Ты получил",points,"очков-(а)! Так держать!")
        time.sleep(1)
        print("У тебя сейчас",score,"очков-(а)! Молодец!")

        time.sleep(1)
        ld = input("Продолжить? Да или нет?")
        if ld == "да":
            time.sleep(1)
            print("продолжаем!")
            time.sleep(1)
            print("=========================")

            time.sleep(1)
            print("Раунд",b + 1,"/ 15")
        elif ld == "нет":
            time.sleep(1)
            print("Игра завершена! Пока!")
            time.sleep(1)
            print("Ты накопил",score,"баллов!")
            quit()

    if ld == "да":
        time.sleep(1)
        print("Сейчас у тебя",score,"очков-(а)")
        time.sleep(1)
        print("Итоги:")
        if score >= 70:
            time.sleep(1)
            print("Молодец!!!! Ты выиграл! Победа твоя!")
        elif score >55 and score <70:
            time.sleep(1)
            print("Ты почти выиграл!")
        else:
            time.sleep(1)
            print("К сожалению ты проиграл. Попробуй еще раз!")
            import sys
            sys.exit()
