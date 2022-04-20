#Insert data
#salario da pessoa
renda = float(input('Inserir sua renda anual: R$'))
#taxa da previdencia publica
previdencia = float(input('Inserir o valor da sua previdencia: R$'))
#Valor pago com educação
educ = float(input('Inserir essa porra agora educ do caralho de educação: R$'))
#
imp = float(input('Inserir o valor do imposto: R$'))

#conditions
base_simplificado = (renda * 0.8) #
#condition1
if previdencia < (renda * 0.12):
    previdencia = previdencia
else:
    previdencia= (renda * 0.12)
#condition2
if educ < 3561.5 :
    educ = educ
else:
    educ = 3561.5

base_completo= (renda - educ - previdencia) 

#condition3
if base_simplificado < 22847.76:
    ir_simplificado = 0

elif base_simplificado < 33919.8:
    ir_simplificado = (base_simplificado * 0.075-1713.58)
elif base_simplificado < 45012.6:
    ir_simplificado = (base_simplificado * 0.15-4257.57)
elif base_simplificado < 55976.16 :
    ir_simplificado = (base_simplificado * 0.225-7633.51)

else:
    ir_simplificado = (base_simplificado * 0.275-10432.32)
#condition4
if base_completo < 22847.76 :
    ir_completo = 0

elif base_completo < 33919.8 :
    ir_completo = (base_completo * 0.075-1713.58)
elif base_completo < 45012.6 :
    ir_completo = (base_completo * 0.15-4257.57)
elif base_completo < 55976.16 :
    ir_completo=base_completo * 0.225-7633.51

else:
    ir_completo = (base_completo * 0.275-10432.32)

ajuste_simplificado = (ir_simplificado - imp)

ajuste_completo = (ir_completo - imp)

#print

print("Base de calculo (Simplificado): ", format(base_simplificado, ".2f").replace(".", ","))

print("Base de calculo (Completo): ", format(base_completo, ".2f").replace(".", ","))

print("Valor do IR (Simplificado): ", format(ir_simplificado, ".2f").replace(".", ","))

print("Valor do IR (Completo): ", format(ir_completo, ".2f").replace(".", ","))

print("Valor do ajuste (Simplificado): ", format(ajuste_simplificado, ".2f").replace(".", ","))

print("Valor do ajuste (Completo): ", format(ajuste_completo, ".2f").replace(".", ","))

