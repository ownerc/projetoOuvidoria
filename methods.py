from operacoesbd import *

connection = criarConexao('localhost', 'root', '53421', 'sistema_ouvidoria')

def listaManifestacoes(connection):
    consultaLista = 'select * from Ouvidoria'
    manifestacoes = listarBancoDados(connection, consultaLista)
    if len(manifestacoes) > 0:
        for item in manifestacoes:
            print(f"Manifestação {item[0]}:\n{item[1]}")
    else:
        print("Nenhuma manifestação registrada até o momento.")

def listaManifestacoesTipo(connection):
    tipoManifestacao = input("Descreva o tipo de manifestação (reclamação, elogio, sugestão): ").lower()
    consultaTipo = 'select * from Ouvidoria where tipo = (%s)'
    dadosManifestacao = [tipoManifestacao]
    manifestacoes = listarBancoDados(connection, consultaTipo, dadosManifestacao)
    if len(manifestacoes) > 0:
        for item in manifestacoes:
            print(f"Manifestação {item[0]}: {item[1]} ({item[2]})")
    else:
        print(f"Não há manifestações do tipo {tipoManifestacao}.")

def registrarManifestacao(connection):
    tipoManifestacao = input("Qual o tipo de manifestação? (reclamação, elogio, sugestão): ").lower()
    novaManifestacao = input("Descreva sua manifestação: ")
    inserirManifestacaoBD = 'insert into Ouvidoria (manifestacao, tipo) values (%s, %s)'
    dadosManifestacao = [novaManifestacao, tipoManifestacao]
    insertNoBancoDados(connection, inserirManifestacaoBD, dadosManifestacao)
    print("A manifestação foi registrada com sucesso.")
