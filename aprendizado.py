def definir_imc (peso,altura):
    if altura <=0 or peso <=0:
        return None,"Peso ou Altura inválida"
    else:
        imc = peso/(altura**2)
    if imc <18.5:
        return imc, "Abaixo do peso"
    elif imc >=18.5 and imc <=24.9:
       return imc, "Peso normal"
    elif imc >=25 and imc <=29.9:
        return imc, "Sobrepeso"
    elif imc >= 30:
        return imc, "Obesidade"

historico = [ ]

while True:
    opção = input (
        "Digite 1 para calcular\n"
        "Digite 2 para exibir o histórico\n"
        "Digite 3 para remover alguém do histórico\n"
        "Digite 4 para atualizar dados\n"
        "Digite 5 para sair\n"
    )

    if opção == "1":
        nome = input ("Digite seu nome e sobrenome ")
        peso = input("Digite seu peso em kg ")
        peso = peso.replace (",",".")
        peso = float(peso)
        altura = input("Digite sua altura em m (Ex: 1,76) ")
        altura = altura.replace (",",".")
        altura = float (altura)
        if altura < 0.5 or altura > 3:
            print ("valor inválido")
        else: 
            imc_calculado, classificação = definir_imc(peso,altura)
            if imc_calculado is not None:
                print ("Seu imc é: ", f"{imc_calculado:.1f}")
            print (classificação)
            historico.append ({
                "Nome": nome,
                "imc": imc_calculado,
                "classificação": classificação})

    elif opção == "2":
        if not historico:
            print("Histórico vázio")
        else:
            for pessoa in historico:
                print (
                    f"Nome: {pessoa['Nome']} | "
                    f"IMC: {pessoa['imc']:.1f} | "
                    f"Classificação {pessoa['classificação']}"
                )

    elif opção == "3":
        if not historico:
            print("Histórico vazio")
        else:
            nome_remover = input ("Digite o nome que desja remover ").strip().lower()
            encontrados = [ ]
            
            for i, pessoa in enumerate(historico):
                if nome_remover.lower() in pessoa["Nome"].strip().lower():
                    encontrados.append((i,pessoa))
            if not encontrados:
                print ("Pessoa não encontrada")
            else:
                print ("\n Pessoas encontradas: ")
                    
                for indice, pessoa in encontrados:
                    print(
                        f"{indice} - "
                        f"{pessoa['Nome']} - |"
                        f"{pessoa['imc']:.1f} |"
                        f"{pessoa['classificação']}"
                        )
                    
                escolha = input("Dgite o número da pessoa que deseja remover: ")
                    
                if escolha.isdigit():
                        escolha = int(escolha)
                        indices_validos = [i for i, _ in encontrados]

                        if escolha in indices_validos:
                            confirmação = input ("Tem certeza? (s/n) ")

                            if confirmação.lower() == "s":
                                    removido = historico.pop(escolha)
                                    print ("Removido com sucesso")

                        else:
                            print ("Número inválido")
                else:
                     print ("Entrada inválida")
    
    elif opção == "4":
        if not historico:
            print ("Histórico vázio")
        else:
            nome_busca = input("Digite o nome que deseja atualizar: ")
            encontrados = []
        
        for i, pessoa in enumerate(historico):
            if nome_busca in pessoa["Nome"].lower():
                encontrados.append((i,pessoa))
            if not encontrados:
                print ("Pessoa não encontrada")
            else:
                print ("\n Pessoas encontradas")
                for posicao, (indice_real, pessoa) in enumerate(encontrados):
                    print (
                        f"{posicao} -"
                        f"{pessoa["Nome"]} | "
                        f"{pessoa["imc"]} | "
                        f"{pessoa["classificação"]}"
                    )

                escolha = input ("Digite o número da pessoa que deseja atualizar: ")

                if escolha.isdigit():
                    escolha = int(escolha)

                    if  0 <= escolha < len(encontrados):
                        indice_real = encontrados [escolha][0]
                        pessoa = historico [indice_real]

                        print ("\n Digite os novos dados ou pressione ENTER para manter")

                        novo_nome = input (f"Nome atual({pessoa["Nome"]}) | ")
                        novo_peso = input ("Digite o novo peso em kg: ")
                        nova_altura = input ("Digite a nova altura em cm: ")

                        if novo_nome:
                            pessoa["Nome"] = novo_nome
                        
                        if novo_peso:
                            novo_peso = float(novo_peso.replace (",","."))
                        
                        else:
                            novo_peso = pessoa["imc"]*0
                        
                        if nova_altura:
                            nova_altura = float(nova_altura.replace (",","."))
                        
                        else:
                            print ("Altura obrigatória para calcular IMC")
                            continue

                        imc_novo, classif_nova = definir_imc(novo_peso, nova_altura)

                        pessoa["imc"] = imc_novo 
                        pessoa["classificação"] = classif_nova

                        print ("Atualizado com sucesso")
                    
                    else:
                        print("Número inválido")
                
                else:
                    print ("Entrada inválida")
    
    elif opção == "5":
        break


