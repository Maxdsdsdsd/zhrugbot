# -*- coding: utf-8 -*-
import vk
import random
import time
import configparser
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
    print('(если вы пригласили бота в первую беседу то айди 1,')
    print('если во вторую беседу то айди 2 и т.д)')
    print('Введите айди беседы:')
    idbesedi = input()
    print('Введите тайм аут отправки сообщений (от 0.1 до 99999999):')
    timeoutinput = input()
    timeoutinput = int(float(timeoutinput))
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
    print('(если вы пригласили бота в первую беседу то айди 1,')
    print('если во вторую беседу то айди 2 и т.д)')
    print('Введите айди беседы:')
    idbesedi = input()
    print('Введите тайм аут отправки сообщений (от 0.1 до 99999999):')
    timeoutinput = input()
    timeoutinput = int(float(timeoutinput))
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
    config.read("settings.ini")
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
        print('[INFO] Пресет загружен!')
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
        
        print('[INFO] Пресет загружен!')
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
    
