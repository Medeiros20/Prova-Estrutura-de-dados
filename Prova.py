import os 
lista_nomes = []
pessoas_atendidas = []
while True:
    os.system('cls')  # Limpa a tela do console
    print("Menu")
    print("1 - Inserir na fila")
    print("2 - Marcar como atendido")
    print("3 - Exibir a fila de espera")
    print("4 - Exibir lista dos atendidos")
    print("5 - Sair")
     
    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
                os.system('cls')
                print("Entrada inválida. Por favor, digite um número.")
                continue
    
    if op == 1:
        os.system('cls') 
        nome = input("Digite o nome a ser adicionado na fila: ").strip().capitalize()
        if nome:
            lista_nomes.append(nome)
            print(f"Nome '{nome}' adicionado.") 
        else:
            print("O nome não pode ser vazio. Por favor, digite um nome válido.")
            
    elif op == 2: 
        os.system('cls')
        if not lista_nomes:
            print("A lista de nomes está vazia. Não há ninguém para marcar como atendido.")
        else:
            print("Nomes na fila de espera (digite 0 para cancelar):")
            for i, nome in enumerate(lista_nomes):
                print(f"{i + 1}. {nome}") 
            try:
                escolha_str = input("Digite o número do nome que foi atendido (ou 0 para cancelar): ")
                escolha_usuario = int(escolha_str)

                if escolha_usuario == 0:
                    print("Operação cancelada.")
                elif 1 <= escolha_usuario <= len(lista_nomes): # Verifica se a escolha está no range dos itens exibidos
                    indice_real_para_remover = escolha_usuario - 1 # Converte para índice baseado em 0
                    nome_removido = lista_nomes.pop(indice_real_para_remover)
                    pessoas_atendidas.append(nome_removido) # Adiciona à lista de atendidos
                    print(f"'{nome_removido}' foi marcado como atendido e movido para a lista de atendidos.")
                else:
                    print("Número inválido. Por favor, digite um número da lista ou 0 para cancelar.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    elif op == 3:
        os.system('cls')
        if not lista_nomes:
            print("A lista de Nomes está vazia.")
        else:
            print("Nomes na fila de espera:") 
            for i, nome_item in enumerate(lista_nomes): 
                print(f"{i + 1}. {nome_item}")
    
    elif op == 4:
            os.system('cls')
            if not pessoas_atendidas: 
                print("Nenhuma pessoa foi atendida ainda.\\n")
            else:
                print("Pessoas atendidas:")
                for i, pessoa in enumerate(pessoas_atendidas): 
                    print(f"{i + 1}. {pessoa}")
            
    elif op == 5:
        print("Saindo do programa...")
        break
    else: 
        print("Opção inválida. Tente novamente.")
    # Pausa para o usuário ver a saída das opções válidas antes de limpar e mostrar o menu
    if op in [1, 2, 3, 4]: 
        input("\\nPressione Enter para continuar...")
    elif op not in [1, 2, 3, 4, 5]: # Se foi uma opção inválida e não saiu
        input("\\nPressione Enter para tentar novamente...")