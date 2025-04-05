from operacoesbd import *

connection = criarConexao('localhost', 'root', '53421', 'sistema_ouvidoria')

opcao = 1

def listaManifestacoes(connection):
    consultaLista = 'select * from Ouvidoria'
    manifestacoes = listarBancoDados(connection, consultaLista)
    if len(manifestacoes) > 0:
        for item in manifestacoes:
            print(f"Manifestação {item[0]}:\n{item[1]}")
    else:
        print("Nenhuma manifestação foi registrada até o momento.")

def registrarManifestacao(connection):
    novaManifestacao = input("Descreva sua manifestação: ")
    inserirManifestacao = 'insert into Ouvidoria (manifestacao) values (%s)'
    dadosManifestacao = [novaManifestacao]
    insertNoBancoDados(connection, inserirManifestacao, dadosManifestacao)
    print("Sua manifestação foi registrada.")

def totalManifestacoes(connection):
    quantidadeManifestacoes = 'select count(*) from Ouvidoria'
    quantidadeTotal = listarBancoDados(connection, quantidadeManifestacoes)
    print(f"O total de manifestções registradas é: {quantidadeTotal[0][0]}.")
























encerrarConexao(connection)