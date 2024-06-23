import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

planilha_clientes = openpyxl.load_workbook('dados_clientes.xlsx')
pagina_clientes = planilha_clientes['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2,values_only=True):
   nome, valor, cpf, vencimento = linha

driver = webdriver.Chrome()
driver.get('inserir o site de consulta da empresa')
sleep(5)
campo_pesquisa = driver.find_element(By.XPATH,"")
sleep(1)
campo_pesquisa.send_keys(cpf)
sleep(1)

botao_pesquisar = driver.find_element(By.XPATH,"")
sleep(1)
botao_pesquisar.click()
