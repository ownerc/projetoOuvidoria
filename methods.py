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
    tipoManifestacao = input("Informe se a manifestação é uma reclamação, elogio ou sugestão: ")
    consultaTipo = 'select * from Ouvidoria where tipo = (%s)'
    dadosManifestacao = [tipoManifestacao]
    manifestacoes = listarBancoDados(connection, consultaTipo, dadosManifestacao)
    if len(manifestacoes) > 0:
        for item in manifestacoes:
            print(f"Manifestação {item[0]}: {item[1]} ({item[2]})")
    else:
        print(f"Não há manifestações do tipo {tipoManifestacao}.")

def registrarManifestacao(connection):
    tipoManifestacao = input("Informe se a manifestação é uma reclamação, elogio ou sugestão: ")
    novaManifestacao = input("Descreva sua manifestação: ")
    inserirManifestacaoBD = 'insert into Ouvidoria (manifestacao, tipo) values (%s, %s)'
    dadosManifestacao = [novaManifestacao, tipoManifestacao]
    insertNoBancoDados(connection, inserirManifestacaoBD, dadosManifestacao)
    print("A manifestação foi registrada com sucesso.")

def totalManifestacoes(connection):
    quantidadeManifestacoes = 'select count(*) from Ouvidoria'
    quantidadeTotal = listarBancoDados(connection, quantidadeManifestacoes)
    print(f"O total de manifestações registradas é: {quantidadeTotal[0][0]}.")

def pesquisarManifestacaoCodigo(connection):
    codigoManifestacao = int(input("Insira o código da manifestação: "))
    consultaLista = 'select * from Ouvidoria where codigo = (%s)'
    dadosManifestacao = [codigoManifestacao]
    manifestacoes = listarBancoDados(connection, consultaLista, dadosManifestacao)
    if len(manifestacoes) > 0:
        print(f"Manifestação {codigoManifestacao}: {manifestacoes[0][1]}")
    else:
        print(f"Não encontramos uma manifestação com o código {codigoManifestacao}.")

def removerManifestacao(connection):
    codigoManifestacao = int(input("Insira o código da manifestação: "))
    manifestacaoDelete = 'delete from Ouvidoria where codigo = (%s)'
    dadosManifestacao = [codigoManifestacao]
    linhasAfetadas = excluirBancoDados(connection, manifestacaoDelete, dadosManifestacao)
    if linhasAfetadas > 0:
        print(f"A manifestação {codigoManifestacao} foi removida.")
    else:
        print("Não há manifestações a serem removidas.")

encerrarConexao(connection)