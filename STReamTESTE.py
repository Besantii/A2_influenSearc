import streamlit as st

# Função para classificar o desafio
def classificar_desafio(desafio):
    return model.predict([desafio])[0]

# Título do aplicativo
st.title("Classificador de Nicho TikTok")

# Entrada de texto para o desafio
desafio_usuario = st.text_input("Digite o desafio do TikTok:")

# Barra de seleção para os nichos
nichos_opcoes = list(nichos_hashtags.keys())
nicho_escolhido = st.selectbox("Escolha o nicho:", nichos_opcoes)

# Botão para classificar
if st.button("Classificar"):
    # Verificar se o usuário digitou algo
    if desafio_usuario:
        # Obter a previsão do modelo
        predicao = classificar_desafio(desafio_usuario)
        
        # Exibir o resultado
        st.success(f"O nicho do desafio é: {predicao}")
    else:
        st.warning("Por favor, digite um desafio para classificar.")
