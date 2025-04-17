from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://br.tradingview.com/markets/stocks-brazil/market-movers-all-stocks/"

# Configurações do Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')

# Inicia o navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

# Espera a tabela aparecer
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.TAG_NAME, "tbody"))
)

# Clicar em "Carregar mais" até não existir mais
while True:
    try:
        # Scroll até o final da página para garantir que o botão aparece
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
        # Buscar o botão pelo span de texto
        btn = driver.find_element(By.XPATH, "//span[contains(@class, 'content-') and contains(text(), 'Carregar Mais')]/ancestor::button")
        if btn.is_enabled() and btn.is_displayed():
            driver.execute_script("arguments[0].click();", btn)
            print("Cliquei em Carregar Mais...")
            time.sleep(2.5)  # Espera mais para garantir carregamento
        else:
            break
    except Exception as e:
        print("Não há mais botão Carregar Mais ou ocorreu erro:", e)
        break

# Extrai o HTML final
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

import re
acoes = []
for row in soup.select('tbody tr'):
    cols = row.find_all('td')
    if len(cols) >= 7:  # Garante que há colunas suficientes
        texto = cols[0].get_text(strip=True)
        ticker = texto[:5].strip()
        nome_match = re.match(r'^([A-Z0-9]{4,5})\s*([A-ZÇÃÕÉÊÍÓÚÂÊÔÜÁÀÈÌÒÙÄËÏÖÜa-zçãõéêíóúâêôüáàèìòùäëïöü\s\./&-]+)', texto)
        if nome_match:
            nome = nome_match.group(2).strip()
        else:
            nome = texto[len(ticker):].strip()
        nome = re.sub(r'\s+(ON|PN|NMD|N1D|OND|EJD|ED|NM|N2D|N2|N1|N3|EDJ|EJ|N|D|B|C|F|G|H|I|J|K|L|M|O|P|Q|R|S|T|U|V|W|X|Y|Z)($|\s)', '', nome, flags=re.IGNORECASE).strip()
        valor_mercado = cols[2].get_text(strip=True)  # Ajuste o índice conforme necessário
        pl = cols[3].get_text(strip=True)
        ps = cols[4].get_text(strip=True)
        pb = cols[5].get_text(strip=True)
        acoes.append({
            'Ticker': ticker,
            'Nome': nome,
            'Valor de Mercado': valor_mercado,
            'PL': pl,
            'PS': ps,
            'PB': pb
        })

driver.quit()

# Salvar em CSV
df = pd.DataFrame(acoes)
df.to_csv('acoes_tradingview.csv', index=False, encoding='utf-8-sig')
print(f'{len(df)} ações salvas em acoes_tradingview.csv')

# --- Pós-processamento do CSV ---
# Lê o arquivo gerado
df = pd.read_csv('acoes_tradingview.csv')
# Remove espaços antes/depois dos valores de todas as colunas (strip)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
# Salva novamente com separador ';'
df.to_csv('acoes_tradingview_tratado.csv', index=False, sep=';', encoding='utf-8-sig')
print(f'Arquivo tratado salvo como acoes_tradingview_tratado.csv com separador ;')

