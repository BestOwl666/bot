import ctypes
from email import message
import os
import telebot
from telebot import types
import pyautogui
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import subprocess
from dotenv import load_dotenv

load_dotenv()

PROXY_URL = 
bot = Bot(token=os.environ.get('TOKEN'), proxy=PROXY_URL)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('GTA V', callback_data='button1')                   #ЕСТЬ
    button2 = types.InlineKeyboardButton('Скрипт', callback_data='button2')                     #ЕСТЬ
    button3 = types.InlineKeyboardButton('Скриншот', callback_data='screenshot')             #ЕСТЬ
    button4 = types.InlineKeyboardButton('Заблокировать экран', callback_data='button4')     #ЕСТЬ
    button5 = types.InlineKeyboardButton('Перезагрузка', callback_data='button5')            #ЕСТЬ
    button6 = types.InlineKeyboardButton('Разблокировать экран', callback_data='button6')
    button7 = types.InlineKeyboardButton('Выключить', callback_data='button7')               #ЕСТЬ
    markup.add(button1, button2,button3,button4,button5,button6,button7)
    bot.send_message(message.chat.id, 'Выберите кнопку:', reply_markup=markup)


                                                                                #Запустить GTA V!
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button1':
        bot.answer_callback_query(call.id, 'Открытие GTA V')
        pass
        file_path = 'steam://rungameid/271590'
        os.startfile(file_path)

                                                                                #Запустить ЧИТ!
    if call.data == 'button2':
        bot.answer_callback_query(call.id, 'Запуск скрипта')
        pass
        file_path = 'F:\GTA Online/555v7fVFkTzq4JuUmq'
        os.startfile(file_path)

                                                                                #Сделать СКРИН экрана!
    if call.data == 'screenshot':
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        with open('screenshot.png', 'rb') as f:
            bot.send_photo(call.message.chat.id, f)



                                                                                 # Выключить ПК!
    elif call.data == "button7":
        subprocess.run(["shutdown", "/s", "/t", "15"], shell=True)
        bot.answer_callback_query(call.id, "ПК выключается")

                                                                                
                                                                                 # Заблокировать экран!
    if call.data == "button4":
        subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"], shell=True)
        bot.answer_callback_query(call.id, "Экран заблокирован")


                                                                                # Разблокировать экран!
    elif call.data == "button6":
        # Команда для разблокировки экрана в Windows
        subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"], shell=True)
        # Отправляем сообщение об успешном выполнении команды
        bot.answer_callback_query(call.id, "Экран разблокирован")






                                                                                 # Перезагрузить ПК!
    elif call.data == "button5":
        subprocess.run(["shutdown", "/r", "/t", "15"], shell=True)
        bot.answer_callback_query(call.id, "ПК перезагружается")


bot.polling()