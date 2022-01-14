#variaveis
reais = float(input('Digite o valor de reais que possue na carteira: R$'))
cotacao = float(input('Digite a cotação do dolar: R$'))

#logica
dolar = float(reais / cotacao)

#imprimir o resultado
print('Você tem ${:.2f}' .format(dolar))
