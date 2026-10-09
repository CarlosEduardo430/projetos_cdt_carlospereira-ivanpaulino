import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

NOME_GRUPO = "Programação 2/26 B/Tarde"
NOME_CONTATO_MENTION = "CarlosPereira" 

options = webdriver.ChromeOptions()

options.add_argument(r"--user-data-dir=C:\WhatsAppAutomacao")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://web.whatsapp.com/")

print("WhatsApp Web aberto...")
print("Aguardando o login/conexão do WhatsApp...")

wait = WebDriverWait(driver, 120)

try:
    
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@role="application"]'))
    )

    print("WhatsApp conectado!")

except Exception as e:
    print("Não foi possível conectar automaticamente.")
    print("Faça a autenticação normalmente e execute novamente.")
    input("Pressione ENTER para continuar...")

time.sleep(3)

try:
    print(f"Procurando o grupo: {NOME_GRUPO}")

    grupo = wait.until(
        EC.element_to_be_clickable((By.XPATH, f'//span[@title="{NOME_GRUPO}"]'))
    )

    grupo.click()

    print("Grupo encontrado e aberto!")

    time.sleep(2)

    caixa_mensagem = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//footer//div[@contenteditable="true"][@role="textbox"]')
        )
    )

    caixa_mensagem.click()

    caixa_mensagem.send_keys(f"@{NOME_CONTATO_MENTION}")

    time.sleep(1.5)

    caixa_mensagem.send_keys(Keys.TAB)
    
    time.sleep(0.5)

    caixa_mensagem.send_keys(Keys.ENTER)

    print("Mensagem enviada e contato mencionado com sucesso! 🔥")

except Exception as erro:
    print("\nERRO ao tentar enviar mensagem:")
    print(erro)
    print("\nVerifique se o nome do grupo e do contato estão exatamente corretos.")

input("\nPressione ENTER para fechar o navegador...")
driver.quit()