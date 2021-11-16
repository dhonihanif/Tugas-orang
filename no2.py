#ini yang a

print("ini a")
a = "1"
for i in range(2,7):
    print(a)
    a+=str(i)

#ini yang b
    
print("")
print("Ini b")
b = "6,5,4,3,2,1"
listt = b.split(",")
b="654321"

for i in b:
    for j in listt:
        print(j,end="")
    print()
    listt.remove(i)
    
