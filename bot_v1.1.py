from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload
import vk_api
import random
import datetime
from datetime import timedelta
import pyowm
from time import sleep as my_sleep
import json
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from options import *

token = vk_token

vk = vk_api.VkApi(token=token)

vk._auth_token()

def Weather_request(body_request):

    if body_request.find("погода") != -1:
        if len(body_request) > 6:
            return True
        else:
            return False
    else:
        return False

def get_link(number_of_city, search_request):
    opts = Options()
    opts.headless = True

    driver = webdriver.Firefox(executable_path=r'P:\Bot VK v3\lib\geckodriver.exe', options=opts) # Невидимый
    #driver = webdriver.Firefox(executable_path=r'P:\Bot VK v3\lib\geckodriver.exe') # Видимый

    driver.get("https://world-weather.ru/search/")

    elem = driver.find_element_by_name("city")
    elem.send_keys(str(search_request))
    my_sleep(2)

    menu_res = driver.find_elements_by_class_name("ui-menu-item")
    menu_res[number_of_city-1].click()
    my_sleep(2)

    url = driver.current_url

    driver.close()
    return url

def find_city_name(search_request):
    opts = Options()
    opts.headless = True

    driver = webdriver.Firefox(executable_path=r'P:\Bot VK v3\lib\geckodriver.exe', options=opts) # Невидимый
    #driver = webdriver.Firefox(executable_path=r'P:\Bot VK v3\lib\geckodriver.exe') # Видимый

    driver.get("https://world-weather.ru/search/")

    elem = driver.find_element_by_name("city")
    elem.send_keys(str(search_request))
    my_sleep(2)

    results_a = driver.find_elements_by_class_name("complit-a")
    results_b = driver.find_elements_by_class_name("complit-b")
    city_names = ""

    for i in range(len(results_a)):
        city_names += str(i + 1) + " " + results_a[i].text + "\n" + results_b[i].text + "\n\n"
    
    driver.close()
    return city_names

def Find_number(str_input):
    index_begin = -1
    index_end = -1
    for i in range(len(str_input)):
        if str_input[i:i + 1].isdigit():
            index_begin = i
            break
    if index_begin != -1:
        index_end = str_input.find(" ", index_begin)
        if index_end != -1:
            str_digit = str_input[index_begin:index_end]
        else:
            str_digit = str_input[index_begin:]
        number = int(str_digit)
        return number
    else:
        return -1

def Hello_request(body_request):
    Hello_Requests = ["здарова", "привет", "приветик", "приветствую", "хай", "хэллоу", "дороу", "здорова"]
    for i in range(len(Hello_Requests)):
        if body_request == Hello_Requests[i]:
            return True
    return False
            
def Hello_responce():
    Hello_Responces = ["Привет, Семпай &#10084;", "Приветик :3"]
    responce = Hello_Responces[random.randint(0, len(Hello_Responces) - 1)]
    return responce

###### Аниме Санка Рэа

def Anime_Sanka_request(body_request):
    Anime_Sanka_requests = ["sankarea", "санка рея", "санка реа", "санка рэя", "санка рэа", "санкарэа", "санкареа", "санкарея", "sanka rea"]
    for i in range(len(Anime_Sanka_requests)):
        if body_request.find(Anime_Sanka_requests[i]) != -1:
            return True
    return False

def Anime_Sanka_responce(body_request):
    Anime_Sanka_responces = ["video-11300549_163603339","video-11300549_163150080", "video-11300549_163156681", "video-11300549_163210305","video-11300549_163246078","video-11300549_163384093","video-11300549_163384106","video-11300549_163485050","video-11300549_163506870","video-11300549_163507866","video-11300549_163532800","video-11300549_163618115","video-11300549_163684243"]
    number_series = Find_number(body_request)
    if number_series != -1:
        if number_series > (len(Anime_Sanka_responces)):
            responce = str(number_series) + " серии нет"
            return responce
        else:
            return Anime_Sanka_responces[number_series - 1]
    else: 
        responce = "Я не понимаю, какая серия тебе нужна, пиши серию цифрой\nНапример:\nСанка рэа 1 серия"
        return responce

######

def Vaguely_responce():
    Vaguely_responces = ["На такое я не знаю ответа", "video237973448_456241662", "Я не понимаю о чём вы говорите"]
    responce = Vaguely_responces[random.randint(0, len(Vaguely_responces) - 1)]
    return responce

def Goodbye_request(body_request):
    Goodbye_requests = ["пока", "до встречи", "до свидания", "я ушёл", "ухожу", "мне нужно идти", "я ушёл", "я ушла"]
    for i in range(len(Goodbye_requests)):
        if body_request == Goodbye_requests[i]:
            return True
    return False

def Goodbye_responce():
    Goodbye_responces = ["Удачи, Сэмпай &#10084;", "Пока пока", "video237973448_456241668"]
    responce = Goodbye_responces[random.randint(0, len(Goodbye_responces) - 1)]
    return responce

def Compliments_request(body_request):
    Compliments_requests = ["ты такая милая", "милашка", "ты супер", "заботливая", "ты превосходна", "ты такая заботливая", "ты милая", "ты милашка", "ты такая классная"]
    for i in range(len(Compliments_requests)):
        if body_request == Compliments_requests[i]:
            return True
    return False

def Compliments_responce():
    Compliments_responces = ["video237973448_456239589", "video237973448_456239653", "photo-188080798_457239019"]
    responce = Compliments_responces[random.randint(0, len(Compliments_responces) - 1)]
    return responce

def Thanks_request(body_request):#
    Thanks_requests = ["спасибо", "пасибо", "благодарю", "спасибо большое", "выручила"]
    for i in range(len(Thanks_requests)):
        if body_request == Thanks_requests[i]:
            return True
    return False

def Thanks_responce():
    Thanks_responces = ["Рада помочь ^^", "Всегда рада помочь ^^", "Обращайся"]
    responce = Thanks_responces[random.randint(0, len(Thanks_responces) - 1)]
    return responce

def Morning_request(body_request):
    Morning_requests = ["утречка", "доброе утро", "доброго утра", "утро", "утра", "утречко"]
    for i in range(len(Morning_requests)):
        if body_request == Morning_requests[i]:
            return True
    return False

def Morning_responce():
    Morning_responces = ["video237973448_456239601", "Доброе утречко &#10084;", "Доброе утро :3"]
    responce = Morning_responces[random.randint(0, len(Morning_responces) - 1)]
    return responce

def Night_request(body_request):
    Night_requests = ["доброй ночи", "ночки", "спокойной ночи", "спокойной", "сладких снов", "сладких"]
    for i in range(len(Night_requests)):
        if body_request == Night_requests[i]:
            return True
    return False

def Night_responce():
    Night_responces = ["Сладких снов &#10084;", "Доброй ночи, Сэмпай &#10084;", "Ночки :3", "video237973448_456239972"]
    responce = Night_responces[random.randint(0, len(Night_responces) - 1)]
    return responce

def get_weather_2(url):
    headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, 'lxml')
    night_temperature = soup.find('tr', class_='night').find('td', class_='weather-temperature').find('span').text
    morning_temperature = soup.find('tr', class_='morning').find('td', class_='weather-temperature').find('span').text
    day_temperature = soup.find('tr', class_='day').find('td', class_='weather-temperature').find('span').text
    evening_temperature = soup.find('tr', class_='evening').find('td', class_='weather-temperature').find('span').text

    night_status = soup.find('tr', class_='night').find('td', class_='weather-temperature').find('div').get('title') # Состояние
    morning_status = soup.find('tr', class_='morning').find('td', class_='weather-temperature').find('div').get('title')
    day_status = soup.find('tr', class_='day').find('td', class_='weather-temperature').find('div').get('title')
    evening_status = soup.find('tr', class_='evening').find('td', class_='weather-temperature').find('div').get('title')
    
    respond = "Утром " + morning_temperature + " " + morning_status + "\n" + "Днём " + day_temperature + " " + day_status + "\n" + "Вечером " + evening_temperature + " " + evening_status + "\n" + "Ночью: " + night_temperature + " " + night_status
    return respond

def get_weather(): # + 3 hours

    owm = pyowm.OWM(weather_token, language = 'ru')
    today = datetime.datetime.today()
    fc = owm.three_hours_forecast('Stavropol')
    three_hours = timedelta(hours = 3)
    now = today + three_hours

    w_now = fc.get_weather_at(now)
    temperature_now = str(w_now.get_temperature('celsius')['temp'])
    status_now = str(w_now.get_detailed_status())

    responce_now = "Ставрополь сейчас: " + temperature_now + " °C, " + status_now

    responce = responce_now

    return responce

def get_hard_weather(body_request):
    index_first = body_request.find(" ")
    responce = "Error"
    if body_request.find(" ", index_first + 1) != -1:
        responce = "Запрос должен быть в виде: погода город\nНапример Погода Москва"
        return responce
    city_name = body_request[index_first + 1:]
    url = get_link(1, city_name)
    responce = get_weather_2(url)
    return responce



def Send_picture_tyan_request(body_request):
    Send_picture_tyan_requests = ["тян", "тянка"]
    for i in range(len(Send_picture_tyan_requests)):
        if body_request.find(Send_picture_tyan_requests[i]) != -1:
            return True
    return False

def Send_picture_tyan_responce(body_request):
    amount_photos = Find_number(body_request)
    if amount_photos != -1:
        if amount_photos > 5:
            responce = "Нельзя получить больше 5 фото семпай"
        else:
            responce = amount_photos
    else:
        responce = 1
    return responce

def send_picture_tyan():
    image_path = '/root/MyBot/images/'
    number_photo = random.randint(1,6405)
    image_path = image_path + str(number_photo) + '.jpg'
    upload = vk_api.VkUpload(vk)
    image = upload.photo_messages(image_path)
    attachment_id = 'photo' + str(image[0]['owner_id']) + '_' + str(image[0]['id'])
    vk.method("messages.send", {"peer_id": id, "attachment": attachment_id, "random_id": random.randint(1, 2147483647)})
    my_sleep(1)

Mon_1 = "Понедельник\n\n\n11:20 - 12:50\nМатематический анализ (2-222)\nЛяхов Павел Алексеевич\n\n13:20 - 14:50\nМатематический анализ (2-222)\nЛяхов Павел Алексеевич\n\n15:00 - 16:30\nАлгебра (1-309)\nДаржания Анна Дмитриевна\n\n\n\n"
Tue_1 = "Вторник\n\n\n11:20 - 12:50\nАнглийский язык (2-215)\nЕрина Лариса Сергеевна\n\n13:20 - 14:50\nФизика (2-205)\nШацкий Владимир Петрович\n\n15:00 - 16:30\nКомпьютерная алгебра (1-309)\nСмирнов Александр Александрович\n(Обычно её не бывает)\n\n\n\n"
Wed_1 = "Среда\n\n\n13:20 - 14:50\nМатематический анализ (2-221)\nЛяхов Павел Алексеевич\n\n15:00 - 16:30\nМатематический анализ (2-221)\nЛяхов Павел Алексеевич\n\n\n\n"
Thu_1 = "Четверг\n\n\n09:40 - 11:10\nБазы данных (2-224)\nМакоха Анатолий Николаевич\n\n11:20 - 12:50\nБазы данных (2-222)\nМакоха Анатолий Николаевич\n\n13:20 - 14:50\nПедагогика и психология (2-310)\nНихаева Яна Михайловна\n\n\n\n"
Fri_1 = "Пятница\n\n\n08:00 - 09:30\nИстория и методология математики (20-208)\nМахринова Марина Владимировна\n\n09:40 - 11:10\nАлгебра (2-219)\nДаржания Анна Дмитриевна\n\n11:20 - 12:50\nАлгебра (2-219)\nДаржания Анна Дмитриевна\n\n\n\n"

Mon_2 = "Понедельник\n\n\n13:20 - 14:50\nПедагогика и психология (2-329)\nСоловьева Евгения Владимировна\n\n15:00 - 16:30\nАлгебра (1-309)\nДаржания Анна Дмитриевна\n\n\n\n"
Tue_2 = "Вторник\n\n\n11:20 - 12:50\nАнглийский язык (2-215)\nЕрина Лариса Сергеевна\n\n13:20 - 14:50\nФизика (2-101)\nШацкий Владимир Петрович\n\n15:00 - 16:30\nФизика (2-101)\nШацкий Владимир Петрович\n\n16:50 - 18:20\nРабота куратора (2-219)\nДаржания Анна Дмитриевна\n(Обычно её не бывает)\n\n\n\n"
Wed_2 = "Среда\n\n\n13:20 - 14:50\nМатематический анализ (2-219)\nЛяхов Павел Алексеевич\n\n15:00 - 16:30\nМатематический анализ (2-219)\nЛяхов Павел Алексеевич\n\n\n\n"
Thu_2 = "Четверг\n\n\n08:00 - 09:30\nИстория и методология математики (20-208)\nМахринова Марина Владимировна\n\n09:40 - 11:10\nБазы данных (2-222)\nМакоха Анатолий Николаевич\n\n11:20 - 12:50\nБазы данных (2-225)\nМакоха Анатолий Николаевич\n\n\n\n"
Fri_2 = "Пятница\n\n\n08:00 - 09:30\nАлгебра (2-221)\nДаржания Анна Дмитриевна\n\n09:40 - 11:10\nАлгебра (2-219)\nДаржания Анна Дмитриевна\n\n11:20 - 12:50\nКомпьютерная алгебра (2-224)\nСмирнов Александр Александрович\n\n\n\n"

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if Hello_request(body.lower()):
                responce = Hello_responce()
                if responce[len(responce) - 6:].isdigit():
                    vk.method("messages.send", {"peer_id": id, "attachment": responce, "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "как дела?":
                vk.method("messages.send", {"peer_id": id, "message": "У меня всё отлично ня\nУ тебя как?", "random_id": random.randint(1, 2147483647)})
            elif Goodbye_request(body.lower()):
                responce = Goodbye_responce()
                if responce[len(responce) - 6:].isdigit():
                    vk.method("messages.send", {"peer_id": id, "attachment": responce, "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif Compliments_request(body.lower()):
                responce = Compliments_responce()
                if responce[len(responce) - 6:].isdigit():
                    vk.method("messages.send", {"peer_id": id, "attachment": responce, "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif Thanks_request(body.lower()):
                responce = Thanks_responce()
                if responce[len(responce) - 6:].isdigit():
                    vk.method("messages.send", {"peer_id": id, "attachment": responce, "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif Morning_request(body.lower()):
                responce = Morning_responce()
                if responce[len(responce) - 6:].isdigit():
                    vk.method("messages.send", {"peer_id": id, "attachment": responce, "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            #### Sanka
            elif Anime_Sanka_request(body.lower()):
                responce = Anime_Sanka_responce(body.lower())
                if responce[len(responce) - 6:].isdigit():
                    vk.method("messages.send", {"peer_id": id, "attachment": responce, "random_id": random.randint(1, 2147483647)})
                    vk.method("messages.send", {"peer_id": id, "message": "Приятного просмотра ^^", "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            ####
            elif Night_request(body.lower()):
                responce = Night_responce()
                if responce[len(responce) - 6:].isdigit():
                    vk.method("messages.send", {"peer_id": id, "attachment": responce, "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif body == "The secret key = Serral":
                vk.method("messages.send", {"peer_id": id, "attachment": "doc255035655_540091824", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "что делаешь?":
                vk.method("messages.send", {"peer_id": id, "message": "Работаю над планом по захвату мира", "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "погода":

                responce = get_weather() + '\n' + get_weather_2('https://world-weather.ru/pogoda/russia/stavropol/')
                vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})

            elif Weather_request(body.lower()): ##### Сложная погода
                responce = get_hard_weather(body.lower())
                vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})

            elif body.lower() == "я тебя не понимаю":
                vk.method("messages.send", {"peer_id": id, "attachment": "video237973448_456239707", "random_id": random.randint(1, 2147483647)})


            elif Send_picture_tyan_request(body.lower()):####### ТЯНКИ
                responce = Send_picture_tyan_responce(body.lower())
                if isinstance(responce, str):
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
                else:
                    for i in range(responce):
                        send_picture_tyan()####### ТЯНКИ


            elif body.lower() == "я тебя люблю":
                vk.method("messages.send", {"peer_id": id, "attachment": "video237973448_456239727", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "который час?":
                vk.method("messages.send", {"peer_id": id, "message": "Сейчас " + datetime.datetime.today().strftime("%H:%M:%S"), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "расписание":
                vk.method("messages.send", {"peer_id": id, "message": "Если вы хотите узнать расписание, то доступны следующие команды :\nРасписание на этой неделе\nРасписание на следующей неделе\nсегодня (расписание на сегодня)\nзавтра (расписание на завтра)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "расписание на этой неделе":
                week_number = datetime.datetime.today().strftime("%W")
                if int(week_number) % 2 == 1:
                    week = True # 1-я неделя
                else:
                    week = False # 2-я неделя
                if week:
                    responce = Mon_1 + Tue_1 + Wed_1 + Thu_1 + Fri_1
                else:
                    responce = Mon_2 + Tue_2 + Wed_2 + Thu_2 + Fri_2
                vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "расписание на следующей неделе":
                week_number = datetime.datetime.today().strftime("%W")
                if (int(week_number) + 1) % 2 == 1:
                    week = True # 1-я неделя
                else:
                    week = False # 2-я неделя
                if week:
                    responce = Mon_1 + Tue_1 + Wed_1 + Thu_1 + Fri_1
                else:
                    responce = Mon_2 + Tue_2 + Wed_2 + Thu_2 + Fri_2
                vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "сколько время?":
                vk.method("messages.send", {"peer_id": id, "message": "Сейчас " + datetime.datetime.today().strftime("%H:%M:%S"), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "какой сегодня день?":
                vk.method("messages.send", {"peer_id": id, "message": "Сегодня " + datetime.datetime.today().strftime("%d.%m.%Y"), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "сегодня":
                day_name = datetime.datetime.today().strftime("%a")
                week_number = datetime.datetime.today().strftime("%W")
                if int(week_number) % 2 == 1:
                    week = True # 1-я неделя
                else:
                    week = False # 2-я неделя
                if week:
                    if day_name == "Mon":
                        responce = Mon_1
                    elif day_name == "Tue":
                        responce = Tue_1
                    elif day_name == "Wed":
                        responce = Wed_1
                    elif day_name == "Thu":
                        responce = Thu_1
                    elif day_name == "Fri":
                        responce = Fri_1
                    elif day_name == "Sat":
                        responce = "Сегодня суббота, отдыхай"
                    elif day_name == "Sun":
                        responce = "Сегодня воскресенье, на учёбу только завтра, дурашка :3"
                    else:
                        responce = "Что-то пошло не так"
                else:
                    if day_name == "Mon":
                        responce = Mon_2
                    elif day_name == "Tue":
                        responce = Tue_2
                    elif day_name == "Wed":
                        responce = Wed_2
                    elif day_name == "Thu":
                        responce = Thu_2
                    elif day_name == "Fri":
                        responce = Fri_2
                    elif day_name == "Sat":
                        responce = "Сегодня суббота, отдыхай"
                    elif day_name == "Sun":
                        responce = "Сегодня воскресенье, на учёбу только завтра, дурашка :3"
                    else:
                        responce = "Что-то пошло не так"
                vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "завтра":
                today = datetime.datetime.today()
                one_more_day = timedelta(days = 1)
                tomorrow = today + one_more_day
                day_name = tomorrow.strftime("%a")
                week_number = tomorrow.strftime("%W")
                if int(week_number) % 2 == 1:
                    week = True # 1-я неделя
                else:
                    week = False # 2-я неделя
                if week:
                    if day_name == "Mon":
                        responce = Mon_1
                    elif day_name == "Tue":
                        responce = Tue_1
                    elif day_name == "Wed":
                        responce = Wed_1
                    elif day_name == "Thu":
                        responce = Thu_1
                    elif day_name == "Fri":
                        responce = Fri_1
                    elif day_name == "Sat":
                        responce = "Сегодня суббота, отдыхай"
                    elif day_name == "Sun":
                        responce = "Сегодня воскресенье, на учёбу только завтра, дурашка"
                    else:
                        responce = "Что-то пошло не так"
                else:
                    if day_name == "Mon":
                        responce = Mon_2
                    elif day_name == "Tue":
                        responce = Tue_2
                    elif day_name == "Wed":
                        responce = Wed_2
                    elif day_name == "Thu":
                        responce = Thu_2
                    elif day_name == "Fri":
                        responce = Fri_2
                    elif day_name == "Sat":
                        responce = "Сегодня суббота, отдыхай"
                    elif day_name == "Sun":
                        responce = "Сегодня воскресенье, на учёбу только завтра, дурашка"
                    else:
                        responce = "Что-то пошло не так"
                vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "дата":
                vk.method("messages.send", {"peer_id": id, "message": "Сегодня " + datetime.datetime.today().strftime("%d.%m.%Y"), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "хорошего денёчка":
                vk.method("messages.send", {"peer_id": id, "message": "Пасиб ^^ и тебе", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "нормально":
                vk.method("messages.send", {"peer_id": id, "message": "Очень рада за тебя", "random_id": random.randint(1, 2147483647)})
            else:
                responce = Vaguely_responce()
                if responce[len(responce) - 6:].isdigit():
                    vk.method("messages.send", {"peer_id": id, "attachment": responce, "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send", {"peer_id": id, "message": responce, "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        my_sleep(1)