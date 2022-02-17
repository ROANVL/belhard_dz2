a = input('Введите значение переменной a:')
b = input('Введите значение переменной b:')
c = input('Введите значение переменной c:')

numerator = (float(a)**2) + (float(b)**2)
denominator = (3*float(b)) - 4
numerator2 = 4*(float(c)**5)
denominator = 6

divisible = numerator / denominatorl
divider = numerator2 / denominator2

nepolnoe_chastnoe = divisible // divider
ostatok = delimoe % divider

print(float(round(numerator, 2)))
print(float(round(denominatorl, 2)))
print(float(round(numerator2, 2)))
print(float(round(denominatorl2, 2)))
print(float(round(divisible, 2)))
print(float(round(divider, 2)) ,'\n')
print('Целая часть', round(nepolnoe_chastnoe, 2))
print('Остаток от деления', round(ostatok, 2))
