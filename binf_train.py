#!/usr/bin/env/python3
#otworzenie pliku pdb o nazwie podanej przez uzytkownika i stworzenie
#pliku do zapisu
nazwa = input('podaj nazwe pliku pdb: ')
prog = open(nazwa,'r')
app = open('zadanie.txt','w+')

#znalezienie linijek 'JRNL', znalezienie fragmentu 'TITL', dodanie odpowiedniego
#fragmentu do listy w pamieci programu
jrnl = []
for linijka in prog:
    if linijka.startswith('JRNL'):
        if linijka[12:16] == 'TITL':
            jrnl.append(linijka[19:])
        else:
            pass
    else:
        pass

#powrot na poczatek pliku pdb
prog.seek(0)

#znalezienie linijek 'HETATM', znalezienie czasteczek wody i policzenie ich
ile = 0
for linijka in prog:
    if linijka.startswith('HETATM'):
        if linijka[17:20] == 'HOH':
            ile += 1
        else:
            pass
    else:
        pass

#przekonwertowanie wszystkich danych do zapisu do formatu 'str',
#zapisanie wymaganych danych do pliku
aha = ''.join(jrnl)
app.write(aha)
app.write('liczba czasteczek wody: ')
app.write(str(ile))

#zamkniecie pliku pdb i pliku do zapisu
app.close()
prog.close()
