# Analyze_computing_projects

Descrição Formal do Projeto: Análise de Regressão da Produção Científica
1. Analyze computing projects

Análise de Tendência Temporal da Produção de Projetos de Pesquisa em Computação na UFRN através de Regressão Polinomial.

2. Objetivo

O objetivo principal deste projeto é analisar e modelar a tendência do número de projetos de pesquisa na área de computação da UFRN ao longo do tempo. Especificamente, o script busca ajustar um modelo de regressão não linear aos dados dos últimos cinco anos para identificar padrões de crescimento, estagnação ou declínio na produção científica e visualizar essa tendência.

3. Metodologia

O projeto é executado através de um script em Python (MMF2.py) que segue uma metodologia estruturada em seis etapas:

3.1. Carregamento de Dados: Os dados brutos são carregados a partir de um arquivo CSV (projetos_computacao_ufrn.csv), que contém informações sobre os projetos de pesquisa. A função de carregamento é robusta, tratando possíveis erros de arquivo não encontrado e utilizando a codificação UTF-8 para compatibilidade com caracteres especiais.

3.2. Pré-processamento e Agregação: A coluna ano é limpa, convertendo-a para um tipo numérico e removendo quaisquer entradas inválidas ou ausentes. Em seguida, os dados são agregados para calcular a variável de interesse: o número total de projetos iniciados por ano (num_projetos).

3.3. Filtragem Temporal: Para focar a análise na tendência mais recente, o conjunto de dados é filtrado para incluir apenas os registros dos últimos cinco anos disponíveis. O script determina dinamicamente o ano máximo e seleciona o intervalo correspondente.

3.4. Modelagem Estatística:

Variáveis: A variável dependente (Y) é o num_projetos e a variável independente (X) é o ano.
Modelo: É empregada uma Regressão Polinomial de 2º Grau. Este modelo não linear é representado pela equação Y = β₀ + β₁X + β₂X² + ε, onde X é o ano e Y é o número de projetos. Para isso, são criadas as variáveis preditoras ano (termo linear) e ano² (termo quadrático).
Implementação: A biblioteca statsmodels é utilizada para ajustar um modelo de Mínimos Quadrados Ordinários (OLS - Ordinary Least Squares) aos dados preparados.
3.5. Análise de Resultados: O script gera e exibe um resumo estatístico completo do modelo ajustado. Este resumo inclui métricas essenciais como o R-quadrado (que indica a proporção da variância da variável dependente que é previsível a partir das variáveis independentes), os coeficientes para cada termo (const, ano, ano_sq) e seus respectivos p-valores (que testam a significância estatística de cada preditor).

3.6. Visualização: Utilizando as bibliotecas matplotlib e seaborn, um gráfico de dispersão é gerado para mostrar os dados reais (pontos). Sobreposto a este, é plotada a curva de regressão polinomial calculada pelo modelo, oferecendo uma representação visual clara da tendência encontrada.

4. Tecnologias Utilizadas

Python 3: Linguagem de programação principal.
Pandas: Para manipulação e análise de dados, incluindo carregamento de CSV e agregação.
Statsmodels: Para a implementação do modelo de regressão OLS e análise estatística.
NumPy: Para operações numéricas, especialmente a geração de pontos para a plotagem da curva de regressão.
Matplotlib & Seaborn: Para a criação de visualizações gráficas de alta qualidade.
OS: Para a manipulação de caminhos de arquivo de forma robusta e independente do sistema operacional.
5. Saídas (Outputs)

O projeto produz duas saídas principais:

Relatório Textual (Console): Um resumo detalhado do modelo de regressão, impresso no terminal, contendo os coeficientes, métricas de ajuste e testes de significância.
Gráfico de Regressão (Janela Gráfica): Uma visualização que exibe os dados observados e a curva do modelo polinomial ajustado para o período de cinco anos analisado.
