#title
print('Calculo mensal de pagamento DARF: Ações - Day Trade')

#variables
compra = float(input('Inserir o valor de compra da ação: R$ '))
venda = float(input('Inserir o valor de venda da ação: R$ '))
lucro = float(venda - compra)
imposto = 0.20
darf = float(lucro * imposto)

#print
print('Seu lucro foi de R$ {:.2f}, com isso terá de pagar um DARF para ações em Day Trade de R$ {:.2f}' .format(lucro,darf))
print('Para realizar o pagamento da DARF, acessar o link: https://www.gov.br/pt-br/servicos/emitir-darf-para-pagamento-de-tributos-federais')