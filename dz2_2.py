a = input('Введите значение переменной a:')
b = input('Введите значение переменной b:')
c = input('Введите значение переменной c:')

chislitel = (float(a)**2) + (float(b)**2)
znamenatel = (3*float(b)) - 4
chislitel2 = 4*(float(c)**5)
znamenatel2 = 6

delimoe = chislitel / znamenatel
delitel = chislitel2 / znamenatel2

nepolnoe_chastnoe = delimoe // delitel
ostatok = delimoe % delitel

print(float(round(chislitel, 2)))
print(float(round(znamenatel, 2)))
print(float(round(chislitel2, 2)))
print(float(round(znamenatel2, 2)))
print(float(round(delimoe, 2)))
print(float(round(delitel, 2)) ,'\n')
print('Целая часть', round(nepolnoe_chastnoe, 2))
print('Остаток от деления', round(ostatok, 2))
