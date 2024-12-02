# # Média

# n1 = n2 = m = float
# print("Valor da média entre dois números!")
# n1 = float(input("Digite o primeiro valor: "))
# n2 = float(input("Digite o segundo valor: "))

# m = (n1 + n2)/2
# print("O valor da média é de: ", m)

# # Par ou Ímpar

# n = float(input("Digite um número para saber se é par ou ímpar: "))
# resto = n % 2
# if resto == 0:
#     print("Este número é par.")
# else:
#     print("Este número é ímpar.")

#     # Celsius pra Farenheit

# c = float(input('Digite a temperatura em °c: '))
# f = float((9 * c) / 5) + 32
# print('A temperatura em fahrenheit: {0}°F'.format(f))

# # Fatorial

# c = f = n = 0

# n = int(input("Digite um número para saber seu fatorial: "))

# if (n == 0):
#     print(1)
# else:
#    f = n
#    c = 1
#    while (c < n):
#         f = f*(n - c)
#         c = c + 1
# print(f)

# # Palíndromo

# pali = input('Digite um palavra: ').upper().replace(' ','')

# if pali == pali[:: -1]:
#     print('A palavra é Palindroma','\n')
#     print('Palavra Invertida: {}'.format(pali),'\n')
# else:
#     print('A palavra não é Palindroma','\n')

# print('Palavra Digitada: {} '.format(pali),'\n')

# Contar Vogais

# frase = input("Digite uma palavra/frase: ")
# vogais = "aeiou"

# frase = frase.lower()

# total = 0
# for vogal in vogais:
#     total += frase.count(vogal)

# print("Total: ", total)

# Maior valor em Lista

# notas = input("Digite uma sequência de números: ").split()
# for n in range(0, len (notas)):
#     notas[n] = int(notas[n])
# print(notas[n])

# maior = 0
# for nota in notas:
#     if nota > maior:
#         maior = nota
# print("O maior valor é: ", maior)

# Ordem Crescente

# n1 = int(input('Digite um número '))
# n2 = int(input('Digite outro '))
# n3 = int(input('Digite outro ')) 
# n4 = int(input('Digite outro '))
# n5 = int(input('Digite outro '))

# Lsta=[n1,n2,n3,n4,n5]
# print('Essa é a lista em ordem crescente:',sorted(Lsta))

# Números Primos
# number = int(input("Digite um número: "))
# if number > 1:
#     for i in range(2, number):
#         if number % i == 0:
#             print(number, 'não é primo')
#             break
#     else:
#         print(number, 'é primo')

# Juros

capital_inicial = float(input('Digite o depósito inicial: R$'))
i = float(input('Agora, digite a taxa de juros de uma poupança: '))
i = (i/100) # Definindo o valor de i separadamente para deixar o código mais limpo
t = 1   # Contador dos meses
aporte = 0 # Não coloque c2. É muito confuso.

while t < 24:
    if t == 1:
        m = capital_inicial + (capital_inicial * i) # Ou: m = capital_inicial * (1 + i)
        print(f'\nNo mês {t}, o valor dos juros será igual a R${m:.2f}')
    else:
        print(f'\nNo mês {t}, o valor dos juros será igual a R${m:.2f}')

    t = t + 1 # Mesma coisa escrever: t += 1

    op = input(f'Deseja realizar um depósito para o {t}° mês[S/N]? ').strip().upper()[0]
    while op != 'S' and op != 'N':
        op = input(f'OPÇÃO INVÁLIDA! Deseja realizar um depósito para o {t}° mês[S/N]? ').strip().upper()[0]

    if op == 'S':
        aporte = float(input(f'Digite o valor do depósito do {t}° mês: R$'))
    else:
        aporte = 0


    m = m + (m * i) + aporte # Ou: m = m * (1 + i) + aporte

ganho_com_juros = m - capital_inicial # (montante final - capital inicial)
print(f'No total, a quantidade de reais ganha com os JUROS COMPOSTOS será igual a R${ganho_com_juros}')