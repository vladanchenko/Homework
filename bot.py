import requests
from bs4 import BeautifulSoup
import telebot

month = ''
number = ''

bot = telebot.TeleBot('1784749415:AAEVEW_YelUTVUhY0FZrD_44OflzNBJ51is')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(func=lambda m: True)
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, ' Давай введем месяц')
        bot.register_next_step_handler(message, reg_month)


def reg_month(message):
    global month
    month = month_check(message.text)
    bot.send_message(message.from_user.id, 'Круто, а теперь давай число ')
    bot.register_next_step_handler(message, reg_number)


def reg_number(message):
    global number
    number = message.text
    question = 'Все ли правильно: ' + '\n' + 'вы ввели месяц: ' + month + ' ' + '\n' + number + '-е число'

    bot.send_message(message.from_user.id, text=question)
    bot.register_next_step_handler(message, callback_worker)


URL = f'https://kakoysegodnyaprazdnik.ru/baza/{month}/{number}'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'accept': '*/*'
}
HOST = f'https://kakoysegodnyaprazdnik.ru/baza/'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    r.encoding = 'utf-8'
    return r


result = ''


def get_content(html):
    global result
    result_lst = []
    soup = BeautifulSoup(html, 'html.parser', )
    items = soup.find_all('div', class_='main')

    for item in items:
        result_lst.append(item.find('span').get_text())
    for i in result_lst:
        result += i
        return result
    return


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        return html


parse()
with open('../result.txt', 'w') as fp:
    fp.write(result)


def month_check(message):
    while True:
        income = message
        if income.lower() == 'январь':
            month = 'yanvar'
            return month
        elif income.lower() == 'февраль':
            month = 'fevral'
            return month

        elif income.lower() == 'март':
            month = 'mart'
            return month

        elif income.lower() == 'апрель':
            month = 'aprel'
            return month

        elif income.lower() == 'май':
            month = 'may'
            return month

        elif income.lower() == 'июнь':
            month = 'iyun'
            return month

        elif income.lower() == 'июль':
            month = 'iyul'
            return month

        elif income.lower() == 'август':
            month = 'avgust'
            return month

        elif income.lower() == 'сентярь':
            month = 'sentyabr'
            return month

        elif income.lower() == 'октябрь':
            month = 'oktyabr'
            return month

        elif income.lower() == 'ноябрь':
            month = 'noyabr'
            return month

        elif income.lower() == 'декабрь':
            month = 'decabr'
            return month
        return


def callback_worker(message):
    if message.text.lower() == "да":
        re = " gotovo " + result
        bot.send_message(message.from_user.id, text=re)


bot.polling(none_stop=True)
