class Pessoa:
    def __init__(self, *filhos, nome=None, idade=33):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    gabriel = Pessoa(nome='Gabriel')
    subtil = Pessoa(gabriel, nome='Subtil')
    print(id(subtil))
    print(subtil.cumprimentar()) # Passagem implicita de p
    print(subtil.nome)
    print(subtil.idade)
    for filho in subtil.filhos:
        print(filho.nome)
