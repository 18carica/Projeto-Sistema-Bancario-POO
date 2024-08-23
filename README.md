# Sistema Bancário em Python

## Descrição

Este projeto é a implementação de um sistema bancário simples desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos (POO). O sistema permite a criação e gerenciamento de clientes, contas bancárias, e a realização de operações como depósitos e saques. Além disso, o sistema registra todas as transações em um histórico para cada conta.

O projeto foi desenvolvido seguindo um diagrama UML específico, garantindo uma estrutura clara e organizada para representar as operações bancárias essenciais.

## Funcionalidades

- **Criar Cliente:** Registra um novo cliente com endereço.
- **Criar Conta:** Cria uma nova conta bancária associada a um cliente existente.
- **Realizar Depósito:** Permite depositar um valor em uma conta bancária.
- **Realizar Saque:** Permite sacar um valor de uma conta bancária, caso haja saldo suficiente.
- **Mostrar Histórico:** Exibe o histórico de todas as transações realizadas em uma conta específica.

## Estrutura do Projeto

- **Cliente:** Classe que representa um cliente do banco, contendo informações como endereço e contas associadas.
- **Conta:** Classe que representa uma conta bancária, contendo saldo, número da conta, agência, cliente associado e histórico de transações.
- **ContaCorrente:** Subclasse de Conta, adicionando atributos como limite e limite de saques.
- **Historico:** Classe que armazena o histórico de transações para cada conta.
- **Transacao:** Interface para definir transações bancárias, como depósitos e saques.
- **Deposito e Saque:** Classes que implementam a interface Transacao para representar operações específicas.

## Como Usar

1. **Requisitos:** Certifique-se de ter o Python instalado em seu sistema.
2. **Clone ou Baixe o Projeto:** Faça o download ou clone o repositório para o seu ambiente local.
3. **Executar o Sistema:** Execute o arquivo `Sistema_Bancario.py` através do terminal ou de um ambiente de desenvolvimento (IDE).
   - Navegue pelo menu apresentado para criar clientes, criar contas, realizar depósitos, saques e visualizar o histórico de transações.
4. **Sair do Sistema:** Selecione a opção de sair no menu para encerrar o programa.

## Exemplo de Execução

Ao iniciar o sistema, você verá o menu com as seguintes opções:

----- Menu -----

Criar Cliente
Criar Conta
Depositar
Sacar
Mostrar Histórico
Sair
Escolha uma opção:

Siga as instruções apresentadas para realizar as operações desejadas. O sistema guiará você através das opções disponíveis e exibirá o resultado de cada operação.

## Conclusão

Este sistema bancário foi desenvolvido com o objetivo de aplicar conceitos de POO em Python, criando uma estrutura clara e fácil de manter para operações bancárias básicas. Sinta-se à vontade para modificar e expandir o código conforme necessário.
