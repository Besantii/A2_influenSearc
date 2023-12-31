import streamlit as st
import pandas as pd

# Nichos

NICHOS = ['Moda', 'Religião', 'Música', 'Comédia', 'Viagem', 'Fitness', 'Arte']
METRICAS = {'likes': 'Curtidas', 'comments': 'Comentários', 'shares': 'Compartilhamentos', 'plays': 'Visualizações', 'author_followers': 'Seguidores'}

# Função do csv

@st.cache
def carregar_dados(filepath):
    data = pd.read_csv(filepath)
    # Certifique-se de que a coluna 'nicho' está em formato de string
    data['nicho'] = data['nicho'].astype(str)
    return data

# Função de autores por nicho e métrica
def obter_autores_por_nicho_e_metrica(data, nicho_escolhido, metrica):
    if metrica == 'author_followers':
        # Ordenar por Seguidores
        subset = data[data['nicho'].str.lower() == nicho_escolhido.lower()]
        sorted_subset = subset.sort_values(by=metrica, ascending=False)
        autores_info = sorted_subset[['author', 'tiktok_url', 'author_followers']].drop_duplicates()
    else:
        # Para outras métricas (likes, comments, shares, plays)
        subset = data[data['nicho'].str.lower() == nicho_escolhido.lower()]
        sorted_subset = subset.sort_values(by=metrica, ascending=False)
        autores_info = sorted_subset[['author', 'tiktok_url']].drop_duplicates()

    return autores_info

# Titulo

st.title('INFLUENSEARCH')

# Dados

df = carregar_dados('tabela.csv')

# Selectbox

nicho_selecionado = st.selectbox('Escolha um nicho', NICHOS)

# Seleção da métrica

metrica_selecionada = st.selectbox('Escolha uma métrica de ordenação', list(METRICAS.values()))

# Inverter o dicionário para obter a métrica real com base na seleção do usuário (para deixar o nome em portugues na seleção, sem atrapalhar o código)

metrica_selecionada = next(key for key, value in METRICAS.items() if value == metrica_selecionada)

# Botão para mostrar autores

if st.button('Mostrar Influencers'):
    autores_info = obter_autores_por_nicho_e_metrica(df, nicho_selecionado, metrica_selecionada)
    
    st.write(f"Autores no nicho de {nicho_selecionado} ordenados por {METRICAS[metrica_selecionada]}:")
    
    # Mostrar os nomes, links e número de seguidores para os perfis de TikTok
    for _, row in autores_info.iterrows():
        st.write(f"- [{row['author']}]({row['tiktok_url']})")
