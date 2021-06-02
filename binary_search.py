def szukaj(tablica, szukana):
  # Definicje
  indeks = 0
  lewa = 0
  prawa = len(tablica)

  # Sprawdzam czy badany zakres nie jest pusty
  while lewa < prawa:
    indeks = (lewa + prawa) // 2
    
    if tablica[indeks] == szukana:
      return indeks
    elif tablica[indeks] > szukana:
      lewa = indeks + 1
    else:
      prawa = indeks
  return -1

testowe_dane = [26,17,16,15,12,11,10,9,8,7,6,5,4,3,2,1] 
do_wyszukania = 9
indeks = szukaj(testowe_dane , do_wyszukania )
print(indeks)

print(testowe_dane.index(26))