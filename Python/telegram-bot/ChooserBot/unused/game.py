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

def update_or_add_player(obj):
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
    if len(userList)>0:
        for i in range(len(userList)): # Обновляем очки, если такой игрок уже есть
            if userList[i][0] == usid:
                userList[i][2] = 0
                userList[i][3] = 0
    return userList

userList = []
userList = read_leaderboard('files/winners.txt') # список победителей

class Player:
    def __init__(self):
        self.shield = 0
        self.maxShield = 50
        self.hp = 100
        self.maxHp = 100
        self.damage = 25
        self.critChance = 3
        self.critProcent = 1.2
        self.items = []
        self.status = "idle"
        self.info = ""

    def attack(self):
        self.status = "attack"
        if enemy.shield>0:
            enemy.shield-=self.damage
        else:
            enemy.hp-=self.damage

    def defend(self):
        self.status = "defend"
        if self.shield>0:
            if randint(0,100)<=game_enemy.critChance:
                self.shield-=int(game_enemy.damage*0.15*game_enemy.critProcent)
            else:
                self.shield-=int(game_enemy.damage*0.15)
        else:
            if randint(0,100)<=game_enemy.critChance:
                self.hp-=int(game_enemy.damage*0.1*game_enemy.critProcent)
            else:
                self.hp-=int(game_enemy.damage*0.1)

    def loot(self, loot0):
        self.status = "loot"
        game_enemy.loot.remove(loot0[0])
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
        self.critProcent = 1.2
        self.items = []

    def attack(self):
        self.status = "attack"
        if player.shield>0:
            player.shield-=self.damage
        else:
            player.hp-=self.damage

    def defend(self):
        self.status = "defend"
        if self.shield>0:
            if randint(0,100)<=game_player.critChance:
                self.shield-=int(game_player.damage*0.15*game_player.critProcent)
            else:
                self.shield-=int(game_player.damage*0.15)
        else:
            if randint(0,100)<=game_player.critChance:
                self.hp-=int(game_player.damage*0.1*game_player.critProcent)
            else:
                self.hp-=int(game_player.damage*0.1)

    def loot(self, loot0):
        self.status = "loot"
        game_enemy.loot.remove(loot0[0])
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
            game_handler[str(message.from_user.id)] = Player()
            userList = update_or_add_player(game_handler[str(message.from_user.id)])
            write_leaderboard(game_handler, 'files/winners.txt')
            keyboard = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.from_user.id, "👋Привяо! Видимо ты уже готов к моей игре, тогда держи 15 вопросов!", reply_markup=keyboard)
            get_question(message)
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
        elif message.text[0:2]!="/s" and message.text != "/reset" and message.text != "Вернуться к вопросам":
            check_question(message)
    except:
        pass
    
def get_enemy(message, boss=False):
    enemy_list = [
        "evil-frog",
        "brain-krot",
        "camerafoot"
    ]
    boss_list = [
        "ghost-knight"
    ]
    if boss==False:
        choose = enemy_list[randint(range(len(enemy_list)))]
    else:
        choose = enemy_list[randint(range(len(boss_list)))]

    game_enemy = Enemy()
    match choose:
        case "evil-frog":
            game_enemy.maxHp = 25
            game_enemy.hp = game_enemy.maxHp
            game_enemy.maxShield = 0
            game_enemy.shield = game_enemy.maxShield
            game_enemy.damage = 5
            game_enemy.critChance = 8
            game_enemy.items = ["heal", "heal"]
        case "brain-krot":
            game_enemy.maxHp = 40
            game_enemy.hp = game_enemy.maxHp
            game_enemy.maxShield = 10
            game_enemy.shield = game_enemy.maxShield
            game_enemy.damage = 7
            game_enemy.critChance = 6
            game_enemy.items = ["addShield", "addShield", "addShield", "addShield", "addShield"]
        case "camerafoot":
            game_enemy.maxHp = 55
            game_enemy.hp = game_enemy.maxHp
            game_enemy.maxShield = 0
            game_enemy.shield = game_enemy.maxShield
            game_enemy.damage = 13
            game_enemy.critChance = 3
            game_enemy.items = []
        case "camerafoot":
            game_enemy.maxHp = 55
            game_enemy.hp = game_enemy.maxHp
            game_enemy.maxShield = 0
            game_enemy.shield = game_enemy.maxShield
            game_enemy.damage = 13
            game_enemy.critChance = 3
            game_enemy.items = []

def enemy_hold(message):
    enemy_choose = False
    if len(game_enemy.loot)>0:
        if game_enemy.loot[0]=="heal" and game_enemy.hp<int(game_enemy.maxHp*0.4):
            enemy_choose = True
            game_enemy.loot("heal")
            if game_enemy.hp>game_enemy.maxHp:
                game_enemy.hp=game_enemy.maxHp
        elif game_enemy.loot[0]=="addShield" and game_enemy.shield<int(game_enemy.maxShield*0.5):
            enemy_choose = True
            game_enemy.loot("addShield")
            if game_enemy.shield>game_enemy.maxShield:
                game_enemy.shield=game_enemy.maxShield
    
    if enemy_choose==False:
        if randint(1,2)==1: # атака
            game_enemy.attack()
        else:
            game_enemy.defend() # защита


def get_hold(message):
    try:
        for i in range(len(userList)): # Обновляем очки, если такой игрок уже есть
            if userList[i][0] == str(message.from_user.id):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                but_attack = telebot.types.KeyboardButton(text="[ АТАКА ]")
                but_defend = telebot.types.KeyboardButton(text="[ ЗАЩИТА ]")
                but_loot = telebot.types.KeyboardButton(text="[ ПРЕДМЕТЫ ]")
                keyboard.add(but_attack, but_defend, but_loot)
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