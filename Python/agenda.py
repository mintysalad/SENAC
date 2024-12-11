import tkinter as tk
from tkinter import messagebox, colorchooser
from tkcalendar import Calendar

class AgendaPessoal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Pessoal")
        self.root.geometry("800x500")

        # Lista de compromissos
        self.compromissos = []

        # Criar o fundo com o padrão de estrelas
        self.criar_fundo_estrelas()

        # Criando os widgets
        self.criar_widgets()

    def criar_fundo_estrelas(self):
        # Criando um canvas para desenhar o fundo
        self.canvas = tk.Canvas(self.root, width=800, height=500)
        self.canvas.grid(row=0, column=0, rowspan=10, columnspan=10)

        # Desenhando o padrão de estrelas no fundo
        for y in range(0, 500, 40):  # Padrão repetido na vertical
            for x in range(0, 800, 40):  # Padrão repetido na horizontal
                self.desenhar_estrela(x, y)

    def desenhar_estrela(self, x, y):
        # Desenha uma estrela no canvas em (x, y)
        size = 15  # Tamanho da estrela
        self.canvas.create_polygon(
            x + size * 0.5, y, 
            x + size * 0.7, y + size * 0.3, 
            x + size, y + size * 0.3, 
            x + size * 0.8, y + size * 0.5, 
            x + size * 0.9, y + size * 0.8, 
            x + size * 0.5, y + size * 0.6, 
            x + size * 0.1, y + size * 0.8, 
            x + size * 0.2, y + size * 0.5, 
            x, y + size * 0.3, 
            x + size * 0.3, y + size * 0.3, 
            fill="#fce279", outline="#fce279"
        )

    def criar_widgets(self):
        # Data do compromisso
        self.label_data = tk.Label(self.root, text="Data do Compromisso:", bg="#ffe1a8")
        self.label_data.grid(row=0, column=0, padx=10, pady=5)
        self.data_entry = tk.Entry(self.root, bg="#ffe1a8")
        self.data_entry.grid(row=0, column=1, padx=10, pady=5)

        # Descrição
        self.label_descricao = tk.Label(self.root, text="Descrição:", bg="#ffe1a8")
        self.label_descricao.grid(row=1, column=0, padx=10, pady=5)
        self.descricao_entry = tk.Entry(self.root, bg="#ffe1a8")
        self.descricao_entry.grid(row=1, column=1, padx=10, pady=5)

        # Cor
        self.label_cor = tk.Label(self.root, text="Selecione a Cor:", bg="#ffe1a8")
        self.label_cor.grid(row=2, column=0, padx=10, pady=5)
        self.botao_cor = tk.Button(self.root, text="Escolher Cor", command=self.selecionar_cor, bg="#f7d697")
        self.botao_cor.grid(row=2, column=1, padx=10, pady=5)

        # Botões
        self.botao_salvar = tk.Button(self.root, text="Salvar Compromisso", command=self.salvar_compromisso, bg="#f7d697")
        self.botao_salvar.grid(row=3, column=0, padx=10, pady=10)
        self.botao_remover = tk.Button(self.root, text="Remover Todos", command=self.remover_todos_compromissos, bg="#f7d697")
        self.botao_remover.grid(row=3, column=1, padx=10, pady=10)

        # Calendário
        self.label_calendario = tk.Label(self.root, text="Calendário de Compromissos:", bg="#ffe1a8")
        self.label_calendario.grid(row=0, column=2, padx=10, pady=5)
        
        # Criar um calendário do ano
        self.calendario = Calendar(self.root, selectmode="day", year=2024, month=12, day=11)
        self.calendario.grid(row=1, column=2, padx=10, pady=5)
        self.calendario.bind("<<CalendarSelected>>", self.data_selecionada)

        # Lista de compromissos
        self.lista_compromissos_label = tk.Label(self.root, text="Compromissos Agendados:", bg="#ffe1a8")
        self.lista_compromissos_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.lista_compromissos = tk.Listbox(self.root, width=50, height=10, bg="#ffe1a8")
        self.lista_compromissos.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def selecionar_cor(self):
        # Abre o seletor de cores
        cor = colorchooser.askcolor()[1]
        if cor:
            self.cor_selecionada = cor

    def salvar_compromisso(self):
        # Obtém os dados dos campos
        data = self.data_entry.get()
        descricao = self.descricao_entry.get()

        if not data or not descricao:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        # Adiciona o compromisso à lista
        compromisso = {"data": data, "descricao": descricao, "cor": getattr(self, "cor_selecionada", "#FFFFFF")}
        self.compromissos.append(compromisso)

        # Atualiza a lista de compromissos exibida
        self.atualizar_lista_compromissos()

        # Limpa os campos
        self.data_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)

    def remover_todos_compromissos(self):
        # Remove todos os compromissos
        self.compromissos.clear()
        self.atualizar_lista_compromissos()

    def atualizar_lista_compromissos(self):
        # Atualiza o conteúdo da lista de compromissos exibida
        self.lista_compromissos.delete(0, tk.END)
        for compromisso in self.compromissos:
            display_text = f"{compromisso['data']} - {compromisso['descricao']}"
            self.lista_compromissos.insert(tk.END, display_text)

    def data_selecionada(self, event):
        # Preenche o campo de data com a data selecionada no calendário
        data_selecionada = self.calendario.get_date()
        self.data_entry.delete(0, tk.END)
        self.data_entry.insert(0, data_selecionada)

# Criar a janela principal
root = tk.Tk()

# Criar a instância da agenda pessoal
agenda = AgendaPessoal(root)

# Iniciar o loop da interface gráfica
root.mainloop()
