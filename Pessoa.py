class Pessoa:
    def __init__(self, ide, nome, cpf, email, produtos):
        self.ide = ide
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.produtos = produtos

    def __str__(self):
        return self.nome

class PessoaJuridica(Pessoa):
    def __init__(self, ide=None, nome=None, email=None, produtos=None, cnpj=None, cpf=None):
        Pessoa.__init__(self, ide=ide, nome=nome, email=email, produtos=produtos, cpf=cpf)
        self.cnpj = cnpj

    def __str__(self):
        return self.nome

class Cliente(PessoaJuridica):
    def __init__(self, ide=None, nome=None, email=None, produtos=None, cnpj=None, cpf=None):
        PessoaJuridica.__init__(self, ide=ide, nome=nome, email=email, produtos=produtos, cnpj=cnpj)
        Pessoa.__init__(self, ide=ide, nome=nome, email=email, cpf=cpf, produtos=produtos)

        self.cpf = cpf


    def set_ide(self):
        self.ide= ide

    def set_nome(self):
        self.nome= nome

    def set_cpf(self):
        self.cpf= cpf

    def set_cnpj(self):
        self.cnpj= cnpj

    def set_email(self):
        self.email= email

    def set_produtos(self):
        self.produtos= produtos

    def exibe_cliente(self):
        return "ID: {} -> Nome: {}. Produtos desejados: {}".format(self.ide, self.nome, self.produtos)


