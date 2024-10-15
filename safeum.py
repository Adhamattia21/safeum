import requests
import random
import os
from user_agent import generate_user_agent
import pyfiglet
import sys
import time
from os import system, name
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps
from websocket import create_connection

# =======================
# Telegram Bot Settings
# =======================
TELEGRAM_API_URL = 'https://api.telegram.org/bot'
TELEGRAM_BOT_TOKEN = '7700841542:AAH8ToiYPfzEKqscB383duw9fUjRfpf5g8Q'
CHAT_ID = '1373461678'

def send_telegram_message(message):
    url = f"{TELEGRAM_API_URL}{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'  # Optional, for formatting
    }
    response = requests.post(url, data=payload)
    return response

# ===========================
# Terminal Color Codes
# ===========================
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
G = '\033[2;36m'
E = '\033[1;31m'
DS = '\033[30m' #رصاصي
V = '\033[1;35m'
U = '\x1b[1;37m'#ابيض

# ===========================
# Script Initialization
# ===========================
os.system('clear')
logo = (f'''{Z}
 4$$c       ""          .$$r
 ^$$$b  @AsiacellI2    e$$$"
 d$$$$$e @MKOOSH   z$$$$$b
4$$$*$$$$$c    .$$$$$*$$$r
 ""    ^*$$$be$$$*"    ^"
          "$$$$"
        .d$$P$$$b
       d$$P   ^$$$b
   .ed$$$"      "$$$be.
 $$$$$$P          *$$$$$$
4$$$$$P            $$$$$$"
 "*$$$"            ^$$P
    ""              ^"
    ''')

print(logo)

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

# ===========================
# WebSocket and Request Setup
# ===========================
failed = 0
success = 0
retry = 0
accounts = []

def work():
    global failed, success, retry
    username = choice('qwertyuiooasdfghjklzxcvpbnm') + ''.join(choices(list('qwertyuioasdfghjklzxcvbnpm1234567890'), k=16))
    try:
        con = create_connection("wss://195.13.182.213/Auth",
                                header={"app": "com.safeum.android", "host": None, "remoteIp": "195.13.182.213",
                                        "remotePort": str(8080), "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                                        "time": "2024-04-11 11:00:00", "url": "wss://51.79.208.190/Auth"},
                                sslopt={"cert_reqs": CERT_NONE})
        con.send(dumps(
            {"action":"Register","subaction":"Desktop","locale":"ar_EG","gmt":"+03","password":{"m1x":"d54bb9dc9d3916a2002e2767af43cd92353c458c54171a47cc8ba502d0d7a338","m1y":"7ece0ab6dfc88dbf68d7d6de016b37c388e1b52e3fd2320c5c83b516d2f4a094","m2":"2c31cd6fd7c7ff633add2a52a197fff2bf65f74e9bec900e25ec669cc432c9f5","iv":"827f3737ef910189cd5020e09590e930","message":"0fc9a9f5d4cc12ed3fc571816098cba8e404fd1e538f3084fe85d9082566f0929ed023e84135074c21c344271714ba24af5f7262696bf4bf6a5aeef27c022e89261e8d62a30f60162ba639fb3d9207b5"},"magicword":{"m1x":"0ae1e8176aca942cf5ae5db82348056637086954abb1e43a8134912299514762","m1y":"b9605265f6f69341fea85bd8451c8f6bc7c603bf1b2c676a7fd1a023966fe881","m2":"6fd9df97bcb34b1c1d1f8da403b965f7a0d1381ee1bb35052778eb9745a67053","iv":"0ba2b1199a30e56732bb5be92cb71902","message":"79d067c011ba1f13e2bebeb6bb53d127"},"magicwordhint":"0000","login":str(username),"devicename":"INFINIX Infinix X678B","softwareversion":"1.1.0.2300","nickname":"MKOOSH","os":"AND","deviceuid":"4b81ce4e8c8208f4","devicepushuid":"*dvjMiSQhREelXsRqPYqrNa:APA91bG6VEVUfHhfjwY4Cpc5Slh8HpjXwKaG2_R7ubjBP1D1rrMS--r1iZhAEVdk9K2wArezDO3TDWWU5_MOvWWm4wz7oH-Qqa4uQjnuTrHGOzniuLMipI1e2vS91eQ8CHfVKNUqrzXv","osversion":"and_13.0.0","id":"1707376691"}))
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            accounts.append(username + ':foxr')
            print(f"Success: {username}")
            with open('SafeUM.txt', 'a') as f:
                f.write(username + '\n')
            # Send username to Telegram
            send_telegram_message(f"{username}")
        else:
            failed += 1
    except Exception as e:
        print(f"Exception: {e}")
        retry += 1

# ===========================
# Main Execution Loop
# ===========================
start = ThreadPoolExecutor(max_workers=1000)

while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + 'Success : ' + str(success) + '\n\n\n' + ' ' * 25 + 'Failed : ' + str(
        failed) + '\n\n\n' + ' ' * 25 + 'ReTry : ' + str(retry))
    hh = str(failed) + str(success) + str(retry)
    if int(success) >= 2990:
        print("Created Acc successfully")
        
    if int(success) > int(0):
        z = "\n".join(accounts)
        print("CREATED ACCOUNTS>>\n", z)
        
    os.system('clear')