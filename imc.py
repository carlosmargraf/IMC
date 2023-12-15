import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class Programa():
    def __init__(self, top):
        self.tela = top
        self.tela.title('IMC')
        self.tela.geometry('695x585')
        self.tela.resizable(False, False)

    def calculo_IMC(self, peso, altura):
        calculo = peso//(altura**2)
        return calculo

    def obter_resultado(self):
        peso = float(self.massa_corporalEntry.get())
        altura = float(self.altura_corporalEntry.get())
        calculo = self.calculo_IMC(peso, altura)
        msg = f'Seu IMC: {calculo}'

        if calculo <= 18.49:
            msg += '\nAbaixo do peso'
        elif 18.5 <= calculo <= 24.99:
            msg += '\nPeso normal'
        else:
            msg += '\nAcima do peso'
        messagebox.showinfo('IMC', msg,)

    def criar_widgets(self):
        self.frame1 = tk.Frame(self.tela)
        self.frame1.pack(fill=tk.BOTH)
        self.frame2 = tk.Frame(self.tela)
        self.frame2.pack(fill=tk.BOTH, padx=10, pady=5)
        self.frame3 = tk.Frame(self.tela)
        self.frame3.pack(fill=tk.BOTH, padx=260, pady=5)
        self.frame4 = tk.Frame(self.tela)
        self.frame4.pack(fill=tk.BOTH, padx=255, pady=5)
        self.frame5 = tk.Frame(self.tela)
        self.frame5.pack(fill=tk.BOTH, padx=0, pady=5)

        # frame1 (background)
        self.image = ImageTk.PhotoImage(Image.open("Captura de tela 2023-12-13 230206.png"))
        self.painel = ttk.Label(self.frame1, image=self.image)
        self.painel.pack(side=tk.LEFT)

        # frame2 (formaula texto)
        self.formaula = ttk.Label(self.frame2, text= 'Cálculo do Índice de Massa Corporal – IMC = Massa (kg) ÷ Altura (m)²', font=('Arial', 13, 'bold', 'italic'))
        self.formaula.pack(side= tk.TOP) # TOP = centralizar

        # frame3 (masssa corporal)
        self.massa_corporal = ttk.Label(self.frame3, text= 'Digite seu peso: ', font=('Arial', 13, 'bold'))
        self.massa_corporal.pack(side=tk.LEFT)
        self.massa_corporalEntry = ttk.Entry(self.frame3, width=5)
        self.massa_corporalEntry.pack(side=tk.TOP)

        # frame4 (altura corporal)
        self.altura_corporal = ttk.Label(self.frame4, text='Digite sua altura:', font=('Arial', 13, 'bold'))
        self.altura_corporal.pack(side=tk.LEFT)
        self.altura_corporalEntry = ttk.Entry(self.frame4, width=5)
        self.altura_corporalEntry.pack(side=tk.TOP)

        # frame5
        button = ttk.Button(self.frame5, text="Calcular", command=self.obter_resultado)
        button.pack(side=tk.TOP)

if __name__ == '__main__':
    tela = tk.Tk()
    app = Programa(tela)
    app.criar_widgets()
    tela.mainloop()