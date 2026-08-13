# Análise de Pedidos e Faturamento - Chipotle

## 📌 Visão Geral
Este projeto consiste em uma análise exploratória de dados (EDA) baseada em logs reais de transações de uma rede de fast-food (Chipotle). O objetivo é realizar a ingestão, limpeza e extração de métricas de negócio a partir de um arquivo de texto bruto (TSV), utilizando **Python** e **Pandas**.

## 🛠️ Stack Tecnológico
* Python
* Pandas

## 💡 Desafios Técnicos e Regras de Negócio
Para garantir a precisão das métricas, o projeto passou pelas seguintes etapas de engenharia e tratamento:

1. **Data Cleaning e Tipagem:** A coluna de faturamento (`item_price`) foi extraída com ruído (strings contendo o caractere `$`). O dado foi higienizado e convertido para formato numérico (`float`) para viabilizar as operações matemáticas.
2. **Validação Empírica de Dados:** Testes lógicos no DataFrame confirmaram que os valores da coluna `item_price` já contemplavam o preço total da linha (preço unitário $\times$ quantidade). Essa validação prévia evitou o erro arquitetural de dupla multiplicação no cálculo da receita total.
3. **Otimização de Agrupamento:** Uso avançado de `.groupby()` em conjunto com funções de agregação (`.sum()`, `.mean()`, `.nunique()`) otimizando o processamento ao operar diretamente em estruturas `Series` ao invés de `DataFrames` completos, mitigando erros de chave (KeyError) durante a filtragem.

## 📊 Indicadores Extraídos
O pipeline de análise respondeu às seguintes questões estratégicas do negócio:
* **Receita Total:** Faturamento bruto no período documentado.
* **Volume de Vendas:** Identificação do produto com maior saída absoluta em unidades.
* **Volume de Transações:** Contagem exata de pedidos únicos fechados.
* **Ticket Médio:** Valor financeiro médio gasto por cliente por pedido.
* **Segmentação de Clientes:** Filtragem e isolamento de pedidos de alto valor (acima de $20) para análise de perfil de consumo.

## 🚀 Como Executar
1. Clone este repositório.
2. Certifique-se de ter a biblioteca Pandas instalada no seu ambiente (`pip install pandas`).
3. Execute o script principal. A base de dados é consumida dinamicamente via URL bruta do repositório, não sendo necessário o download prévio do arquivo `.tsv`.
