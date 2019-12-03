from Pessoa import Pessoa, PessoaJuridica, Cliente

def lista_produtos():
    lista = ['1','2','3','4','5','6','7','Maria','Joao']
    print ("Escolha os produtos: ", lista)
    produtos = input("Quais produtos o cliente deseja? ")
    return produtos

if __name__== '__main__':
    cliente = input("O cliente PF (0) ou PJ(1)? ")
    ide = input("Digite seu ID: ")
    nome = input("Digite seu nome: ")
    cpf = ''
    cnpj = ''
    if cliente == "0":
        cpf = input("Digite seu CPF: ")
    else:
        cnpj = input("Digite o CNPJ: ")
    email = input("Digite o email: ")
    produtos = lista_produtos()
    print("Produtos comprados", produtos.split(","))

    obj = Cliente(ide, nome, cpf, cnpj, email, produtos)
    print(obj.exibe_cliente())


