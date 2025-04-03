import telebot, random, os
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
            file.write(f"{entry[0]} {entry[1]} {entry[2]} {entry[3]}\n")

def update_or_add_player(usid, name, update):
    if len(userList)>0:
        for i, entry in enumerate(userList): # Обновляем очки, если такой игрок уже есть
            if userList[i][0] == usid:
                userList[i][1] = name
                if update==True:
                    userList[i][2] = int(userList[i][2])+1
                userList[i][3] = int(userList[i][3])+1
                return userList
    userList.append([usid, name, 0, 0]) # Если игрока с таким именем нет, добавляем новую запись
    return userList

def reset_player(usid, name):
    print("sex2")
    if len(userList)>0:
        for i in range(len(userList)): # Обновляем очки, если такой игрок уже есть
            if userList[i][0] == usid:
                userList[i][2] = 0
                userList[i][3] = 0
    return userList

userList = []
userList = read_leaderboard('files/winners.txt') # список победителей

questions = [ # все вопросы
    [
        "Когда сидишь что напрягается?",
        "👆То, на чтом сидишь",
        "🍑Попа",
        2
    ],
    [
        "Что Марат сегодня поел?",
        "🐈Кота",
        "🥟Пельмени со вкусом абрикоса",
        2
    ],
    [
        "Если штаны в говнящке, то трусы в какащке?",
        "😆Конечно!",
        "😒Ни в коем случае!",
        1
    ],
    [
        "https://t.me/tarntoxicwaste/8259",
        "Да",
        "Хыххыы)",
        1
    ],
    [
        "Тебе нравится этот телеграмм бот?",
        "🤩Оооочень!",
        "😤Мне не вкатил этот бот",
        1
    ],
    [
        "Айфон или Андройд?",
        "🍎Айфон",
        "👾Андройд",
        2
    ],
    [
        "Какое молоко круче? Козлячье или Собачье",
        "🐐Козлячье",
        "🐩Собачье",
        1
    ],
    [
        "xD или UwU?",
        "xD",
        "UwU",
        2
    ],
    [
        "🍔Бургер кинг говно",
        "🤝Бургер Кинг говно",
        "😡Сам говно",
        2
    ],
    [
        "Сосал?",
        "😰С-с-сосал..~",
        ". . .",
        1
    ],
    [
        "Кто из них фурри?",
        "😏Покемоны",
        "🦔Соники",
        1
    ],
    [
        "Какой вид спорта предполагает использование ракеток и мяча?",
        "Шахматы",
        "Теннис",
        2
    ],
    [
        "Какое из этих животных является млекопитающим?",
        "🦈Акула",
        "🐬Дельфин",
        2
    ],
    [
        "Было 15 кириловичей\nВ комнату зашёл Виталий Аи\nСколько было оргий, если могут принимать участие только 3-я\n и не должны учавствовать те которые уже были?",
        "🔞105 оргий",
        "🍅42 помидор",
        1
    ],
    [
        "Как называется столица Франции?",
        "📊Берлин",
        "📊Париж",
        2
    ],
]

class Quest:
    def __init__(self, x0):
        question = questions[x0]
        self.quest = question[0]
        self.choose1 = question[1]
        self.choose2 = question[2]

class Player:
    def __init__(self):
        self.shield = 0
        self.maxShield = 50
        self.hp = 100
        self.maxHp = 100
        self.damage = 25
        self.critChance = 3
        self.items = []

    def attack(self):
        if enemy.shield>0:
            enemy.shield-=self.damage
        else:
            enemy.hp-=self.damage

    def defend(self):
        if enemy.shield>0:
            enemy.shield-=self.damage*0.5
        else:
            enemy.hp-=self.damage*0.5

    def loot(self, loot0):
        match loot0[0]:
            case "damage":
                self.damage+=int(loot0[1])
            case "heal":
                self.hp+=int(loot0[1])
            case "maxHp":
                self.hp=self.maxHp
            case "setMaxHp":
                self.maxHp+=int(loot0[1])
            case "addShield":
                self.shield+=int(loot0[1])
            case "addCrit":
                self.critChance+=int(loot0[1])

class Enemy:
    def __init__(self):
        self.shield = 0
        self.maxShield = 50
        self.hp = 100
        self.maxHp = 100
        self.damage = 25
        self.critChance = 3
        self.items = []

    def attack(self):
        if player.shield>0:
            player.shield-=self.damage
        else:
            player.hp-=self.damage

    def defend(self):
        if player.shield>0:
            player.shield-=self.damage*0.5
        else:
            player.hp-=self.damage*0.5

    def loot(self, loot0):
        match loot0[0]:
            case "damage":
                self.damage+=int(loot0[1])
            case "heal":
                self.hp+=int(loot0[1])
            case "maxHp":
                self.hp=self.maxHp
            case "setMaxHp":
                self.maxHp+=int(loot0[1])
            case "addShield":
                self.shield+=int(loot0[1])
            case "addCrit":
                self.critChance+=int(loot0[1])

game_player = Player()
game_enemy = Enemy()

game_handler = {}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        if message.text == "/start":
            userList = update_or_add_player(str(message.from_user.id), str(message.chat.first_name), False)
            write_leaderboard(userList, 'files/winners.txt')
            keyboard = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.from_user.id, "👋Привяо! Видимо ты уже готов к моей игре, тогда держи 15 вопросов!", reply_markup=keyboard)
            get_question(message)
        elif message.text[0:2] == "/s" and str(message.from_user.id) == "5366217758":
            txt = str(message.text)
            try:
                for i in range(len(userList)):
                    bot.send_message(userList[i][0], text=txt[3:])
            except:
                pass
        elif message.text == "/leaders":
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back_but = telebot.types.KeyboardButton(text="Вернуться к вопросам")
            keyboard.add(back_but)
            fullMessage=''
            userList = read_leaderboard('files/winners.txt') # список победителей
            if len(userList)>0:
                fullMessage="👑Вот текущий список лидеров : \n"
                sorted_leaderboard = sorted(userList, key=lambda x: int(x[2]), reverse=True)
                for rank, (player_id, name, score, sex) in enumerate(sorted_leaderboard, start=1):
                    name+="           "
                    name = name[0:8]
                    fullMessage+=(f"{rank}. {name} | Счёт: {score}"+"\n")
            else:
                fullMessage="Список лидеров в данный момент пуст :("
            bot.send_message(message.from_user.id, text=fullMessage, reply_markup=keyboard)
        elif message.text == "/reset":
            print("sex1")
            newList = reset_player(str(message.from_user.id), str(message.chat.first_name))
            print("sex3")
            write_leaderboard(newList, 'files/winners.txt')
            get_question(message)
        elif message.text == "Вернуться к вопросам":
            get_question(message)
        elif message.text[0:2]!="/s" and message.text != "/reset":
            check_question(message)
    except:
        pass
    
def get_question(message):
    try:
        for i in range(len(userList)): # Обновляем очки, если такой игрок уже есть
            if userList[i][0] == str(message.from_user.id):
                q_sys = Quest(int(userList[i][3]))
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                choose1_but = telebot.types.KeyboardButton(text=q_sys.choose1)
                choose2_but = telebot.types.KeyboardButton(text=q_sys.choose2)
                keyboard.add(choose1_but, choose2_but)
                bot.send_message(message.chat.id, text=str(q_sys.quest), reply_markup=keyboard)
    except:
        keyboard = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text="😔К сожалению вопросы закончились. Но на этом мы ещё не прощаемся! \nРасскажу тебе кое какой секретик :)\nЕсли написать /leaders, то можно посмотреть \nрезультаты других опросников, также и свои! \nА написав /reset можно начать всё с начала!", reply_markup=keyboard)

def check_question(message):
    keyboard = telebot.types.ReplyKeyboardRemove()
    foundNum = 0
    userList = read_leaderboard('files/winners.txt') # список победителей
    for i in range(len(userList)): # ищет пользователя в массиве
        if userList[i][0] == int(message.from_user.id):
            foundNum=i
            break
    if int(userList[foundNum][3]) <= len(questions): # если меньше 15 то задаёт вопрос
        quest_found = False
        for i in range(len(questions)):
            winNum = questions[i][3]
            if message.text == questions[i][winNum]:
                bot.send_message(message.from_user.id, text="✅Ответ оказался правильным!\nСледующий вопрос!", reply_markup=keyboard)
                userList = update_or_add_player(str(message.from_user.id), str(message.chat.first_name), True)
                write_leaderboard(userList, 'files/winners.txt')
                quest_found=True
                break
        if quest_found == False:
            bot.send_message(message.from_user.id, text="❌Ответ оказался неправильным!\nВ следующий раз будешь внимательней!", reply_markup=keyboard)
            userList = update_or_add_player(str(message.from_user.id), str(message.chat.first_name), False)
            write_leaderboard(userList, 'files/winners.txt')
    get_question(message) # новый вопрос

bot.polling(none_stop=True, interval=0)