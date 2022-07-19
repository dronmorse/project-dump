#!/usr/bin/env/python3

nazwa = input('podaj nazwe pliku pdb: ')
plik = open(nazwa,'r')
app = open('informacje.txt','w+')
for linijka in plik:
    if linijka.startswith('EXPDTA'):
        print linijka
        app.write(linijka[10:])
plik.seek(0)
for linijka in plik:
    if linijka[11:21] == 'RESOLUTION':
        print linijka
        app.write('rozdzielczosc: ')
        app.write(linijka[26:41])
        app.write('\n')
plik.seek(0)
d = 0
for linijka in plik:
    if linijka.startswith('HELIX'):
        d += 1
        app.write(linijka[74:77])
        print linijka[74:77]
print ('ilosc: ', d)
app.write('\n')
app.write('ilosc: ')
app.write(str(d))

amino = input('podaj nazwe aminokwasu: ')
at = input('podaj nazwe atomu: ')

plik.seek(0)
x1 = ''
y1 = ''
z1 = ''
for linijka in plik:
    if linijka.startswith('ATOM'):
        if linijka.split()[3] == amino:
            if linijka.split()[11] == at:
                x1 += linijka.split()[6]
                y1 += linijka.split()[7]
                z1 += linijka.split()[8]
                break

amino2 = input('podaj nazwe 2 aminokwasu: ')
at2 = input('podaj nazwe 2 atomu: ')

plik.seek(0)
x2 = ''
y2 = ''
z2 = ''
for linijka in plik:
    if linijka.startswith('ATOM'):
        if linijka.split()[3] == amino2:
            if linijka.split()[11] == at2:
                x2 += linijka.split()[6]
                y2 += linijka.split()[7]
                z2 += linijka.split()[8]
                break
print (x1, x2)
odl = ((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2 + (float(z1)-float(z2))**2)**0.5
app.write(str(odl))
app.write('obliczone miedzy: ')
app.write(amino)
app.write(at)
app.write('i')
app.write(amino2)
app.write(at2)
print (odl, 'odleglosc obliczona miedzy: ', amino, ':', at, ',', amino2, ':', at2)

plik.seek(0)
ilosc = input('podaj nazwe aminokwasu, ktorego ilosc chcesz policzyc: ')
p = 0
for linijka in plik:
    if linijka.startswith('SEQRES'):
        for i in range(0,14):
            if linijka.split()[i] == ilosc:
                p += 1
print ('ilosc: ', p)
app.write('\n')
app.write('ilosc aminokwasu ')
app.write(ilosc)
app.write(':')
app.write(str(p))
app.close()
plik.close()
