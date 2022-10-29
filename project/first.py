def get_req(req):
    if "расп" in req.lower():
        hold()
    elif "трен" in req.lower():
        trainer()
    elif "плат" in req.lower():
        many()
    elif "або" in req.lower():
        abo()
    elif "одежд" in req.lower():
        things()
    else:
        print("Не можем понять Вас, пожалуйста, проверьте правильность написания запроса.")

def hold():
    print("Пн - 13.00, "
          "Вт - 11.00, "
          "Пт - 10.00. ")


def trainer():
    print("Контактные данные тренера: Иванов Сергей Алексеевич +7 (998) 935 00 00.")


def many():
    print("Пробное занятие стоит 150 рублей,"
          "разовое посещение 1000 рублей.")


def abo():
    a = int(input("Сколько раз в месяц, Вы хотели бы заниматься?" + "\n"))
    if 1 <= a and a <= 4:
        print("Предлагаю Вам light абонемент!")
    elif 5 <= a and a <= 9:
        print("Предлагаю Вам strong абонемент!")
    else:
        print("Вам поможет администратор в студии.")

def things():
    print("Возьмите любую спортивную, удобную для Вас одежду.")