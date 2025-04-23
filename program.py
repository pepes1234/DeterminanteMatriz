#escolha de qual tipo de matriz vai ser utilizada
tamanhoMatriz = int(input("Escolha o tamanho da matriz:\n1 - 2x2\n2 - 3x3\nEscolha: "))

#verificação de qual tipo de matriz foi selecionada, e tratamento de erro
if tamanhoMatriz == 1:
    #determinação da matriz 2x2
    matriz = [[0 for _ in range(2)] for _ in range(2)]
    #leitura da matriz 2x2
    for i in range(2):
        for j in range(2):
            matriz[i][j] = int(input(f"Digite o valor [{i}][{j}]: "))

    #atribuição dos dados da matriz para variaveis
    a, b = matriz[0]
    c, d = matriz[1]
    #calculo da determinante
    det = (a * d) - (b * c)

    #impressão do resultado
    print("\nMatriz 2x2:")
    for linha in matriz:
        print(linha)
    print(f"\nDeterminante: {det}")
elif tamanhoMatriz == 2:
    #determinação da matriz 3x3
    matriz = [[0 for _ in range(3)] for _ in range(3)]
    #leitura da matriz 3x3
    for i in range(3):
        for j in range(3):
            matriz[i][j] = int(input(f"Digite o valor [{i}][{j}]: "))

    #valores das diagonais da regra de sarrus
    positivos = [1, 1, 1]
    negativos = [1, 1, 1]

    for i in range(3):
        for j in range(3):
            #atribuição dos valores mencionados
            if j == i:            
                positivos[0] *= matriz[i][j]   
            if j == (i+1) % 3:    
                positivos[1] *= matriz[i][j]     
            if j == (i+2) % 3:    
                positivos[2] *= matriz[i][j]  

            if j ==  2 - i:      
                negativos[0] *= matriz[i][j]   
            if j == (2 - i + 1) % 3: 
                negativos[1] *= matriz[i][j]  
            if j == (2 - i + 2) % 3: 
                negativos[2] *= matriz[i][j]  
    #operação final
    det = sum(positivos) - sum(negativos)
    #impressão do resultado
    print("\nMatriz 3x3:")
    for linha in matriz:
        print(linha)
    print(f"\nDeterminante: {det}")

else:
    #tratamento de erro
    print("Opção inválida. Escolha 1 para 2x2 ou 2 para 3x3.")
