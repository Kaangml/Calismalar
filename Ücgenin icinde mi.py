def Ucgeninicindemi():
 Ax=int(input("A kosesinin x degerini giriniz:\n"))
 Ay=int(input("A kosesinin y degerini giriniz:\n"))
 Bx=int(input("B kosesinin x degerini giriniz:\n"))
 By=int(input("B kosesinin y degerini giriniz:\n"))
 Cx=int(input("C kosesinin x degerini giriniz:\n"))
 Cy=int(input("C kosesinin y degerini giriniz:\n"))

 Px=int(input("Aradıgınız P kosesinin x degerini giriniz:\n"))
 Py=int(input("Aradıgınız p kosesinin y degerini giriniz:\n"))

 bx = Bx-Ax
 by = By-Ay
 cx = Cx-Ax
 cy = Cy-Ay
 x = Px-Ax
 y = Py-Ay

 d=bx*cy-cx*by
 WA=(x*(by-cy)+y*(cx-bx)+d)/d
 WB=(x*cy-y*cx)/d
 WC=(y*bx-x*by)/d
 if 0<WA and WB and WC<1:
  return True
