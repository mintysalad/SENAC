algoritmo "calculo imc"
// Função :
// Autor :
// Data : 21/11/2024
// Seção de Declarações 
var
   nome: Caracter
   imc, peso, altura: Real
inicio
// Seção de Comandos
   Escreval ("Digite o seu nome: ")
   Leia (nome)
   Escreval ("Digite o seu peso: ")
   Leia (peso)
   Escreval ("Digite a sua altura:  ")
   Leia (altura)
   imc<- peso / (altura * altura)
   Escreval ("o IMC de ", nome, " é ", imc)
   
fimalgoritmo
