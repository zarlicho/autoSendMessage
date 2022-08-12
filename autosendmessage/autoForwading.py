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
api_id = '17691195'
api_hash = '5dc315d015c6b7907cf682756d7b6a4a'
phone = '+6287879012895'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

chats = []
last_date = None
chunk_size = 200
groups=[]
bot = []
i=0
channel = "19375432"
# get all channels
channel_username = 'nessC'# your channel
groupUsername = "JOSS ALERT"# your group
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
                sleep(1)
            except Exception as e:
                print(e)
                
client.start()
client.run_until_disconnected()
