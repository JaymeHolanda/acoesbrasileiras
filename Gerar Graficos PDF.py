import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Carrega o CSV tratado
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

with PdfPages('relatorio_graficos.pdf') as pdf:
    # Top 3 maior valor de mercado
    top3_maior_vm = df.nlargest(3, 'Valor de Mercado Num')
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Ticker', y='Valor de Mercado Num', data=top3_maior_vm, palette='viridis')
    plt.title('Top 3 Maior Valor de Mercado')
    plt.ylabel('Valor de Mercado (R$)')
    plt.xlabel('Ticker')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # Top 3 menor valor de mercado
    top3_menor_vm = df[df['Valor de Mercado Num'] > 0].nsmallest(3, 'Valor de Mercado Num')
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Ticker', y='Valor de Mercado Num', data=top3_menor_vm, palette='viridis')
    plt.title('Top 3 Menor Valor de Mercado')
    plt.ylabel('Valor de Mercado (R$)')
    plt.xlabel('Ticker')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # Top 3 maior P/L
    top3_maior_pl = df.nlargest(3, 'P/L Num')
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Ticker', y='P/L Num', data=top3_maior_pl, palette='viridis')
    plt.title('Top 3 Maior P/L')
    plt.ylabel('P/L')
    plt.xlabel('Ticker')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # Top 3 menor P/L
    top3_menor_pl = df[df['P/L Num'] > 0].nsmallest(3, 'P/L Num')
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Ticker', y='P/L Num', data=top3_menor_pl, palette='viridis')
    plt.title('Top 3 Menor P/L')
    plt.ylabel('P/L')
    plt.xlabel('Ticker')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # Top 5 setores com maior valor de mercado total
    top_setores_vm = df.groupby('Setor')['Valor de Mercado Num'].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(10,5))
    sns.barplot(x=top_setores_vm.index, y=top_setores_vm.values, palette="Blues_d")
    plt.title('Top 5 setores - Valor de Mercado Total')
    plt.ylabel('Valor de Mercado (R$)')
    plt.xlabel('Setor')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # Top 10 setores - Dividend Yield médio
    dy_medio_setor = df.groupby('Setor')['Div. Yield % Num'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,5))
    x_labels = [f'Setor: {setor}' for setor in dy_medio_setor.index]
    sns.barplot(x=x_labels, y=dy_medio_setor.values, palette="Greens_d")
    plt.title('Top 10 setores - Dividend Yield médio')
    plt.ylabel('Dividend Yield médio (%)')
    plt.xlabel('Setor')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    pdf.savefig(); plt.close()

    # Top 10 empresas baratas com alto Dividend Yield (com preço)
    pl_mediana = df['P/L Num'].median()
    dy_mediana = df['Div. Yield % Num'].median()
    empresas_baratas_dy = df[(df['P/L Num'] < pl_mediana) & (df['Div. Yield % Num'] > dy_mediana)]
    baratas_dy_plot = empresas_baratas_dy.head(10).copy()
    baratas_dy_plot['Ticker+Preço'] = baratas_dy_plot.apply(lambda row: f"{row['Ticker']} ({row['Preço']})", axis=1)
    plt.figure(figsize=(12,5))
    sns.barplot(x=baratas_dy_plot['Ticker+Preço'], y=baratas_dy_plot['Div. Yield % Num'], palette="Oranges_d")
    plt.title('Top 10 empresas baratas com alto Dividend Yield')
    plt.ylabel('Dividend Yield (%)')
    plt.xlabel('Empresa (Ticker e Preço)')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    pdf.savefig(); plt.close()

print('PDF gerado como relatorio_graficos.pdf')
