import requests
import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
app = QApplication(sys.argv)
os.chdir("C:\\Users\\shilo\\Downloads\\arquivos.ui")
resposta = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL').json()
compra = resposta ['USDBRL']['bid']
compra_float = float(compra)

def funcao_conversao():
    valor_inicial = pag_conversor.lineEdit.text()
    try:
        valor_inicial_int = float(valor_inicial)
        valor_convertido = compra_float * valor_inicial_int
        valor_conv_int = float(valor_convertido)
        valor_round = round(valor_conv_int, 2)
        pag_conversor.close()
        pag02_conversor.show()
        pag02_conversor.label.setText(f"O valor é de {valor_round} dólares americanos")
    except ValueError:
         pag02_conversor.label.setText(f"ERRO: Por favor, insira um valor válido!")

def back():
    pag02_conversor.close()
    pag_conversor.show()

def carregar_ui(caminho_ui):
    ui_file = QFile(caminho_ui)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file.fileName()}: {ui_file.errorString()}")
        exit(-1)
    
    loader = QUiLoader()
    pag_conversor = loader.load(ui_file)
    return pag_conversor

pag_conversor = carregar_ui("conversor.ui")
pag_conversor.botao.clicked.connect(funcao_conversao)

pag02_conversor = carregar_ui("conversao_page2.ui")
pag02_conversor.botao.clicked.connect(back)

pag_conversor.show()
app.exec()
