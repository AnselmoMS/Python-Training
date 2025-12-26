import customtkinter as ctk
from tkinter import messagebox

# Configuração global de aparência (O "Skin Manager" do Python)
ctk.set_appearance_mode("dark")  # "dark", "light" ou "system"
ctk.set_default_color_theme("blue") # "blue", "green", "dark-blue"

class FrmTaskCustomTkinterView:
    def __init__(self):
        # Em vez de tk.Tk(), usamos ctk.CTk()
        self.root = ctk.CTk()
        self.root.title("Gestor de Tarefas 2025")
        self.root.geometry("600x500")

        # Título com fonte moderna
        self.label_titulo = ctk.CTkLabel(self.root, text="Minhas Tarefas", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # Botão arredondado (estilo moderno)
        self.btn_carregar = ctk.CTkButton(
            self.root, 
            text="Carregar Tarefas", 
            command=None, # Será definido pelo Presenter
            corner_radius=10,
            hover_color="#2c3e50"
        )
        self.btn_carregar.pack(pady=10)

        # A lista (No CTK, usamos o CTkTextbox para texto rico ou frames para listas)
        self.lista_tarefas = ctk.CTkTextbox(self.root, width=500, height=200)
        self.lista_tarefas.pack(pady=10)

        # Barra de Status Moderna
        self.status_bar = ctk.CTkLabel(
            self.root, 
            text="A carregar cotações...", 
            fg_color="gray20", # Cor de fundo da barra
            corner_radius=0,
            anchor="w"
        )

        self.status_bar.pack(side="bottom", fill="x")

    def exibir_lista(self, tarefas):
        """
        Recebe uma lista de objetos 'Task' e exibe-os no componente de texto.
        No Delphi, seria como percorrer um ClientDataSet e adicionar strings a um TMemo.
        """
        # 1. Limpar o componente (do início '1.0' até ao fim 'end')
        self.lista_tarefas.delete("1.0", ctk.END)

        if not tarefas:
            self.lista_tarefas.insert(ctk.END, "Nenhuma tarefa encontrada.")
            return

        # 2. Percorrer as tarefas e formatar o texto
        for tarefa in tarefas:
            # Aqui podes usar f-strings (o formato de string mais moderno do Python)
            linha = f"[{tarefa.id}] |"
            linha += f"   Descrição: {tarefa.description}\n"
            linha += "-" * 40 + "\n"
            
            # 3. Inserir no final do componente
            self.lista_tarefas.insert(ctk.END, linha)

    def atualizar_status(self, texto):
        self.status_bar.configure(text=texto)

    def mostrar_erro(self, mensagem: str) -> None:
        """Exibe uma caixa de diálogo de erro com visual do sistema."""
        messagebox.showerror("Erro", mensagem)
        
    def mostrar_mensagem(self, mensagem: str) -> None:
        """Exibe uma mensagem informativa."""
        messagebox.showinfo("Informação", mensagem)

    def iniciar_loop(self):
        self.root.mainloop()