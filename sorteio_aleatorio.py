import tkinter as tk
from tkinter import messagebox
import random

def sorteio_aleatorio(total_numeros, numeros_sorteados):
    if numeros_sorteados > total_numeros:
        raise ValueError("O número de sorteios não pode ser maior que o número total de números.")
    return random.sample(range(1, total_numeros + 1), numeros_sorteados)

def realizar_sorteio():
    try:
        total_numeros = int(entry_total_numeros.get())
        numeros_sorteados = int(entry_numeros_sorteados.get())
        resultado = sorteio_aleatorio(total_numeros, numeros_sorteados)
        messagebox.showinfo("Resultado", f"Números sorteados: {resultado}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
    except Exception as e:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Sorteio Aleatório")
root.geometry("300x200")
root.configure(bg="lightblue")

# Rótulos e entradas
label_total_numeros = tk.Label(root, text="Total de números:", bg="lightblue")
label_total_numeros.pack(pady=5)

entry_total_numeros = tk.Entry(root)
entry_total_numeros.pack(pady=5)

label_numeros_sorteados = tk.Label(root, text="Números a serem sorteados:", bg="lightblue")
label_numeros_sorteados.pack(pady=5)

entry_numeros_sorteados = tk.Entry(root)
entry_numeros_sorteados.pack(pady=5)

# Botão para realizar o sorteio
button_sortear = tk.Button(root, text="Sortear", command=realizar_sorteio, bg="green", fg="white")
button_sortear.pack(pady=20)

# Iniciar a aplicação
root.mainloop()
