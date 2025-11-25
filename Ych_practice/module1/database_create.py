import sqlite3

from module_import import Export

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
role TEXT,
fio TEXT,
login TEXT UNIQUE,
password TEXT
)
''')

# Создаем таблицу Goods
cursor.execute('''
CREATE TABLE IF NOT EXISTS Goods (
id INTEGER PRIMARY KEY,
article TEXT UNIQUE,
name TEXT,
um TEXT,
price INTEGER,
provider TEXT,
maker TEXT,
category TEXT,
sale INTEGER,
count INTEGER,
desc TEXT,
photo_path TEXT
)
''')

# Создаем таблицу Orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
id INTEGER PRIMARY KEY,
articles TEXT,
date_order DATE,
date_ready DATE,
adress TEXT,
fio TEXT,
code INTEGER,
status TEXT
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

# Добавляет данные с Excel
Export.add_to_base_users()
Export.add_to_base_goods()
Export.add_to_base_orders()