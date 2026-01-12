import joblib
import pandas as pd
import os

def analisar_pedido(tempo_estimado, tipo_entrega):
    caminho = 'modelos/modelo_atraso.pkl'
    
    if not os.path.exists(caminho):
        print("Erro: Modelo não encontrado")
        return

    ia = joblib.load(caminho)

    #Fazendo as previsões necessarias 
    dados_novos = pd.DataFrame([[tempo_estimado]], columns=['tempo_entrega'])
    probabilidade_atraso = ia.predict_proba(dados_novos)[0][1] 

    print(f"\n--- Analise de Pedido ---")
    print(f"Tempo previsto: {tempo_estimado} dias")
    print(f"Risco calculado pela IA: {probabilidade_atraso * 100:.2f}%")

    # Regras do Sistema
    # 1. Se a IA diz que o risco é alto (> 50%)
    # 2. OU se for uma regra de negócio (Tipo Expressa sempre gera alerta)

    if probabilidade_atraso > 0.5 or tipo_entrega == 'Expressa':
        print("Decisão: [ALERTA] Risco alto detectado.")
        print("Ação: Enviar mensagem automatica para o cliente confirmar presenca.")
        return True
    else:
        print("Decisão: Fluxo normal.")
        print("Ação: Seguir com o carregamento do veiculo.")
        return False

if __name__ == "__main__":
    # Teste 1: Tempo alto, detectar risco
    analisar_pedido(25, 'Normal')
    
    # Teste 2: Tempo baixo, mas regra de negócio
    analisar_pedido(3, 'Expressa')
    
    # Teste 3: entrega Normal
    analisar_pedido(5, 'Normal')