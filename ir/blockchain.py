#title
print('Calculo mensal de pagamento DARF: Blockchain')

#variables
compra = float(input('Inserir o valor de compra da ação: R$ '))
venda = float(input('Inserir o valor de venda da ação: R$ '))
lucro = float(venda - compra)
imposto = 0.15
darf = float(lucro * imposto)
limite = 35000.00

#conditions
if venda > limite:
    print('Seu lucro foi de R$ {:.2f}, com isso terá de pagar um DARF para Blockchain de R$ {:.2f}' .format(lucro,darf))
    print('Para realizar o pagamento da DARF, acessar o link: https://www.gov.br/pt-br/servicos/emitir-darf-para-pagamento-de-tributos-federais')
else:
    print ('Você não irá precisar pagar DARF, pois sua venda foi abaixo de R${:.2f} no mês!' .format(limite))