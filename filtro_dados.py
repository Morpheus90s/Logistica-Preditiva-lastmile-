import pandas as pd
import os

def filtra_pedidos():
    caminho = 'dados/olist_orders_dataset.csv'
    dados = pd.read_csv(caminho)
    
    # 1. Organizando as datas
    colunas_tempo = [
        'order_purchase_timestamp', 
        'order_delivered_customer_date', 
        'order_estimated_delivery_date'
    ]
    
    for c in colunas_tempo:
        dados[c] = pd.to_datetime(dados[c])

    #filtra para pegar só o que já foi entregue
    pedidos_entregues = dados.dropna(subset=['order_delivered_customer_date'])

    #Calcula o tempo que levou
    pedidos_entregues['tempo_entrega'] = (pedidos_entregues['order_delivered_customer_date'] - pedidos_entregues['order_purchase_timestamp']).dt.days

    #Add coluna de atraso, marca como 1. Se nao, 0.
    pedidos_entregues['atrasou'] = (pedidos_entregues['order_delivered_customer_date'] > pedidos_entregues['order_estimated_delivery_date']).astype(int)

    if not os.path.exists('data'):
        os.makedirs('data')
    
    pedidos_entregues.to_csv('dados/pedidos_limpos.csv', index=False)
    
    print("Dados filtrados")
    print(f"Total de pedidos na pasta: {len(pedidos_entregues)}")
    print(f"Quantos pedidos atrasaram: {pedidos_entregues['atrasou'].sum()}")

if __name__ == "__main__":
    filtra_pedidos()