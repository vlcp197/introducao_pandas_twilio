import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = #IdTwilio
# Your Auth Token from twilio.com/console
auth_token  = #tokenTwilio

client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel('{}.xlsx'.format(mes))
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print()
        message = client.messages.create(
            to="" , #Numero de quem recebe
            from_="" , #Numero de quem envia
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}. Vendas: {vendas}')
        print(message.sid)





# Para cada arquivo:

# verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o nome, o mês e a as vendas do vendedor

# Caso não seja maior do que 55.000, não fazer nada
