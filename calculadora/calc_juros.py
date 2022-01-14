# Calculadora de juros compostos #

# Inserir o valor inicial

valor_inicial = int(input("Digite o valor inicial: "))

# Inserir o valor do aporte

#valor_aporte = int(input("Digite o valor do aporte fixo mensal: "))

# Inserir o juros Mensal

valor_juros = float(input("Digite o valor do juros fixo mensal: "))

# Inserir a quantidade de meses

valor_meses = int(input("Digite a quantidade de meses: "))

# Realizar o cálculo

total = (valor_inicial * (1 + valor_juros)) ^ valor_meses
    #Imprimir o resultado
print('O valor total do rendimento é: ' + str(total))
