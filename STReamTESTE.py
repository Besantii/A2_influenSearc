import streamlit as st
import pandas as pd

# ... (seu código anterior)

# Carregar a base de dados dos influenciadores (substitua pelo seu próprio caminho e nome do arquivo)
influenciadores_df = pd.read_csv('seu_arquivo.csv')

# Barra de seleção para os nichos
nichos_opcoes = list(nichos_hashtags.keys())
nicho_escolhido = st.selectbox("Escolha o nicho:", nichos_opcoes)

# Botão para mostrar influenciadores relevantes
if st.button("Mostrar Influenciadores"):
    # Filtrar influenciadores com base no nicho escolhido
    influenciadores_nicho = influenciadores_df[influenciadores_df['nicho'] == nicho_escolhido]

    # Exibir a tabela de influenciadores
    st.table(influenciadores_nicho)
