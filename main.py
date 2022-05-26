#openpyxl, pillow 9.0.1, numpy, pandas, matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1
#Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx
print("Zadanie 1")
xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, header=0)
print(df)

#Zadanie 2
#Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
#tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print("Zadanie 2")
#print(df['Liczba'] > 1000, 'Imie')
#a = input('podaj rok od 2000 do 2017:\n')
#a = int(a)
a = 2000
print(df['Imie'][(df['Liczba'] > 1000) & (df['Rok'] == a)])
print("###############################")

#tylko rekordy gdzie nadane imię jest takie jak Twoje
print(df['Imie'][(df['Imie'] == 'PRZEMYSŁAW')])
print("###############################")

#sumę wszystkich urodzonych dzieci w całym danym okresie
print(df.agg({'Liczba':['sum']}))
print("###############################")

#sumę dzieci urodzonych w latach 2000-2005
b = (df['Liczba'][(df['Rok'] >= 2000) & (df['Rok'] <= 2005)])
print(b)
print("Suma dzieci urodzonych w latach 2000-2005: ", df.loc[(df['Rok'] >= 2000) & (df['Rok'] <= 2005), 'Liczba'].sum())
print("###############################")

#sumę urodzonych chłopców i dziewczynek
ch = df.loc[(df['Plec'] == 'M'), 'Plec'].count()
dz = df.loc[(df['Plec'] == 'K'), 'Plec'].count()
print("Suma urodzonych chlopcow: ", ch)
print("Suma urodzonych dziewczynek: ", dz)
print("Laczna suma: ", (df.loc[(df['Plec'] == 'K'), 'Plec'].count()) + (df.loc[(df['Plec'] == 'M'), 'Plec'].count()))
print("###############################")

#najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)
for i in range(2000, 2018, 1):
    a = df.loc[(df['Plec'] == 'M') & (df['Rok'] == i), 'Liczba'].max()
    name = df.loc[(df['Liczba'] == a)]
    print(name)
    a = df.loc[(df['Plec'] == 'K') & (df['Rok'] == i), 'Liczba'].max()
    name = df.loc[(df['Liczba'] == a)]
    print(name)
    print("\n")
print("###############################")

#najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
print("Najbardziej popularne imie dziewczynki i chlopca w calym danym okresie")
a = df.loc[(df['Plec'] == 'K'), 'Liczba'].max()
name = df.loc[(df['Liczba'] == a)]
print(name)
a = df.loc[(df['Plec'] == 'M'), 'Liczba'].max()
name = df.loc[(df['Liczba'] == a)]
print(name)
print("###############################")
print("Rozszerzenie zadania:")
startRok = input("Podaj poczatkowy rok (min 2000): ")
startRok = int(startRok)
koniecRok = input("Podaj koncowy rok (max 2017): ")
koniecRok = int(koniecRok)
a = df.loc[(df['Plec'] == 'M') & (df['Rok'] >= startRok) & (df['Rok'] <= koniecRok), 'Liczba'].max()
name = df.loc[(df['Liczba'] == a)]
print(name)
a = df.loc[(df['Plec'] == 'K') & (df['Rok'] >= startRok) & (df['Rok'] <= koniecRok), 'Liczba'].max()
name = df.loc[(df['Liczba'] == a)]
print(name)

#Zadanie 3
#Wczytaj plik /datasets/zamowienia.csv a następnie wyświetl:
print("Zadanie 3")
df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=',')
print(df)
print("###############################")
#listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
print(df['Sprzedawca'].unique())
print("###############################")
#5 najwyższych wartości zamówień
#print(df.loc[(df.index) == 0])
#print(df['Utarg'].astype(float).nlargest(n=5))
for i in range(0, 5, 1):
    a = df.loc[df.index == df['Utarg'].astype(float).nlargest(n=5).index[i]]
    print(a, "\n")
print("###############################")
#ilość zamówień złożonych przez każdego sprzedawcę
a = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
print(a)
print("###############################")
#sumę zamówień dla każdego kraju
df['Utarg'] = pd.to_numeric(df['Utarg'])
a = df.groupby(['Kraj']).agg({'Utarg':['sum']})
print(a)
print("###############################")
#sumę zamówień dla roku 2005, dla sprzedawców z Polski
df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia']) #konwersja stringa na date (pandas)
#df['Rok'] = pd.DatetimeIndex(df['Data zamowienia']).year #utworzenie nowej kolumny 'Rok'!
#a = df.loc[(df['Kraj'] == 'Polska') & (df['Rok'] == 2005)]
a = df.loc[(df['Kraj'] == 'Polska') & (pd.DatetimeIndex(df['Data zamowienia']).year == 2005), 'Utarg'].sum()
print("Suma zamowien dla roku 2005, dla sprzedawcow z Polski: ", a)
print("###############################")
#średnią kwotę zamówienia w 2004 roku
a = df.loc[(pd.DatetimeIndex(df['Data zamowienia']).year == 2004), 'Utarg'].mean()
print("Srednia kwota zamowienia w 2004: ", a)
print("###############################")
#zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
a = df[pd.DatetimeIndex(df['Data zamowienia']).year == 2004]
a.to_csv('zamowienia_2004.csv')
a = df[pd.DatetimeIndex(df['Data zamowienia']).year == 2005]
a.to_csv('zamowienia_2005.csv')
print("Dane pomyslnie zapisano do plikow")
print("THE END")