# Napisz program symulujący loterię. Program powinien wykorzystywać
# listę o nazwie lottery złożoną z pięciu losowych liczb całkowitych z zakresu od 0 do
# 9. Program powinien prosić użytkownika o podanie pięciu liczb, zapisywać je na liście o
# nazwie user, a następnie porównywać odpowiednie elementy obu tablic i liczyć zgodne
# liczby. Program ma wyświetlać losowe liczby zapisane w tablicy lottery i liczbę zgodnych
# liczb. Jeżeli wszystkie liczby będą zgodne, program ma wyświetlać komunikat, że użytkownik
# wygrał główną nagrodę.

from random import sample

# available_numbers = list(range(0, 10))
# # available_numbers = [0,1,2,3,4,5,6,7,8,9]
# shuffle(available_numbers)
# # available_numbers = [4,3,6,1,8,7,9,0,2,5]
# lottery = available_numbers[0:5]
# # lottery = [4,3,6,1,8]

lottery = sample(range(0, 10), 5)

user = []
while len(user) < 5:
    number = int(input("Podaj liczbę: "))
    if number in user:
        print("Ta liczba już została podana")
    else:
        user.append(number)

k = 0
for x in lottery:
    if x in user:
        k = k + 1

print("Wylosowane liczby:", lottery)
print("Trafiono liczb:", k)
if k == 5:
    print("Zwycięstwo")
else:
    print("Spróbuj ponownie")
