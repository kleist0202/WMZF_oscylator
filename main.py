import sys
import os


def load_from_file(file_name):
    d = {}
    with open(file_name, 'r') as f:
        next(f)
        for i in f:
            s = i.split()
            d[s[0]] = float(s[1])

    return d

def menu(lepkosci):

    os.system("clear")

    ilosc_substancji = len(lepkosci)

    lista_substancji = list(lepkosci.keys())

    lista_wybranych = []

    while True:
        print("Wybrane substancje: ({})".format(lista_wybranych), end="\n\n")
        print("1. Dodaj substancje")
        print("2. Usun substancje")
        print("3. Pokaz wykresy")
        print("4. Wyjdz")
        print("\n", end="")

        try:
            wybor = int(input("Co chcesz zrobic? (1-4): "))
        except ValueError:
            os.system("clear")
            print("Musisz podac liczbe!")
            continue

        os.system("clear")
        
        ilosc_wybranych = len(lista_wybranych) 
        
        if wybor == 1:

            if ilosc_wybranych >= 5:
                os.system("clear")
                print("Limit przekroczony!")
                continue

            i = 1
            for key, value in lepkosci.items():
                print("{}. {} ".format(i, key))
                i += 1

            try:
                wybrany_nr = int(input("Wybierz numer substancji sposrod listy (1-{}):".format(ilosc_substancji)))
            except ValueError:
                os.system("clear")
                print("Muisz podac liczbe!")
                continue

            if wybrany_nr < 1 or wybrany_nr > ilosc_substancji:
                os.system("clear")
                print("Nie ma takiego numeru!")
                continue
            
            if lista_substancji[wybrany_nr - 1] in lista_wybranych:
                os.system("clear")
                print("Substancja zostala juz wybrana!")
                continue

            lista_wybranych.append(lista_substancji[wybrany_nr - 1])

            os.system("clear")

        elif wybor == 2:

            if ilosc_wybranych < 1:
                os.system("clear")
                print("Nic nie wybrales!")
                continue

            print("Wybrane substancje: ({})".format(lista_wybranych))

            try:
                usun = int(input("Ktora substancje chcesz usunac?: "))
            except ValueError:
                os.system("clear")
                print("Musisz podac liczbe!")
                continue

            if usun < 1 or usun > ilosc_wybranych:
                os.system("clear")
                print("Nie ma takiego numeru!")
                continue

            lista_wybranych.pop(usun - 1)

            os.system("clear")

        elif wybor == 3:
            pass

        elif wybor == 4:
            sys.exit()

        else:
            print("Nie ma takiej opcji!")
    

if __name__ == "__main__":
    lepkosci = load_from_file("tabela-substancji-WMZF.txt")
    menu(lepkosci)
