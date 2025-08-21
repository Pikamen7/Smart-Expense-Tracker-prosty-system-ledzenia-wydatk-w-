from datetime import date

lista_zakupów = [
    [20, "biedronka", date(2023, 10, 1)],
    [210, "buty", date(2023, 10, 2)],
    [30, "książki", date(2023, 10, 3)],
    [50, "kino", date(2025, 6, 4)],
    [100, "restauracja", date(2025, 7, 5)],
]

def suma_wydatków(lista):
    suma = 0
    for wydatek in lista:
        suma += wydatek[0]
    return suma

def suma_miesiaca(lista, rok, miesiac):
    suma1 = 0
    for wydatek in lista:
        data = wydatek[2]
        if data.year == rok and data.month == miesiac:
            suma1 += wydatek[0]
    return suma1
def kat_wydatku(opis):
    opis = opis.lower()
    slowo_kluczowe = ["jedzenie", "restauracja","kino","pizza", "biedronka"]
    for slowo in slowo_kluczowe:
        if slowo in opis:
            return "Jedzenie"
    opis = opis.lower()
    slowo_kluczowe = ["buty", "koszulka","spodnie","spodenki", "skarpetki", "kurtka", "plaszcz", "czapka", "rękawiczki", "szalik", "pasek", "portfel", "torebka", "torba", "plecak", "walizka", "bielizna", "sukienka", "spodnica", "kombinezon", "kostium kąpielowy", "rajstopy"]
    for slowo in slowo_kluczowe:
        if slowo in opis:
                return "Ubrania"
    return "Inne"

print("Liczba wydatków:", len(lista_zakupów))
print("Najdroższy:", max(lista_zakupów, key=lambda x: x[0]))
print("Suma wszystkich:", suma_wydatków(lista_zakupów))
print("Suma lipiec 2025:", suma_miesiaca(lista_zakupów, 2025, 7))
for wydatek in lista_zakupów:
    opis = wydatek[1]
    print(opis, "-->", kat_wydatku(opis))


