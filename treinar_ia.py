import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def treinar_modelo():
    if not os.path.exists('data/pedidos_limpos.csv'):
        print("Erro: O arquivo de dados limpos não foi encontrado!")
        return

    dados = pd.read_csv('data/pedidos_limpos.csv')

    #escolhendo a caracteristica que iremos treinar a IA
    X = dados[['tempo_entrega']] 
    y = dados['atrasou']

    # Dividir os dados: 80% para a IA estudar e 20% para o teste final
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Treinando a IA...")

    #Criar e treinar a "Floresta de Decisão"
    modelo = RandomForestClassifier(n_estimators=100)
    modelo.fit(X_treino, y_treino)

    #Testar a precisão
    previsoes = modelo.predict(X_teste)
    precisao = accuracy_score(y_teste, previsoes)
    
    print(f"Treinamento concluido. Precisão da IA: {precisao * 100:.2f}%")

    if not os.path.exists('modelos'):
        os.makedirs('modelos')
    
    joblib.dump(modelo, 'modelos/modelo_atraso.pkl')
    print("Modelo salvo na pasta 'modelos/modelo_atraso.pkl'")

if __name__ == "__main__":
    treinar_modelo()