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
phone = '+6287879012524'
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

print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.RESET + 'pilih text midnight atau night: ', end="")
text = input("")

pesanMid = """📹𝑺𝑪𝑹𝑰𝑴 𝑳𝑰𝑽𝑬 𝑹𝑴 𝟯 •
📹𝑺𝑪𝑹𝑰𝑴 𝑳𝑰𝑽𝑬 𝑹𝑴 𝟯 •


‼️𝟱 𝑺𝑳𝑶𝑻 𝑳𝑬𝑭𝑻(𝑴𝑰𝑫𝑵𝑰𝑮𝑯𝑻)‼️

‼️𝟱 𝑺𝑳𝑶𝑻 𝑳𝑬𝑭𝑻(𝑴𝑰𝑫𝑵𝑰𝑮𝑯𝑻)‼️


        🎥 🔥𝐀𝐃𝐀 𝐋𝐈𝐕𝐄🔥🎥
             (𝐃𝐄𝐋𝐀𝐘 𝟐 𝐌𝐈𝐍𝐈𝐓) 

࿔⊰━━━━━༺❦༻━━━━━⊱࿔ 
        𝐌𝐈𝐃𝐍𝐈𝐆𝐇𝐓 𝐋𝐈𝐕𝐄 𝐒𝐂𝐑𝐈𝐌 
             𝐁𝐘 𝐇𝐀𝐇𝐀 𝐄𝐒𝐏𝐎𝐑𝐓
࿔⊰━━━━━༺❦༻━━━━━⊱࿔
       
      😱 𝐓𝐎𝐏🥇🥈𝐈𝐍𝐕𝐈𝐓𝐄𝐃 
                𝐍𝐄𝐗𝐓 𝐒𝐂𝐑𝐈𝐌😱


🎥🄻🄸🅅🄴 🄸🄽 🄵🄰🄲🄴🄱🄾🄾🄺🎥

     
🗓𝐇𝐀𝐑𝐈 : 𝙆𝙃𝘼𝙈𝙄𝙎
🗓𝐓𝐀𝐑𝐈𝐊𝐇 : 𝟭𝟭 𝐀𝐔𝐆𝐔𝐒𝐓 𝟮𝟬𝟮𝟮

💵𝟷 𝚂𝙻𝙾𝚃 (𝚁𝙼𝟹) 😱
💵𝟸 𝚂𝙻𝙾𝚃 (𝚁𝙼𝟻) 😱

𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐕𝐈𝐀⤵️⤵️
✅𝐎𝐍𝐋𝐈𝐍𝐄 𝐓𝐑𝐀𝐍𝐒𝐅𝐄𝐑
✅𝐓𝐎𝐔𝐂𝐇 𝐀𝐍𝐃 𝐆𝐎
✅𝐒𝐇𝐎𝐏𝐄𝐄𝐏𝐀𝐘
✅𝐓𝐎𝐏𝐔𝐏 𝐑𝐌𝟓 (𝟏 𝐒𝐋𝐎𝐓)
❌𝐔𝐂
．．．．．．．．．．．

𝐁𝐎𝐎𝐊 𝐒𝐋𝐎𝐓 𝐂𝐋𝐈𝐂𝐊 𝐋𝐈𝐍𝐊
⤵️⤵️⤵️⤵️⤵️⤵️
(𝐀𝐃𝐌𝐈𝐍 𝟏) 
https://wa.me/601136677311?text=Live𝐌𝐈𝐃𝐍𝐈𝐆𝐇𝐓rm3

(𝐀𝐃𝐌𝐈𝐍 𝟐) 
https://wa.me/601125388959?text=Live𝐌𝐈𝐃𝐍𝐈𝐆𝐇𝐓rm3
⤴️⤴️⤴️⤴️⤴️⤴️
𝐁𝐎𝐎𝐊 𝐒𝐋𝐎𝐓 𝐂𝐋𝐈𝐂𝐊 𝐋𝐈𝐍𝐊
．．．．．．．．．．．

🔊🄱🄴🄽🄴🄵🄸🅃🅂🔊
     👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻
💎ᴛᴏᴘ 🥇🥈ɪɴᴠɪᴛᴇᴅ ɴᴇxᴛ ꜱᴄʀɪᴍ
💎ᴇ-ᴄᴇʀᴛɪꜰɪᴄᴀᴛᴇ 🥇🥈🥉
💎ᴀᴅᴠᴀɴᴄᴇ ʀᴏᴏᴍ
💎3× ʟᴏᴏᴛ 
💎ᴢᴏɴᴇ ꜱʜʀɪɴᴋ 1.2
💎ᴠᴀᴜɢᴇ ɪɴꜰᴏ (ᴏɴ) 
💎ꜱᴠ & ᴀᴀ (ᴏɴ) 
💎ꜰᴀꜱᴛ ʀᴇꜱᴜʟᴛ

🔊🅁🅄🄻🄴🅂🔊
    👇🏻👇🏻👇🏻👇🏻
✅ ᴘᴍᴘʟ ꜱ2 ᴘᴏɪɴᴛ ꜱʏꜱᴛᴇᴍ
✅ ᴛʀɪᴏ/ꜱQᴜᴀᴅ ᴏɴʟʏ
✅ ꜱꜱ ʀᴇꜱᴜʟᴛ ꜰᴏʀ ʙᴀᴄᴋᴜᴘ ᴏɴʟʏ
✅ ᴛᴇᴍʙᴀᴋ ᴋᴏᴛᴀᴋ (ᴛᴀᴜɴᴛɪɴɢ) 
✅ 16 - 19 ꜱʟᴏᴛ
❌ꜱᴏʟᴏ/ᴅᴜᴏ (-10)
❌ʜᴀᴄᴋᴇʀ (ᴅQ) 
❌ɴᴏ ᴇᴍᴜʟᴀᴛᴏʀ (ᴅQ)
❌ᴡʀᴏɴɢ ꜱʟᴏᴛ (-10)
❌ɴᴏ ʀᴇꜰᴜɴᴅ


🎑𝗠𝗜𝗗ɴɪɢʜᴛ🎑
🕘ᴏᴘᴇɴ ʀᴏᴏᴍ:12.40am
🚀ꜰʟʏ:12.47am


 🗺️𝐃𝐄𝐓𝐀𝐈𝐋 𝐌𝐀𝐏𝐒 🗺️
⛺𝗥𝗢𝗨𝗡𝗗 𝟭 - 𝗘𝗥𝗔𝗡𝗚𝗟𝗘
🌋𝗥𝗢𝗨𝗡𝗗 𝟮 - 𝗠𝗜𝗥𝗔𝗠𝗔𝗥
🏕️𝗥𝗢𝗨𝗡𝗗 𝟯 - 𝗦𝗔𝗡𝗛𝗢𝗞
🌋𝗥𝗢𝗨𝗡𝗗 𝟰 - 𝗠𝗜𝗥𝗔𝗠𝗔𝗥
⛺𝗥𝗢𝗨𝗡𝗗 𝟱 - 𝗘𝗥𝗔𝗡𝗚𝗟𝗘

⏰𝐂𝐇𝐄𝐂𝐊 𝐈𝐍 : 𝐀𝐅𝐓𝐄𝐑 𝐖𝐖𝐂𝐃 
✈️ 𝐅𝐋𝐘: 7 𝐌𝐈𝐍𝐒 𝐀𝐅𝐓𝐄𝐑 𝐎𝐏𝐄𝐍

．．．．．．．．．．．

📹🅂🄲🅁🄸🄼 🄶🅁🄾🅄🄿 🄸🄽🄵🄾📹
                      𝐕𝟐
https://chat.whatsapp.com/KXIRJuDuXitEJdN5PenlYp"""
pesanNight = """📹𝑺𝑪𝑹𝑰𝑴 𝑳𝑰𝑽𝑬 𝑹𝑴 𝟯 •
📹𝑺𝑪𝑹𝑰𝑴 𝑳𝑰𝑽𝑬 𝑹𝑴 𝟯 •


‼️𝟱 𝑺𝑳𝑶𝑻 𝑳𝑬𝑭𝑻(𝑵𝑰𝑮𝑯𝑻)‼️

‼️𝟭𝟬 𝑺𝑳𝑶𝑻 𝑳𝑬𝑭𝑻(𝑴𝑰𝑫𝑵𝑰𝑮𝑯𝑻)‼️


        🎥 🔥𝐀𝐃𝐀 𝐋𝐈𝐕𝐄🔥🎥
              (𝐃𝐄𝐋𝐀𝐘 𝟐 𝐌𝐈𝐍𝐈𝐓) 

࿔⊰━━━━━༺❦༻━━━━━⊱࿔ 
           𝐍𝐈𝐆𝐇𝐓 & 𝐌𝐈𝐃𝐍𝐈𝐆𝐇𝐓
               𝐋𝐈𝐕𝐄 𝐒𝐂𝐑𝐈𝐌 𝐁𝐘         
                𝐇𝐀𝐇𝐀 𝐄𝐒𝐏𝐎𝐑𝐓
࿔⊰━━━━━༺❦༻━━━━━⊱࿔
       
      😱 𝐓𝐎𝐏🥇🥈𝐈𝐍𝐕𝐈𝐓𝐄𝐃 
                𝐍𝐄𝐗𝐓 𝐒𝐂𝐑𝐈𝐌😱

 
🎥🄻🄸🅅🄴 🄸🄽 🄵🄰🄲🄴🄱🄾🄾🄺🎥


🗓𝐇𝐀𝐑𝐈 : 𝙆𝙃𝘼𝙈𝙄𝙎
🗓𝐓𝐀𝐑𝐈𝐊𝐇 : 𝟭𝟭 𝐀𝐔𝐆𝐔𝐒𝐓 𝟮𝟬𝟮𝟮

💵𝟷 𝚂𝙻𝙾𝚃 (𝚁𝙼𝟹) 😱
💵𝟸 𝚂𝙻𝙾𝚃 (𝚁𝙼𝟻) 😱
💵𝙽𝙸𝙶𝙷𝚃 & 𝙼𝙸𝙳𝙽𝙸𝙶𝙷𝚃 (𝚁𝙼𝟻) 😱😱

𝐏𝐀𝐘𝐌𝐄𝐍𝐓 𝐕𝐈𝐀⤵️⤵️
✅𝐎𝐍𝐋𝐈𝐍𝐄 𝐓𝐑𝐀𝐍𝐒𝐅𝐄𝐑
✅𝐓𝐎𝐔𝐂𝐇 𝐀𝐍𝐃 𝐆𝐎
✅𝐒𝐇𝐎𝐏𝐄𝐄𝐏𝐀𝐘
✅𝐓𝐎𝐏𝐔𝐏 𝐑𝐌𝟓 (𝟏 𝐒𝐋𝐎𝐓)
❌𝐔𝐂
．．．．．．．．．．．

𝐁𝐎𝐎𝐊 𝐒𝐋𝐎𝐓 𝐂𝐋𝐈𝐂𝐊 𝐋𝐈𝐍𝐊
⤵️⤵️⤵️⤵️⤵️⤵️
(𝐀𝐃𝐌𝐈𝐍 𝟏) 
https://wa.me/601136677311?text=Live𝐍𝐈𝐆𝐇𝐓rm3

https://wa.me/601136677311?text=Live𝐌𝐈𝐃𝐍𝐈𝐆𝐇𝐓rm3


(𝐀𝐃𝐌𝐈𝐍 𝟐) 
https://wa.me/601125388959?text=Live𝐍𝐈𝐆𝐇𝐓rm3

https://wa.me/601125388959?text=Live𝐌𝐈𝐃𝐍𝐈𝐆𝐇𝐓rm3
⤴️⤴️⤴️⤴️⤴️⤴️
𝐁𝐎𝐎𝐊 𝐒𝐋𝐎𝐓 𝐂𝐋𝐈𝐂𝐊 𝐋𝐈𝐍𝐊
．．．．．．．．．．．

🔊🄱🄴🄽🄴🄵🄸🅃🅂🔊
     👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻
💎ᴛᴏᴘ 🥇🥈ɪɴᴠɪᴛᴇᴅ ɴᴇxᴛ ꜱᴄʀɪᴍ
💎ᴇ-ᴄᴇʀᴛɪꜰɪᴄᴀᴛᴇ 🥇🥈🥉
💎ᴀᴅᴠᴀɴᴄᴇ ʀᴏᴏᴍ
💎3× ʟᴏᴏᴛ 
💎ᴢᴏɴᴇ ꜱʜʀɪɴᴋ 1.2
💎ᴠᴀᴜɢᴇ ɪɴꜰᴏ (ᴏɴ) 
💎ꜱᴠ & ᴀᴀ (ᴏɴ) 
💎ꜰᴀꜱᴛ ʀᴇꜱᴜʟᴛ

🔊🅁🅄🄻🄴🅂🔊
    👇🏻👇🏻👇🏻👇🏻
✅ ᴘᴍᴘʟ ꜱ2 ᴘᴏɪɴᴛ ꜱʏꜱᴛᴇᴍ
✅ ᴛʀɪᴏ/ꜱQᴜᴀᴅ ᴏɴʟʏ
✅ ꜱꜱ ʀᴇꜱᴜʟᴛ ꜰᴏʀ ʙᴀᴄᴋᴜᴘ ᴏɴʟʏ
✅ ᴛᴇᴍʙᴀᴋ ᴋᴏᴛᴀᴋ (ᴛᴀᴜɴᴛɪɴɢ) 
✅ 16 - 19 ꜱʟᴏᴛ
❌ꜱᴏʟᴏ/ᴅᴜᴏ (-10)
❌ʜᴀᴄᴋᴇʀ (ᴅQ) 
❌ɴᴏ ᴇᴍᴜʟᴀᴛᴏʀ (ᴅQ)
❌ᴡʀᴏɴɢ ꜱʟᴏᴛ (-10)
❌ɴᴏ ʀᴇꜰᴜɴᴅ


🌠ɴɪɢʜᴛ🌠
🕘ᴏᴘᴇɴ ʀᴏᴏᴍ: 8.50pm
🚀ꜰʟʏ:8.57pm

🎑𝗠𝗜𝗗ɴɪɢʜᴛ🎑
🕘ᴏᴘᴇɴ ʀᴏᴏᴍ:12.40am
🚀ꜰʟʏ:12.47am


 🗺️𝐃𝐄𝐓𝐀𝐈𝐋 𝐌𝐀𝐏𝐒 🗺️
⛺𝗥𝗢𝗨𝗡𝗗 𝟭 - 𝗘𝗥𝗔𝗡𝗚𝗟𝗘
🌋𝗥𝗢𝗨𝗡𝗗 𝟮 - 𝗠𝗜𝗥𝗔𝗠𝗔𝗥
🏕️𝗥𝗢𝗨𝗡𝗗 𝟯 - 𝗦𝗔𝗡𝗛𝗢𝗞
🌋𝗥𝗢𝗨𝗡𝗗 𝟰 - 𝗠𝗜𝗥𝗔𝗠𝗔𝗥
⛺𝗥𝗢𝗨𝗡𝗗 𝟱 - 𝗘𝗥𝗔𝗡𝗚𝗟𝗘

⏰𝐂𝐇𝐄𝐂𝐊 𝐈𝐍 : 𝐀𝐅𝐓𝐄𝐑 𝐖𝐖𝐂𝐃 
✈️ 𝐅𝐋𝐘: 7 𝐌𝐈𝐍𝐒 𝐀𝐅𝐓𝐄𝐑 𝐎𝐏𝐄𝐍

．．．．．．．．．．．

📹🅂🄲🅁🄸🄼 🄶🅁🄾🅄🄿 🄸🄽🄵🄾📹
                        𝐕𝟐 
https://chat.whatsapp.com/KXIRJuDuXitEJdN5PenlYp"""

while True:
    for group in client.iter_dialogs():
        if group.is_group:
            i+=1
            groups.append(group)
            try:
                if i==5:
                    print(Fore.LIGHTGREEN_EX+"[+] "+Fore.RED+"stoping")
                    sleep(randint(10,100))
                    i=0
                print(Fore.LIGHTGREEN_EX+"[+] "+Fore.RESET+"Sending message to "+Fore.YELLOW+ group.title)
                if text == "mid":
                    client.send_message(group.id, pesanMid)
                elif text == "night":
                    client.send_message(group.id, pesanNight)
                else:
                    print(Fore.RED+"[-] "+Fore.RESET+"error")
                sleep(1)
            except Exception as e:
                print(e)

client.start()
client.run_until_disconnected()
