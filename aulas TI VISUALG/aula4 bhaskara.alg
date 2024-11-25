algoritmo "aula4 bhaskara"
// Fun��o :
// Autor :
// Data : 25/11/2024
// Se��o de Declara��es
var
a, b,c, xm, xn, d, r, dn: Real
inicio
// Se��o de Comandos
Escreval("Digite o valor de A: ")
Leia(a)
Escreval
Escreval
Escreval("Digite o valor de B: ")
Leia(b)
Escreval
Escreval
Escreval("Digite o valor de C: ")
Leia(c)
Escreval
Escreval
d <- ((b*b)-(4*a*c))
Escreval("Delta: ", d)
se d<0 entao
   dn <- -(d)
   d <- dn
   r <- RaizQ(d)
   Escreval("Raiz de Delta: ", r)
   xm <- ((-b + (r)) / (2*a))
   Escreval
   Escreval
   Escreval("O valor de X1 �: ", xm, "!")
   Escreval
   Escreval
   xn <- ((b - (r)) / (2*a))
   Escreval("O valor de X2 �: ", xn, "!")
 senao
 r <-RaizQ(d)
 Escreval("Raiz de Delta: ", r)
 Escreval
 Escreval
 xm <- ((b + (r)) / (2*a))
 Escreval ("O valor de X1 �: ", xm)
 Escreval
 Escreval
 xn <- ((b - (r)) / (2*a))
 Escreval("O valor de X2 �: ", xn)
 fimse
fimalgoritmo

