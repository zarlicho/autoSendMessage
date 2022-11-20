from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetInlineBotResultsRequest
from telethon import TelegramClient, events
from telethon import TelegramClient, events, sync
import colorama
from colorama import Fore, Back, Style
from random import randint
from time import sleep
import csv
colorama.init(autoreset=True)
api_id = '16093788'
api_hash = '1f8acac96faeb96d4f095360e9f74760'
phone = '+60146333803'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

groups=[]
i=0
channel = "19375432"
psn = []

while True:
    for group in client.iter_dialogs():
        if "HAHA ESPORT" in group.title:
            psn = group.message.message
        if group.is_group:
            i+=1
            groups.append(group)
            # send message to group
            try:
                if i==5:
                    print(Fore.LIGHTGREEN_EX+"[+] "+Fore.RED+"stoping")
                    sleep(randint(10,100))
                    i=0
                print(Fore.LIGHTGREEN_EX+"[+] "+Fore.RESET+"Sending message to "+Fore.YELLOW+ group.title)
                client.send_message(group.id, psn)
                sleep(randint(1,6))
            except Exception as e:
                print(e)
                
client.start()
client.run_until_disconnected()
