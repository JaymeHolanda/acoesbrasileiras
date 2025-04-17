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
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. O arquivo `acoes_tradingview_tratado.csv` será gerado com os dados prontos para análise.

## Próximos Passos
O próximo passo deste projeto será a implementação de dashboards interativos para análise das 290 empresas listadas, permitindo visualizações dinâmicas, filtros e insights personalizados para o RH e demais áreas interessadas.


