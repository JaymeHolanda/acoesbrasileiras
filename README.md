# Projeto: Web Scraping de Ações Brasileiras

## Objetivo

O objetivo deste projeto é coletar, organizar e disponibilizar dados de todas as ações negociadas na bolsa brasileira, extraindo informações relevantes como Ticker, Nome, Valor de Mercado, P/L (Preço/Lucro), P/S (Preço/Vendas) e P/VPA (Preço/Valor Patrimonial). O foco é fornecer uma base de dados confiável e padronizada para análises de inteligência de mercado, business intelligence, estudos financeiros e aplicações em ciência de dados.

## Motivação

Ter acesso a indicadores financeiros de todas as empresas listadas em bolsa é fundamental para análises comparativas, construção de dashboards, estudos de mercado, avaliação de oportunidades de investimento, e desenvolvimento de aplicações analíticas.

## Desafios Encontrados

Durante o desenvolvimento, enfrentamos grandes desafios para encontrar fontes de dados públicas, confiáveis e que permitissem o uso de web scraping. Muitos sites bloqueiam robôs, exigem autenticação ou não fornecem os dados de forma estruturada. Após muitos testes, a TradingView se mostrou a melhor opção, pois apresenta os dados de forma dinâmica e relativamente acessível via automação.


## Dependências Utilizadas

O projeto utiliza as seguintes bibliotecas:

- **Selenium**: Para automação do navegador e coleta de dados dinâmicos.

- **webdriver-manager**: Facilita o gerenciamento do driver do navegador.

- **BeautifulSoup**: Para parsing e extração dos dados HTML.

- **Pandas**: Para organização, limpeza e exportação dos dados em CSV.

- **Matplotlib**: Para geração de gráficos e visualizações.

- **Seaborn**: Para gráficos estatísticos avançados e mais bonitos.

Instale todas as dependências com:
```bash
pip install -r requirements.txt
```

## Como rodar o projeto
1. Certifique-se de ter o Python 3 instalado.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal para coletar e tratar os dados:
   ```bash
   python main.py
   ```
   O arquivo `acoes_tradingview_tratado.csv` será gerado com os dados prontos para análise.

4. Para gerar os gráficos e o relatório em PDF:
   ```bash
   python "Gerar Graficos.py"
   ```
   Isso irá criar o arquivo `relatorio_graficos.pdf` com todos os principais gráficos e análises extraídas dos dados.

<<<<<<< HEAD
## Funcionalidades dos Gráficos

- Top 3 ações com maior e menor valor de mercado
- Top 3 ações com maior e menor P/L
- Top 5 setores com maior valor de mercado total
- Top 10 setores com maior Dividend Yield médio
- Top 10 empresas “baratas” (baixo P/L) com alto Dividend Yield (mostrando preço)
- Todos os gráficos são salvos em PDF para fácil compartilhamento

=======
<<<<<<< HEAD

=======
## Funcionalidades dos Gráficos

- Top 3 ações com maior e menor valor de mercado
- Top 3 ações com maior e menor P/L
- Top 5 setores com maior valor de mercado total
- Top 10 setores com maior Dividend Yield médio
- Top 10 empresas “baratas” (baixo P/L) com alto Dividend Yield (mostrando preço)
- Todos os gráficos são salvos em PDF para fácil compartilhamento

>>>>>>> 92716de

## Principais Insights Extraídos dos Gráficos

- **Setores de maior valor de mercado:** O setor Financeiro lidera em valor de mercado total, seguido por Serviços Públicos e Minerais Energéticos.
  
  ![Setores de maior valor de mercado](IMG/Figure_1.png)

- **Setor mais lucrativo:** O setor de Minerais Energéticos apresenta o maior Dividend Yield médio entre todos os setores analisados.
  
  ![Setor mais lucrativo - DY médio](IMG/Figure_2.png)

- **Empresas “baratas” com alto Dividend Yield:** Foram identificadas diversas empresas com P/L abaixo da mediana e Dividend Yield acima da mediana, o que pode indicar boas oportunidades de investimento.
  
  ![Empresas baratas com alto Dividend Yield](IMG/Figure_3.png)

- **Ação mais barata do setor mais lucrativo:** Dentro do setor de maior DY médio, foi possível identificar a ação de menor preço, facilitando análises de custo-benefício.
  
  ![Ação mais barata do setor mais lucrativo](IMG/Figure_4.png)

- **Ranking de empresas:** Os gráficos permitem identificar rapidamente as empresas com maior e menor valor de mercado, bem como aquelas com extremos de P/L e Dividend Yield.
  
<<<<<<< HEAD
  ![Ranking de empresas](IMG/Figure_5.png)
=======
  ![Ranking de empresas](IMG/Figure_5.png)
>>>>>>> 21ffda5 (Atualiza README, adiciona imagens dos insights e mantém gráficos e scripts atualizados)
>>>>>>> 92716de
