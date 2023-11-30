import streamlit as st
import pandas as pd

# Define os nichos disponíveis
NICHOS = ['Moda', 'Religião', 'Música', 'Comédia', 'Viagem', 'Fitness', 'Arte']

# Função para carregar dados do CSV
@st.cache
def carregar_dados(filepath):
    data = pd.read_csv(filepath)
    # Certifique-se de que a coluna 'nicho' está em formato de string
    data['nicho'] = data['nicho'].astype(str)
    return data

# Função para obter autores por nicho
def obter_autores_por_nicho(data, nicho_escolhido):
    return data[data['nicho'].str.lower() == nicho_escolhido.lower()]['author'].unique()

# Interface do Streamlit
st.title('Descobridor de Influenciadores por Nicho')

# Carregar dados
df = carregar_dados('tabela.csv')

# Seleção do nicho
nicho_selecionado = st.selectbox('Escolha um nicho', NICHOS)

# Botão para mostrar autores
if st.button('Mostrar Autores'):
    autores = obter_autores_por_nicho(df, nicho_selecionado)
    st.write(f"Autores no nicho de {nicho_selecionado}:")
    st.write(autores)

