historico = [ ]

while True:
        opção = input(
            "1 - Lançar livro\n"
            "2 - Ver histórico\n"
            "3 - Remover algum livro\n"
            "4 - Editar histórico\n"
            "5 - Sair \n"
        )

        if opção == "1":
            livro = input("Digite o nome do seu livro: ")
            editora = input("Digite a editora: ")
            ano_lançamento = input("Digite o ano de lançamento: ")
            historico.append({
                "livro": livro,
                "editora": editora,
                "ano": ano_lançamento
            }
            )
        
        elif opção == "2":
            if not historico:
                    print ("Histórico vazio")
            else:
                for book in historico:
                    print(
                        f"livro: :{book['livro']} | "
                        f"editora: {book['editora']} | "
                        f"ano: {book['ano']}"
                    )
        
        elif opção == "3":
            if not historico:
                print("Historico vazio")
            else:
                nome_remover = input("Digite o nome que deseja remover: ").strip().lower()
                encontrados = [ ]
                
                for i, book in enumerate(historico):
                    if nome_remover.lower() in book["livro"].strip().lower():
                            encontrados.append ((i,book))

                if not encontrados:
                    print ("Livro não encontrado!")
                else: 
                    print("\n Livros encontrados")

                    for indice, book in encontrados:
                            print( 
                                f"{indice} - "
                                f"livro: :{book['livro']} | "
                                f"editora: {book['editora']} | "
                                f"ano: {book['ano']}"
                            )
                        
                    escolha = input ("Digite o número do livro que deseja remover: ")

                    if escolha.isdigit():
                            escolha = int(escolha)
                            indices_validos = [i for i, _ in encontrados]

                            if escolha in indices_validos:
                                confirmação = input ("Tem certeza? (s/n)")

                                if confirmação.lower() == "s":
                                    removido = historico.pop(escolha)
                                    print ("Removido com sucesso")
                            else:
                                print("Número inválido")
                        
                    else:
                            print("Entrda inválida")


                
        elif opção == "5":
            break
