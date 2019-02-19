import requests
from bs4 import BeautifulSoup
import os
import lxml
import json
import datetime

class Advert:
    def __init__(self, title, price, price_with_delivery, buyer):
        self.title = title
        self.price = price
        self.price_with_delivery = price_with_delivery
        self.buyer = buyer
    def __str__(self):
        return self.title
    def show(self):
        print(self.title)
        print('cena: '+ self.price)
        print(str(self.price_with_delivery))
        print(str(self.buyer))
    def saveToFile(self, file):
        f= file
        f.write(
            self.title+'\n'+
            self.price+'\n'+
            self.price_with_delivery+'\n'+
            self.buyer+'\n'+
            '----------------------------------------------------------\n'
            )
        

url = 'https://allegro.pl/listing?string=????'
print('Czego szukasz na allegro?')
key = input(':')
url = url.replace('????', key)

r = requests.get(url)
r.encoding = 'utf-8'

page = BeautifulSoup(r.text, 'lxml')

page_body = page.body

offers = page_body.find_all('div',{'class':'edfdbf1'})

adverts = []

for offer in offers:
    
    title = offer.find('h2',{'class':'ebc9be2'})
    price = offer.find('span',{'class':'fee8042'})
    price2 = offer.find('div',{'class':'_870e91c'})
    buyer = offer.find('span',{'class':'_41ddd69'})
    if price!=None:
        price = price.text
    else:
        price = ''
    if price2!=None:
        price2 = price2.text
    else:
        price2 = ''
    if buyer!=None:
        buyer = buyer.text
    else:
        buyer = ''
    advert = Advert(title.text, price, price2, buyer)
    adverts.append(advert)

number = str(len(adverts))

print('Znaleziono '+number+' ofert')

file= open(key+'.txt',"a+")
file.write('Zanaleziono ofert: '+number+', dnia: '+str(datetime.datetime.now())+'\n')

for advert in adverts:
    advert.saveToFile(file)

print('zapisano je do pliku: '+key+'.txt')
input()


