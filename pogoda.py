import requests
from bs4 import BeautifulSoup
import os



def get_weather():
    city = "Rzeszów"
    url = "https://pogoda.interia.pl/prognoza-szczegolowa-rzeszow,cId,30389"
    page = requests.get(url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'lxml')
    body = soup.body
    time = body.find('span', {'class':'weather-currently-info-item-time'}).text
    main_temp = body.find('div', {'class':'weather-currently-temp-strict'}).text
    details = body.find_all('span', {'class':'weather-currently-details-value'})
    wind = details[2].text
    preassure = details[1].text
    temp = details[0].text

    wind = wind.replace(' ','')
    preassure = preassure.replace(' ','')
    temp = temp.replace(' ','')

    return {'city':city, 'time':time, 'main_temp':main_temp, 'temp':temp, 'wind':wind, 'preassure':preassure}

def table_show(dic):
    for elem in dic:
        label = elem+((20*' ')[:-len(elem)])
        print(label + dic[elem])


os.system('mode con: cols=30 lines=8')
print('Download data ...')

info = get_weather()

os.system('cls' if os.name == 'nt' else 'clear')

table_show(info)



input("\nPress Enter to exit...")

