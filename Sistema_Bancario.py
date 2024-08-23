from abc import ABC, abstractmethod

# Classe Transacao (Interface)
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Deposito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

# Classe Saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

# Classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Classe Conta
class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            saque = Saque(valor)
            self.historico.adicionar_transacao(saque)
            saque.registrar(self)
            return True
        else:
            return False

    def depositar(self, valor):
        self.saldo += valor
        deposito = Deposito(valor)
        self.historico.adicionar_transacao(deposito)
        deposito.registrar(self)
        return True

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe ContaCorrente (herdando de Conta)
class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite, limite_saques):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

# Funções do menu
def criar_cliente():
    endereco = input("Digite o endereço do cliente: ")
    cliente = Cliente(endereco)
    return cliente

def criar_conta(cliente):
    numero = int(input("Digite o número da conta: "))
    agencia = input("Digite a agência da conta: ")
    conta = Conta(numero, agencia, cliente)
    cliente.adicionar_conta(conta)
    return conta

def depositar(conta):
    valor = float(input("Digite o valor para depósito: "))
    conta.depositar(valor)
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def sacar(conta):
    valor = float(input("Digite o valor para saque: "))
    if conta.sacar(valor):
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente para realizar o saque.")

def mostrar_historico(conta):
    print("Histórico de transações:")
    for transacao in conta.historico.transacoes:
        print(f"{type(transacao).__name__}: R$ {transacao.valor:.2f}")

# Main
def main():
    clientes = []
    while True:
        print("\n----- Menu -----")
        print("1. Criar Cliente")
        print("2. Criar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Mostrar Histórico")
        print("6. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cliente = criar_cliente()
            clientes.append(cliente)
            print("Cliente criado com sucesso.")
        elif opcao == 2:
            if clientes:
                print("Selecione um cliente:")
                for i, cliente in enumerate(clientes):
                    print(f"{i+1}. Cliente com endereço {cliente.endereco}")
                escolha_cliente = int(input("Escolha o número do cliente: ")) - 1
                criar_conta(clientes[escolha_cliente])
                print("Conta criada com sucesso.")
            else:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
        elif opcao == 3:
            if clientes:
                print("Selecione um cliente:")
                for i, cliente in enumerate(clientes):
                    print(f"{i+1}. Cliente com endereço {cliente.endereco}")
                escolha_cliente = int(input("Escolha o número do cliente: ")) - 1
                conta = clientes[escolha_cliente].contas[0]  # Supondo uma conta por cliente para simplicidade
                depositar(conta)
            else:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
        elif opcao == 4:
            if clientes:
                print("Selecione um cliente:")
                for i, cliente in enumerate(clientes):
                    print(f"{i+1}. Cliente com endereço {cliente.endereco}")
                escolha_cliente = int(input("Escolha o número do cliente: ")) - 1
                conta = clientes[escolha_cliente].contas[0]
                sacar(conta)
            else:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
        elif opcao == 5:
            if clientes:
                print("Selecione um cliente:")
                for i, cliente in enumerate(clientes):
                    print(f"{i+1}. Cliente com endereço {cliente.endereco}")
                escolha_cliente = int(input("Escolha o número do cliente: ")) - 1
                conta = clientes[escolha_cliente].contas[0]
                mostrar_historico(conta)
            else:
                print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
