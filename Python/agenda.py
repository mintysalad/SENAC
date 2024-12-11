import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

# Função para carregar os compromissos salvos
def carregar_compromissos():
    try:
        with open('compromissos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Função para salvar os compromissos
def salvar_compromisso():
    data_compromisso = entry_data.get()
    descricao_compromisso = entry_descricao.get()

    if not data_compromisso or not descricao_compromisso:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return
    
    try:
        datetime.strptime(data_compromisso, "%d/%m/%Y")  # Verifica o formato da data
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido! Use dd/mm/aaaa")
        return
    
    compromissos = carregar_compromissos()

    if data_compromisso in compromissos:
        messagebox.showwarning("Aviso", "Já existe um compromisso para esta data!")
    else:
        compromissos[data_compromisso] = descricao_compromisso
        with open('compromissos.json', 'w') as arquivo:
            json.dump(compromissos, arquivo)
        atualizar_lista()
        entry_data.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)

# Função para remover um compromisso
def remover_compromisso():
    data_compromisso = entry_data.get()
    if not data_compromisso:
        messagebox.showerror("Erro", "Por favor, insira uma data para remover um compromisso!")
        return
    
    compromissos = carregar_compromissos()

    if data_compromisso in compromissos:
        del compromissos[data_compromisso]
        with open('compromissos.json', 'w') as arquivo:
            json.dump(compromissos, arquivo)
        atualizar_lista()
        entry_data.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Não há compromisso para essa data!")

# Função para atualizar a lista de compromissos exibida na tela
def atualizar_lista():
    compromissos = carregar_compromissos()
    lista_compromissos.delete(0, tk.END)
    for data, descricao in compromissos.items():
        lista_compromissos.insert(tk.END, f"{data} - {descricao}")

# Interface Gráfica
root = tk.Tk()
root.title("Agenda Pessoal")
root.configure(bg="#4fc287")

# Entrada de dados
tk.Label(root, text="Data (dd/mm/aaaa):", bg= "#47ad79").grid(row=0, column=0, padx=10, pady=5)
entry_data = tk.Entry(root)
entry_data.grid(row=0, column=1, padx=10, pady=5)
entry_data.configure(bg="#47ad79")

tk.Label(root, text="Descrição do compromisso:", bg="#47ad79").grid(row=1, column=0, padx=10, pady=5)
entry_descricao = tk.Entry(root)
entry_descricao.grid(row=1, column=1, padx=10, pady=5)
entry_descricao.configure(bg="#47ad79")

# Botões
btn_salvar = tk.Button(root, text="Salvar Compromisso", bg= "#47ad79", command=salvar_compromisso)
btn_salvar.grid(row=2, column=0, columnspan=2, pady=5)

btn_remover = tk.Button(root, text="Remover Compromisso", bg="#47ad79", command=remover_compromisso)
btn_remover.grid(row=3, column=0, columnspan=2, pady=5)

# Lista de compromissos
tk.Label(root, text="Lista de Compromissos:", bg="#47ad79").grid(row=4, column=0, columnspan=2, pady=10)
lista_compromissos = tk.Listbox(root, height=10, width=50, bg="#47ad79")
lista_compromissos.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Atualizar lista ao iniciar
atualizar_lista()

root.mainloop()

# Como funciona:
# Interface Gráfica (Tkinter): A interface foi feita com a biblioteca tkinter e contém:

# Um campo de entrada para a data do compromisso.
# Um campo de entrada para a descrição do compromisso.
# Botões para salvar e remover compromissos.
# Uma lista para mostrar os compromissos salvos.
# Salvar Compromisso: Quando o usuário preenche a data e a descrição e clica no botão "Salvar Compromisso", o programa salva o compromisso em um arquivo JSON (compromissos.json).

# Remover Compromisso: O usuário pode remover um compromisso inserindo a data no campo e clicando no botão "Remover Compromisso". O compromisso correspondente será excluído do arquivo JSON.

# Exibição de Compromissos: A lista de compromissos é atualizada sempre que um compromisso é salvo ou removido.

# Dependências:
# tkinter (geralmente já vem com Python)
# json (já integrado no Python)
# Observações:
# Este programa não valida o formato de entrada do compromisso. Ele espera a data no formato dd/mm/aaaa.
# Se você quiser armazenar os compromissos em outro tipo de banco de dados, como SQLite, é possível modificar o código para usar um banco de dados.