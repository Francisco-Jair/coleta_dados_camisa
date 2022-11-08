import pandas as pd
from coleta import coleta_camisa


dataset = pd.read_csv("captura_dados_camisa.csv")
# url = dataset["link_para_publicacao"]
# vai até o 3051

cont = 41
for urls in dataset["link_para_publicacao"][cont:61]:
    coleta_camisa(urls)
    print("OK")
    cont += 1
    print(cont)