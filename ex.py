numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)  # Adiciona elemento
numeros.remove(4)
print(numeros)

def saudacao(nome):
    return f"ola {nome}!"

print(saudacao("Genesis"))

class Humano:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Me chamo {self.nome} e tenho {self.idade} anos."
    
pessoa = Humano("GINIVALDO", 18)
print(pessoa.apresentar())


lista = ["maça", "uva", "banana"]
for indece, frutas in enumerate(lista):
    print(f"{indece} , {frutas}")

pessoa = {"nome": "Ana julia", "idade": 22}
for indice, valor in pessoa.items():
    print(f"{indice}: {valor}")

for i in range(3):
    print(i)
    
else:
    print("Loop concluido!")


seres = ["aninha", "julinha"]
idadezinhas = ["18", "19"]

for sere, idadezinha in zip(seres, idadezinhas):
    print(f"{sere} tem {idadezinha} anos!")

quadrados = [x ** 2 for x in range(5)]
print(quadrados)
