'''
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Para cada X e Y, escreva uma mensagem para indicar se tais valores foram digitados em ordem crescente ou decrescente.

Entrada
A entrada é composta por vários casos de teste. Cada caso contém dois valores inteiros: X e Y. A leitura deve ser encerrada caso sejam fornecidos os mesmos valores para X e Y.

Saída
Caso os valores tenham sido digitados na ordem crescente, imprima “Crescente”. No contrário, “Decrescente”.
'''

x, y = map(int, input().split())
while (x != y):
    floor = min(x, y)
    top = max(x, y)
    if (x < y):
        print("Crescente")
    elif (x > y):
        print("Decrescente")
    x, y = map(int, input().split())