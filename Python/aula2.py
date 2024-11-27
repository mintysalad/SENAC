faturamento = 1200
custo = 700
lucro = faturamento - custo
margemLucro =lucro / faturamento

print(f"Faturamento da empresa: R${faturamento:.2f}Custo: R$ {custo:.2f} Lucro: R${lucro:.2f}")

emailCliente = "meowmeowmeow@gmail.com"

print(emailCliente)

# Maiusculas
emailCliente = emailCliente.upper()
print(emailCliente)

# Minusculas
emailCliente = emailCliente.lower()
print(emailCliente)

# Encontrar o @ ou outros caracteres quaisquer
print(emailCliente.find("@"))

# Tamanho do Texto:
print(len(emailCliente))

# Pegar um Caracter
print(emailCliente[3])
print(emailCliente[-4]) # se for negativo, vai pesquisar por trás.

# Pegar uma parte do Texto
print(emailCliente[:8])
print(emailCliente[8:])
print(emailCliente[4:12])

# Trocar uma parte do Texto
novoEmail = emailCliente.replace("gmail.com", "yahoo.com.br")
print(emailCliente)
print(novoEmail)

nome = "mae my love"
print(nome.capitalize())
print(nome.title())
print(nome.upper())
print(nome.lower())

# Pegar o servidor do Email
posicaoArroba = emailCliente.find("@") + 1
servidor = emailCliente[posicaoArroba:]
print(servidor)

# Pegar o primeiro Nome
posicaoEspaco = nome.find(" ") 
primeiroNome = nome[:posicaoEspaco].title()
print(primeiroNome)

# Pegar Sobrenome
sobrenome = nome[posicaoEspaco + 1:].title()
print(sobrenome)
print(f"Faturamento da empresa: R${faturamento:.2f}Custo: R$ {custo:.2f} Lucro: R${lucro:.2f} Margem: {margemLucro: .0%}")