# Desafio-Projeto-Sistema-Banc-rio
Desafio de Projeto: Criando um Sistema Bancário
# Sistema Bancário Simples em Python

Este é um projeto de sistema bancário simples em Python que permite realizar operações de depósito, saque e visualização de extrato. O projeto foi criado como parte de um desafio de código.

## Funcionalidades

- **Depósito:** É possível depositar valores positivos na conta bancária. Todos os depósitos são armazenados e exibidos no extrato.

- **Saque:** O sistema permite até 3 saques diários, com um limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema exibe uma mensagem informando que não é possível sacar devido à falta de saldo. Todos os saques são registrados e exibidos no extrato.

- **Extrato:** A operação de extrato lista todas as movimentações, incluindo depósitos e saques, juntamente com a data e hora em que foram realizados. No final do extrato, o saldo atual da conta é exibido. Se não houver movimentações, o sistema exibirá a mensagem "Não foram realizadas movimentações."

## Uso

Para usar o sistema, você pode criar uma instância da classe `SistemaBancario` e chamar os métodos `depositar`, `sacar` e `extrato`. Aqui está um exemplo:

```python
import SistemaBancario

banco = SistemaBancario.SistemaBancario()
banco.depositar(1000.50)
banco.sacar(300)
banco.depositar(700)
banco.sacar(800)
banco.extrato()
