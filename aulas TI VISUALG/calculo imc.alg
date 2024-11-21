algoritmo "calculo imc"
// Fun��o :
// Autor :
// Data : 21/11/2024
// Se��o de Declara��es 
var
   nome: Caracter
   imc, peso, altura: Real
inicio
// Se��o de Comandos
   Escreval ("Digite o seu nome: ")
   Leia (nome)
   Escreval ("Digite o seu peso: ")
   Leia (peso)
   Escreval ("Digite a sua altura:  ")
   Leia (altura)
   imc<- peso / (altura * altura)
   Escreval ("o IMC de ", nome, " � ", imc)
   Escreval ("Tabela IMC")
   Escreval ("Magreza: <18,5")
   Escreval ("Normal: 18,5 a 24,9")
   Escreval ("Sobrepeso: 25 a 29,9")
   Escreval ("Obesidade: >30")
   
fimalgoritmo
