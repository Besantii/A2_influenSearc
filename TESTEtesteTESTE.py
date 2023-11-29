import streamlit as st

# Barra de seleção para os nichos
nichos_opcoes = ['Música', 'Comédia', 'Viagem', 'Religião', 'Moda', 'Fitness', 'Arte']
nicho_escolhido = st.selectbox("Escolha o nicho:", nichos_opcoes)

# Exibir a seleção feita pelo usuário
st.write(f"Você escolheu o nicho: {nicho_escolhido}")


