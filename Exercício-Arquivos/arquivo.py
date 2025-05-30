
try:
    arquivo = open("produtos.txt", "r")
except FileNotFoundError:
    arquivo = open("produtos.txt", "w")
    arquivo.close() 
    arquivo = open("produtos.txt", "r")#Tratei para criar o arquivo caso ele não exista.

escreverArquivo = open("produtos.txt","a")#Feito exclusivamente para editar o arquivo.
listaProdutos = dict()#usado para verificar se um produto já existe.

for linha in arquivo:#Salvo cada item do documento em um dicionário, para depois fazer comparações.
    produto = linha.split(";")
    listaProdutos[produto[0]]=produto[1]

while True:
    nomeProduto = input("Insira o nome do produto.\nDigite SAIR para encerrar\n")
    if nomeProduto.lower() == "sair":
        break
    elif nomeProduto in listaProdutos:#Aqui é verificado se o produto já existe.
        print("Este produto já está inserido")
        continue
    precoProduto = input("Insira o preço do produto.\nDigite SAIR para encerrar\n")
    if precoProduto.lower() == "sair":
        break
    try:#Aqui o código confere se o valor é válido.(Um número que seja maior que 0)
        if float(precoProduto) <= 0:
            print("Você inseriu um valor inválido")
            continue
    except:
        print("Você não inseriu um valor real.")
        continue

    listaProdutos[nomeProduto] =precoProduto#Adiciono o produto no dicionário, para que este também seja verificado na repetição de produtos.
    escreverArquivo.write(nomeProduto+";"+precoProduto+"\n")#Produto é adicionado

escreverArquivo.close()
valorTotal = 0
menorValor = float("inf")#Medida bruta para que qualquer valor seja menor que este quando for feita a comparação, se for inicializado como um número, há a possibilidade de que nenhum número seja menor, resultando em um output incorreto no fim.
maiorValor = 0

arquivo.close()#Precisei fechar e abrir novamente para o for percorrer as linhas assim como pedido na atividade, senão eu teria usado pelo que está salvo no dicionário mesmo
arquivo = open("produtos.txt", "r")

for linha in arquivo:
    produto = linha.split(";")
    print(f"Produto: {produto[0]}, preço: {produto[1]}")

    if float(produto[1])>maiorValor:
        maiorValor = float(produto[1])
    if float(produto[1])<menorValor:#não usei elif pois há a possibilidade de um valor ser o menor e o maior simultaneamente.
        menorValor = float(produto[1])

    valorTotal = valorTotal + float(produto[1])
if menorValor == float("inf"):
    menorValor = 0
print(f"O valor total é de: {valorTotal}\nO maior valor é de: {maiorValor}\nO menor valor é de: {menorValor}")

    