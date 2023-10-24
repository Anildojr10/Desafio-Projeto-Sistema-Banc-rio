import datetime

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.historico = Historico()
        self.cliente = cliente

    def saldo(self):
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            return True
        else:
            print("Saldo insuficiente para o saque.")
            return False

    def depositar(self, valor):
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite, limite_saques):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

class Transacao:
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def criar_conta(self, numero, agencia="0001"):
        conta = Conta(self, numero, agencia)
        self.contas.append(conta)
        return conta

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Lista de clientes para evitar a criação de clientes duplicados com o mesmo CPF
clientes = []

# Menu atualizado
while True:
    print("Menu:")
    print("1. Criar Cliente")
    print("2. Criar Conta")
    print("3. Realizar Depósito")
    print("4. Realizar Saque")
    print("5. Consultar Saldo")
    print("6. Consultar Clientes")
    print("7. Consultar Histórico de Transações")
    print("8. Sair")

    escolha = int(input("Escolha a opção desejada: "))

    if escolha == 1:
        endereco = input("Digite o endereço do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        if any(cliente.cpf == cpf for cliente in clientes):
            print("CPF já cadastrado. Não é possível criar outro cliente com o mesmo CPF.")
        else:
            nome = input("Digite o nome do cliente: ")
            data_nascimento = input("Digite a data de nascimento do cliente (no formato YYYY-MM-DD): ")
            data_nascimento = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
            cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
            clientes.append(cliente)
            print(f"Cliente {cliente.nome} cadastrado com sucesso!")

    elif escolha == 2:
        if not clientes:
            print("Não há clientes cadastrados. Crie um cliente primeiro.")
        else:
            cpf = input("Digite o CPF do cliente para criar uma conta: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                numero_conta = len(cliente.contas) + 1
                conta = cliente.criar_conta(numero_conta)
                print(f"Conta criada com sucesso para o cliente {cliente.nome}. Número da conta: {conta.numero}")
            else:
                print("CPF não encontrado.")

    elif escolha == 3:
        if not clientes:
            print("Não há clientes cadastrados. Crie um cliente primeiro.")
        else:
            cpf = input("Digite o CPF do cliente para realizar um depósito: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                if cliente.contas:
                    escolha_conta = int(input("Escolha a conta para fazer o depósito (pelo número da conta): "))
                    conta = next((c for c in cliente.contas if c.numero == escolha_conta), None)
                    if conta:
                        valor = float(input("Digite o valor a ser depositado: "))
                        cliente.realizar_transacao(conta, Deposito(valor))
                        print(f"Depósito realizado com sucesso na conta {conta.numero}.")
                    else:
                        print("Conta não encontrada.")
                else:
                    print("O cliente não tem contas.")
            else:
                print("CPF não encontrado.")

    elif escolha == 4:
        if not clientes:
            print("Não há clientes cadastrados. Crie um cliente primeiro.")
        else:
            cpf = input("Digite o CPF do cliente para realizar um saque: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                if cliente.contas:
                    escolha_conta = int(input("Escolha a conta para fazer o saque (pelo número da conta): "))
                    conta = next((c for c in cliente.contas if c.numero == escolha_conta), None)
                    if conta:
                        valor = float(input("Digite o valor a ser sacado: "))
                        if cliente.realizar_transacao(conta, Saque(valor)):
                            print(f"Saque de R${valor:.2f} realizado com sucesso na conta {conta.numero}.")
                        else:
                            print("Saldo insuficiente para o saque.")
                    else:
                        print("Conta não encontrada.")
                else:
                    print("O cliente não tem contas.")
            else:
                print("CPF não encontrado.")

    elif escolha == 5:
        if not clientes:
            print("Não há clientes cadastrados. Crie um cliente primeiro.")
        else:
            cpf = input("Digite o CPF do cliente para consultar o saldo: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                if cliente.contas:
                    escolha_conta = int(input("Escolha a conta para consultar o saldo (pelo número da conta): "))
                    conta = next((c for c in cliente.contas if c.numero == escolha_conta), None)
                    if conta:
                        saldo = conta.saldo()
                        print(f"Saldo da conta {conta.numero}: R${saldo:.2f}")
                    else:
                        print("Conta não encontrada.")
                else:
                    print("O cliente não tem contas.")
            else:
                print("CPF não encontrado.")

    elif escolha == 6:
        if not clientes:
            print("Não há clientes cadastrados.")
        else:
            print("Clientes cadastrados:")
            for cliente in clientes:
                print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}")

    elif escolha == 7:
        if not clientes:
            print("Não há clientes cadastrados.")
        else:
            cpf = input("Digite o CPF do cliente para consultar o histórico de transações: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                if cliente.contas:
                    escolha_conta = int(input("Escolha a conta para consultar o histórico de transações (pelo número da conta): "))
                    conta = next((c for c in cliente.contas if c.numero == escolha_conta), None)
                    if conta:
                        print(f"Histórico de transações da conta {conta.numero}:")
                        for transacao in conta.historico.transacoes:
                            if isinstance(transacao, Deposito):
                                print(f"Depósito de R${transacao.valor:.2f}")
                            elif isinstance(transacao, Saque):
                                print(f"Saque de R${transacao.valor:.2f}")
                    else:
                        print("Conta não encontrada.")
                else:
                    print("O cliente não tem contas.")
            else:
                print("CPF não encontrado.")

    elif escolha == 8:
        print("Saindo do sistema. Até a próxima!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
