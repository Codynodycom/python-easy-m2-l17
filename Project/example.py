# ЗАВИСИМОСТИ
from translate import Translator


# ФУНКЦИИ
def is_correct_language(user_selected_language):
    # проверка на корректность ввода
    for i in '012345':
        if user_selected_language == i:
            return True
    return False 


def translate_message(message, language):
    if language=='0':
        config= Translator(
          to_lang="en", 
          from_lang="ru"
        ) # ru_to_e
    elif language == '1':
        translated_text= Translator(
          to_lang="de", 
          from_lang="ru"
        ) # ru_to_deu
    elif language == '2':
        config= Translator(
          to_lang="ru", 
          from_lang="en"
        ) # en_to_rus
    elif language == '3':
        config= Translator(
          to_lang="de", 
          from_lang="en"
        ) # en_to_deu
    elif language == '4':
        config= Translator(
          to_lang="ru", 
          from_lang="de"
        ) # deu_to_ru
    elif language == '5':
        config= Translator(
          to_lang="en", 
          from_lang="de"
        ) # deu_to_en

    ans = config.translate(message)
    return ans


# ПЕРЕМЕННЫЕ И ОБЪЕКТЫ
languages = '''Выберите переводчик:
[0] - русско-агнглийский
[1] - русско-немецкий
[2] - англо-русский
[3] - англо-немецкий
[4] - немецко-русский
[5] - немецко-английский'''

user_selected_language = input(languages + '\n>>>')

# проверка на корректность ввода языка
while not is_correct_language(user_selected_language):
    print('Такого языка нет.')
    user_selected_language = input(languages + '\n>>>')

is_working = True


# ГЛАВНЫЙ ЦИКЛ
while is_working:
    user_message = input('\nВведите текст для перевода:\n')

    # выключаем цикл в случае команды off
    if user_message == 'off':
      is_working = False
      break

    # отправляем текст на перевод и выводим полученный результат на экран
    translate_text = translate_message(user_message, user_selected_language)
    print('Перевод:', translate_text)

# главный цикл
