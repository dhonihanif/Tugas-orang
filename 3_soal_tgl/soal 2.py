#soal no 2 perbedaan waktu

x = input("Jam(hh:mm) : ")
y = input("Tanggal(dd-mm-yyyy) : ")
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
if int(y[-4::]) % 400 == 0 or (int(y[-4::]) % 4 == 0 and int(y[-4::]) % 100 != 0):
    tgl_bulan["2"] = "29"
if y[:2] == "01":
    if y[3:5] == "01":
        tgl_arizona = tgl_bulan[str((int(y[4])-2)%12+1)] + "-" +str((int(y[4])-2)%12+1) + "-" + str(int(y[-4::])-1)
    else:
        if y[3] == "0":
            tgl_arizona = tgl_bulan[str((int(y[4])-1)%12)] + "-" + str((int(y[4])-1)%12) + "-" + y[-4::]
        else:
            tgl_arizona = tgl_bulan[str((int(y[3:5])-1)%12)] + "-" + str((int(y[4])-1)%12) + "-" + y[-4::]
else:
    if y[0] == "0" or y[3] == "0":
        tgl_arizona = str((int(y[3:5])-1)%int(tgl_bulan[str((int(y[4])-1))])) + "-" + y[3:5] + "-" + y[-4::]
    else:
        if (int(x[:2])-14) >= 0:
            tgl_arizona = y
        else:
            tgl_arizona = str((int(y[3:5])-1)%int(tgl_bulan[str((int(y[3:5])-1))])) + "-" + y[3:5] + "-" + y[-4::]

if x[:2] == "24":
    x = "00" + x[2::]
    if y[0] == "0":
        if y[1] + 1 <= 9:
            y = y[0] + str(int(y[1])+1) + y[2::]
        else:
            y = str(int(y[:2])+1) + y[2::]
    else:
        y = str(int(y[:2])+1) + y[2::]
if x[0]=="0":
    if int(x[1]) - 3 <= 2 or int(x[1]) - 14 <= 0 :
        jam_dubai = str((int(x[1])-3)%24) + x[2::]
        if int(x[1]) - 3 <= 0 or (int(x[1])-14)%24 >= 9:
            tgl_dubai = tgl_arizona
            jam_dubai = "" + str((int(x[1])-3)%24) + x[2::]
            jam_arizona = str((int(x[1])-14)%24) + x[2::]
        else:
            tgl_dubai = tgl_arizona
            jam_arizona = str((int(x[1]) - 14)%24) + x[2::]
    else:
        if int(x[1]) - 3 <=0:
            jam_dubai = x[0] + str(int(x[1])-3) + x[2::]
        else:
            tgl_dubai = y
            jam_dubai = str(int(x[0:2]) - 3) + x[2::]
else:
    if (int(x[:2]) - 3)%24 <= 9 or (int(x[:2]) - 14) % 24 <= 9:
        jam_dubai = "" + str(int(x[:2]) - 3) + x[2::]
        if (int(x[:2]) - 14) % 24 >= 9 or (int(x[:2]) - 3) < 0:
            jam_arizona = str((int(x[:2])-14)%24) + x[2::]
            tgl_dubai = tgl_arizona
        else:
            tgl_dubai = y
            jam_arizona = "" + str((int(x[:2]) - 14)%24) + x[2::]
    else:
        jam_dubai = str(int(x[0:2]) - 3) + x[2::]
        if int(x[:2]) - 14 % 24 >= 9 or (int(x[:2])-3) < 0:
            jam_arizona = str((int(x[1])-14)%24) + x[2::]
            tgl_dubai = tgl_arizona
        else:
            tgl_dubai = y
            jam_arizona = x[0] + str((int(x[1]) - 14)%24) + x[2::]
if x[0] == "0":
    if int(x[1]) < 3:
        tgl_dubai = tgl_arizona
    else:
        tgl_dubai = y
else:
    tgl_dubai = y
print("Di Surabaya Jam {} WIB dan Tanggal {}".format(x,y))
print("Di Dubai Jam {} UEA dan Tanggal {}".format(jam_dubai,tgl_dubai))
print("Di Arizona Jam {} dan Tanggal {}".format(jam_arizona,tgl_arizona))
