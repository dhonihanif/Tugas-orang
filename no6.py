#no 6

npm = input("Masukkan NPM : ")
nilai_tugas = int(input("Masukkan Nilai Tugas : "))
nilai_uts = int(input("Masukkan Nilai UTS : "))
nilai_uas = int(input("Masukkan Nilai UAS : "))
total = ((30/100)*nilai_tugas)+((30/100)*nilai_uts)+((40/100)*nilai_uas)
print("Total Nilai adalah",total)
if total>=90:
    print("Grade Nilainya : A")
elif total>=80:
    print("Grade Nilainya : B")
elif total>=70:
    print("Grade Nilainya : C")
elif total>=60:
    print("Grade Nilainya : D")
else:
    print("Grade Nilainya : E")
