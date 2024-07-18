class Animal:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo protegido
        self.idade = idade

    def exibir_informacoes(self):
        return f"Nome do animal: {self._nome}, Idade: {self.idade} anos"

    def emitir_som(self):
        return "O animal emite um som."
    
class Cachorro(Animal):
    def __init__(self, nome, idade, raca, peso):
        super().__init__(nome, idade)
        self.raca = raca
        self.peso = peso

    def exibir_detalhes(self):
        return f"Nome do cachorro: {self._nome}, Idade: {self.idade} anos, Raça: {self.raca}, Peso: {self.peso} kg"

    def emitir_som(self):
        return "O cachorro late."

    def calcular_idade_humana(self):
        return self.idade * 7

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso
