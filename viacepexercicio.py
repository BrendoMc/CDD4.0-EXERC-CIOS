import mysql.connector as mysqlc
import requests
banco = mysqlc.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turmaa"
)
cep = input("Qual o seu CEP?: ")
if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json'
    requisicao = requests.get(link)
    print(requisicao)
    dic_requisicao = requisicao.json()

    cep = dic_requisicao['cep']
    logadouro = dic_requisicao['logradouro']
    complemento = dic_requisicao['complemento']
    print(dic_requisicao)
    meucursor = banco.cursor()
    sql = "INSERT INTO enderecos ( cep, logadouro, complemento) VALUES (%s,%s,%s);"
    data = (cep, logadouro, complemento,)
    meucursor.execute(sql, data)
    banco.commit()
    meucursor.close()
    banco.close()
else:
    print("CEP invalído")
