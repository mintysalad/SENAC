import tk
import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacaoUSD = requisicao_dic["USDBRL"]['bid']
    cotacaoEUR = requisicao_dic['EURBRL']['bid']
    cotacaoBTC = requisicao_dic["BTCBRL"]['bid']

    textoR['text'] = f'''
    Dólar:{cotacaoUSD}
    Euro: {cotacaoEUR}
    BitCoin: {cotacaoBTC}'''

janela = Tk()
janela.title("Cotação Atual de Moedas :D")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)

botao.grid(column=0, row=1, padx=10, pady=10)
textoR = Label(janela, text="")
textoR.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()