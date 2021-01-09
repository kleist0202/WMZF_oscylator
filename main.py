import sys
import os
from compute_functions import Amplitudy, Energie
from plots_module import *


def load_from_file(file_name):
    d = {}
    with open(file_name, 'r') as f:
        next(f)
        for i in f:
            s = i.split()
            d[s[0]] = float(s[1])

    return d

def menu(lepkosci):

    if os.name == "nt":
        wyczysc = "cls"
    else:
        wyczysc = "clear"

    os.system(wyczysc)

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
            os.system(wyczysc)
            print("Musisz podac liczbe!")
            continue

        os.system(wyczysc)
        
        ilosc_wybranych = len(lista_wybranych) 
        
        if wybor == 1: ########## dodaj substancje ##########

            if ilosc_wybranych >= 5:
                os.system(wyczysc)
                print("Limit przekroczony!")
                continue

            i = 1
            for key, value in lepkosci.items():
                print("{}. {} ".format(i, key))
                i += 1

            try:
                wybrany_nr = int(input("Wybierz numer substancji sposrod listy (1-{}):".format(ilosc_substancji)))
            except ValueError:
                os.system(wyczysc)
                print("Muisz podac liczbe!")
                continue

            if wybrany_nr < 1 or wybrany_nr > ilosc_substancji:
                os.system(wyczysc)
                print("Nie ma takiego numeru!")
                continue
            
            if lista_substancji[wybrany_nr - 1] in lista_wybranych:
                os.system(wyczysc)
                print("Substancja zostala juz wybrana!")
                continue

            lista_wybranych.append(lista_substancji[wybrany_nr - 1])

            os.system(wyczysc)

        elif wybor == 2: ########## usun substancje ##########

            if ilosc_wybranych < 1:
                os.system(wyczysc)
                print("Nic nie wybrales!")
                continue

            for num, value in enumerate(lista_wybranych):
                print("{}. {} ".format(num + 1, value))
            
            #print("Wybrane substancje: ({})".format(lista_wybranych))

            try:
                usun = int(input("Ktora substancje chcesz usunac?: "))
            except ValueError:
                os.system(wyczysc)
                print("Musisz podac liczbe!")
                continue

            if usun < 1 or usun > ilosc_wybranych:
                os.system(wyczysc)
                print("Nie ma takiego numeru!")
                continue

            lista_wybranych.pop(usun - 1)

            os.system(wyczysc)

        elif wybor == 3: ########## pokaz wykresy ##########

            do_wykresow_ampl = {}
            do_wykresow_ener = {}

            if len(lista_wybranych) == 0: 
                os.system(wyczysc)
                print("Nie wybrales substancji!")
                continue

            ########### promien ###########
            print('Wpisz promień kuli (w metrach): ')
            try:
                R = float(input())
            except ValueError:
                os.system(wyczysc)
                print("Musisz podac liczbe!")
                continue

            if R <= 0:
                os.system(wyczysc)
                print("Liczba musi byc dodatnia!")
                continue

            ########### masa ############
            print('Wpisz masę kuli (w kilogramach): ')
            try:
                m = float(input())
            except ValueError:
                os.system(wyczysc)
                print("Musisz podac liczbe!")
                continue

            if m <= 0:
                os.system(wyczysc)
                print("Liczba musi byc dodatnia!")
                continue
            
            ########### czas maksymalny ###########
            print('Wpisz czas maksymalny (w sekundach): ')
            try:
                t_max = int(input())
            except ValueError: 
                os.system(wyczysc)
                print("Musisz podać liczbe!")
                continue

            if t_max <= 0:
                os.system(wyczysc)
                print("Liczba musi byc dodatnia!")
                continue

            ########### sprezystosc ###########
            k = 0.1 

            for i in lista_wybranych:
                do_wykresow_ampl[i] = Amplitudy(lepkosci[i], m, R, k, t_max)

            for i in lista_wybranych:
                do_wykresow_ener[i] = Energie(lepkosci[i], m, R, k, t_max)
            
            make_plot(do_wykresow_ampl, do_wykresow_ener)

            os.system(wyczysc)

        elif wybor == 4: ########## wyjdz ##########

            sys.exit()

        else:
            print("Nie ma takiej opcji!")
    

if __name__ == "__main__":
    lepkosci = load_from_file("tabela-substancji-WMZF.txt")
    menu(lepkosci)
