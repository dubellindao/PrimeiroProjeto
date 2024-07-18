from animal import *

# Exemplo de uso
animal = Animal("Bicho", 5)
print(animal.exibir_informacoes())
print(animal.emitir_som())

cachorro = Cachorro("Rex", 3, "Labrador", 30)
print(cachorro.exibir_detalhes())
print(cachorro.emitir_som())
print(f"Idade em anos humanos: {cachorro.calcular_idade_humana()}")

# Atualizando o peso do cachorro
cachorro.atualizar_peso(32)
print(cachorro.exibir_detalhes())