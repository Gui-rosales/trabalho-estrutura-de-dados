class Conta:

    __numero_de_contas = 0

    def __init__(self, nome: str, cpf: str, saldo: float):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        Conta.__numero_de_contas += 1

    def get_saldo(self) -> float:
        return self.__saldo
    
    def get_nome(self) -> str:
        return self.__nome

    def creditar(self, valor: float) -> float:
        if valor > 0:         
            self.__saldo += valor 
            return self.__saldo
        else:
            return -1
    
    def debitar(self, valor: float) -> float:
        if valor > 0:
            self.__saldo -= valor 
            return self.__saldo
        else:
            return -1
    
    def get_numero_da_conta() -> int:
        return Conta.__numero_de_contas
