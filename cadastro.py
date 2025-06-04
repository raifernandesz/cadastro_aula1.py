


def menu():
   cadastro = []
   while True:
      print("\n--------Cadastro de funcionarios------------")
      print("[1] Cadastrar Pessoa")
      print("[2] Listar Pessoas ")
      print("[3] Excluir Pessoa")
      print("[0]")
      opcao = input ("Escolha uma opção: ")

      if opcao == '1':
         novo_nome = input("Digite o nome da Pessoa")
         cadastro.append(novo_nome)
         print(f"Usuário {novo_nome} foi adicionado com sucesso")
    
      elif opcao == '2':
         print("\nLista de nomes Cadastrados: ")
         for i, nome in enumerate(cadastro, start=1):
             print(f"{i} .{nome}")
      elif opcao == '3':
         excluir_nome = input("Digite o nome para excluir: ")
         if excluir_nome in cadastro:
             print(f"{excluir_nome} foi removido. ")
         else:    
          print("Saindo...")
         break
      else:
            print("!!! Opção inválida . Tente novamente. !!! ")
menu()
