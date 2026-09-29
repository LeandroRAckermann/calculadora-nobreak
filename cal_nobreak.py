import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        watts = float(entrada_watts.get())
        tempo = float(entrada_tempo.get())
        voltagem = float(entrada_voltagem.get())

        
        potencia = watts * tempo

        
        amperagem = potencia / (voltagem * 0.85)

        bateria = int (voltagem / 12)

        resultado.config(
            text=f" Serão necessárias {bateria} baterias de {amperagem:.2f} Ah\n" 
            f"aproximadamente"
                   )

    except ValueError:
        messagebox.showerror(   
            "Erro",
            "Digite apenas valores numéricos."
        )


# Criando a janela
janela = tk.Tk()
janela.title("Calculadora de Nobreak")
janela.geometry("400x300")


# Potência
tk.Label(
    janela,
    text="Potência dos equipamentos (W):"
).pack(pady=5)

entrada_watts = tk.Entry(janela)
entrada_watts.pack()


# Tempo
tk.Label(
    janela,
    text="Autonomia desejada (horas):"
).pack(pady=5)

entrada_tempo = tk.Entry(janela)
entrada_tempo.pack()


# Voltagem
tk.Label(
    janela,
    text="Tensão do banco de baterias (V):"
).pack(pady=5)

entrada_voltagem = tk.Entry(janela)
entrada_voltagem.pack()


# Botão
botao = tk.Button(
    janela,
    text="CALCULAR",
    command=calcular
)

botao.pack(pady=20)


# Resultado
resultado = tk.Label(
    janela,
    font=("Arial", 12, "bold")
)

resultado.pack(pady=10)

# Quem Fez
desenvolvido =tk.Label (
    janela,
    text="Desenvolvido por:\n"
     f" Leandro R Ackerman",
    font=("Arial", 8, "bold")
    
)
desenvolvido.pack(pady=5)


# Mantém a janela aberta
janela.mainloop()