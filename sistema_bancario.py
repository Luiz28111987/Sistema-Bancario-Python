# Variaveis do menu
titulo = " MENU "
linha = "=" * 36
mensagem_menu = """Escolha uma opção. 
Obrigado por usar nosso sistema!!!!"""

# Desenvolvendo o Menu
menu = f"""
    {titulo.center(36, "=")}

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    {linha}

    {mensagem_menu}
"""

# Variaveis utilizadas
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Sistema bancario

while True:

    opcao = input(menu)

    if opcao == "d":

        while True:
            deposito = float(input("Digite o valor do deposito: "))
            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
                print(f"Deposito de {deposito:.2f} Reais realizado com sucesso!")
                break
            else:
                print("Digite um valor positivo.")        

    elif opcao == "s":

        while True:

            valor = float(input("Digite o valor do saque: "))
            if valor > 0:
                if saldo >= valor and numero_saques < LIMITE_SAQUES and valor <= limite:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    print(f"Saque no valor de {valor:.2f} Reais realizado com sucesso!")
                    numero_saques += 1
                    break
                elif saldo < valor:
                    print("Saldo indisponivel.")
                    break

                elif numero_saques >= LIMITE_SAQUES:
                    print("Quantidade de saques excedida")
                    break

                else:
                    print("Valor maior que o limite de saque permitido.")

            else:
                print("Digite um valor positivo.")

    elif opcao == "e":
        if not extrato:
            extrato_msg = "Não foram realizadas movimentações."
        else:
            extrato_msg = extrato

        # Desenvolvendo o extrato
        imprimir_extrato = f"""
{linha}
Extrato Bancario
{linha}

Limites de saque: R$ {limite}
Saques permitidos: {LIMITE_SAQUES}
Saques utilizados: {numero_saques}    

detalhes da Conta
{linha}

{extrato_msg}
Saldo: R$ {saldo:.2f}

{linha}
"""
        print(imprimir_extrato)

    elif opcao == "q":
        print("Obrigado por usar nosso sistema!!!!")
        break

    else:
        print("Operação invalida, por favor selecionar novamente a operação desejada.")