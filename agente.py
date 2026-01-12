import math

def calcular_distancia(p1, p2):
    distancia = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return distancia

def buscar_ponto_proximo(local_cliente):
    pontos = [
        {"nome": "Locker Posto Shell", "coord": (2, 3)},
        {"nome": "Farmacia Central", "coord": (8, 12)},
        {"nome": "Mercado do Bairro", "coord": (5, 8)},
        {"nome": "Estacao de Metro", "coord": (1, 1)},
        {"nome": "Shopping Local", "coord": (10, 10)},
        {"nome": "Padaria 24h", "coord": (7, 2)},
        {"nome": "Academia VIP", "coord": (3, 9)}
    ]
    
    #Pegando o primeiro da lista
    ponto_mais_perto = pontos[0]
    menor_km = calcular_distancia(local_cliente, pontos[0]["coord"])

    print("\n--- Agente Logistico: Verificando Opcoes ---")
    print("Local do Cliente: " + str(local_cliente))

    for i in range(1, len(pontos)):
        ponto_atual = pontos[i]
        dist_atual = calcular_distancia(local_cliente, ponto_atual["coord"])
        
        print("Testando " + ponto_atual["nome"] + " | Distancia: " + str(round(dist_atual, 2)))

        if dist_atual < menor_km:
            menor_km = dist_atual
            ponto_mais_perto = ponto_atual

    print("\nResultado da Busca")
    print("O pacote sera enviado para: " + ponto_mais_perto["nome"])
    print("Distancia final: " + str(round(menor_km, 2)))

if __name__ == "__main__":
    # Teste 1:
    buscar_ponto_proximo((4, 5))
    
    # Teste 2:
    buscar_ponto_proximo((9, 11))
    
    # Teste 3:
    buscar_ponto_proximo((1, 2))