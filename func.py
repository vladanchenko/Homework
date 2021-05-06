import requests
from bs4 import BeautifulSoup


def month_check(message):
    while True:
        income = input(message)
        if income.lower() == 'январь':
            month = 'yanvar'
            return month
        elif income.lower() == 'февраль':
            month = 'fevral'
            return  month

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

mess_month = "Введите месяц: "
month= month_check(mess_month)

def number_check (message, mon):
    while True:
        income = input(message)
        if income.isdecimal() and mon == 'yanvar' and int(income) >= 1 and int(income) <= 31:
            return income
        if income.isdecimal() and month == 'fevral' and int(income) >= 1 and int(income) <= 28:
            return income
        if income.isdecimal() and month == 'mart' and int(income) >= 1 and int(income) <= 31:
            return income
        if income.isdecimal() and month == 'aprel' and int(income) >= 1 and int(income) <= 30:
            return income
        if income.isdecimal() and month == 'may' and int(income) >= 1 and int(income) <= 31:
            return income
        if income.isdecimal() and month == 'iyun' and int(income) >= 1 and int(income) <= 30:
            return income
        if income.isdecimal() and month == 'iyul' and int(income) >= 1 and int(income) <= 31:
            return income
        if income.isdecimal() and month == 'avgust' and int(income) >= 1 and int(income) <= 31:
            return income
        if income.isdecimal() and month == 'sentyabr' and int(income) >= 1 and int(income) <= 30:
            return income
        if income.isdecimal() and month == 'oktyabr' and int(income) >= 1 and int(income) <= 31:
            return income
        if income.isdecimal() and month == 'noyabr' and int(income) >= 1 and int(income) <= 30:
            return income
        if income.isdecimal() and month == 'decabr' and int(income) >= 1 and int(income) <= 31:
            return income

def dig_check (message):
    while True:
        income = input(message)
        if income.isdecimal() :return int(income)
mess_num = "Enter number: "
number = number_check(mess_num, month)

URL = f'https://kakoysegodnyaprazdnik.ru/baza/{month}/{number}'
HEADERS = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
           'accept': '*/*'
           }
HOST = 'https://kakoysegodnyaprazdnik.ru/baza/'
def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    r.encoding = 'utf-8'
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser', )
    items = soup.find_all('div', class_= 'main')

    base = []
    for item in items:
       base.append(
        item.find('span').get_text()
       )
    for i in base:
        print(i)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')
parse()
r = f'https://kakoysegodnyaprazdnik.ru/baza/{month}/{number}'
print(r)

