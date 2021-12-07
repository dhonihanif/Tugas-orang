#1. Program Otomotif

import datetime

class Otomotif:
    def __init__(self,modal):
        self.modal = modal
        self.list_motor()
        self.pembeli()
        self.history()
        
    def list_motor(self):
        self.motor = {
            "jenis_motor":[
            "Revo F1 110",
            "New Supra X 125 F1",
            "New Beat F1",
            "Vega ZR",
            "Jupiter Z",
            "Jupiter MX",
            "Satria FU 150",
            "Shogun R 125"
            ],
            "QTY":[30,30,20,10,20,15,10,5],
            "harga":[12500000,
                     18500000,
                     12000000,
                     13500000,
                     14000000,
                     17000000,
                     19500000,
                     14000000
                     ]
            }
        
    def pembeli(self):
        self.pelanggan = {"nik":[],
                          "nama":[],
                          "ttl":[],
                          "alamat":[],
                          "agama":[],
                          "status":[],
                          "pekerjaan":[],
                          "kewarganegaraan":[],
                          "jenis_motor":[],
                          "QTY":[],
                          "harga":[]
                          }
        nik = input("NIK\t : ")
        nama = input("Nama\t : ")
        ttl = input("TTL\t : ")
        alamat = input("Alamat\t : ")
        agama = input("Agama\t : ")
        status = input("Status nikah\t : ")
        pekerjaan = input("Pekerjaan\t : ")
        kewarganegaraan = input("Kewarganegaraan\t : ")
        self.pelanggan["nik"].append(nik)
        self.pelanggan["nama"].append(nama)
        self.pelanggan["ttl"].append(ttl)
        self.pelanggan["alamat"].append(alamat)
        self.pelanggan["agama"].append(agama)
        self.pelanggan["status"].append(status)
        self.pelanggan["pekerjaan"].append(pekerjaan)
        self.pelanggan["kewarganegaraan"].append(kewarganegaraan)
        stop =False
        while not stop:
            x = input("Apakah anda ingin membeli? : ")
            if x.startswith("Y") or x.startswith("y"):
                
                print("")
                print("Tersedia Jenis Motor ")
                for i,j in zip(range(1,len(self.motor["jenis_motor"])),self.motor["jenis_motor"]):
                    print(i,j)

                beli = int(input("Anda mau membeli no berapa? : "))
                qty = int(input("Mau beli berapa? : "))
                
                if self.motor["QTY"][beli-1]>0 and qty<=self.motor["QTY"][beli-1]:
                    self.pelanggan["jenis_motor"].append(self.motor["jenis_motor"][beli-1])
                    self.pelanggan["QTY"].append(qty)
                    self.motor["QTY"][beli-1] -= qty
                    self.modal+=self.motor["harga"][beli-1] * qty
                    self.pelanggan["harga"].append(self.motor["harga"][beli-1])
                    print("Modal bertambah menjadi",self.modal)
                    print("")
                elif qty==0:
                    print("Anda membatalkan pesanan") 
                else:
                    print("Maaf stok kurang/sudah habis")
            else:
                print("")
                print(" Pembelian anda ".center(75,'-'))
                print("")
                print(f"""
------------------------------------------------------------
| No | Pembeli | Tgl Pembelian | Jenis Motor | QTY | Harga |
------------------------------------------------------------
""")
                for i,j,k,l in zip(range(1,len(self.pelanggan["jenis_motor"])+1),
                                       self.pelanggan["jenis_motor"],
                                       self.pelanggan["QTY"],
                                       self.pelanggan["harga"]
                                       ):
                    print(f"""
{'-'*70}
| {i} | {nama} | {datetime.datetime.now().date()} | {j} | {k} | {l} |
{'-'*70}
""")
                self.txt = open("histori.txt","a")
                self.txt.write(f"""
------------------------------------------------------------
| No | Pembeli | Tgl Pembelian | Jenis Motor | QTY | Harga |
------------------------------------------------------------
""")
                for i,j,k,l in zip(range(1,len(self.pelanggan["jenis_motor"])+1),
                                       self.pelanggan["jenis_motor"],
                                       self.pelanggan["QTY"],
                                       self.pelanggan["harga"]
                                       ):
                    self.txt.write(f"""
{'-'*70}
| {i} | {nama} | {datetime.datetime.now().date()} | {j} | {k} | {l} |
{'-'*70}
""")
                    
                stop = True

    def history(self):
        self.txt = open("history.txt","a")
        self.txt.write(f"""
------------------------------------------------------------
| No | Pembeli | Tgl Pembelian | Jenis Motor | QTY | Harga |
------------------------------------------------------------
""")
        for i,j,k,l,m,n in zip(range(1,len(self.pelanggan["nama"])+1),
                                       self.pelanggan["nama"],
                                       self.pelanggan["ttl"],
                                       self.pelanggan["jenis_motor"],
                                       self.pelanggan["QTY"],
                                       self.pelanggan["harga"]
                                       ):
                    self.txt.write(f"""
| {i} | {j} | {k} | {l} | {m} | {n} |
-------------------------------------
""")


dhoni = Otomotif(400000000)
