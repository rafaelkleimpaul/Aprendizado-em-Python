import pandas as pd

pedidos_df = pd.read_excel(
    r"C:\Users\Pichau\Desktop\Projeto-Estoque\Pedidos.xlsx")
# In[58]:

produtos = []
quantidade = []
valor_un = []
for i_produto in range(len(pedidos_df)):
    produtos.extend(pedidos_df['Produtos'][i_produto].split(','))
    quantidade.extend(pedidos_df['Quantidade'][i_produto].split(','))
    valor_un.extend(pedidos_df['Valor un'][i_produto].split(','))

# In[51]:
num_vendas = []
data_hora = []
cliente = []
bairro = []
for i_vendas in range(len(pedidos_df)):
    for i in range(int(len(produtos) / 3)):
        num_vendas.append(pedidos_df['Número da venda'][i_vendas])
        data_hora.append(pedidos_df['Data/hora de emissão'][i_vendas])
        cliente.append(pedidos_df['Cliente'][i_vendas])
        bairro.append(pedidos_df['Bairro'][i_vendas])

# In[62]:

data = {
    "Número da venda": num_vendas,
    "Data e Hora": data_hora,
    "Cliente": cliente,
    "Bairro": bairro,
    "Produtos": produtos,
    "Quantidade": quantidade,
    "Valor Un": valor_un,
}

# In[63]:

output = pd.DataFrame.from_dict(data)

# In[66]:

output.to_excel(
    r"C:\Users\Pichau\Desktop\Projeto-Estoque\output-arquivos\output1.xlsx",
    index=False)

# In[ ]:
