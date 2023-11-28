from conta import Conta

def validarCpf(cpf) -> int:
    if len(cpf) != 11:
                return False

        # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verificar se os dígitos calculados são iguais aos dígitos fornecidos
    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        return cpf
    else:
        raise "Cpf digitado é inválido"
    
cpf = validarCpf("07897834130")



conta = Conta(cpf, "Guilherme", 50.50)


