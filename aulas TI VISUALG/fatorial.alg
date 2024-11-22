algoritmo "fatorial"
// Função :
// Autor :
// Data : 22/11/2024
// Seção de Declarações 
var
   c, f, n: Inteiro
inicio
// Seção de Comandos
   Escreval("Digite um número: ", n)
   Leia(n)
   se(n = 0) entao
        Escreval(1)
   senao
        f <- n
        c <- 1
        enquanto (c < n)faca
                 f <- f*(n-c)
                 c <- c + 1
                 Escreval(f)
        fimenquanto
   fimse

fimalgoritmo
