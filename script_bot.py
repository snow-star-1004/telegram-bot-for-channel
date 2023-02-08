from telethon.sync import TelegramClient

from telethon.tl.functions.messages import GetDialogsRequest

from telethon.tl.types import InputPeerEmpty

import time

import os

api_id = 29214446

api_hash = 'b155af7ffaedd6ef1dbc2f68a7f250e9'

phone = '+380951839208'

client = TelegramClient(phone, api_id, api_hash)

client.connect()

if not client.is_user_authorized():

    client.send_code_request(phone)

    client.sign_in(phone, input('Enter the code: '))

chats = []

last_date = None

chunk_size = 200

groups = []

result = client(GetDialogsRequest(

    offset_date=last_date,

    offset_id=0,

    offset_peer=InputPeerEmpty(),

    limit=chunk_size,

    hash=0

))
print(result.chats)

chats.extend(result.chats)

for chat in chats:

    try:

       groups.append(chat)

    except:

        continue

print('Choose a group to scrape members from:')

i = 0

for g in groups:

    print(str(i) + '- ' + g.title)

    i += 1

g_index = input("Enter a Number: ")

target_group = groups[int(g_index)]
flag = ''

while True:
    message = client.get_messages(target_group)

    date_time = message[0].date
    blog = message[0].message

    if(flag != date_time):
        title_directory = target_group.title.replace(' ', '_')
        if (not os.path.exists(title_directory)):
            os.makedirs(title_directory)

        title = title_directory + "/" + str(date_time).replace(' ', '_').replace(':', '').replace('+','_') + '.txt'    

        with open(title, 'w', encoding='utf-8') as f:
            f.write(blog)
        flag = date_time
        print(flag)
    time.sleep(1)
    # if(flag != date_time):
    #     title_directory = target_group.title.replace(' ', '_')
    #     if (not os.path.exists(title_directory)):
    #         os.makedirs(title_directory)

    #     title = title_directory + "/" + title_directory + '.txt'    

    #     if(not os.path.exists(title)):
    #         with open(title, 'w', encoding='utf-8') as f:
    #             f.write(blog)
    #     else:
    #         with open(title) as txt:
    #             lines = txt.readlines()
    #         # print(lines)
    #         # print(type(lines))
    #         lines.append('\n \n')
    #         lines.append(blog)
    #         # print(lines)
    #         with open(title, 'w') as updated_txt:
    #             updated_txt.writelines(lines)
    #     flag = date_time
    #     print(flag)



