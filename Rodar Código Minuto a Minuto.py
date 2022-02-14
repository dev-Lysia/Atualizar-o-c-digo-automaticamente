#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") #requisição dos dados

requisicao_dic = requisicao.json() #selecionando os dados desejados
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

tabela = pd.read_excel("Cotações.xlsx") #transformando os dados e atualizando
tabela.loc[0, "Cotação"] = float(cotacao_dolar)
tabela.loc[1, "Cotação"] = float(cotacao_euro)
tabela.loc[2, "Cotação"] = float(cotacao_btc) * 1000
tabela.loc[0, "Data Última Atualização"] = datetime.now()

tabela.to_excel("Cotações.xlsx", index=False) #exportando na planilha desejada
print(f"Cotação Atualizada. {datetime.now()}")


# In[ ]:




