import sqlite3

conexao = sqlite3.connect("rh.db") #conexão com o banco de dados chamado rh.db // sqlite3 é o módulo que sabecon versar com sqlite //conexão= guarda a conexão nessa variável
# O comando CREATE TABLE IF NOT EXISTS funcionarios SIGNIFICA "SQLite, crie uma tabela chamada funcionarios, mas somente se ela ainda não existir." E 
# id       → número único de cada funcionário
#nome     → texto
#cargo    → texto
#salario  → número decimal

cursor = conexao.cursor()  #cursor é o objeto que usamos para mandar comandos sqlpara esse banco

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL
)
""") #a  chave primaria é criada automaticamente

conexao.commit() #"Salve definitivamente essa alteração no banco."

funcionarios = []


def cadastrar_funcionario():
    print("\nCADASTRAR FUNCIONÁRIO")

    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))

    cursor.execute("""
        INSERT INTO funcionarios(nome, cargo, salario)
        VALUES (?,?,?)
        """,(nome, cargo,salario))

    conexao.commit()

    print("Funcionário cadastrado com sucesso!")


def listar_funcionario():
    print("\nLISTA DE FUNCIONÁRIOS")

    cursor.execute("SELECT * FROM funcionarios")

    funcionarios = cursor.fetchall()#fetch significa buscar/obter e all significa todos. (Pegue todos os resultados que o SELECT encontrou)

    for funcionario in funcionarios:
        print(f"ID: {funcionario[0]}")
        print(f"Nome: {funcionario[1]}")
        print(f"Cargo: {funcionario[2]}")
        print(f"Salário: R$ {funcionario[3]:.2f}")
        print("_________________________________")


def buscar_funcionario():
    print("\nBUSCAR FUNCIONÁRIO")

    busca = input("Digite o nome do funcionário: ")

    cursor.execute("""SELECT * FROM funcionarios
    WHERE nome LIKE ?
    """, (f"%{busca}%",))

    funcionarios_encontrados = cursor.fetchall()

    if len(funcionarios_encontrados) > 0:
        for funcionario in funcionarios_encontrados:
            print(f"ID: {funcionario[0]}")
            print(f"Nome: {funcionario[1]}")
            print(f"Cargo: {funcionario[2]}")
            print(f"Salário: R$ {funcionario[3]:.2f}")
            print("_________________________________")
    else:
        print("Funcionário não encontrado.")

def estatistica():
    print("\nESTATÍSTICA")

    cursor.execute("SELECT COUNT(*) FROM funcionarios")
    resultado = cursor.fetchone()
    quantidade = resultado[0]

    cursor.execute("SELECT SUM(salario) FROM funcionarios")
    resultado_salarios = cursor.fetchone()
    total_salarios = resultado_salarios[0]

    cursor.execute("SELECT AVG(salario) FROM funcionarios")
    resultado_media = cursor.fetchone()
    media_salarios = resultado_media[0]

    cursor.execute("SELECT MAX(salario) FROM funcionarios")
    resultado_maior = cursor.fetchone()
    maior_salario = resultado_maior[0]

    cursor.execute("SELECT MIN(salario) FROM funcionarios")
    resultado_menor = cursor.fetchone()
    menor_salario = resultado_menor[0]

    print(f"Funcionários cadastrados: {quantidade}")
    print(f"Total dos salários: R${total_salarios:.2f}")
    print(F"Média salarial: R$ {media_salarios: .2f}")
    print(f"Maior salário: R$ {maior_salario: .2f}")
    print(f"Menor salário: R$ {menor_salario: .2f}")

def editar_funcionario():
    print("\nEDITAR FUNCIONÁRIO")

    busca = input("Digite o nome do funcionário.")

    cursor.execute("""
    SELECT * FROM funcionarios
    WHERE nome LIKE ?
    """, (f"%{busca}%",))

    funcionario = cursor.fetchone()

    print(funcionario)



while True:
    print("\n====================SISTEMA DE RH============================")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("4 - Estatísticas")
    print("5 - Excluir funcionário")
    print("6 - Editar funcionário")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            cadastrar_funcionario()

        case "2":
            listar_funcionario()

        case "3":
            buscar_funcionario()

        case "4":
            estatistica()

        case "5":
            excluir_funcionario()

        case "6":
            editar_funcionario()

        case "0":
            print("Saindo...")
            break