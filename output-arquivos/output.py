import pandas as pd

pedidos_df = pd.read_excel(
    "C:/Users/Pichau/Desktop/Projeto-Estoque/Pedidos.xlsx")

num_venda = pedidos_df['Número da venda']
data = pedidos_df['Data/hora de emissão']

# Número da Venda
print(num_venda, data)

for valores in num_venda.iteritems():
    num_venda.pd = valores[1]
    escrever = pd.ExcelWriter('output1.xlsx')
    pedidos_df['Número da venda'].to_excel(escrever,
                                           'Sheet1',
                                           startcol=0,
                                           index=False)
    escrever.save()
    break
for valores in data.iteritems():
    data.pd = valores[1]
    escrever = pd.ExcelWriter('output1.xlsx')
    pedidos_df['Data/hora de emissão'].to_excel(escrever,
                                                'Sheet1',
                                                startcol=1,
                                                index=False)
    escrever.save()
    break

#pedidos_df['Número da venda'] = num_venda.pd
#pedidos_df['Data/hora de emissão'] = valor_data

##pedidos_df['Número da venda'].to_excel('output1.xlsx', index=False, startcol=0)
