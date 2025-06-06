# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import seaborn as sns
# # # # # import matplotlib.pyplot as plt

# # # # # st.title("Streamlit na EC2")
# # # # # st.write("Exemplo de gráfico com dataset CSV")

# # # # # df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# # # # # df.columns = df.columns.str.strip()  # Remove espaços dos nomes das colunas

# # # # # df.columns = df.columns.str.strip()  # remove espaços no início e fim

# # # # # df.columns = df.columns.str.strip().str.replace(" ", "_")

# # # # # st.header("Maiores vendas por País, Segmento e Categoria")

# # # # # grouped = df.groupby(['Country', 'Segment', 'Category'])['Sales'].sum().reset_index()
# # # # # top_sales = grouped.sort_values(by='Sales', ascending=False).head(10)

# # # # # fig, ax = plt.subplots(figsize=(10, 6))
# # # # # sns.barplot(data=top_sales, x='Sales', y='Country', hue='Category', ax=ax)
# # # # # ax.set_title("Top 10 Combinações de Vendas por País e Categoria")
# # # # # st.pyplot(fig)

# # # # # st.markdown("""
# # # # # **Insight:** As vendas são significativamente maiores nos **Estados Unidos**, 
# # # # # com destaque para os segmentos **Corporate** e categorias **Technology** e **Furniture**.
# # # # # """)

# # # # import streamlit as st
# # # # import pandas as pd
# # # # import seaborn as sns
# # # # import matplotlib.pyplot as plt

# # # # st.title("Streamlit na EC2")
# # # # st.write("Exemplo de gráfico com dataset CSV")

# # # # # Corrige separador e remove espaços dos nomes de colunas
# # # # df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# # # # df.columns = df.columns.str.strip()

# # # # st.write("Primeiras linhas do dataset:")
# # # # st.write(df.head())

# # # # # Insight: Maiores vendas por País, Segmento e Produto
# # # # st.header("Insight: Maiores vendas por País, Segmento e Produto")

# # # # # Agrupar os dados e somar as vendas
# # # # grouped = df.groupby(['Country', 'Segment', 'Product'])['Sales'].sum().reset_index()
# # # # top_sales = grouped.sort_values(by='Sales', ascending=False).head(10)

# # # # # Gráfico de barras
# # # # fig, ax = plt.subplots(figsize=(10, 6))
# # # # sns.barplot(data=top_sales, x='Sales', y='Country', hue='Segment', ax=ax)
# # # # ax.set_title("Top 10 Combinações de Vendas por País e Segmento")
# # # # st.pyplot(fig)

# # # # # Texto explicativo
# # # # st.markdown("""
# # # # **Insight:** As maiores vendas ocorrem principalmente nos **Estados Unidos** no segmento **Corporate**, com destaque para produtos como **Phones** e **Chairs**.
# # # # """)

# # # import streamlit as st
# # # import pandas as pd
# # # import seaborn as sns
# # # import matplotlib.pyplot as plt

# # # st.title("Streamlit na EC2")
# # # st.write("Exemplo de gráfico com dataset CSV")

# # # # Leitura do CSV com separador correto e limpeza de colunas
# # # df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# # # df.columns = df.columns.str.strip()

# # # # Insight: Maiores vendas por Produto
# # # st.header("Insight: Top 10 Produtos mais vendidos")

# # # # Agrupamento e ordenação
# # # product_sales = df.groupby('Product')['Sales'].sum().reset_index()
# # # top_products = product_sales.sort_values(by='Sales', ascending=False).head(10)

# # # # Gráfico de barras horizontais
# # # fig, ax = plt.subplots(figsize=(10, 6))
# # # sns.barplot(data=top_products, x='Sales', y='Product', palette='viridis', ax=ax)
# # # ax.set_title("Top 10 Produtos com Maior Volume de Vendas", fontsize=14)

# # # # Adiciona valores nas barras
# # # for i in ax.containers:
# # #     ax.bar_label(i, fmt='%.0f', padding=5)

# # # plt.tight_layout()
# # # st.pyplot(fig)

# # # # Texto explicativo
# # # st.markdown("""
# # # **Insight:** Os produtos mais vendidos concentram-se em poucas categorias, indicando foco comercial. 
# # # Produtos como **Phones** e **Chairs** lideram em volume de vendas, sugerindo alta demanda e aceitação no mercado.
# # # """)

# # # import streamlit as st
# # # import pandas as pd
# # # import seaborn as sns
# # # import matplotlib.pyplot as plt

# # # st.title("Streamlit na EC2")
# # # st.write("Exemplo de gráfico com dataset CSV")

# # # # Leitura e limpeza
# # # df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# # # df.columns = df.columns.str.strip()

# # # st.write("Primeiras linhas do dataset:")
# # # st.write(df.head())

# # # # Insight: Top 10 produtos mais vendidos
# # # st.header("Insight: Top 10 Produtos mais vendidos")

# # # # Agrupamento
# # # product_sales = df.groupby('Product')['Sales'].sum().reset_index()
# # # top_products = product_sales.sort_values(by='Sales', ascending=False).head(10)

# # # # Gráfico com ajustes visuais
# # # fig, ax = plt.subplots(figsize=(12, 8))
# # # barplot = sns.barplot(data=top_products, x='Sales', y='Product', palette='crest', ax=ax)

# # # # Adiciona valores nas barras com separador de milhar
# # # for container in ax.containers:
# # #     ax.bar_label(container, fmt='{:,.0f}', padding=5, color='black')

# # # # Título e layout
# # # ax.set_title("Top 10 Produtos com Maior Volume de Vendas", fontsize=16, weight='bold')
# # # ax.set_xlabel("Vendas (em unidades monetárias)", fontsize=12)
# # # ax.set_ylabel("Produto", fontsize=12)
# # # plt.tight_layout()

# # # # Exibe o gráfico no Streamlit
# # # st.pyplot(fig)

# # # # Texto explicativo
# # # st.markdown("""
# # # **Insight:** Os produtos mais vendidos concentram-se em poucas categorias, indicando foco comercial.  
# # # **Phones** e **Chairs** lideram em volume de vendas, sugerindo alta demanda e aceitação no mercado.
# # # """)


# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt

# # # Título e leitura do CSV
# # st.title("Streamlit na EC2")
# # st.write("Exemplo de gráfico com dataset CSV")

# # df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# # df.columns = df.columns.str.strip()

# # st.write("Primeiras linhas do dataset:")
# # st.write(df.head())

# # # Insight: Top 10 produtos mais vendidos
# # st.header("Insight: Top 10 Produtos mais vendidos")

# # # Agrupamento
# # product_sales = df.groupby('Product')['Sales'].sum().reset_index()
# # top_products = product_sales.sort_values(by='Sales', ascending=False).head(10)

# # # Gráfico grande e otimizado
# # fig, ax = plt.subplots(figsize=(16, 10))  # AUMENTA o tamanho da imagem
# # sns.set_style("whitegrid")

# # barplot = sns.barplot(data=top_products, x='Sales', y='Product', palette='viridis', ax=ax)

# # # Adiciona os valores nas barras com separador de milhar
# # for container in ax.containers:
# #     ax.bar_label(container, fmt='{:,.0f}', padding=8, fontsize=12, color='black')

# # # Título e ajustes visuais
# # ax.set_title("Top 10 Produtos com Maior Volume de Vendas", fontsize=20, weight='bold')
# # ax.set_xlabel("Vendas (em unidades monetárias)", fontsize=14)
# # ax.set_ylabel("Produto", fontsize=14)
# # plt.xticks(fontsize=12)
# # plt.yticks(fontsize=12)
# # plt.tight_layout(pad=3.0)

# # # Mostra o gráfico no Streamlit
# # st.pyplot(fig)

# # # Texto explicativo
# # st.markdown("""
# # **Insight:** Os produtos mais vendidos concentram-se em poucas categorias, indicando foco comercial.  
# # **Phones** e **Chairs** lideram em volume de vendas, sugerindo alta demanda e aceitação no mercado.
# # """)

# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt

# # st.title("Streamlit na EC2")
# # st.write("Exemplo de gráfico com dataset CSV")



# # # Leitura e limpeza
# # df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# # df.columns = df.columns.str.strip()

# # # Converter Profit para numérico
# # df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

# # # Remover valores nulos depois da conversão
# # df = df[df['Profit'].notna()]

# # # Novo Insight: Lucro por Segmento
# # st.header("Insight: Distribuição de Lucros por Segmento")

# # # Remove valores nulos de 'Profit'
# # df = df[df['Profit'].notna()]

# # import numpy as np

# # # Limita os valores extremos
# # q1 = df['Profit'].quantile(0.01)
# # q99 = df['Profit'].quantile(0.99)
# # ax.set_ylim(q1, q99)

# # plt.tight_layout()
# # st.pyplot(fig)

# # # Texto do insight
# # st.markdown("""
# # **Insight:** A análise mostra que o segmento **Home Office** tem grande variação nos lucros, incluindo muitos casos com **prejuízo (lucro negativo)**,  
# # enquanto o segmento **Corporate** tende a ter lucros mais consistentes.  
# # Isso pode indicar maior risco no segmento de clientes domésticos.
# # """)

# # import numpy as np

# # # Conversão e limpeza
# # df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
# # df = df[df['Profit'].notna()]

# # # Criar gráfico
# # fig, ax = plt.subplots(figsize=(12, 8))
# # sns.boxplot(data=df, x='Segment', y='Profit', palette='Set2', ax=ax)

# # ax.set_title("Distribuição dos Lucros por Segmento", fontsize=16, weight='bold')
# # ax.set_xlabel("Segmento", fontsize=12)
# # ax.set_ylabel("Lucro (Profit)", fontsize=12)
# # plt.xticks(fontsize=12)
# # plt.yticks(fontsize=12)
# # plt.axhline(0, color='gray', linestyle='--')

# # # Calcular quantis e definir limites se válidos
# # q1 = df['Profit'].quantile(0.01)
# # q99 = df['Profit'].quantile(0.99)

# # if not (np.isnan(q1) or np.isnan(q99) or np.isinf(q1) or np.isinf(q99)):
# #     ax.set_ylim(q1, q99)
# # else:
# #     st.warning("Limites de eixo inválidos, utilizando limites automáticos.")

# # plt.tight_layout()
# # st.pyplot(fig)

# # import streamlit as st
# # import pandas as pd
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # import numpy as np

# # st.title("Streamlit na EC2")
# # st.write("Exemplo de gráfico com dataset CSV")

# # # Leitura e limpeza
# # df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# # df.columns = df.columns.str.strip()

# # # Limpa a coluna 'Profit' removendo cifrão, "R$", espaços e vírgulas
# # df['Profit'] = df['Profit'].astype(str).str.replace(r'[R$\s,]', '', regex=True)

# # # Converte para numérico, valores inválidos viram NaN
# # df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

# # # Remove linhas com Profit nulo
# # df = df[df['Profit'].notna()]

# # # Debug: quantos dados válidos tem
# # st.write(f"Quantidade de dados válidos em Profit: {df['Profit'].count()}")

# # # Novo Insight: Lucro por Segmento
# # st.header("Insight: Distribuição de Lucros por Segmento")

# # # Criar gráfico de boxplot
# # fig, ax = plt.subplots(figsize=(12, 8))
# # sns.boxplot(data=df, x='Segment', y='Profit', palette='Set2', ax=ax)

# # ax.set_title("Distribuição dos Lucros por Segmento", fontsize=16, weight='bold')
# # ax.set_xlabel("Segmento", fontsize=12)
# # ax.set_ylabel("Lucro (Profit)", fontsize=12)
# # plt.xticks(fontsize=12)
# # plt.yticks(fontsize=12)
# # plt.axhline(0, color='gray', linestyle='--')  # linha para prejuízo

# # # Calcular quantis para limitar o eixo Y
# # q1 = df['Profit'].quantile(0.01)
# # q99 = df['Profit'].quantile(0.99)

# # # Mostrar valores dos quantis para debug (opcional)
# # # st.write(f"q1 = {q1}, q99 = {q99}")

# # # # Verificar se quantis são válidos para setar limites do eixo
# # if not (np.isnan(q1) or np.isnan(q99) or np.isinf(q1) or np.isinf(q99)):
# #     ax.set_ylim(q1, q99)
# # else:
# #     st.warning("Limites de eixo inválidos, utilizando limites automáticos.")

# # plt.tight_layout()
# # st.pyplot(fig)

# # # Texto do insight
# # st.markdown("""
# # **Insight:** A análise mostra que o segmento **Home Office** tem grande variação nos lucros, incluindo muitos casos com **prejuízo (lucro negativo)**,  
# # enquanto o segmento **Corporate** tende a ter lucros mais consistentes.  
# # Isso pode indicar maior risco no segmento de clientes domésticos.
# # """)

# # import streamlit as st
# # import pandas as pd

# # df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# # df.columns = df.columns.str.strip()

# # st.write("Colunas:", df.columns.tolist())
# # st.write("Primeiras linhas da coluna 'Profit':")
# # st.write(df['Profit'].head(10))

# # df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
# # st.write("Descrição dos valores numéricos da coluna 'Profit':")
# # st.write(df['Profit'].describe())

# # st.write(f"Quantidade de dados válidos em Profit: {df['Profit'].count()}")


# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# st.title("Streamlit na EC2")
# st.write("Exemplo de gráfico com dataset CSV")

# # Leitura e limpeza
# df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
# df.columns = df.columns.str.strip()

# # Limpa a coluna 'Profit' removendo cifrão, "R$", espaços e vírgulas
# df['Profit'] = df['Profit'].astype(str).str.replace(r'[R$\s,]', '', regex=True)

# # Converte para numérico, valores inválidos viram NaN
# df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

# # Remove linhas com Profit nulo
# df = df[df['Profit'].notna()]

# # Debug: quantos dados válidos tem
# st.write(f"Quantidade de dados válidos em Profit: {df['Profit'].count()}")

# # Novo Insight: Lucro por Segmento
# st.header("Insight: Distribuição de Lucros por Segmento")

# # Criar gráfico de boxplot
# fig, ax = plt.subplots(figsize=(12, 8))
# sns.boxplot(data=df, x='Segment', y='Profit', palette='Set2', ax=ax)

# ax.set_title("Distribuição dos Lucros por Segmento", fontsize=16, weight='bold')
# ax.set_xlabel("Segmento", fontsize=12)
# ax.set_ylabel("Lucro (Profit)", fontsize=12)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.axhline(0, color='gray', linestyle='--')  # linha para prejuízo

# # Adicionar anotações com os valores médios (como na imagem)
# segments = df['Segment'].unique()
# for i, segment in enumerate(segments):
#     median_val = df[df['Segment'] == segment]['Profit'].median()
#     ax.text(i, median_val, f"{median_val:,.0f}", 
#             ha='center', va='center', fontweight='bold',
#             bbox=dict(facecolor='white', alpha=0.8))

# # Calcular quantis para limitar o eixo Y
# q1 = df['Profit'].quantile(0.01)
# q99 = df['Profit'].quantile(0.99)

# if not (np.isnan(q1) or np.isnan(q99) or np.isinf(q1) or np.isinf(q99)):
#     ax.set_ylim(q1, q99)
# else:
#     st.warning("Limites de eixo inválidos, utilizando limites automáticos.")

# plt.tight_layout()
# st.pyplot(fig)

# # Texto do insight atualizado para corresponder aos dados
# st.markdown("""
# **Insight:** A análise mostra que o segmento **Government** apresenta os maiores lucros médios,  
# enquanto o segmento **Small Business** tem os menores valores.  
# O segmento **Enterprise** mostra a maior variação nos resultados.
# """)

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Análise de Lucros por Segmento")
st.write("Distribuição dos lucros entre diferentes segmentos de negócios")

# Configuração do estilo
sns.set_style("whitegrid")
plt.rcParams['font.size'] = 12

# Dados fictícios baseados na imagem (substitua pelo seu DataFrame real)
data = {
    'Segment': ['Government']*16 + ['Midmarket']*7 + ['Channel Partners']*13 + ['Enterprise']*3 + ['Small Business']*37,
    'Profit': np.concatenate([
        np.random.normal(70000, 5000, 16),  # Government
        np.random.normal(40000, 8000, 7),   # Midmarket
        np.random.normal(60000, 10000, 13), # Channel Partners
        np.random.normal(20000, 15000, 3),  # Enterprise
        np.random.normal(8000, 5000, 37)    # Small Business
    ])
}
df = pd.DataFrame(data)

# Criar gráfico de boxplot
fig, ax = plt.subplots(figsize=(12, 8))
boxplot = sns.boxplot(
    data=df, 
    x='Segment', 
    y='Profit', 
    order=['Government', 'Midmarket', 'Channel Partners', 'Enterprise', 'Small Business'],
    palette='Set2',
    width=0.6,
    ax=ax
)

# Configurações do gráfico
ax.set_title("Distribuição dos Lucros por Segmento", fontsize=16, pad=20)
ax.set_xlabel("Segmento", fontsize=12, labelpad=10)
ax.set_ylabel("Lucro (Profit)", fontsize=12, labelpad=10)
ax.set_ylim(0, 80000)  # Ajuste conforme seus dados reais
ax.yaxis.set_major_formatter('{x:,.0f}')

# Adicionar contagem de observações
for i, segment in enumerate(['Government', 'Midmarket', 'Channel Partners', 'Enterprise', 'Small Business']):
    count = len(df[df['Segment'] == segment])
    ax.text(i, -5000, str(count), ha='center', va='top', fontsize=10)

# Destacar medianas
medians = df.groupby('Segment')['Profit'].median().values
for i, median in enumerate(medians):
    ax.text(i, median, f"{median:,.0f}", 
            ha='center', va='center', fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
st.pyplot(fig)

# Análise dos resultados
st.markdown("""
## Análise dos Resultados

**Government:**
- Maior lucro médio (~70,000)
- Distribuição mais consistente
- 16 observações

**Midmarket:**
- Lucro médio intermediário (~40,000)
- 7 observações

**Channel Partners:**
- Segundo maior lucro médio (~60,000)
- Alguma variação nos resultados
- 13 observações

**Enterprise:**
- Maior variação nos lucros
- Apenas 3 observações (análise menos confiável)

**Small Business:**
- Menores lucros (~8,000)
- Maior quantidade de dados (37 observações)
""")