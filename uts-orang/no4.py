#no 4

while True:
    jam = int(input("Masukkan data jam : "))
    if jam<0 or jam>23:
        print("Maaf jam yang dimasukkan tidak sesuai ketentuan")
        break
    
    menit = int(input("Masukkan data menit : "))
    if menit<0 or menit>59:
        print("Maaf menit yang dimasukkan tidak sesuai ketentuan")
        break
    
    detik = int(input("Masukkan data detik : "))
    if detik<0 or detik>59:
        print("Maaf detik yang dimasukkan tidak sesuai ketentuan")
        break
    
    else:
        print("Anda memasukkan jam {}:{}:{}".format(jam,menit,detik))
        break
