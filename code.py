import tkinter as tk
import requests

def converter():
    try:
        response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        if response.status_code == 200:
            cotacoes = response.json()
            cotacao_dolar = cotacoes['USDBRL']['bid']
            
            real = float(entry_real.get())
            
            conversao = real / float(cotacao_dolar)

            label_resultado.config(text=f'{real} reais equivalem a {conversao:.2f} dólares americanos.')
        else:
            label_resultado.config(text="Erro ao obter cotação. Tente novamente.")
    except ValueError:
        label_resultado.config(text="Por favor, insira um valor numérico válido.")
    except Exception as e:
        label_resultado.config(text=f"Erro: {str(e)}")



root = tk.Tk()
root.title("Conversor de Moeda")

root.geometry("400x300")

label_instrucoes = tk.Label(root, text="Digite o valor em reais:")
label_instrucoes.pack(pady=10)

entry_real = tk.Entry(root, width=20)
entry_real.pack(pady=10)

button_converter = tk.Button(root, text="Converter", command=converter)
button_converter.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 12))
label_resultado.pack(pady=20)

root.mainloop()
