# Napisz program, który będzie pomocnikiem w rozwiązywaniu krzyżówek.
# Jako przykład załóżmy, że w krzyżówce poszukiwane hasło ma postać:
# _ o _ _ u t _ _
# Zadaniem programu będzie wyszukanie wyrazów, które pasują do podanego w skryp-
# cie wzorca. Wykorzystaj w programie plik slownik pl.txt (słownik z polskimi wyrazami).
# Uwaga: program nie powinien rozróżniać wielkich i małych liter

import codecs
string = "pliki/slownik_pl.txt"
file = codecs.open(string, "r", 'windows-1250')
words = file.read().splitlines()

pattern = input("Podaj wzorzec: ").lower()

possible = []
for word in words:
    word = word.lower()
    if len(pattern) == len(word):
        matches = True
        for i in range(0, len(pattern)):
            if pattern[i] != '_' and pattern[i] != word[i]:
                matches = False
                break
        if matches:
            possible.append(word)

print(possible)
