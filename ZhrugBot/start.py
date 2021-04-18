# -*- coding: utf-8 -*-
import vk
import random
import time
import configparser
import json
import pyfiglet
from pyfiglet import Figlet

rndid = random.randint(0, 200000000)
rnd1 = random.randint(0, 10)

def defaultraid():
    print('Получить токен: vkhost.github.io')
    print('Введите токен группы:')
    tokeninput = input()
    session = vk.Session(access_token=tokeninput)
    vk_api = vk.API(session)
    print('Введите сообщение для спама (1):')
    msg1input = input()
    print('Введите сообщение для спама (2):')
    msg2input = input()
    print('Введите сообщение для спама (3):')
    msg3input = input()
    print('Получить айди стикера: vk.com/id_stickera')
    print('Введите айди стикера для спама (1):')
    sticker1input = input()
    print('Введите айди стикера для спама (2):')
    sticker2input = input()
    print('Введите название кнопки для клавиатуры: (1)')
    keybbut1input = input()
    print('Введите название кнопки для клавиатуры: (2)')
    keybbut2input = input()
    print('Введите название кнопки для клавиатуры: (3)')
    keybbut3input = input()
    print('Введите название кнопки для клавиатуры: (4)')
    keybbut4input = input()
    print('Введите название кнопки для клавиатуры: (5)')
    keybbut5input = input()
    print('Введите название кнопки для клавиатуры: (6)')
    keybbut6input = input()
    print('(primary - синий цвет, secondary - белый цвет, negative - красный цвет, positive - зеленый цвет)')
    print('Введите цвет кнопки: (1)')
    keycolor1input = input()
    print('Введите цвет кнопки: (2)')
    keycolor2input = input()
    print('Введите цвет кнопки: (3)')
    keycolor3input = input()
    print('Введите цвет кнопки: (4)')
    keycolor4input = input()
    print('Введите цвет кнопки: (5)')
    keycolor5input = input()
    print('Введите цвет кнопки: (6)')
    keycolor6input = input()
    keyboard = {
        "one_time": False,
        "buttons": [
          [
            {
                "action": {
                    "type": "text",
                    "label": keybbut1input,
                    "payload": ""
            },
            "color": keycolor1input
            },
            {
                "action": {
                    "type": "text",
                    "label": keybbut2input,
                    "payload": ""
            },
        "color": keycolor2input
          }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "label": keybbut3input,
                    "payload": ""
            },
        "color": keycolor3input
          },
            {
                "action": {
                    "type": "text",
                    "label": keybbut4input,
                    "payload": ""
            },
        "color": keycolor4input
          }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "label": keybbut5input,
                    "payload": ""
            },
        "color": keycolor5input
          },
            {
                "action": {
                    "type": "text",
                    "label": keybbut6input,
                    "payload": ""
            },
        "color": keycolor6input
            }
          ]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    print('(если вы пригласили бота в первую беседу то айди 1,')
    print('если во вторую беседу то айди 2 и т.д)')
    print('Введите айди беседы:')
    idbesedi = input()
    print('Введите тайм аут отправки сообщений (от 0.1 до 99999999):')
    timeoutinput = input()
    timeoutinput = int(float(timeoutinput))
    keybrnd = random.randint(0, 200000000)
    vk_api.messages.send(chat_id=idbesedi, message='​⠀​', keyboard=keyboard, random_id=keybrnd, v=5.45)
    while True:
        rndid1 = random.randint(0, 200000000)
        rndid2 = random.randint(0, 200000000)
        rndid3 = random.randint(0, 200000000)
        rndid4 = random.randint(0, 200000000)
        rndid5 = random.randint(0, 200000000)
        time.sleep(timeoutinput)
        print("[INFO] Отправлено сообщение 1!")
        vk_api.messages.send(chat_id=idbesedi, message=msg1input, random_id=rndid1, v=5.92)
        time.sleep(timeoutinput)
        print("[INFO] Отправлено сообщение 2!")
        vk_api.messages.send(chat_id=idbesedi, message=msg2input, random_id=rndid2, v=5.92)
        time.sleep(timeoutinput)
        print("[INFO] Отправлено сообщение 3!")
        vk_api.messages.send(chat_id=idbesedi, message=msg3input, random_id=rndid3, v=5.92)
        time.sleep(timeoutinput)
        print("[INFO] Отправлен стикер 1!")
        vk_api.messages.send(chat_id=idbesedi, sticker_id=sticker1input, random_id=rndid4, v=5.92)
        time.sleep(timeoutinput)
        print("[INFO] Отправлен стикер 2!")
        vk_api.messages.send(chat_id=idbesedi, sticker_id=sticker2input, random_id=rndid5, v=5.92)
        time.sleep(timeoutinput)

   
def multipleraid():
    print('Получить токен: vkhost.github.io')
    print('Введите токен группы (1):')
    token1input = input()
    session1 = vk.Session(access_token=token1input)
    vk_api1 = vk.API(session1)
    print('Введите токен группы (2):')
    token2input = input()
    session2 = vk.Session(access_token=token2input)
    vk_api2 = vk.API(session2)
    print('Введите сообщение для спама (1):')
    msg1input = input()
    print('Введите сообщение для спама (2):')
    msg2input = input()
    print('Введите сообщение для спама (3):')
    msg3input = input()
    print('Получить айди стикера: vk.com/id_stickera')
    print('Введите айди стикера для спама (1):')
    sticker1input = input()
    print('Введите айди стикера для спама (2):')
    sticker2input = input()
    print('Введите название кнопки для клавиатуры: (1)')
    keybbut1input = input()
    print('Введите название кнопки для клавиатуры: (2)')
    keybbut2input = input()
    print('Введите название кнопки для клавиатуры: (3)')
    keybbut3input = input()
    print('Введите название кнопки для клавиатуры: (4)')
    keybbut4input = input()
    print('Введите название кнопки для клавиатуры: (5)')
    keybbut5input = input()
    print('Введите название кнопки для клавиатуры: (6)')
    keybbut6input = input()
    print('(primary - синий цвет, secondary - белый цвет, negative - красный цвет, positive - зеленый цвет)')
    print('Введите цвет кнопки: (1)')
    keycolor1input = input()
    print('Введите цвет кнопки: (2)')
    keycolor2input = input()
    print('Введите цвет кнопки: (3)')
    keycolor3input = input()
    print('Введите цвет кнопки: (4)')
    keycolor4input = input()
    print('Введите цвет кнопки: (5)')
    keycolor5input = input()
    print('Введите цвет кнопки: (6)')
    keycolor6input = input()
    keyboard = {
        "one_time": False,
        "buttons": [
          [
            {
                "action": {
                    "type": "text",
                    "label": keybbut1input,
                    "payload": ""
            },
            "color": keycolor1input
            },
            {
                "action": {
                    "type": "text",
                    "label": keybbut2input,
                    "payload": ""
            },
        "color": keycolor2input
          }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "label": keybbut3input,
                    "payload": ""
            },
        "color": keycolor3input
          },
            {
                "action": {
                    "type": "text",
                    "label": keybbut4input,
                    "payload": ""
            },
        "color": keycolor4input
          }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "label": keybbut5input,
                    "payload": ""
            },
        "color": keycolor5input
          },
            {
                "action": {
                    "type": "text",
                    "label": keybbut6input,
                    "payload": ""
            },
        "color": keycolor6input
            }
          ]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    print('(если вы пригласили бота в первую беседу то айди 1,')
    print('если во вторую беседу то айди 2 и т.д)')
    print('Введите айди беседы:')
    idbesedi = input()
    print('Введите тайм аут отправки сообщений (от 0.1 до 99999999):')
    timeoutinput = input()
    timeoutinput = int(float(timeoutinput))
    keybrnd = random.randint(0, 200000000)
    vk_api1.messages.send(chat_id=idbesedi, message='​⠀​', keyboard=keyboard, random_id=keybrnd, v=5.45)
    while True:
        rndid1 = random.randint(0, 200000000)
        rndid2 = random.randint(0, 200000000)
        rndid3 = random.randint(0, 200000000)
        rndid4 = random.randint(0, 200000000)
        rndid5 = random.randint(0, 200000000)
        time.sleep(timeoutinput)
        print("[INFO] Отправлено сообщение 1! (1 и 2)")
        vk_api1.messages.send(chat_id=idbesedi, message=msg1input, random_id=rndid1, v=5.92)
        vk_api2.messages.send(chat_id=idbesedi, message=msg1input, random_id=rndid1, v=5.92)
        time.sleep(timeoutinput)
        print("[INFO] Отправлено сообщение 2! (1 и 2)")
        vk_api1.messages.send(chat_id=idbesedi, message=msg2input, random_id=rndid2, v=5.92)
        vk_api2.messages.send(chat_id=idbesedi, message=msg2input, random_id=rndid2, v=5.92)
        time.sleep(timeoutinput)
        print("[INFO] Отправлено сообщение 3! (1 и 2)")
        vk_api1.messages.send(chat_id=idbesedi, message=msg3input, random_id=rndid3, v=5.92)
        vk_api2.messages.send(chat_id=idbesedi, message=msg3input, random_id=rndid3, v=5.92)
        time.sleep(timeoutinput)
        print("[INFO] Отправлен стикер 1! (1 и 2)")
        vk_api1.messages.send(chat_id=idbesedi, sticker_id=sticker1input, random_id=rndid4, v=5.92)
        vk_api2.messages.send(chat_id=idbesedi, sticker_id=sticker1input, random_id=rndid4, v=5.92)
        time.sleep(timeoutinput)
        print("[INFO] Отправлен стикер 2! (1 и 2)")
        vk_api1.messages.send(chat_id=idbesedi, sticker_id=sticker2input, random_id=rndid5, v=5.92)
        vk_api2.messages.send(chat_id=idbesedi, sticker_id=sticker2input, random_id=rndid5, v=5.92)
        time.sleep(timeoutinput)
    
def loadpreset():
    config = configparser.ConfigParser()
    config.read("settings.ini", encoding='utf-8')
    typer = config["preset"]["type"]
    typer = int(typer)
    if typer == 1:
        token = config["preset"]["token"]
        msg1r = config["preset"]["msg1"]
        msg2r = config["preset"]["msg2"]
        msg3r = config["preset"]["msg3"]
        sk1 = config["preset"]["stickerid1"]
        sk1 = int(sk1)
        sk2 = config["preset"]["stickerid2"]
        sk2 = int(sk2)
        idbes = config["preset"]["idbes"]
        idbes = int(idbes)
        timeot = config["preset"]["timeout"]
        ses1 = vk.Session(access_token=token)
        vk_api1 = vk.API(ses1)
        timeot = int(float(timeot))
        buttontext1 = config["keyboard"]["buttontext1"]
        buttontext2 = config["keyboard"]["buttontext2"]
        buttontext3 = config["keyboard"]["buttontext3"]
        buttontext4 = config["keyboard"]["buttontext4"]
        buttontext5 = config["keyboard"]["buttontext5"]
        buttontext6 = config["keyboard"]["buttontext6"]
        buttoncolor1 = config["keyboard"]["buttoncolor1"]
        buttoncolor2 = config["keyboard"]["buttoncolor2"]
        buttoncolor3 = config["keyboard"]["buttoncolor3"]
        buttoncolor4 = config["keyboard"]["buttoncolor4"]
        buttoncolor5 = config["keyboard"]["buttoncolor5"]
        buttoncolor6 = config["keyboard"]["buttoncolor6"]
        keyboard1 = {
            "one_time": False,
            "buttons": [
            [
                {
                    "action": {
                        "type": "text",
                        "label": buttontext1,
                        "payload": ""
                },
                "color": buttoncolor1
                },
                {
                    "action": {
                        "type": "text",
                        "label": buttontext2,
                        "payload": ""
                },
            "color": buttoncolor2
            }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": buttontext3,
                        "payload": ""
                },
            "color": buttoncolor3
            },
                {
                    "action": {
                        "type": "text",
                        "label": buttontext4,
                        "payload": ""
                },
            "color": buttoncolor4
            }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": buttontext5,
                        "payload": ""
                },
            "color": buttoncolor5
            },
                {
                    "action": {
                        "type": "text",
                        "label": buttontext6,
                        "payload": ""
                },
            "color": buttoncolor6
                }
            ]
            ]
        }
        keyboard1 = json.dumps(keyboard1, ensure_ascii=False).encode('utf-8')
        keyboard1 = str(keyboard1.decode('utf-8'))
        print('[INFO] Пресет загружен!')
        keybrnd = random.randint(0, 200000000)
        vk_api1.messages.send(chat_id=idbes, message='​⠀​', keyboard=keyboard1, random_id=keybrnd, v=5.45)
        while True:
            rndid1 = random.randint(0, 200000000)
            rndid2 = random.randint(0, 200000000)
            rndid3 = random.randint(0, 200000000)
            rndid4 = random.randint(0, 200000000)
            rndid5 = random.randint(0, 200000000)
            time.sleep(timeot)
            print("[INFO] Отправлено сообщение 1!")
            vk_api1.messages.send(chat_id=idbes, message=msg1r, random_id=rndid1, v=5.92)
            time.sleep(timeot)
            print("[INFO] Отправлено сообщение 2!")
            vk_api1.messages.send(chat_id=idbes, message=msg2r, random_id=rndid2, v=5.92)
            time.sleep(timeot)
            print("[INFO] Отправлено сообщение 3!")
            vk_api1.messages.send(chat_id=idbes, message=msg3r, random_id=rndid3, v=5.92)
            time.sleep(timeot)
            print("[INFO] Отправлен стикер 1!")
            vk_api1.messages.send(chat_id=idbes, sticker_id=sk1, random_id=rndid4, v=5.92)
            time.sleep(timeot)
            print("[INFO] Отправлен стикер 2!")
            vk_api1.messages.send(chat_id=idbes, sticker_id=sk2, random_id=rndid5, v=5.92)
            time.sleep(timeot)
    if typer == 2:
        token1 = config["preset"]["token11"]
        token2 = config["preset"]["token21"]
        msg1r = config["preset"]["msg11"]
        msg2r = config["preset"]["msg21"]
        msg3r = config["preset"]["msg31"]
        sk1 = config["preset"]["stickerid11"]
        sk1 = int(sk1)
        sk2 = config["preset"]["stickerid21"]
        sk2 = int(sk2)
        idbes = config["preset"]["idbes1"]
        idbes = int(idbes)
        timeot = config["preset"]["timeout1"]
        ses1 = vk.Session(access_token=token1)
        vk_api1 = vk.API(ses1)
        ses2 = vk.Session(access_token=token2)
        vk_api2 = vk.API(ses2)
        timeot = int(float(timeot))
        buttontext1 = config["keyboard"]["buttontext1"]
        buttontext2 = config["keyboard"]["buttontext2"]
        buttontext3 = config["keyboard"]["buttontext3"]
        buttontext4 = config["keyboard"]["buttontext4"]
        buttontext5 = config["keyboard"]["buttontext5"]
        buttontext6 = config["keyboard"]["buttontext6"]
        buttoncolor1 = config["keyboard"]["buttoncolor1"]
        buttoncolor2 = config["keyboard"]["buttoncolor2"]
        buttoncolor3 = config["keyboard"]["buttoncolor3"]
        buttoncolor4 = config["keyboard"]["buttoncolor4"]
        buttoncolor5 = config["keyboard"]["buttoncolor5"]
        buttoncolor6 = config["keyboard"]["buttoncolor6"]
        keyboard1 = {
            "one_time": False,
            "buttons": [
            [
                {
                    "action": {
                        "type": "text",
                        "label": buttontext1,
                        "payload": ""
                },
                "color": buttoncolor1
                },
                {
                    "action": {
                        "type": "text",
                        "label": buttontext2,
                        "payload": ""
                },
            "color": buttoncolor2
            }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": buttontext3,
                        "payload": ""
                },
            "color": buttoncolor3
            },
                {
                    "action": {
                        "type": "text",
                        "label": buttontext4,
                        "payload": ""
                },
            "color": buttoncolor4
            }
            ],
            [
                {
                    "action": {
                        "type": "text",
                        "label": buttontext5,
                        "payload": ""
                },
            "color": buttoncolor5
            },
                {
                    "action": {
                        "type": "text",
                        "label": buttontext6,
                        "payload": ""
                },
            "color": buttoncolor6
                }
            ]
            ]
        }
        keyboard1 = json.dumps(keyboard1, ensure_ascii=False).encode('utf-8')
        keyboard1 = str(keyboard1.decode('utf-8'))
        print('[INFO] Пресет загружен!')
        keybrnd = random.randint(0, 200000000)
        vk_api1.messages.send(chat_id=idbes, message='​⠀​', keyboard=keyboard1, random_id=keybrnd, v=5.45)
        while True:
            rndid1 = random.randint(0, 200000000)
            rndid2 = random.randint(0, 200000000)
            rndid3 = random.randint(0, 200000000)
            rndid4 = random.randint(0, 200000000)
            rndid5 = random.randint(0, 200000000)
            time.sleep(timeot)
            print("[INFO] Отправлено сообщение 1! (1 и 2)")
            vk_api1.messages.send(chat_id=idbes, message=msg1r, random_id=rndid1, v=5.92)
            vk_api2.messages.send(chat_id=idbes, message=msg1r, random_id=rndid1, v=5.92)
            time.sleep(timeot)
            print("[INFO] Отправлено сообщение 2! (1 и 2)")
            vk_api1.messages.send(chat_id=idbes, message=msg2r, random_id=rndid2, v=5.92)
            vk_api2.messages.send(chat_id=idbes, message=msg2r, random_id=rndid2, v=5.92)
            time.sleep(timeot)
            print("[INFO] Отправлено сообщение 3! (1 и 2)")
            vk_api1.messages.send(chat_id=idbes, message=msg3r, random_id=rndid3, v=5.92)
            vk_api2.messages.send(chat_id=idbes, message=msg3r, random_id=rndid3, v=5.92)
            time.sleep(timeot)
            print("[INFO] Отправлен стикер 1! (1 и 2)")
            vk_api1.messages.send(chat_id=idbes, sticker_id=sk1, random_id=rndid4, v=5.92)
            vk_api2.messages.send(chat_id=idbes, sticker_id=sk1, random_id=rndid4, v=5.92)
            time.sleep(timeot)
            print("[INFO] Отправлен стикер 2! (1 и 2)")
            vk_api1.messages.send(chat_id=idbes, sticker_id=sk2, random_id=rndid5, v=5.92)
            vk_api2.messages.send(chat_id=idbes, sticker_id=sk2, random_id=rndid5, v=5.92)
            time.sleep(timeot)
        
    

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('ZhrugBot'))
print("by vk.com/habader")
print("")
print("1 - Обычный режим")
print("2 - С несколькоми сообществами режим")
print("3 - Загрузить пресет")

check1 = input()

if check1 == "1":
    defaultraid()
if check1 == "2":
    multipleraid()
if check1 == "3":
    loadpreset()
    
