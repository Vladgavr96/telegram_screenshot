import time

import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

token = "5573275971:AAGlpJ8z7xuy-ozVZIkERLN4e-DYf_E3v9Q"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я скриншотбот. Пришли мне ссылки на страницу которую зайти "
                                      "и я пришлю тебе скриншот")


@bot.message_handler(content_types=['text'])
def screenshot_message(message):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(message.text)
        res = driver.get_screenshot_as_png()
        bot.send_photo(message.chat.id, res, caption=f'URL: {message.text}')
    except:
        bot.send_message(message.chat.id, "Я вас не понял. Возможно ссылка введена неверно или сайт не доступен")

bot.polling()
