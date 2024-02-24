import tkinter as tk
from tkinter import ttk, messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz de Perguntas e Respostas")

        self.pontuacao = 0
        self.pergunta_atual = 0

        # Lista de perguntas e respostas
        self.perguntas = [
            {
                "pergunta": "Quem é o autor de 'A Moreninha'?",
                "opcoes": ["José de Alencar", "Machado de Assis", "Aluísio Azevedo"],
                "resposta": "José de Alencar"
            },
            {
                "pergunta": "Qual é o maior oceano do mundo?",
                "opcoes": ["Oceano Atlântico", "Oceano Índico", "Oceano Pacífico"],
                "resposta": "Oceano Pacífico"
            },
            {
                "pergunta": "Quem foi o primeiro presidente dos Estados Unidos?",
                "opcoes": ["Thomas Jefferson", "George Washington", "John Adams"],
                "resposta": "George Washington"
            },
            {
                "pergunta": "Qual é o animal nacional da Austrália que é uma espécie de marsupial?",
                "opcoes": ["Koala", "Wombat", "Canguru"],
                "resposta": "Canguru"
            },
            {
                "pergunta": "Quem escreveu 'Cem Anos de Solidão'?",
                "opcoes": ["Isabel Allende", "Jorge Luis Borges", "Gabriel García Márquez"],
                "resposta": "Gabriel García Márquez"
            },
            # Adicione mais perguntas conforme necessário
        ]

        self.respostas_corretas = []
        self.respostas_incorretas = []

        self.criar_interface()

    def criar_interface(self):
        self.label_pergunta = ttk.Label(self.root, text="")
        self.label_pergunta.pack(pady=10)

        self.opcoes_var = tk.StringVar()
        self.opcao_radios = []

        for i in range(3):  # Reduzi para 3 opções
            opcao_radio = ttk.Radiobutton(self.root, text="", variable=self.opcoes_var, value=i)
            opcao_radio.pack(pady=5)
            self.opcao_radios.append(opcao_radio)

        self.botao_responder = ttk.Button(self.root, text="Responder", command=self.verificar_resposta)
        self.botao_responder.pack(pady=10)

        self.proxima_pergunta()

    def proxima_pergunta(self):
        if self.pergunta_atual < len(self.perguntas):
            pergunta_atual = self.perguntas[self.pergunta_atual]
            self.label_pergunta.config(text=pergunta_atual["pergunta"])

            opcoes = pergunta_atual["opcoes"]

            for i, opcao_radio in enumerate(self.opcao_radios):
                if i < len(opcoes):
                    opcao_radio.config(text=opcoes[i])
                else:
                    opcao_radio.config(text="")

            self.opcoes_var.set(None)

            self.pergunta_atual += 1
        else:
            mensagem_final = f"Quiz concluído! Sua pontuação final é {self.pontuacao}\n"
            mensagem_final += f"Respostas corretas: {', '.join(self.respostas_corretas)}\n"
            mensagem_final += f"Respostas incorretas: {', '.join(self.respostas_incorretas)}"

            messagebox.showinfo("Fim do Quiz", mensagem_final)

    def verificar_resposta(self):
        if self.opcoes_var.get() is not None:
            resposta_usuario = self.opcao_radios[int(self.opcoes_var.get())]["text"]
            resposta_correta = self.perguntas[self.pergunta_atual - 1]["resposta"]

            if resposta_usuario == resposta_correta:
                self.pontuacao += 1
                self.respostas_corretas.append(f"Pergunta {self.pergunta_atual}: {resposta_usuario}")
            else:
                self.respostas_incorretas.append(f"Pergunta {self.pergunta_atual}: {resposta_usuario}")

            self.proxima_pergunta()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
