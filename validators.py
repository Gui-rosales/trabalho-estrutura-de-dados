class Validator: 

    @staticmethod
    def validarCpf(cpf: str) -> str:

        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            return False
        
            # Verificar se todos os dígitos são iguais (blacklist)
        if cpf == cpf[0] * 11:
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
            return True
        else:
            return False