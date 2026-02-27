totalvendido = 0
vendas = []

while True:
    entrada = input("Digite um número ou (sair) ")

    if entrada.lower() == "sair":
        print ("Sistema encerrado")
        print ("Quantidade de vendas é", len((vendas)))
        print ("O valor total em vendas é: ", sum((vendas)))
        print ("A média das vendas é: ", sum((vendas))/len((vendas)))
        break

    elif entrada.lower() == "vendas":
        print (len((vendas)))

    elif entrada.lower () == "valor das vendas":
        print (sum((vendas)))
    
    elif entrada.lower() == "médias das vendas":
        print (sum((vendas))/len((vendas)))

    preço = float(entrada)
    desconto = float(input("digite o desconto: "))

    if desconto > 100:
        print ("valor inválido")
    
    else: 
        valorfinal = preço - (preço*desconto/100)
        totalvendido += valorfinal 
        vendas.append (valorfinal)
        print ("o valor final é R$",valorfinal)
        print ("o total vendido é", totalvendido)
