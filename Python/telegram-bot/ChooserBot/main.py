import telebot, random, os, schedule, time, threading
from telebot import types # для указание типов

token='7977018450:AAGIXy_phYGd-t24wDjG266m27Yi6HLwxFc'
bot=telebot.TeleBot(token)

def read_leaderboard(file_path):
    try:
        with open(file_path, 'r') as file:
            userList = [line.strip().split() for line in file]
        return userList
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

def write_leaderboard(userList, file_path):
    with open(file_path, 'w') as file:
        for entry in userList:
            fullPath=''
            for entryTwo in entry:
                fullPath+=f"{entryTwo} "
            file.write(f"{fullPath}\n")

def update_or_add_player(usid, name, start, word):
    if len(userList)>0:
        for i in range(len(userList)): # Обновляем очки, если такой игрок уже есть
            if userList[i][0] == usid:
                #userList[i][1] = name
                if start==False:
                    try:
                        if is_integer(word)==False:
                            word = format_word(word)
                            userList[i].append(str(word))
                            #print(userList[i].index(str(word)))
                            userList[i][2] = int(userList[i][2])+1
                            write_leaderboard(userList, 'files/winners.txt')
                    except:
                        pass
                return userList
    userList.append([usid, name, 0, name]) # Если игрока с таким именем нет, добавляем новую запись
    write_leaderboard(userList, 'files/winners.txt')
    return userList

def update_surname(usid, name): # обновление второго имени (любое имя)
    try:
        if len(userList)>0:
                for i in range(len(userList)):
                    if userList[i][0] == usid:
                        userList[i][3] = name
                        write_leaderboard(userList, 'files/winners.txt')
                        return userList
    except:
        pass

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def reset_player(usid, name):
    userList = read_leaderboard('files/winners.txt')
    if len(userList)>0:
        for i in range(len(userList)): # Обновляем очки, если такой игрок уже есть
            if int(userList[i][0]) == int(usid):
                userList[i][1] = str(name)
                userList[i][2] = 0
                #try:
                #    userList[i][0:4]
                #    print(userList[0:4])
                #except:
                #    pass
                write_leaderboard(userList, 'files/winners.txt')

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][2] < arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

userList = []
userList = read_leaderboard('files/winners.txt') # список победителей

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        if message.text == "/start":
            userList = update_or_add_player(str(message.from_user.id), str(message.chat.first_name), True, None)
            keyboard = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.from_user.id, "👋Привяо! Пиши всё что хочешь и каждые 2 часа бот будет повторять всё раннее сказанное!\nПиши всё что угодно!", reply_markup=keyboard)
        #elif message.text[0:8] == "/setname":
        #    print("meow1")
        #    setName = message.text[10:]
        #    fullMessage = ''
        #    if len(userList) > 0:
        #        print("meow2")
        #        update_surname(str(message.from_user.id), str(setName))
        #        bot.send_message(message.from_user.id, text="✅Успешно обновлено")
        #elif message.text[0:2] == "/s" and str(message.from_user.id) == "5366217758": # админ фича
        #    txt = str(message.text)
        #    try:
        #        for i in range(len(userList)):
        #            bot.send_message(userList[i][0], text=txt[3:])
        #    except:
        #        pass
        elif message.text == "/leaders":
            fullMessage = ''
            userList = read_leaderboard('files/winners.txt')  # список победителей
            if len(userList) > 0:
                fullMessage = "👑Вот текущий список лидеров:\n"
                sorted_leaderboard = bubble_sort(userList)
                top_10 = []
                rank = 1
                for i in range(len(sorted_leaderboard)):
                    top_10.append(f"{rank}. {str(sorted_leaderboard[i][1])} | Счёт: {str(sorted_leaderboard[i][2])}")
                    rank += 1
                fullMessage+="\n".join(top_10)
                bot.send_message(message.from_user.id, text=str(fullMessage))
            else:
                fullMessage = "Список лидеров в данный момент пуст :("
                bot.send_message(message.from_user.id, text=fullMessage)
        elif message.text == "/stats":
            #print(len(message.text))
            userList = read_leaderboard('files/winners.txt')  # список победителей
            #if len(message.text)>7:
            #    try:
            #        fullMessage=''
            #        if len(userList)>0:
            #            for i in range(len(userList)):
            #                if userList[i][1] == message.text[5:]:
            #                    fullMessage=(f"Кол-во слов : {len(userList[i])-4} "+"\n")
            #                    for j in range(4, len(userList[i])):
            #                        fullMessage+=(f"- {userList[i][j]}"+"\n")
            #            bot.send_message(message.from_user.id, text=fullMessage)
            #    except:
            #        bot.send_message(message.from_user.id, text="😔Ошибка")
            #else:
            try:
                if len(userList)>0:
                    for i in range(len(userList)):
                        if str(userList[i][0]) == str(message.from_user.id):
                            fullMessage=(f"Кол-во слов : {len(userList[i])-4} "+"\n")
                            for j in range(4, len(userList[i])):
                                fullMessage+=(f"- {userList[i][j]}"+"\n")
                    bot.send_message(message.from_user.id, text=fullMessage)
            except:
                bot.send_message(message.from_user.id, text="😔Ошибка")
        elif message.text == "/get":
            try:
                if len(userList)>1:
                    userNum = random.randint(0,len(userList)-1)
                    while len(userList[userNum])<=4: # проверка есть ли слово
                        userNum= random.randint(0,len(userList))
                    userName = str(userList[userNum][3])
                    word = str(userList[userNum][random.randint(5, len(userList[userNum]))])
                    word = format_word(word)
                    bot.send_message(message.from_user.id, text=word+"\n * от "+userName)
            except:
                pass
        elif message.text == "/reset":
            newList = reset_player(str(message.from_user.id), str(message.chat.first_name))
            bot.send_message(message.from_user.id, text="✅Список слов успешно обнулён")
        elif message.text == "Написать своё сообщение!":
            keyboard = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.from_user.id, text="🥰Пиши", reply_markup=keyboard)
        else:
            save_word(message)
    except:
        pass

def save_word(message):
    if is_integer(message.text)==True:
        bot.send_message(message.from_user.id, text="❌Извините, но только числами нельзя!")
    else:
        userList = update_or_add_player(str(message.from_user.id), str(message.chat.first_name), False, str(message.text))
        #print("save3")
        bot.send_message(message.from_user.id, text="✅Слово успешно добавлено, может вы желаете добавить что-то ещё?")

def get_word(): # отправка сообщения
    try:
        if len(userList)>1:
            userNum = random.randint(0,len(userList)-1)
            while len(userList[userNum])<=4: # проверка есть ли слово
                userNum= random.randint(0,len(userList))
            userName = str(userList[userNum][3])
            word = str(userList[userNum][random.randint(5, len(userList[userNum]))])
            word = format_word(word)
            for i in range(len(userList)):
                bot.send_message(chat_id=userList[i][0], text=word+"\n * от "+userName)
    except:
        pass

def format_word(word):
    word = str(word)
    word = word.replace("[", "")
    word = word.replace("]", "")
    word = word.replace("'", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    return word

def tg_bot():
    bot.polling(none_stop=True, interval=0)

def everyMsg():
    schedule.every(1).hour.do(get_word)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=tg_bot)
    t2 = threading.Thread(target=everyMsg)
    t1.start()
    t2.start()

#schedule.every().day.at("10:00").do(get_word)