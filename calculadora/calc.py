# Calculadora Python #

# Perguntar qual o tipo de operação que quer fazer?

operation = input('Qual operação deseja realizar? (+ - / *)')

# Perguntar o primeiro número

num1 = int(input('Digite o primeiro número: '))

# Perguntar o segundo número

num2 = int(input('Digite o segundo número: '))

# Calculo dos números
#total = num1 (operation) num2

if operation == '+':
    total = num1 + num2
    # Imprimir o resultado na tela
    print('O resultado é: ' + str(total))
elif operation == '-':
    total = num1 - num2
    # Imprimir o resultado na tela
    print('O resultado é: ' + str(total))
elif operation == '*':
    total = num1 * num2
    # Imprimir o resultado na tela
    print('O resultado é: ' + str(total))
elif operation == '/':
    total = num1 / num2
    # Imprimir o resultado na tela
    print('O resultado é: ' + str(total))
else:
    print("A operação é inválida!")
