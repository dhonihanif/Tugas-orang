from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import os

class Univ:
    def __init__(self,page):
        self.page = page
    def abstract(self):
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.div = self.soup.find('div',class_='desc-l-univ')
        self.h3 = self.div.find('h3')
        print(self.h3.text)
    def data(self):
        a = input("Mau menampilkan data ?(y/t) : ")
        pilihan = []
        if a == "y":
            while True:
                b = input("Mau memfilter data?(y/t) : ")
                if b== "y":
                    self.dataa = ["Lokasi Kampus","Kategori Kampus","Tipe Kampus","Akreditasi"]
                    for i,j in zip(range(1,len(self.dataa)+1),self.dataa):
                        print(str(i) + "." + " " + j)
                    pilih = int(input("Pilih angka : "))
                    if pilih == 1:
                        prov = input("Provinsi : ")
                        prov = prov.replace(".","-")
                        prov = prov.replace(" ","-")
                        pilihan.append("provinsi/" + prov + "/")
                    elif pilih == 2:
                        kategori = ["akademik","institut","sekolah_tinggi","politeknik","universitas"]
                        for i,j in zip(range(1,len(kategori)+1),kategori):
                            print(str(i) + "." + " " + j)
                        ka = int(input("Pilih angka : "))
                        pilihan.append("kategori/" + kategori[ka-1] + "/")
                    elif pilih == 3:
                        tipe = ["negeri","swasta"]
                        for i,j in zip(range(1,len(tipe)+1),tipe):
                            print(str(i) + "." + " " + j)
                        ti = int(input("Pilih angka : "))
                        pilihan.append("tipe_kampus/" + tipe[ti-1] + "/")
                    elif pilih == 4:
                        akreditas = ["a","b","c"]
                        for i,j in zip(range(1,len(akreditas)+1),akreditas):
                            print(str(i) + "." + " " + j)
                        ak = int(input("Pilih angka : "))
                        pilihan.append("akreditas/" + akreditas[ak-1] + "/")
                    else:
                        print("Tidak ada selain itu")
                else:
                    break
        url = "https://ayokuliah.id/universitas/"
        for i in pilihan:
            url+=i
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.listt = []
        self.data = self.soup.find_all('div',class_ = 'univ-list')
        for i in self.data:
            univ = i.find('h3').text
            alamat = i.find('div',class_ = 'univ-list-address').text
            alamatt = re.sub(r"[\n\t<br>]","",alamat)
            self.listt.append({
                "Nama Universitas":univ,
                "Alamat":alamatt}
                              )
        df = pd.DataFrame(self.listt)
        if df.empty == True:
            print("Data tidak ditemukan")
        else:
            print(df)
            simpan = input("Apakah anda mau menyimpannya?(y/t) : ")
            if simpan == "y":
                df.to_csv('daftar_universitas.csv',index=False,encoding='utf-8')
                print("Data berhasil tersimpan di",os.getcwd())
    
    
page = Univ(requests.get('https://ayokuliah.id/universitas/'))
print(page.abstract())
print(page.data())
