class Animal:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo protegido
        self.idade = idade

    def exibir_informacoes(self):
        return f"Nome do animal: {self._nome}, Idade: {self.idade} anos"

