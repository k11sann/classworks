import telebot, random
from telebot import types # для указание типов

token='7695499782:AAFR1fzhSXZIkXudQd2MABQwH2DDsSSQy88'
bot=telebot.TeleBot(token)

winnerTxt = open( 'files/winners.txt', 'w' )
winnerList = [] # список победителей
userList = []
questions = [ # все вопросы
    [
        "Когда сидишь что напрягается?",
        "То, на чтом сидишь",
        "Попа",
        1
    ],
    [
        "Что Марат сегодня поел?",
        "Кота",
        "Пельмени со вкусом абрикоса",
        2
    ],
    [
        "Если штаны в говнящке, то трусы в какащке?",
        "Конечно!",
        "Ни в коем случае!",
        1
    ],
    [
        "Тебе нравится этот телеграмм бот?",
        "Оооочень!",
        "Мне не вкатил этот бот",
        2
    ],
    [
        "Айфон или Андройд?",
        "Айфон",
        "Андройд",
        1
    ],
    [
        "Какое молоко круче? Козлячье или Собачье",
        "Козлячье",
        "Собачье",
        1
    ],
    [
        "xD или UwU?",
        "xD",
        "UwU",
        2
    ],
    [
        "Бургер кинг говно",
        "Бургер Кинг говно",
        "Сам говно",
        1
    ]
]

class Quest:
    def __init__(self):
        question = questions[random.randint(0, len(questions)-1)]
        self.quest = question[0]
        self.choose1 = ''
        self.choose2 = ''
        if random.randint(1,2)==1:
          self.choose1 = question[1]
          self.choose2 = question[2]
        else:
          self.choose1 = question[2]
          self.choose2 = question[1]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/start":
        try: # проверка есть ли юзер
          user_found=False  
          for i in range(len(userList)):
             if int(message.from_user.id) == userList[i][0]:
                user_found=True
                break
          if user_found==False: # если не нашёл
            userId = int(message.from_user.id)
            userName = str(message.chat.first_name)
            print(userName)
            answers = 0
            userList.append([userId, userName, answers])
        except IndexError: # если нету, то в лист добавляется
            userId = int(message.from_user.id)
            userName = str(message.chat.first_name)
            print(userName)
            answers = 0
            userList.append([userId, userName, answers])

        keyboard = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Привяо! Видимо ты уже готов к моей игре. Тогда держи вопрос!", reply_markup=keyboard)
        get_question(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    elif message.text == "/leaders":
        fullMessage="Вот текущий список лидеров : \n"
        print(userList)
        for i in range(len(userList)):
          fullMessage+=str(userList[i][1])+" - "+str(userList[i][2])+"\n"
          print(str(userList[i][1])+" - "+str(userList[i][2])+"\n")
        bot.send_message(message.from_user.id, text=fullMessage)
    else:
        check_question(message)
    
def get_question(message):
    q_sys = Quest()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    choose1_but = telebot.types.KeyboardButton(text=q_sys.choose1)
    choose2_but = telebot.types.KeyboardButton(text=q_sys.choose2)
    keyboard.add(choose1_but, choose2_but)
    bot.send_message(message.chat.id, text=str(q_sys.quest), reply_markup=keyboard)

def check_question(message):
    keyboard = telebot.types.ReplyKeyboardRemove()
    quest_found = False
    for i in range(len(questions)):
        winNum = questions[i][3]
        if message.text == questions[i][winNum]:
            bot.send_message(message.from_user.id, text="Ответ оказался правильным!\nСледующий вопрос!", reply_markup=keyboard)
            quest_found=True
            for i in range(len(userList)):
              if int(message.from_user.id) == userList[i][0]:
                userList[i][2]+=1
            break
    if quest_found == False:
        bot.send_message(message.from_user.id, text="Ответ оказался неправильным!\nВ следующий раз будешь внимательней!", reply_markup=keyboard)
    get_question(message)

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True, interval=0)