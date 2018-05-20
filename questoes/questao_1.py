## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234 @ 1, um F1 #, 2w3E *, 2We3345
# Então, a saída do programa deve ser:
# ABd1234 @ 1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

def main():
    def checkAlpha(var):
        for i in var:
            if i.isalpha() == True :
                return True     

    def checkNumber(var):
        for i in var:
            if i.isnumeric() == True :
                return True
    
    def checkUpper(var):
        for i in var:
            if i.isupper() == True :
                return True

    def checkLower(var):
        for i in var:
            if i.islower() == True :
                return True

    def checkSpecial(var):
        char1 = '$'
        char2 = '#' 
        char3 = '@'
        for i in var:
            if i == char1 or i == char2 or i == char3 :
                return True

    def checkLen(var):
        if len(var) >= 6 and len(var) <= 12 :
            return True

    def checkAll(var):
        if checkLen(var) and checkNumber(var) and checkUpper(var) and checkLower(var) and checkAlpha(var) and checkSpecial(var): 
            return True

    password = input()

    password = password.split(',')

    right = []

    for word in password :
        if checkAll(word) == True:
            right.append(word)
        else:
            continue
    print(','.join(right))    

if __name__ == '__main__':
    main()
