from selenium.webdriver.common.by import By
from modulos.starting_driver import*
from modulos.actions import *

# LEIA O PRODUTO DO USUÁRIO 
entrada = input('Digite o produto que deseja: ')

# ABRIR O NAVEGADOR
driver = start_driver()

# NAVEGUE ATÉ O SITE: https://lista.mercadolivre.com.br/PRODUTO#D[A:PRODUTO]
driver.get(f'https://lista.mercadolivre.com.br/{entrada}#D[A:{entrada}]')
###FAZER ISSO ATÉ A ÚLTIMA PÁGINA
produtos = '//div[@class="andes-card ui-search-result shops__cardStyles ui-search-result--core andes-card--flat andes-card--padding-16"]'

titulos = '//h2[@class="ui-search-item__title shops__item-title"]/text()'

precos = '//div[@class="ui-search-item__group__element ui-search-price__part-without-link shops__items-group-details"]//div[@class="ui-search-price ui-search-price--size-medium shops__price"]//div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="andes-money-amount__fraction"]/text()'

links = '//div[@class="andes-card ui-search-result shops__cardStyles ui-search-result--core andes-card--flat andes-card--padding-16"]//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]/@href'


while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    produtos_titulos = driver.find_elements(By.XPATH, f'{produtos}{titulos}')
    produtos_precos = driver.find_elements(By.XPATH,f'{produtos}{precos}')
    produtos_links = driver.find_elements(By.XPATH, f'{produtos}{links}')
    with open('../resultado.csv', 'add', encoding='UTF-8') as arquivo:
        
	# DESCER ATÉ O FINAL DA TELA
