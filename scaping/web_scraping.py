from bs4 import BeautifulSoup
import requests
import numpy as np

class Penduduk:
    def __init__(self,page):
        self.page = page
    def abstract(self):
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.div = self.soup.find('div',class_='desc-l-univ')
        self.h3 = self.div.find('h3')
        print(self.h3.text)
    def data(self):
        self.data = self.soup.find_all('div',class_ = 'univ-list')
        for i in self.data:
            a = i.find('div',class_ = 'univ-list-logo col-md-2 col-xs-2')
            aa = a.get('img scr')
            print(aa)

page = Penduduk(requests.get('https://ayokuliah.id/universitas/'))
print(page.abstract())
print(page.data())
