# Logística Preditiva: Inteligência Artificial Aplicada ao Last-Mile

Este projeto foi feito para aplicar na prática os conceitos do Nano Course de Inteligência Artificial e Computacional da FIAP. Como estudante, meu objetivo foi unir o que aprendi no curso com um problema real do e-commerce: o custo de entregas insucedidas.

## O Desafio
O Last-Mile é a etapa mais cara. Entregas que falham (cliente ausente ou endereço comercial fechado) gerando prejuízos. Este sistema atua prevendo o risco de falha e sugerindo ações para tais.

## Arquitetura do Sistema
O projeto foi estruturado seguindo os pilares do curso:

1. Predição de Risco: Analisa o histórico para calcular a probabilidade da falha.
2. Motor de Decisão: Aplica regras de negócio (ex: horários comerciais) para validar a entrega.
3. Agente de Rota: Simula o recalculo durante a rota.

## Técnica
- Linguagem: Python 3
- Ambiente: GitHub Codespaces
- Bibliotecas Principais: Pandas, Scikit-learn, Joblib
- Datasets: Dados reais de e-commerce (Olist) filtrados para 10.000 registros para facilitar o processamento no github.

---

## Como Executar (Passo a Passo)

### 1. Preparar o Ambiente

pip install -r requirements.txt
