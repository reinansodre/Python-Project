#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples, O sistema vai ter duas opções: cadastrar uma nova pessoa
# e listar todas as pessoas cadastradas.

def cabecario():
    print()
    print("*"*40)
    print(f"{'     \033[1;34mCadastro de Colaboradores\033[m    ':*^50}")
    print("*" * 40)
    print("""\n[1] - Cadastra novo colaborador
[2] - Lista de Colaboradores
[3] - Remover colaborador
[4] - Sair do programa""")

def cadastro():
    while True:
        try:
            nome = str(input("\nDigite o nome: "))
            idade = int(input("Digite a idade: "))
        except:
            print("\033[1;31mDigite informações válidas!\033[m \n")
        else:
            colaborador = {nome:idade}
            return colaborador

if __name__ == "__main__":
    colab = list()
    while True:
        cabecario()
        try:
            resp = int(input("Selecione a opção desejada : "))
        except:
            print("\033[1;31mOpção inválida, tente novamente!\033[m")
            continue
        if resp == 4:
            print(f"{'\033[1;34mObrigado! Até a próxima...':^40}")
            break
        elif resp == 3:
            if len(colab) == 0:
                print("\033[1;34mA lista de colaboradores cadastrados está vazia!\033[m")
            else:
                while True:
                    try:
                        resp = int(input("Digite o ID do colaborador : "))
                        if resp > len(colab) or resp <= 0:
                            print("\033[1;31mOpção inválida, tente novamente!\033[m")
                            continue
                    except:
                        print("\033[1;31mOpção inválida, tente novamente!\033[m")
                        continue
                    colab.pop(resp-1)
                    print("\033[1;34mColaborador removido com sucesso!\033[m")
                    break
        elif resp == 2:
            print(f"\n{'ID':^4}{'Nome':31}Idade")
            print("="*40)
            for id, x in enumerate(colab):
                for name, idade in x.items():
                    print(f"{id+1:^4}{name:<31}{idade:>5}")
        elif resp == 1:
            colab.append(cadastro())
            print("\033[1;34mColaborador registrado com sucesso!\033[m")
        else:
            print("\033[1;31mOpção inválida, tente novamente!\033[m")


