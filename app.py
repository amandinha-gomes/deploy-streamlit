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