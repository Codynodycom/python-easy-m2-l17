# зависимости
import datetime


# функции (до и после функций - 2 отступа)
def get_date_time():
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time()

    current_date = str(current_date)
    current_time = str(current_time)[:-7]

    return current_date, current_time

def start_dialog():
    ...

def open_webpage(name):
    ...

def choose_game():
    ...

def start_game_numbers():
    ...

def start_game_words():
    ...

def open_shop():
    ...

def recomendation_function():
    ...


# переменные и объекты
working = True
date, time = get_date_time()

print('Сегодня ' + date)
print('Бот запущен в ' + time)
print()


user_input = input('Привет! Как у тебя дела?' + '\n>>>')
# главный цикл
while working is True:
    # Отступ между сообщениями в диалоге
    print()
    # Переменная ответа ботом
    message_from_bot = ''

    # Проверка пользовательского ввода и создание реакции
    if user_input == 'хорошо':
        message_from_bot = 'И у меня отлично! Какие планы на сегодня?'
    elif user_input == 'который час?':
        # Получаем дату и время
        date, time = get_date_time()
        # Записываем ответ
        message_from_bot = 'Сейчас ' + time
    else:
        message_from_bot = 'Лучше спроси меня о чем-нибудь ещё :)'

    # Отправляем ответ бота и получаем данные от пользователя
    user_input = input(message_from_bot + '\n>>>')

    # Выключение бота
    if user_input == 'off':
        working = False


print('До скорых встреч!')
