import datetime

f = open("Barang.txt","a")
f.write(f"""
Kode\t Nama\t Jenis\t Hargabeli\t Sisa\t Untung
""")
f.close()
f = open("Jual.txt","a")
f.write(f"""
Tanggal\t Kode\t Jumlah\t Harga\t Diskon
""")
f.close()
class Dagangan:
    def __init__(self,kode,nama,jenis,jumlah,hargabeli,sisa,untung):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis
        self.jumlah = jumlah
        self.hargabeli = hargabeli
        self.sisa = sisa
        self.untung = untung
    def Isibarang(self):
        f = open("Barang.txt","a")
        f.write(f"""
{self.kode}\t {self.nama}\t {self.jenis}\t {self.jumlah}\t {self.hargabeli}\t {self.sisa}\t {self.untung}
""")
        f.close()
    def Isijual(self):
        self.tanggal = datetime.datetime.now()
        self.diskon = int(input("Masukkan diskon : "))
        self.jumlahbeli = int(input("Beli berapa? : "))
        self.harga = (self.hargabeli-(self.hargabeli*(self.diskon/100)))*self.jumlahbeli
        f = open("Jual.txt","a")
        f.write(f"""
{self.tanggal.day}-{self.tanggal.month}-{self.tanggal.year}\t {self.kode}\t {self.jumlahbeli}\t {self.harga}\t {self.diskon}
""")
        f.close()
        
    def Buatarray(self):
        print("Mengisi Array dan menampilkan".center(30,'-'))
        print("Tersedia".center(30,'-'))
        print("1. Barang")
        print("2. Nota")
        y = int(input("Anda pilih yang mana?1/2 : "))
        if y==1:
            self.listt = [input("Kode : "),input("Nama : "),input("Jenis : "),input("jumlah : "),input("Harga beli : "),self.sisa,self.untung]
            self.jumlahbeli = int(input("Beli berapa? : "))
            self.diskon = int(input("Masukkan diskon : "))
            f = open("Barang.txt","a")
            f.write(f"""
{self.listt[0]}\t {self.listt[1]}\t {self.listt[2]}\t {self.listt[3]}\t {self.listt[4]}\t {self.listt[5]}\t {self.listt[6]}
""")
            f.close()
            arr = ["Kode","Nama","Jenis","Jumlah","Hargabeli","Sisa","Untung"]
            print("Tampilan Array")
            for i,j in zip(arr,self.listt):
                print(i,":",j)
                
        elif y==2:
            self.tanggal = datetime.datetime.now()
            tanggal = f"{self.tanggal.day}-{self.tanggal.month}-{self.tanggal.year}"
            self.listt2 = [tanggal,input("Kode : "),int(input("Jumlah : ")),int(input("Diskon : "))]
            hargabeli = int(input("Harga beli : "))
            harga = hargabeli-(hargabeli*(self.listt2[-1]/100))
            self.listt2.insert(-2,harga)
            f = open("Jual.txt","a")
            f.write(f"""
{self.listt2[0]}\t {self.listt2[1]}\t {self.listt2[2]}\t {self.listt2[3]}\t {self.listt2[4]}
""")
            f.close()
            arr = ["Tanggal","Kode","Jumlah","Harga","Diskon"]
            print("Tampilan Array")
            for i,j in zip(arr,self.listt2):
                print(i,":",j)
                
        else:
            print("Tidak ada selain itu")
    
    def Sisabarang(self):
        try:
            self.sisa = self.jumlah-self.jumlahbeli
            self.untung = (self.hargabeli*((100-self.diskon)/100)-100)
            print("Sisa\t :",self.sisa)
            print("Untung\t :",self.untung)

        except:
            print("Pilih 1/yang pertama terlebih dahulu setelah itu anda baru bisa memilih 2")
    def Urut(self):
        f = open("Barang.txt","r")
        a = f.readlines()
        for i in a:
            if i=="\n":
                a.remove(i)
        f.close()
        a.sort()
        f = open("Barang.txt","a")
        f.write(f"{a}")
        f.close()
    
