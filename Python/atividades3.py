#1) Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.

listaNumero = []
print ('Informe os 5 numeros')
for i in range(5):
	listaNumero.append(input('Numero '+ str(i+1) + ':\n'))
print (listaNumero) 

#2) Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.

listaNumerosReais = []
print ('Informe os 10 numeros reais')
for i in range(10):
	listaNumerosReais.append(int(input('Numero '+ str(i+1) + ':\n')))
listaNumerosReais.reverse()
print (listaNumerosReais) 

#3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

listaNotas = []
media = 0
print ('Informe as 4 notas')
for i in range(4):
	listaNotas.append(float(input('Nota '+ str(i+1) + ':\n')))
	media += listaNotas[i]
media = media/4
print (listaNotas) 
print (media)
