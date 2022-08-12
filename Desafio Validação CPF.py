"""
CPF modelo: 168.995.350-09

1 * 10  = 10            #       1 * 11  = 11
6 * 9   = 54            #       6 * 10  = 60
8 * 8   = 64            #       8 * 9   = 72
9 * 7   = 63            #       9 * 8   = 72
9 * 6   = 54            #       5 * 6   = 30
5 * 5   = 25            #       3 * 5   = 15
3 * 4   = 12            #       5 * 4   = 20
5 * 3   = 15            #       0 * 3   = 0
0 * 2   = 0             #       0 * 2   = 0
          297           #                 343
11 - (297 % 11) = 11    #   11 - (343 % 11) = 9
11 > 9 = 0              #
Digito 1 = 0            #   Digito 2 = 9
"""
cpf = input('Digite o CPF desejado sem pontos ou traços: ')
i = 10
j = 11
x1 = 0
x2 = 0
for numero in cpf[0:9]:
    numero = int(numero)
    numero = numero * i
    lista = numero
    x1 += numero
    i -= 1
n2 = (11 - (x1 % 11))
if n2 > 9:
    n2 = 0
else:
    n2 = n2

for numero in cpf[0:10]:
    numero = int(numero)
    numero = numero * j
    lista = numero
    x2 += numero
    j -= 1
n3 = (11 - (x2 % 11))
if n3 > 9:
    n3 = 0
else:
    n3 = n3
n2 = str(n2)
n3 = str(n3)
novo_cpf = cpf[0:9] + n2 + n3
if cpf == novo_cpf:
    print('Válido!')
else:
    print('Inválido')