# Automatiza-o-Python

Script criado para automatizar consuta de cpf, se o cliente realizou o pagamento, qual o foi o tipo de pagamento e data do pagamento.

Utilizei a biblioteca Openpyxl, pois está biblioteca é quem verifica qual a planilha que vamos usar e qual formato ela está.

Utilizei o Selenium, para poder utilizar a função web.driver, para poder acessar o site que confere se o cliente pagou, quando pagou e qual foi a forma de pagamento.

utilizei o By.XPATH pois é o comando que indica qual dado queremos pegar na planilha e verificar se está pago ou em atraso.

A função driver, é para saber qual a URL vamos usar para ter acesso ao banco de dados para verificarmos a procedencia de cada cliente.

Na linha "driver.get('')" é onde colocamos a URL do cliente para o script saber onde ele ira fazer a conferência de pagamento/forma de pagamento, dos clientes
