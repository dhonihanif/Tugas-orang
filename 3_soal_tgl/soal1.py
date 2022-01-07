#soal 1 weton

hari = input("Masukkan nama hari (huruf kecil semua) : ")
weton = input("Masukkan nama weton (huruf kecil semua) : ")
tgl_bulan = {
    "1":"31",
    "2":"28",
    "3":"31",
    "4":"30",
    "5":"31",
    "6":"30",
    "7":"31",
    "8":"31",
    "9":"30",
    "10":"31",
    "11":"30",
    "12":"31"}
listt = ["jumat pahing","sabtu pon","minggu wage","senin kliwon","selasa legi","rabu pahing","kamis pon","jumat wage","sabtu kliwon",
         "minggu legi","senin pahing","selasa pon","rabu wage","kamis kliwon",
         "jumat legi","sabtu pahing","minggu pon","senin wage","selasa kliwon","rabu legi","kamis pahing","jumat pon",
         "sabtu wage","minggu kliwon","senin legi","selasa pahing","rabu pon","kamis wage","jumat kliwon","sabtu legi","minggu pahing"]

c = listt.index(hari+ " " + weton)+1
month = 1
month2 = [1,2,3,4,5,6,7,8,9,10,11,12]
while month != month2[-1]+1:
    print("Tanggal \t : {}-{}-2021".format(c,month))
    if (c+35) >= int(tgl_bulan[str(month)]):
        c = (c+35)-int(tgl_bulan[str(month)])
        month+=1
        if month+1 > month2[-1]+1:
            break
        if c > int(tgl_bulan[str(month)]):
            c -=int(tgl_bulan[str(month)])
            month+=1
    else:
        c = (c+35)-int(tgl_bulan[str(month)])
        
