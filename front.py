from methods import *
from operacoesbd import *

connection = criarConexao('localhost', 'root', '53421', 'sistema_ouvidoria')

while True:
    print("Bem vindo ao Sistema de Ouvidoria!")
    input("Aperte 'Enter' para continuar\n")
    break

while True:
    print("\n1) Lista de todas as manifestações\n2) Lista de manifestações por tipo\n3) Registrar uma manifestação\n4) Exibir total de manifestações registradas\n5) Pesquisar uma manifestação por código\n6) Remover uma manifestação\n7) Sair do Sistema.\n")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        listaManifestacoes(connection)

    elif opcao == 2:
        listaManifestacoesTipo(connection)

    elif opcao == 3:
        registrarManifestacao(connection)

    elif opcao == 4:
        totalManifestacoes(connection)

    elif opcao == 5:
        pesquisarManifestacaoCodigo(connection)

    elif opcao == 6:
        removerManifestacao(connection)

    elif opcao == 7:
        break
    else:
        print("Opção inválida, tente novamente.")

encerrarConexao(connection)
print("Obrigado por usar o Sistema de Ouvidoria!")