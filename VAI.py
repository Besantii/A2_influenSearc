import streamlit as st
import pandas as pd

# Define os nichos disponíveis
NICHOS = ['Moda', 'Religião', 'Música', 'Comédia', 'Viagem', 'Fitness', 'Arte']
METRICAS = ['likes', 'comments', 'shares', 'plays']

# Função para carregar dados do CSV
@st.cache
def carregar_dados(filepath):
    data = pd.read_csv(filepath)
    # Certifique-se de que a coluna 'nicho' está em formato de string
    data['nicho'] = data['nicho'].astype(str)
    return data

# Função para obter autores por nicho e métrica de ordenação
def obter_autores_por_nicho_e_metrica(data, nicho_escolhido, metrica):
    subset = data[data['nicho'].str.lower() == nicho_escolhido.lower()]
    return subset.sort_values(by=metrica, ascending=False)['author'].unique()

# Interface do Streamlit
st.title('INFLUENSEARCH')

# Carregar dados
df = carregar_dados('tabela.csv')

# Seleção do nicho
nicho_selecionado = st.selectbox('Escolha um nicho', NICHOS)

# Seleção da métrica de ordenação
metrica_selecionada = st.selectbox('Escolha uma métrica de ordenação', METRICAS)

# Botão para mostrar autores
if st.button('Mostrar Influencers'):
    autores = obter_autores_por_nicho_e_metrica(df, nicho_selecionado, metrica_selecionada)
    st.write(f"Autores no nicho de {nicho_selecionado} ordenados por {metrica_selecionada}:")
    st.write(autores)

