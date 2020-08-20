class Pessoa:
    def __init__(self, nome=None, idade=33):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Subtil')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # Passagem implicita de p
    print(p.nome)
    p.nome = 'Welinton'
    print(p.nome)