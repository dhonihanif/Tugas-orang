#soal 3 Input hari

hari = input("Hari : ").capitalize()
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
a = ["Jumat","Sabtu","Minggu","Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu","Minggu"]
c = a.index(hari)+1
month = 1
month2 = [1,2,3,4,5,6,7,8,9,10,11,12]
while month != month2[-1]+1:
    print("Tanggal \t : {}-{}-2021".format(c,month))
    if (c+7) >= int(tgl_bulan[str(month)]):
        c = (c+7)%int(tgl_bulan[str(month)])
        month+=1
    else:
        c = (c+7)%int(tgl_bulan[str(month)])
        
