import streamlit as st
import pandas as pd
pip install openpyxl



st.title('InfluenSearch')

# Carregar os dados do arquivo .xlsx
df = pd.read_excel('novo_arquivo_tiktok.xlsx')




# Barra de seleção para os nichos
nichos_opcoes = ['Música', 'Comédia', 'Viagem', 'Religião', 'Moda', 'Fitness', 'Arte']
nicho_escolhido = st.selectbox("Escolha o nicho:", nichos_opcoes)

# Exibir a seleção feita pelo usuário
st.write(f"Você escolheu o nicho: {nicho_escolhido}")


