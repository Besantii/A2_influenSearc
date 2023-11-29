import streamlit as st
import pandas as pd

# Carregar os dados do arquivo .xlsx
df = pd.read_excel('novo_arquivo_tiktok.xlsx')

# Substituir valores nulos na coluna 'challenges'
df['challenges'].fillna('', inplace=True)

# Definir as hashtags para cada nicho
# ... (código para definir as hashtags para cada nicho)

# Criar uma nova coluna 'nicho'
df['nicho'] = 'Outro'

# Atualizar as hashtags e nichos
for nicho, hashtags in nichos_hashtags.items():
    df.loc[df['challenges'].apply(lambda x: any(tag in x.lower() for tag in hashtags)), 'nicho'] = nicho

# Filtrar apenas as colunas relevantes
df = df[['challenges', 'nicho']]

# Dividir os dados em conjunto de treinamento e teste
train_data, test_data, train_labels, test_labels = train_test_split(df['challenges'], df['nicho'], test_size=0.2, random_state=42)

# Criar o modelo
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Treinar o modelo
model.fit(train_data, train_labels)

# Avaliar a precisão do modelo nos dados de teste
accuracy = model.score(test_data, test_labels)
print(f'Acurácia do modelo: {accuracy:.2f}')


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
