'''Python 2'''

#Entrada

nome = input("Digite seu nome: ")
local = float(input("Digite o código de sua região: "))
num_pecas = float(input("Dígite o número de peças adquiridas: "))
nome_vendedor = input("Digite o nome de seu vendedor: ") 



#Processamento

sul = 1
norte = 2
leste = 3
oeste = 4


if local == 1:
    valor_frete = (num_pecas * 1.00)
    if num_pecas > 1000:
       valor_frete = (num_pecas * 0.9)

if local == 2:
    valor_frete = (num_pecas * 1.10)
    if num_pecas > 1000:
       valor_frete = (num_pecas * 1.0)

if local == 3:
    valor_frete = (num_pecas * 1.15)
    if num_pecas > 1000:
        valor_frete = (num_pecas * 1.10)


if local == 4:
    valor_frete = (num_pecas * 1.20)
    if num_pecas > 1000:
        valor_frete = (num_pecas * 1.15)
        

valor_pecas = (num_pecas * 7)

valor_total = (valor_pecas + valor_pecas/2)

comissao = (valor_total * 0.065)

lucro = round(valor_total - valor_pecas - comissao,2)



#Saída

print("O valor do frete para sua região é de: ", valor_frete)
print("O valor total de sua compra foi de: ", valor_total)
print("Comissão do vendedor", nome_vendedor, "é de: ", comissao)
print("Este é o lucro total: ", lucro)





