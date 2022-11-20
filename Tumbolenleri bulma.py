def tumbolenler():
  sayi=int(input("Bir sayi girin:\n "))
  bas=1
  if sayi>=0:
    for i in range(1,sayi+1):
     if sayi % i == 0:
        print(i)
tumbolenler()
