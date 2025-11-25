import openpyxl, sqlite3

class Export():
    def import_users():
        df = openpyxl.load_workbook("excel\\user_import.xlsx")
        sheet = df.worksheets[0]

        e_list = []
        
        for i, row in enumerate(sheet): # вниз
            result = []
            if i==0 or row[0].value==None:
                continue

            for i in range(0,4):
                result.append(row[i].value)

            e_list.append(result)

        return e_list
    
    def import_goods():
        df = openpyxl.load_workbook("excel\\Tovar.xlsx")
        sheet = df.worksheets[0]

        e_list = []
        
        for i, row in enumerate(sheet): # вниз
            result = []
            if i==0 or row[0].value==None:
                continue

            for i in range(0,11):
                result.append(row[i].value)

            e_list.append(result)

        return e_list
    
    def import_orders():
        df = openpyxl.load_workbook("excel\\orders_import.xlsx")
        sheet = df.worksheets[0]

        e_list = []
        
        for i, row in enumerate(sheet): # вниз
            result = []
            if i==0 or row[0].value==None:
                continue

            for i in range(0,8):
                result.append(row[i].value)

            e_list.append(result)
        #print(e_list)
        return e_list
    
    def add_to_base_users():
        try:
            e_list = Export.import_users()
            conn = Export.get_base()
            cur = conn.cursor()
            for e in e_list: # Unique сделать логин нужно (сделал)
                cur.execute(
                    """ 
                    INSERT OR IGNORE INTO users(role, fio, login, password) VALUES(?, ?, ?, ?)
                    """,
                    e
                )
            conn.commit()  # Применяем изменения
            conn.close()
        except:
            print("! ! ! ! ОШИБКА БАЗЫ ДАННЫХ")

    def add_to_base_goods():
        try:
            e_list = Export.import_goods()
            conn = Export.get_base()
            cur = conn.cursor()
            for e in e_list: # Unique сделать логин нужно (сделал)
                cur.execute(
                    """ 
                    INSERT OR IGNORE INTO goods(article, name, um, price, provider, maker, category, sale, count, desc, photo_path) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    e
                )
            conn.commit()  # Применяем изменения
            conn.close()
        except:
            print("! ! ! ! ОШИБКА БАЗЫ ДАННЫХ")

    def add_to_base_orders():
        try:
            e_list = Export.import_orders()
            conn = Export.get_base()
            cur = conn.cursor()
            for e in e_list: # Unique сделать логин нужно (сделал)
                cur.execute(
                    """ 
                    INSERT OR IGNORE INTO orders(articles, date_order, date_ready, adress, fio, code, status) VALUES(?, ?, ?, ?, ?, ?, ?)
                    """,
                    e
                )
            conn.commit()  # Применяем изменения
            conn.close()
        except:
            print("! ! ! ! ОШИБКА БАЗЫ ДАННЫХ")

    def get_base():
        conn = sqlite3.connect("database.db")
        return conn