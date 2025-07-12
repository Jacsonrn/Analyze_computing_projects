import pandas as pd
import statsmodels.api as sm
import os
import matplotlib.pyplot as plt
import seaborn as sns # Adicionado para gráficos mais elaborados
import numpy as np    # Adicionado para operações numéricas (linspace)

def carregar_dados(caminho_arquivo):
    """Carrega dados de um arquivo CSV."""
    try:
        # CORREÇÃO: O separador é vírgula (,), não ponto e vírgula (;).
        # Adicionado encoding='utf-8' para caracteres especiais (ç, ã, etc.).
        # Adicionado on_bad_lines='warn' para avisar sobre linhas mal formatadas.
        return pd.read_csv(caminho_arquivo, sep=',', encoding='utf-8', on_bad_lines='warn')
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho_arquivo}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao carregar ou processar o arquivo: {e}")
        return None
# Constrói um caminho mais robusto para o arquivo de dados.
# Isso assume que a pasta 'data' está no mesmo nível da pasta 'src' onde este script está.
# Ex: MM2/src/MMF2.py e MM2/data/projetos_computacao_ufrn.csv
script_dir = os.path.dirname(__file__) # Diretório do script
caminho_dados_filtrados = os.path.join(script_dir, '..', 'data', 'projetos_computacao_ufrn.csv')

# Carregar os dados
df_projetos = carregar_dados(caminho_dados_filtrados)

if df_projetos is not None:
    # 1. Preparação dos Dados para Regressão Linear
    df_projetos['ano'] = pd.to_numeric(df_projetos['ano'], errors='coerce')
    df_projetos.dropna(subset=['ano'], inplace=True)
    df_projetos['ano'] = df_projetos['ano'].astype(int)

    projetos_por_ano = df_projetos.groupby('ano').size().reset_index(name='num_projetos')

    # 2. FILTRAGEM: Selecionar apenas os últimos 5 anos de dados
    if not projetos_por_ano.empty:
        ano_maximo = projetos_por_ano['ano'].max()
        ano_inicio = ano_maximo - 4  # Intervalo de 5 anos
        
        print(f"Analisando o intervalo de 5 anos: de {ano_inicio} a {ano_maximo}")
        dados_filtrados = projetos_por_ano[projetos_por_ano['ano'] >= ano_inicio].copy()
    else:
        dados_filtrados = projetos_por_ano # Mantém o DataFrame vazio se não houver dados

    # Verifica se há dados suficientes para a regressão (mínimo de 3 pontos para grau 2)
    if len(dados_filtrados) < 3:
        print("Dados insuficientes para a regressão no intervalo de 5 anos. O modelo não será executado.")
    else:
        # Definir variáveis X e Y a partir dos dados filtrados
        x_data = dados_filtrados['ano']
        y_data = dados_filtrados['num_projetos']

        # 3. Preparação dos Dados para Regressão Polinomial (Grau 2)
        X_poly_df = pd.DataFrame({
            'ano': x_data,
            'ano_sq': x_data**2
        })
        X_poly_df = sm.add_constant(X_poly_df)

        # 4. Construção do Modelo de Regressão Polinomial
        modelo = sm.OLS(y_data, X_poly_df)
        resultados = modelo.fit()

        # 5. Exibir os Resultados da Regressão
        print("\nResumo do Modelo de Regressão Polinomial (Grau 2) - Últimos 5 Anos:")
        print(resultados.summary())

        # 6. Visualização dos Resultados
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='ano', y='num_projetos', data=dados_filtrados, label='Projetos Reais', s=100)

        anos_pred = np.linspace(x_data.min(), x_data.max(), 100)
        X_pred_df = pd.DataFrame({'ano': anos_pred, 'ano_sq': anos_pred**2})
        X_pred_df = sm.add_constant(X_pred_df)
        projetos_pred = resultados.predict(X_pred_df)

        plt.plot(anos_pred, projetos_pred, color='red', label='Regressão Polinomial (Grau 2)')
        plt.title(f'Regressão Polinomial: Número de Projetos por Ano ({ano_inicio} - {ano_maximo})')
        plt.xlabel('Ano')
        plt.ylabel('Número de Projetos')
        plt.grid(True)
        plt.legend()
        plt.show()