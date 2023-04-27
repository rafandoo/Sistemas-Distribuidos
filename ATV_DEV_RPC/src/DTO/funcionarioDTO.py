from enum import Enum


class Cargo(Enum):
    ADMINISTRATIVO = 1
    COMERCIAL = 2
    SUPORTE = 3


class FuncionarioDTO:
    def __init__(self, matricula: int, nome: str, email: str, cargo: Cargo, salario: float):
        self._matricula = matricula
        self._nome = nome
        self._email = email
        self._cargo = cargo
        self._salario = salario

    def exportComma(self):
        return f"{self._matricula},{self._nome},{self._email},{self._cargo.value},{self._salario}"

    def __str__(self):
        return f"Funcionario [" \
               f"Matricula: {self._matricula} | " \
               f"Nome: {self._nome} | " \
               f"E-mail: {self._email} | " \
               f"Cargo: {self._cargo.name} | " \
               f"Salario: {self._salario}]"

    def __repr__(self):
        return f"Funcionario(matricula={self._matricula}, nome={self._nome}, email={self._email}, cargo={self._cargo}, salario={self._salario})"
