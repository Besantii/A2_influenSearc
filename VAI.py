import streamlit as st
import pandas as pd

# Define os nichos disponíveis
NICHOS = ['Moda', 'Religião', 'Música', 'Comédia', 'Viagem', 'Fitness', 'Arte']
METRICAS = {'likes': 'Curtidas', 'comments': 'Comentários', 'shares': 'Compartilhamentos', 'plays': 'Vizualizações', 'author_followers': 'Seguidores'}

# Função para carregar dados do CSV
@st.cache
def carregar_dados(filepath):
    data = pd.read_csv(filepath)
    # Certifique-se de que a coluna 'nicho' está em formato de string
    data['nicho'] = data['nicho'].astype(str)
    return data

# Função para obter autores por nicho e métrica de ordenação
def obter_autores_por_nicho_e_metrica(data, nicho_escolhido, metrica):
    if metrica == 'author_followers':
        # Ordenar por followers de autor
        subset = data[data['nicho'].str.lower() == nicho_escolhido.lower()]
        sorted_subset = subset.sort_values(by=metrica, ascending=False)
        autores_info = sorted_subset[['author', 'tiktok_url', 'author_followers']].drop_duplicates()
    else:
        # Para outras métricas (likes, comments, shares, plays)
        subset = data[data['nicho'].str.lower() == nicho_escolhido.lower()]
        sorted_subset = subset.sort_values(by=metrica, ascending=False)
        autores_info = sorted_subset[['author', 'tiktok_url']].drop_duplicates()

    return autores_info

# Interface do Streamlit
st.title('INFLUENSEARCH')

# Carregar dados
df = carregar_dados('tabela.csv')

# Seleção do nicho
nicho_selecionado = st.selectbox('Escolha um nicho', NICHOS)

# Seleção da métrica de ordenação
metrica_selecionada = st.selectbox('Escolha uma métrica de ordenação', list(METRICAS.values()))

# Inverter o dicionário para obter a métrica real com base na seleção do usuário
metrica_selecionada = next(key for key, value in METRICAS.items() if value == metrica_selecionada)

# Botão para mostrar autores
if st.button('Mostrar Influencers'):
    autores_info = obter_autores_por_nicho_e_metrica(df, nicho_selecionado, metrica_selecionada)
    
    st.write(f"Autores no nicho de {nicho_selecionado} ordenados por {METRICAS[metrica_selecionada]}:")
    
    # Mostrar os nomes, links e número de seguidores para os perfis de TikTok
    for _, row in autores_info.iterrows():
        if metrica_selecionada == 'author_followers':
            st.write(f"- [{row['author']}](row['tiktok_url']) - {row['author_followers']} seguidores")
        else:
            st.write(f"- [{row['author']}](row['tiktok_url'])")
