#no 5

def is_prima (x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True

def cari_bilangan_prima (awal, akhir):
  list_bilangan_prima = []
  if awal==1:
    awal+=1
  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  for i in list_bilangan_prima:
      if i==list_bilangan_prima[-1]:
          return i
      print(i)

print(cari_bilangan_prima(1,20))
