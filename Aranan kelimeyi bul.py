def KelimeBul (metin,aranan):
    sayac=0
    for i in metin:
        if (i==aranan):
            sayac+=1
        if(sayac==0):
            print("Kelime bulunamadi.")
        else:
            print(sayac," kadar kelime bulundu  ")

metin = input("Metni giriniz.\n")
aranan = input("Aranan kelimeyi giriniz:\n ")
metin.split

KelimeBul(metin,aranan)