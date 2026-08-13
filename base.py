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

AcimaDe20_df = df.groupby('order_id',)['item_price'].sum()

AcimaDe20_df = AcimaDe20_df[AcimaDe20_df > 20]

print(AcimaDe20_df)
