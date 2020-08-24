class Pessoa:
    olhos = 2 # atributo default ou atributo de classe

    def __init__(self, *filhos, nome=None, idade=33):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod # tem acesso a classe que está executando esse método
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    gabriel = Homem(nome='Gabriel')
    subtil = Homem(gabriel, nome='Subtil')
    print(id(subtil))
    print(subtil.cumprimentar())  # Passagem implicita de p
    print(subtil.nome)
    print(subtil.idade)
    for filho in subtil.filhos:
        print(filho.nome)
    subtil.sobrenome = 'Oliveira' # apenas para esse objeto
    del subtil.filhos # Não é uma boa pratica
    print(subtil.sobrenome)
    print(subtil.__dict__)
    print(gabriel.__dict__)
    print(gabriel.olhos)
    print(subtil.olhos)
    print(id(Pessoa.olhos), id(subtil.olhos), id(gabriel.olhos))
    print(Pessoa.metodo_estatico(), subtil.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), subtil.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(gabriel, Pessoa))
    print(isinstance(gabriel, Homem))
