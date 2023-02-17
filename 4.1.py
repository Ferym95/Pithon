a = input()
b = input()
if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')

    a = int(input())

    if a % 2 == 0:
        print('Четное')
    else:
        print('Нечетное')

a = int(input())
first = a // 1000
second = a // 100 - (a // 1000 * 10)
third = (a % 100 - a % 10) / 10
last = a % 10
if first + last == second - third:
    print('ДА')
else:
    print('НЕТ')

age = int(input())
    if age >= 18:
        print('Доступ разрешен')
    else:
        print('Доступ запрещен'

a = int(input())
b = int(input())
c = int(input())
if b - a == c - b:
    print('YES')
else:
    print('NO')

a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)





a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)


age = int(input())

if age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if age >= 60:
    print('старость')

 age = int(input())

    if age <= 13:
            print('детство')
    if 14 <= age <= 24:
            print('молодость')
    if 25 <= age <= 59:
            print('зрелость')
    if age >= 60:
            print('старость')