from conta import Conta
from validators import Validator



def main(): 
    # cpf = "577.954.920-61"
    cpf = "111.222.333-11"
    resultado = Validator.validarCpf(cpf)

    if resultado == False:
        print(f"O CPF informado é inválido!")
    else:
        conta1 = Conta("Teste", cpf, 30.00)
        if conta1.creditar(40.25) != -1:
            print(f"{conta1.get_nome()} seu saldo é {conta1.get_saldo()}")
        else:
            print("O valor passado não pode ser negativo!")

        print(Conta.get_numero_da_conta())

    cpf2 = "111.222.333-11"
    resultado2 = Validator.validarCpf(cpf2)

    if resultado2 == False:
        print(f"O CPF informado é inválido!")
    else:
        conta2 = Conta("Guilherme", "044026", 50.00)

        if conta2.creditar(-40.25) != -1:
            print(conta2.get_saldo())
        else:
            print("O valor passado não pode ser negativo!")
            print(f"{conta2.get_nome()} seu saldo é {conta2.get_saldo()}")

        print(Conta.get_numero_da_conta)

main()
