def faktoriyelhesapla():
  sayi=int(input("Bir sayi girin:\n "))
  faktoriyel=1
  if sayi>=0:
    for i in range(1,sayi+1):
     faktoriyel=i*faktoriyel
    return faktoriyel
  else:
    print("Negatif sayi!!")
    return 0
faktoriyelhesapla()
