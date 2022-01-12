import Dagang
import datetime
from Dagang import Dagangan

class Catatan(Dagangan):
    def __init__(self,kode,nama,jenis,jumlah,hargabeli,sisa,untung):
        super().__init__(kode,nama,jenis,jumlah,hargabeli,sisa,untung)
        while True:
            x = input("mau dirun?(y/t) : ")
            if x.startswith("y") or x.startswith("Y"):
                self.Buatarray()
                y = ["Laporan","CatatLaporan","Sisabarang","Lihat Data","exit"]
                print()
                while True:
                    print(" Kami menyediakan menu ".center(50,"-"))
                    for i,j in zip(range(1,len(y)+1),y):
                        print(str(i) + ". " + j)
                    z = int(input("Pilih angka : "))
                    if z==1:
                        self.Laporan()
                    elif z==2:
                        self.CatatLaporan()
                    elif z==3:
                        self.Sisabarang()
                    elif z==4:
                        self.LihatData()
                    elif z==5:
                        break
                    else:
                        print("Tidak ada selain itu")
            else:
                break
            
    def LihatData(self):
            f = open("laporan.txt","r")
            a = f.readlines()
            for i in a:
                if i == '\n':
                    a.remove(i)
            for i in range(len(a)):
                a[i] = a[i].split()
            print(" Laporan Barang yang Telah Terjual ".center(50,"-"))
            for i in a:
                for j,k in zip(range(1,len(i)+1),i):
                        print(j,k)
    def Laporan(self):
        print("Jenis Barang : ",self.jenis)
        print("Keuntungan total :",self.untung)
    def CatatLaporan(self):
        try:
            f = open("laporan.txt","a")
            f.write(f"{self.listt[2]} {self.untung}")
            f.close()
            print("Berhasil menyimpan ke catatan")

        except:
            print("Pilih 1/yang pertama terlebih dahulu setelah itu anda baru bisa memilih 2")
  


if __name__ == '__main__':
    x = Catatan(100,"Bayam","Sayuran",15,1500,'','')
    print(x)
    
