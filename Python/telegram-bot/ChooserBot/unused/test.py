import schedule
import time

def my_function():
    print("Функция вызвана!")
    # Здесь можно добавить любую необходимую логику

# Планируем выполнение функции каждые 60 секунд (1 минуту)
schedule.every(1).minutes.do(my_function)

while True:
    schedule.run_pending()
    time.sleep(1)