import streamlit as st
import pandas as pd


if st.button("Mostrar Influenciadores"):
    # Filtrar influenciadores com base no nicho escolhido
    influenciadores_nicho = influenciadores_df[influenciadores_df['nicho'] == nicho_escolhido]

    # Exibir a tabela de influenciadores
    st.table(influenciadores_nicho)
