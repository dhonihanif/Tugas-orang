#Sistem Informasi Data-Data Mahasiswa

class Informasi_mahasiswa:
    def __init__(self,data):
        self.data = data
        while True:
            x = ["Create/add","Read","Update","Delete","Laporan","Exit"]
            for i,j in zip(range(1,len(x)+1),x):
                print(i,j)
            y = int(input("Pilih angka : ")
                    )
            if y==1:
                self.add()
            elif y==2:
                self.read()
            elif y==3:
                self.update()
            elif y==4:
                self.delete()
            elif y==5:
                self.laporan()
            elif y==6:
                print("Terimakasih")
                break
            else:
                print("Tidak ada pilihan selain itu")
                if type(y)==str:
                    print("Inputan harus integer/bilangan bulat")
                break

    def add(self):
        print(" Menambah Data ".center(70,'-'))
        name = input("Nama : ")
        nim = int(input("Nim : "))
        kelas = input("Kelas : ")
        semester = int(input("Semester\t : "))
        umur = int(input("Umur : "))
        if nim not in self.data["nim"]:
            self.data["name"].append(name)
            self.data["nim"].append(nim)
            self.data["kelas"].append(kelas)
            self.data["smt"].append(semester)
            self.data["umur"].append(umur)
            print("Data berhasil ditambahkan")
        else:
            print("Nim telah digunakan")
            raise NameError("Nim sudah ada")

    def read(self):
        print(" Data Mahasiswa ".center(70,'-'))
        print("Nama\t\t Nim\t\t Kelas\t\t Semester\t\t Umur")
        for i,j,k,l,m,n in zip(range(1,len(self.data["name"])+1),self.data["name"],
                             self.data["nim"],self.data["kelas"],
                               self.data["smt"],self.data["umur"]
                             ):
            print(i,".",j,k,l,m,n)
        print()
    def update(self):
        print(" Mengupdate Data Mahasiswa ".center(70,'-'))
        print()
        for i,j,k,l,m,n in zip(range(1,len(self.data["name"])+1),self.data["name"],
                             self.data["nim"],self.data["kelas"],
                               self.data["smt"],self.data["umur"]
                             ):
            print(i,".",j,k,l,m,n)
        print()
        hapus = int(input("Siapa yang ingin anda ubah?(sebutkan nomornya) : "))
        print("Anda ingin mengubah {}".format(self.data["name"][hapus-1]))
        pilih = input("Diubah name/nim/kelas/semester/umur ? : ")
        if pilih=="name":
            ubah = input("Nama\t : ")
        elif pilih=="nim":
            ubah = int(input("Nim\t : ")
                       )
        elif pilih=="kelas":
            ubah = input("Kelas\t : ")
        elif pilih=="umur":
            ubah = input("Umur\t : ")
        elif pilih=="semester":
            ubah = int(input("Semester\t : "))
        else:
            print("Tidak ada pilihan selain itu")

        self.data[pilih].remove(self.data[pilih][hapus-1])
        self.data[pilih].insert(hapus-1,ubah)
        print("Data berhasil diubah")
        print()

    def delete(self):
        print(" Mendelete Data Mahasiswa ".center(70,'-'))
        print()
        for i,j,k,l,m in zip(range(1,len(self.data["name"])+1),self.data["name"],
                             self.data["nim"],self.data["kelas"],self.data["umur"]
                             ):
            print(i,".",j,k,l,m)
        hapus = int(input("Siapa yang ingin anda delete ? (sebutkan nomornya)"))
        print("Anda ingin menghapus {}".format(self.data["name"][hapus-1]))
        self.data["name"].remove(self.data["name"][hapus-1])
        self.data["nim"].remove(self.data["nim"][hapus-1])
        self.data["kelas"].remove(self.data["kelas"][hapus-1])
        self.data["smt"].remove(self.data["smt"][hapus-1])
        self.data["umur"].remove(self.data["umur"][hapus-1])
        print("Data Berhasil dihapus")
        print()
    def laporan(self):
        print(" Laporan ".center(70,'-'))
        while True:
            x = ["Sistem Informasi Data Mahasiswa",
                 "Sebaran umur mahasiswa",
                 "Lama masa studi",
                 "Mencari mahasiswa berdasarkan name/nim/kelas/umur",
                 "Exit"]
            for i,j in zip(range(1,len(x)+1),x):
                print(i,".",j)
            y = int(input("Input no : "))
            if y==1:
                smt1 = [i for i in self.data["smt"] if i==1]
                smt2 = [i for i in self.data["smt"] if i==2]
                smt3 = [i for i in self.data["smt"] if i==3]
                smt4 = [i for i in self.data["smt"] if i==4]
                smt5 = [i for i in self.data["smt"] if i==5]
                smt6 = [i for i in self.data["smt"] if i==6]
                smt7 = [i for i in self.data["smt"] if i==7]
                smt8 = [i for i in self.data["smt"] if i==8]
                smt_lebih_besar_dari8 = [i for i in self.data["smt"] if i>8]
                b = [smt1,smt2,smt3,smt4,smt5,smt6,smt7,smt8,smt_lebih_besar_dari8]
                print("Sistem Informasi Data Mahasiswa".center(70,'-'))
                for i in range(1,10):
                    if i==9:
                        print("Jumlah mahasiswa lebih dari semester 8\t : {}".format(len(b[i-1])))
                    print("Jumlah mahasiswa semester {}\t : {}".format(
                        i,len(b[i-1])))
                print()
            elif y==2:
                print(" Sebaran Umur Mahasiswa ".center(70,'-'))
                for i,j,k in zip(range(1,len(self.data["name"])+1),self.data["name"],
                                 self.data["umur"]):
                    print(i,".",j,":",k)
                print()
            elif y==3:
                print(" Lama Masa Studi ".center(70,'-'))
                for i,j,k,l in zip(range(1,len(self.data["name"])+1),self.data["name"],
                                 self.data["nim"],self.data["smt"]):
                    print(i,".","{} dengan nim {} masa studi\t : {} tahun".format(
                        j,k,l/2))
                print()
            elif y==4:
                print(" Mencari Mahassiwa Berdasarkan Nama/Nim/Kelas/Semester/Umur ".center(70,'-'))
                a = input("Mau mencari berdasarkan apa?name/nim/kelas/smt/umur : ")
                if a=="name":
                    b = input("Nama\t : ")
                    print("Nama\t\t Nim\t\t Kelas\t\t Semester\t\t Umur")
                    for i,j,k,l,m,n in zip(range(1,len(self.data["name"])+1),self.data["name"],
                                       self.data["nim"],self.data["kelas"],self.data["smt"],
                                       self.data["umur"]):
                        if j==b:
                            print(i,".",j,k,l,m,n)
                    print()
                elif a=="nim":
                    b = int(input("nim\t : "))
                    for i,j,k,l,m,n in zip(range(1,len(self.data["name"])+1),self.data["name"],
                                       self.data["nim"],self.data["kelas"],self.data["smt"],
                                       self.data["umur"]):
                        if k==b:
                            print(i,".",j,k,l,m,n)
                    print()
                elif a=="kelas":
                    b = input("Kelas\t : ")
                    for i,j,k,l,m,n in zip(range(1,len(self.data["name"])+1),self.data["name"],
                                       self.data["nim"],self.data["kelas"],self.data["smt"],
                                       self.data["umur"]):
                        if l==b:
                            print(i,".",j,k,l,m,n)
                    print()
                elif a=="smt":
                    b = int(input("Semester\t : "))
                    for i,j,k,l,m,n in zip(range(1,len(self.data["name"])+1),self.data["name"],
                                       self.data["nim"],self.data["kelas"],self.data["smt"],
                                       self.data["umur"]):
                        if m==b:
                            print(i,".",j,k,l,m,n)
                    print()
                elif a=="umur":
                    b = int(input("Umur\t : "))
                    for i,j,k,l,m,n in zip(range(1,len(self.data["name"])+1),self.data["name"],
                                       self.data["nim"],self.data["kelas"],self.data["smt"],
                                       self.data["umur"]):
                        if n==b:
                            print(i,".",j,k,l,m,n)
                    print()
                else:
                    print("Maaf menu kami hanya menyediakan menu :")
                    x = ["name","nim","kelas","smt","umur"]
                    for i,j in zip(range(1,len(x)+1),x):
                        print(i,".",j)
                    print("Sesuaikan inputan dengan menu diatas!!!")
                    print()
            elif y==5:
                print("Terumakasih")
                break
            else:
                print("Tidak ada selain itu")
                print()

data = {
    "name":[],
    "nim":[],
    "kelas":[],
    "smt":[],
    "umur":[]
    }
o = Informasi_mahasiswa(data)
if __name__ == '___main__':
    print(o)

    
