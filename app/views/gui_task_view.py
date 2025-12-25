import tkinter as tk
from tkinter import messagebox
from app.views.task_view import TaskView
from app.models.entities import Task

class GuiTaskView(TaskView):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerenciador de Tarefas Python")
        self.root.geometry("400x300")
        
        # Equivalente ao TListBox
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Botão para carregar (O Presenter será vinculado aqui)
        self.btn_carregar = tk.Button(self.root, text="Atualizar Lista")
        self.btn_carregar.pack(pady=5)

        # Criamos a "StatusBar" (um Label fixado no fundo)
        # relief="sunken" dá aquele efeito de borda para dentro, comum no Delphi
        self.status_bar = tk.Label(
            self.root, 
            text="A carregar cotações...", 
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def atualizar_status(self, texto):
        self.status_bar.config(text=texto)

    def exibir_lista(self, tasks: list[Task]):
        self.listbox.delete(0, tk.END) # Limpa a lista
        for t in tasks:
            self.listbox.insert(tk.END, f"ID: {t.id} - {t.description}")

    def mostrar_erro(self, mensagem: str):
        messagebox.showerror("Erro no Sistema", mensagem)

    def iniciar_loop(self):
        self.root.mainloop() # Equivalente ao Application.Run do Delphi
