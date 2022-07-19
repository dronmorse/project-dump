#!/usr/bin/env/python3

# otwieranie pliku fasta
kod = ''
tytul = ''
fasta = open('myszka.fasta','r')

# czyszczenie pliku fasta, linijka z '>' oczyszczana i  dodawana do  tytul
# a reszta linijek oczyszczona do kod

for linijka in fasta:
    if linijka.startswith('>'):
    	tytul += linijka[1:].strip()
    else:
    	kod += linijka.strip()
    	
# zamykanie fasty  	

fasta.close()

# tworzenie pliku o nazwie z wczesniej zapisanego tytul, zapisanie w nim kod, zamkniecie

plik = open(tytul,'w+')
plik.write(kod)
plik.close()

# znalezienie kodonu start

start = kod.find('ATG')

# znalezienie kodonu koncowego

kon = kod.find('TAG' or 'TGA' or 'TAA')

# zapisanie ramki odczytu do osobnego stringa, kon+3, �eby z�apa� ca�y ostatni kodon, bez tego to by pominelo koden stop

ramka = ''
ramka += kod[start:kon+3]

# transkrypcja za pomoca slownika, do trans dodajemy po kolei klucze z slownik

trans = ''

slownik ={'A':'T', 'C':'G', 'G':'C', 'T':'A'}

for i in ramka:
	trans += slownik[i]

# ddlugosc DNA po transkrypcji

liczba = 0
for i in trans:
	liczba += 1

# policzenie procentowych udzialoww kazdej zasady

x = trans.count('C')
proc1 = 100*x/len(trans)

y = trans.count('G')
proc2 = 100*y/len(trans)

z = trans.count('A')
proc3 = 100*z/len(trans)

s = trans.count('T')
proc4 = 100*s/len(trans)

# zapisanie liczby i procentow do pliku, + daje to, ze tworzy nowy plik jak nie istnial wczesniej, to tworzy go nowego 

plik2 = open('liczba','w+')
plik2.write(str(liczba))
plik2.write('\n')
plik2.write(str(proc1))
plik2.write('\n')
plik2.write(str(proc2))
plik2.write('\n')
plik2.write(str(proc3))
plik2.write('\n')
plik2.write(str(proc4))
plik2.write('\n')
plik2.close()
