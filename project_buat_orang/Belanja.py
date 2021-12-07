import os

print(" Program Belanja ".center(77,"-"))
print("="*77)

menu = ["Tambah barang","Kembalikan barang","Hentikan program"]
loop = True
keranjang = []
total = []
while loop:
    print("Pilih Menu".center(77,"-"))
    for i,j in zip(range(1,4),menu):
        print(f"{str(i)}.\t {j}")

    user = int(input("Menu yang anda pilih\t : "))
    if user==1:
        tersedia = ["Baju","Celana","Sepatu"]
        print("Kami Menyediakan : ")
        for i,j in zip(range(1,4),tersedia):
            print(f"{str(i)}.\t {j}")

        user2 = int(input("Menu yang anda pilih\t : "))
        if user2==1:
            baju = ["Kemeja","Kaos","Kaos Berkerah"]
            print("Kami menyediakan : ")
            for i,j in zip(range(1,4),baju):
                print(f"{str(i)}.\t {j}")
                
            user3 = int(input("Menu yang anda pilih\t : "))
            if user3==1:
                print("Anda membeli Kemeja")
                print("Harga\t : Rp.50.000")
                keranjang.append(baju[0])
                harga = 50000
                total.append(harga)
                
            elif user3==2:
                print("Anda membeli Kaos")
                print("Harga\t : Rp.30.000")
                keranjang.append(baju[1])
                harga=30000
                total.append(harga)
            elif user3==3:
                print("Anda membeli Kaos Berkerah")
                print("Harga\t : Rp.40.000")
                keranjang.append(baju[2])
                harga=40000
                total.append(harga)
            else:
                print("Maaf kami hanya menyediakan beberapa menu saja ^^")
                
        elif user2==2:
            celana = ["Jeans","Celana Panjang","Celana Pendek"]
            print("Kami menyediakan : ")
            for i,j in zip(range(1,4),celana):
                print(f"{str(i)}.\t {j}")

            user3 = int(input("Menu yang anda pilih\t : "))
            if user3==1:
                print("Anda membeli Jeans")
                print("Harga\t : Rp.50.000")
                keranjang.append(celana[0])
                harga = 50000
                total.append(harga)
            elif user3==2:
                print("Anda membeli Celana Panjang")
                print("Harga\t : Rp.40.000")
                keranjang.append(celana[1])
                harga = 40000
                total.append(harga)
            elif user3==3:
                print("Anda membeli Celana Pendek")
                print("Harga\t : Rp.45.000")
                keranjang.append(celana[2])
                harga = 45000
                total.append(harga)
            else:
                print("Maaf kami hanya menyediakan beberapa menu saja ^^")
                
        elif user2==3:
            sepatu = ["Panther","Warrior","Pink"]
            print("Kami menyediakan : ")
            for i,j in zip(range(1,4),sepatu):
                print(f"{str(i)}.\t {j}")

            user3 = int(input("Menu yang anda pilih\t : "))
            if user3==1:
                print("Anda memilih Panther")
                print("Harga\t : Rp.60.000")
                keranjang.append(sepatu[0])
                harga = 60000
                total.append(harga)
            elif user3==2:
                print("Anda memilih Warrior")
                print("Harga\t : Rp.50.000")
                keranjang.append(sepatu[1])
                harga = 50000
                total.append(harga)
            elif user3==3:
                print("Anda memilih Pink")
                print("Harga\t : Rp.50.000")
                keranjang.append(sepatu[2])
                harga = 50000
                total.append(harga)
            else:
                print("Maaf kami hanya menyediakan beberapa menu saja ^^")
                
        else:
          print("Maaf kami hanya menyediakan beberapa menu saja ^^")

    elif user==2:
        try:
           print("Anda membeli : ")
           for i,j in zip(range(1,len(keranjang)+1),keranjang):
               print(f"{str(i)}.\t {j}")

           user = int(input("Data ke berapa yang ingin anda hapus?\t : "))
           total.remove(total[user-1])
           keranjang.remove(keranjang[user-1])
           print("Data berhasil dihapus")
           
        except:
            print("Maaf anda tidak membeli barang tersebut atau anda tidak membeli apapun")
            
    elif user==3:
        print("Program berhenti....")
        os.system("pause")
        if keranjang==[]:
            print("Anda tidak membeli apapun :(")
        else:
            print("Anda Membeli\t : ")
            for i,j,k in zip(range(1,len(keranjang)+1),keranjang,total):
                print(f"{str(i)}.\t {j}\t Rp.{k}")

        print(f"Total belanjaan anda\t : Rp.{sum(total)}")
        loop = False
    else:
        print("Maaf kami hanya menyediakan beberapa menu saja ^^")
