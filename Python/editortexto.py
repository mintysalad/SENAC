import customtkinter as ctk
from tkinter import filedialog, messagebox, Menu
import os

class TextEditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Editor de Texto Básico ;D")
        self.geometry("800x600")

        self.file_path = None

        # Configuração da interface
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        # Área de texto
        self.text_area = ctk.CTkTextbox(self, wrap="word", font=("Arial", 14))
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Alternância de tema
        self.theme_switch = ctk.CTkSwitch(self, text="Tema Claro/Escuro", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def create_menu(self):
        # Menubar padrão do Tkinter
        self.menu_bar = Menu(self)

        # Menu Arquivo
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Novo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_command(label="Salvar Como", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.quit)

        self.menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        # Associar menubar à janela
        self.config(menu=self.menu_bar)

    def new_file(self):
        if self.confirm_discard_changes():
            self.text_area.delete("1.0", "end")
            self.file_path = None
            self.title("Editor de Texto Básico - Novo Arquivo :3")

    def open_file(self):
        if self.confirm_discard_changes():
            file_path = filedialog.askopenfilename(filetypes=[
                ("Arquivos de Texto", "*.txt"),
                ("Markdown", "*.md"),
                ("Todos os Arquivos", ".")
            ])
            if file_path:
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                    self.text_area.delete("1.0", "end")
                    self.text_area.insert("1.0", content)
                    self.file_path = file_path
                    self.title(f"Editor de Texto Básico - {os.path.basename(file_path)}")
                except Exception as e:
                    messagebox.showerror("Erro ao Abrir Arquivo", str(e))

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get("1.0", "end-1c"))
                messagebox.showinfo("Salvar Arquivo", "Arquivo salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro ao Salvar Arquivo D:", str(e))
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
            ("Arquivos de Texto", "*.txt"),
            ("Markdown", "*.md"),
            ("Todos os Arquivos", ".")
        ])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_area.get("1.0", "end-1c"))
                self.file_path = file_path
                self.title(f"Editor de Texto Básico - {os.path.basename(file_path)}")
                messagebox.showinfo("Salvar Arquivo", "Arquivo salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro ao Salvar Arquivo", str(e))

    def confirm_discard_changes(self):
        if self.text_area.edit_modified():
            response = messagebox.askyesnocancel("Descartar Alterações", "Deseja salvar as alterações antes de continuar?")
            if response:  # Sim
                self.save_file()
            return response is not None
        return True

    def toggle_theme(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

if __name__ == "__main__":
    app = TextEditorApp()
    app.mainloop()