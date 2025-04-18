import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('acoes_tradingview_tratado.csv', sep=';')

def parse_valor_mercado(valor):
    if pd.isna(valor) or valor == '—':
        return 0
    valor = valor.replace('BRL', '').replace(' ', '').replace('\u202f', '').replace(',', '.')
    if 'B' in valor:
        return float(valor.replace('B', '')) * 1e9
    if 'M' in valor:
        return float(valor.replace('M', '')) * 1e6
    if 'K' in valor:
        return float(valor.replace('K', '')) * 1e3
    try:
        return float(valor)
    except:
        return 0

def parse_float(valor):
    if pd.isna(valor) or valor == '—':
        return float('nan')
    valor = valor.replace('%', '').replace(',', '.').replace('+','').replace('−','-')
    try:
        return float(valor)
    except:
        return float('nan')

# Normaliza colunas numéricas
df['Valor de Mercado Num'] = df['Valor de Mercado'].apply(parse_valor_mercado)
df['P/L Num'] = df['P/L'].apply(parse_float)
df['Crescimento EPS dil. Num'] = df['Crescimento EPS dil.'].apply(parse_float)
df['Div. Yield % Num'] = df['Div. Yield %'].apply(parse_float)

# Top 3 maior/menor Valor de Mercado
top3_maior_vm = df.nlargest(3, 'Valor de Mercado Num')
top3_menor_vm = df[df['Valor de Mercado Num'] > 0].nsmallest(3, 'Valor de Mercado Num')

# Top 3 maior/menor P/L
top3_maior_pl = df.nlargest(3, 'P/L Num')
top3_menor_pl = df[df['P/L Num'] > 0].nsmallest(3, 'P/L Num')

# Maior e menor valor de mercado
maior_vm = df.loc[df['Valor de Mercado Num'].idxmax()]
menor_vm_idx = df[df['Valor de Mercado Num'] > 0]['Valor de Mercado Num'].idxmin()
menor_vm = df.loc[menor_vm_idx]

# Maior crescimento EPS
grow_eps = df.loc[df['Crescimento EPS dil. Num'].idxmax()]
# Maior Dividend Yield
grow_dy = df.loc[df['Div. Yield % Num'].idxmax()]

# Gráficos
def plot_bar(data, col, title, ylabel):
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Ticker', y=col, data=data, palette='viridis')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel('Ticker')
    plt.tight_layout()
    plt.show()

# Top 3 maior valor de mercado
plot_bar(top3_maior_vm, 'Valor de Mercado Num', 'Top 3 Maior Valor de Mercado', 'Valor de Mercado (R$)')
# Top 3 menor valor de mercado
plot_bar(top3_menor_vm, 'Valor de Mercado Num', 'Top 3 Menor Valor de Mercado', 'Valor de Mercado (R$)')
# Top 3 maior P/L
plot_bar(top3_maior_pl, 'P/L Num', 'Top 3 Maior P/L', 'P/L')
# Top 3 menor P/L
plot_bar(top3_menor_pl, 'P/L Num', 'Top 3 Menor P/L', 'P/L')

print('\nMaior valor de mercado:')
print(maior_vm[['Ticker', 'Nome', 'Valor de Mercado']])
print('\nMenor valor de mercado:')
print(menor_vm[['Ticker', 'Nome', 'Valor de Mercado']])
print('\nMaior crescimento EPS:')
print(grow_eps[['Ticker', 'Nome', 'Crescimento EPS dil.']])
print('\nMaior Dividend Yield:')
print(grow_dy[['Ticker', 'Nome', 'Div. Yield %']])


top_setores_vm = df.groupby('Setor')['Valor de Mercado Num'].sum().sort_values(ascending=False).head(5)
print('\nTop 5 setores com maior valor de mercado total:')
print(top_setores_vm)


plt.figure(figsize=(10,5))
sns.barplot(x=top_setores_vm.index, y=top_setores_vm.values, palette="Blues_d")
plt.title('Top 5 setores - Valor de Mercado Total')
plt.ylabel('Valor de Mercado (R$)')
plt.xlabel('Setor')
plt.tight_layout()
plt.show()


pl_medio_setor = df.groupby('Setor')['P/L Num'].mean().sort_values(ascending=False)
print('\nSetor com maior P/L médio:')
print(pl_medio_setor.head(1))


dy_medio_setor = df.groupby('Setor')['Div. Yield % Num'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,5))
x_labels = [f'Setor: {setor}' for setor in dy_medio_setor.index]
sns.barplot(x=x_labels, y=dy_medio_setor.values, palette="Greens_d")
plt.title('Top 10 setores - Dividend Yield médio')
plt.ylabel('Dividend Yield médio (%)')
plt.xlabel('Setor')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()


pl_mediana = df['P/L Num'].median()
dy_mediana = df['Div. Yield % Num'].median()
empresas_baratas_dy = df[(df['P/L Num'] < pl_mediana) & (df['Div. Yield % Num'] > dy_mediana)]
print('\n=== Empresas “baratas” com alto Dividend Yield ===')
print(f'Critérios: P/L abaixo da mediana ({pl_mediana:.2f}) e DY acima da mediana ({dy_mediana:.2f}%)')
print(empresas_baratas_dy[['Ticker', 'Nome', 'P/L', 'Div. Yield %']])


plt.figure(figsize=(12,5))
baratas_dy_plot = empresas_baratas_dy.head(10).copy()
baratas_dy_plot['Ticker+Preço'] = baratas_dy_plot.apply(lambda row: f"{row['Ticker']} ({row['Preço']})", axis=1)
sns.barplot(x=baratas_dy_plot['Ticker+Preço'], y=baratas_dy_plot['Div. Yield % Num'], palette="Oranges_d")
plt.title('Top 10 empresas baratas com alto Dividend Yield')
plt.ylabel('Dividend Yield (%)')
plt.xlabel('Empresa (Ticker e Preço)')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()


setor_mais_lucrativo = df.groupby('Setor')['Div. Yield % Num'].mean().sort_values(ascending=False).index[0]
print(f'\nSetor mais lucrativo (maior DY médio): {setor_mais_lucrativo}')
df_setor_lucrativo = df[df['Setor'] == setor_mais_lucrativo]
acao_mais_barata = df_setor_lucrativo.loc[df_setor_lucrativo['Preço'].apply(lambda x: float(str(x).replace("BRL","").replace(",",".").replace(" ","").strip()) if pd.notna(x) else float("inf")).idxmin()]
print('Ação mais barata desse setor:')
print(acao_mais_barata[['Ticker', 'Nome', 'Preço', 'Div. Yield %']])
