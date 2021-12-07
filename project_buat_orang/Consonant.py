import re

solve = lambda s : max([sum([ord(letter)-ord('a')+1 for letter in consOnly]) for consOnly in re.split("a|e|i|o|u",s)])
y = []
while True:
    z = input("Apakah anda ingin menginput kata : ")
    if z.startswith("Y") or z.startswith("y") or z.startswith("i"):#jawab ya atau iya
        x = input("Inputkan kata : ")
        print("Angka terbesar dari input :",solve(x))
        y.append(f"Angka terbesar dari input : {solve(x)}\n")
        txt = open("consonan.txt","a")
        for i in y:
            txt.write(f"{i}")

    else:
        break

