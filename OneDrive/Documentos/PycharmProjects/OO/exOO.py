class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Criando objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"""Saldo: {self.__saldo}
Titular: {self.__titular}""")

    def dados(self):
        dadosConta = {"numero": self.__numero,
                      "titular": self.__titular,
                      "saldo": self.__saldo,
                      "limite": self.__limite}
        for k, v in dadosConta.items():
            print(f"{k} é {v}")

    def deposita(self, valor=50):
        if self.__saldo <= self.__limite:
            self.__saldo += valor

    def saque(self, valor=50):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print(f"Erro, limite ultrapassado, valor disponivel: {self.__saldo}")

    def transferir(self, valor, destinatario):
        if valor > self.__saldo:
            print(f"Erro, limite ultrapassado, valor disponível: {self.__saldo}")
            print(f"Erro, limite ultrapassado, valor disponível: {self.__saldo}")
        else:
            self.saque(valor)
            destinatario.deposita(valor)
# getters e setters

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @titular.setter
    def titular(self, titular):
        self.__titular = titular


conta = Conta(123, "André", 900, 1000)



