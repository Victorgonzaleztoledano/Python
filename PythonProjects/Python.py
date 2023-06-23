'''
x = 3
y = 5
for i in range(x, y+1): print(i)
'''

#for n in range(1,7) :print('*' * n)

'''
def maximo (numero1, numero2):
    if numero1 > numero2 : return numero1
    else : return numero2
x = 4
y = 5
z = 6
i = 7
mayor1 = maximo(x, y)
mayor2 = maximo(z, i)
mayor3 = maximo(mayor1, mayor2)
print(mayor3)
'''

'''
numeros = 2, 6, 9, 4, 2, 10, 1
def media (numeros) :
    total = 0
    for i in range (len(numeros)):
        total = total + numeros[i]
    total = total / len(numeros)
    return total
print(media(numeros))
'''

'''
def media(numeros):
    suma = 0
    for i in range(len(numeros)):
        suma = suma + numeros[i]
    return suma / len(numeros)
numeros = [2, 5, 9, 10, 54, -5]
print(media(numeros))
'''

'''
palindromo = [2, 3, 6, 3, 6, 3, 2]
def verify (palindromo):
    y = len(palindromo) -1
    for i in range(len(palindromo)):
        if palindromo[i] == palindromo[y - i]:
            verificacion = True
        else: verificacion = False
        if verificacion != True:
            return verificacion
    return verificacion
print("¿Es un palíndromo?",verify(palindromo))
'''

'''
one = [-4, -2, -1, 1, 6, 7]
two = [-4, -2, -1, 0, 1, 6, 7]
def comunes (one, two):
    total = 0
    for i in range(len(one)):
        for j in range(len(two)):
            if one[i] == two[j]:
                total = total + 1
    return total
print("Tienen en común:",comunes(one, two),"numeros")
'''

'''
one = [-4, -3, 0, 2, 3, 4]
two = [-2, -1, 1, 5, 6]
def fusion (one, two):
    three = []
    j = 0
    k = 0
    while j < len(one) and k < len(two):
        if one[j] <= two[k]:
            three.append(one[j])
            j += 1
        else:
            three.append(two[k])
            k += 1
    while j < len(one):
        three.append(one[j])
        j += 1
    while k < len(two):
        three.append(two[k])
        k += 1
    return three
print("La fusión de los vectores quedaría así", fusion(one, two))
'''

