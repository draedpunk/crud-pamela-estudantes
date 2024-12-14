import os
import json

# Definindo o caminho do arquivo no escopo global
arquivo = os.path.join(os.path.dirname(__file__), "estudantes.json")

def carregar_estudantes():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as f:
            json.dump([], f, indent=4)
    
    # Carrega o conteúdo do arquivo
    with open(arquivo, "r") as f:
        return json.load(f)

def exibir_titulo():
    print("\033[1;35m✩░▒▓▆▅▃▂▁MÓDULO DO ESTUDANTE▁▂▃▅▆▓▒░✩\033[m\n")

def exibir_subtitulo(texto):
    os.system("cls")
    linha = f'{"*" * 80: ^75}'
    print(linha)
    print(texto)
    print(linha)
    print("")

def cadastrar_estudante(nome, curso, periodo, turno):
    estudantes = carregar_estudantes()

    estudantes.append({"nome": nome, "curso": curso, "periodo": periodo, "turno": turno})

    with open(arquivo, "w") as f:
        json.dump(estudantes, f, indent=4, ensure_ascii=False)
    print("\n \033[1;32m✅ ESTUDANTE ADICIONADO COM SUCESSO!\033[m")
    voltar_menu()
  

def atualizar_estudante(nome_antigo, novo_nome, novo_curso, novo_periodo, novo_turno):
    estudantes = carregar_estudantes()

    for estudante in estudantes: 
        if estudante["nome"] == nome_antigo:
            estudante["nome"] = novo_nome
            estudante["curso"] = novo_curso
            estudante["periodo"] = novo_periodo
            estudante["turno"] = novo_turno
            break

    with open(arquivo, "w") as f:
        json.dump(estudantes, f, indent=4, ensure_ascii=False)
    print("\n\033[1;32m✅ ESTUDANTE ATUALIZADO COM SUCESSO!\033[m")
    voltar_menu()

def exibir_estudantes(): # terminal feiosinho
    estudantes = carregar_estudantes()

    if estudantes:
        for estudante in estudantes:
            print("NOME: " + estudante["nome"].center(14) + 
                  " | CURSO: " + estudante["curso"].center(14) + 
                  " | PERIODO: " + str(estudante["periodo"]).center(14) + 
                  " | TURNO: " + estudante["turno"].center(14))
    else:
        print("\n\033[1;31m❌ NENHUM ESTUDANTE CADASTRADO!\033[m")
    voltar_menu()

def excluir_estudante(nome): #excluir estudante pelo NOME
    estudantes = carregar_estudantes()
    encontrado = False

    for estudante in estudantes:
        if estudante["nome"] == nome:
            estudantes.remove(estudante)
            encontrado = True
            print("\n\033[1;32m✅ ESTUDANTE EXCLUÍDO COM SUCESSO!\033[m")

    if not encontrado:
        print("\n\033[1;31m❌ ESTUDANTE NÃO ENCONTRADO.\033[m")

    with open(arquivo, "w") as f:
        json.dump(estudantes, f, indent=4, ensure_ascii=False)
    voltar_menu()

def buscar_estudante(nome): 
    estudantes = carregar_estudantes()  
    encontrado = False

    for estudante in estudantes:
        if estudante["nome"] == nome:
            print("\nSegue dados do(a) estudante:")
            print("NOME: " + estudante["nome"].center(14) + 
                  " | CURSO: " + estudante["curso"].center(14) + 
                  " | PERIODO: " + str(estudante["periodo"]).center(14) + 
                  " | TURNO: " + estudante["turno"].center(14))
            encontrado = True
            break  # sai do loop assim que encontrar o estudante
    if not encontrado:
        print("\n\033[1;31m❌ ESTUDANTE NÃO ENCONTRADO.\033[m")
    voltar_menu()

def exibir_menu_estudantes():
    os.system("cls") #limpar terminal
    exibir_titulo()
    print("1 - Cadastrar novo estudante")
    print("2 - Atualizar estudante")
    print("3 - Exibir estudantes cadastrados")
    print("4 - Excluir estudante")
    print("5 - Buscar estudante")
    print("6 - Encerrar")

def escolher_opcao():
    while True:
        try:
            op = int(input("\n\033[0;34m➤  Escolha uma opcao:\033[m "))

            if (op == 1):
                exibir_subtitulo(f'\033[1;35m{"Novo Cadastro":^75}\033[m')
                nome = input("▸ Informe o NOME do estudante: ")
                curso = input("▸ Informe o CURSO do estudante: ")
                periodo = int(input("▸ Informe o PERÍODO em que o estudante está: "))
                turno = input("▸ Informe o TURNO do curso (matutino/vespertino/noturno): ")
                cadastrar_estudante(nome, curso, periodo, turno)
                break

            elif (op == 2):
                exibir_subtitulo(f'\033[1;35m{"Atualizar Estudante":^75}\033[m')
                nome_antigo = input("▸ Informe o ESTUDANTE (nome) a ser atualizado: \n")
                novo_nome = input("▸ Informe o novo NOME: ")
                novo_curso = input("▸ Informe o novo CURSO: ")
                novo_periodo = int(input("▸ Informe o novo PERÍODO: "))
                novo_turno = input("▸ Informe o novo TURNO (matutino/vespertino/noturno): ")
                atualizar_estudante(nome_antigo, novo_nome, novo_curso, novo_periodo, novo_turno)
                break

            elif (op == 3):
                exibir_subtitulo(f'\033[1;35m{"Estudantes Cadastrados":^75}\033[m')
                exibir_estudantes()
                break

            elif (op == 4):
                exibir_subtitulo(f'\033[1;35m{"Excluir Estudante":^75}\033[m')
                nome = input("▸ Informe o nome do estudante que você deseja excluir: ")
                excluir_estudante(nome)
                break

            elif (op == 5):
                exibir_subtitulo(f'\033[1;35m{"Buscar Estudante":^75}\033[m')
                nome = input("▸ Informe o nome do estudante que você deseja buscar: ")
                buscar_estudante(nome)
                break

            elif (op == 6):
                print("\n\033[1;36mEncerrando o programa...\033[m")
                return False

            else:
                print("\n\033[1;33m⚠️  OPÇÃO INVÁLIDA!\033[m")
                
        except ValueError:
            print("\n\033[1;33m⚠️  OPÇÃO INVÁLIDA!\033[m")
    return True

def voltar_menu():
    input("\n\033[0;34m➤  Digite qualquer tecla para voltar ao menu anterior:\033[m ")
    main()

def main():
    while True:
        os.system("cls")
        exibir_menu_estudantes()
        if not escolher_opcao():
            break

if __name__ == "__main__":
    main()
