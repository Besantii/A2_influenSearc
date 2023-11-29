import streamlit as st
import pandas as pd








for nicho, hashtags in nichos_hashtags.items():
    df.loc[df['challenges'].apply(lambda x: any(tag in x.lower() for tag in hashtags)), 'nicho'] = nicho

nichos_opcoes = list(nichos_hashtags.keys())
nicho_escolhido = st.selectbox("Escolha o nicho:", nichos_opcoes)

if st.button("Mostrar Influenciadores"):
    # Filtrar influenciadores com base no nicho escolhido
    influenciadores_nicho = influenciadores_df[influenciadores_df['nicho'] == nicho_escolhido]

    # Exibir a tabela de influenciadores
    st.table(influenciadores_nicho)
