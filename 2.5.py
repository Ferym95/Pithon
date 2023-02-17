b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n-1))

cm = int(input())
m = cm // 100
print(m)

sch = int(input())
fru = int(input())

print(fru//sch)
print(fru%sch)

guys = int(input())
print(guys // 2 + guys % 2)

n = int(input())
m = 4
k = (n + m - 1) // m
print(k)

m = int(input())
h = m // 60    # часы    целочисленное деление
s = m % 60     # минуты  остаток от деления

print(m, "мин - это", h, "час", s, "минут.")

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100

print("Сумма цифр =", c + b + a)
print("Произведение цифр =", c * b * a)

abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(a,b,c, sep='')
print(a,c,b, sep='')
print(b,a,c, sep='')
print(b,c,a, sep='')
print(c,a,b, sep='')
print(c,b,a, sep='')

m = int(input())
m1 = m // 1000
m2 = (m // 100) % 10
m3 = (m // 10) % 10
m4 = m % 10
print("Цифра в позиции тысяч равна", m1)
print("Цифра в позиции сотен равна", m2)
print("Цифра в позиции десятков равна", m3)
print("Цифра в позиции единиц равна", m4)
