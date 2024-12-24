import sys

#Validando CPF Com Python
strCPF = '11122233396'
numDV1 = 0
numDV2 = 0
numCheckDV1 = 0
numCheckDV2 = 0
i = 0
# Verificar o numero de cacteres do CPF

if len(strCPF) < 11:
    difcpf = 11 - len(strCPF)
    strCPF = '0' * difcpf + strCPF

# Captura o numero do digito verificador
numDV1 = int(strCPF[9:10])
numDV2 = int(strCPF[10:11])

# Calcula o primeiro digito verificador
for i in range(1, 10):
    numDV1 = numDV1 + int(strCPF[i-1:i]) * i

#Resto da divisão
numDV1 = numDV1 % 11

#Verifcar se o numero é mais que 10
if (numDV1 == 10):
    numDV1 = 0


if numDV1 != numCheckDV1:
    sys.exit('CPF invalido')
 

# Calcula o segundo digito verificador
for i in range(2, 11):
    numDV2 = numDV2 + int(strCPF[i:i+1]) * (i - 1)

#Resto da divisão
numCheckDV2 = numDV2 % 11

