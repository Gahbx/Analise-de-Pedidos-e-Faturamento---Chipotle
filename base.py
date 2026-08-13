import pandas as pd 

urlVendas = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
df = pd.read_table(urlVendas, sep='\t')

df['item_price'] = df['item_price'].str.replace('[\$,]', '', regex=True).astype(float)

# # colunas


# # Receita
# Receita_df = df['item_price'].sum()

# Item Mais Pedido
# ItemMaisPedido = df[['item_name', 'quantity']].groupby('item_name').sum().sort_values(by='quantity', ascending=False)
# print(ItemMaisPedido)

# # Pedidos unicos individuais
# PedidosUnicos = df['order_id'].nunique()
# print(PedidosUnicos)

# tarefa 7 Media De Valor Por Pedido
MediaDeValorPorPedido = df.groupby('order_id')['item_price'].sum().mean()



# tarefa 8 Crie um novo DataFrame que contenha apenas os pedidos que custaram mais de $20.

# 1. Agrupa e soma (Gera uma Series)
AcimaDe20 = df.groupby('order_id')['item_price'].sum()

# 2. Filtra (Continua sendo uma Series)
AcimaDe20 = AcimaDe20[AcimaDe20 > 20]

# 3. Converte a Series de volta para um DataFrame
AcimaDe20_df = AcimaDe20.reset_index()

print(AcimaDe20_df)
