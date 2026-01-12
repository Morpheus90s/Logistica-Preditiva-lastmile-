from decisao_ia import analisar_pedido
from agente import buscar_ponto_proximo

def processar_fluxo_entrega(id_pedido, dias, tipo, casa_cliente, cliente_respondeu):
    print(f"\n--- Iniciando o processo: {id_pedido} ---")
    
    tem_risco = analisar_pedido(dias, tipo)
    
    if tem_risco == True:
        print(f"[SISTEMA] Alerta detectado. Enviando mensagem de confirmacao...")
        
        if cliente_respondeu == False:
            print("[SISTEMA] Cliente nao retornou o contato. Pedido NAO SEGURO.")
            print("[SISTEMA] Acionando Agente Logistico para buscar ponto de coleta...")
            buscar_ponto_proximo(casa_cliente)
        else:
            print("[SISTEMA] Cliente respondeu: 'Estarei em casa'. Seguindo fluxo normal.")
            
    else:
        print("[SISTEMA] Pedido com baixo risco. Seguindo para entrega direta.")

    print(f"--- Fim do processo: {id_pedido} ---")

if __name__ == "__main__":
    # TESTE 1: Risco detectado e cliente não responde
    processar_fluxo_entrega("PED-001", 3, "Expressa", (4, 5), False)
    
    # TESTE 2: Risco detectado, mas cliente responde
    processar_fluxo_entrega("PED-002", 25, "Normal", (8, 10), True)
    
    # TESTE 3: Sem risco detectado
    processar_fluxo_entrega("PED-003", 5, "Normal", (1, 1), False)