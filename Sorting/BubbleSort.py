def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
                
 
DaftarAngka = [
    [23,7,32,99,4,15,11,20],
    [1,2,3,4,5,6,7,8,9,10],
    [2,2,3,2,5,6,7,1,2,3],
    [10,11,12,13,10,2,4,2,3,4],
    [5,4,3,6,2,5,4,9,8,10]]

BubbleSort(DaftarAngka)
print(DaftarAngka)
x = [23,7,32,99,4,15,11,20]
BubbleSort(x)
print(x)
