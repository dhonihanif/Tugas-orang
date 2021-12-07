data = []
nilai = []
alphabet = []

stop = False

while not stop:
    print("--Data Mahasiswa--")
    print("1. Menambahkan Data")
    print("2. Menghapus Data")
    print("3. Exit")

    x = int(input("Pilih angka : "))
    if x==1:
        y = input("Nama : ")
        z = int(input("Nilai : "))
        data.append(y)
        nilai.append(z)
        if z>=81:
            alphabet.append("A")
        elif z>=76:
            alphabet.append("B")
        elif z>=71:
            alphabet.append("C")
        elif z>=66:
            alphabet.append("D")
        elif z>=0:
            alphabet.append("E")
        else:
            print("Tidak ada")

        print("")
        print("Data Mahasiswa")
        for i,j,k,l in zip(range(1,len(data)+1),data,nilai,alphabet):
            print(i,j,k,l)

    elif x==2:
        print("")
        print("Data Mahasiswa")
        for i,j,k,l in zip(range(1,len(data)+1),data,nilai,alphabet):
            print(i,j,k,l)

        a = int(input("Data yang ingin dihapus angka : "))
        data.remove(data[a-1])
        nilai.remove(nilai[a-1])
        alphabet.remove(alphabet[a-1])
        print("Data berhasil dihapus")
        for i,j,k,l in zip(range(1,len(data)+1),data,nilai,alphabet):
            print(i,j,k,l)

    else:
        stop = True
        
