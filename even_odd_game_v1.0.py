import time
import random 
phrases = ("Хм..Интересно","Хороший выбор!","Думаю это очевидно!","Идеально","Прекрасный выбор!")
time.sleep(1)
print("Привет! Это игра Чётное - нечётное, правила тут простые: пиши любое число, а я тебе скажу его чётность. Тебе будут даваться баллы за это, если наберешь 20 баллов, выиграешь. Удачи! И помни, у тебя только 5 попыток.")
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
