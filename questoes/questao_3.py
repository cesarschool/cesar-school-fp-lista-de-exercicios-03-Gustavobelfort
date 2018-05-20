## QUESTÃO 3 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
cima = 0
baixo = 0
direita = 0
esquerda = 0

def main():

    def classify(a):
        global cima
        global baixo
        global direita
        global esquerda

        a = a.split(' ')

        if a[0] == 'CIMA':
            cima += int(a[1])
        if a[0] == 'BAIXO':
            baixo += int(a[1])
        if a[0] == 'DIREITA':
            direita += int(a[1])
        if a[0] == 'ESQUERDA':
            esquerda += int(a[1])

    while True:
        b = input()
        if b == '':
            break
        else:
            classify(b)
            continue

    rounded = ((baixo - cima)**2 + (esquerda - direita)**2 )**(1/2)
    print( round(rounded))



    
if __name__ == '__main__':
    main()
