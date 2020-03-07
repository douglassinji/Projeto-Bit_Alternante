# Projeto - Bit Alternante
## Transporte confiável de dados utilizando protocolo de bit alternante 

Esse projeto consistem em dois arquivos, um chamado sender.py e outro receiver.py. 
O primeiro arquivo, sender.py ira enviar mensagens para outro host através do protocolo UDP, porem de forma segura.
Esse programa precisa de tres inputs, sendo eles o Port# por qual o msg sera enviada, a qtd de msg que deseja enviar e o IP do destinatario.
Já o receiver.py, precisa de apenas um Input, nesse caso apenas o Port#.
Importante: Para que se possivel a comunicacao entre os dois computadores, tanto o sender quanto o receive deve recever o msm port#.
#### O programa funciona da seguinte forma:
Primeiramente o deve abrir o arquivo receiver.py, no inicio, o programa solicitará o Port Number, esse input deve ser um numero inteiro
de 10001 a 11000. Apos isso, o usuario devera abrir o arquivo sender. py, o primeiro valor solicitado pelo programa é a qtd de msg
que o usuario deseja enviar, esse valor deve ser um numero inteiro. Logo apos, sera solicitado o port# de comunicacao, esse valor deve ser
o mesmo valor "inputado" no receiver e tambem deve ser um numero inteiro de 10001 a 11000 e por ultimo sera solicitado  o IP do destinatario.
Apos os 3 valores serem inputados, ambos computadores  iram mostrar na tela os valores enviados e recebidos.
