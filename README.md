# Logística Preditiva: Inteligência Artificial Aplicada ao Last-Mile

Este projeto foi feito para aplicar na prática os conceitos do Nano Course de Inteligência Artificial e Computacional da FIAP. Como estudante, meu objetivo foi unir o que aprendi no curso com um problema real do e-commerce: o custo de entregas insucedidas.

## O Desafio
Entregas que falham no "Last-Mile" geram custos altos. Eu quis criar um fluxo que ajudasse o sistema a "pensar" antes de mandar o motorista para a rua:
1. Prever se vai dar problema (IA).
2. Seguir regras da empresa (Motor de Decisão).
3. Resolver o problema se o cliente não estiver (Agente de Busca).

## Como o projeto está organizado:
'filtro_dados.py': Onde fiz a limpeza dos dados.
'treinar_ia.py': Onde treinei a IA a prever os atrasos.
'decisao.py': Onde criei as regras (Ex: Se for Expressa, atenção total).
'agente.py': Onde criei a busca pelo lugar mais perto para o pacote ficar.
'main.py': O arquivo que junta tudo.

## Técnica
- Linguagem: Python 3
- Ambiente: GitHub Codespaces
- Bibliotecas Principais: Pandas, Scikit-learn, Joblib
- Datasets: Dados reais de e-commerce (Olist) filtrados para 10.000 registros para facilitar o processamento no github.

## Como Executar

### 1. Preparar o Ambiente

pip install -r requirements.txt

### 2. Rodar o Sistema

python main.py
