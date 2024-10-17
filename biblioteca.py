def imprimir_nomes(nome):
    print(f"nome: {nome}")


def imprimir_numeros(n):
    for x in range(1, n + 1, 1):
        print(x, end=" ")


class Pessoa:
    def __init__(self, nome, peso, idade):
        self.comendo = False
        self.andando = False
        self.dormindo = False
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def comer(self):

        if self.comendo == False:
            if self.andando == False:
                if self.dormindo == False:
                    print(f"{self.nome} já foi comer")
                    self.comendo = True
                else:
                    print(f"{self.nome} não pode dormir pois já está dormindo")
            else:
                print(f"{self.nome} não  pode andar pois já esta andando")
        else:
            print(f"{self.nome} não pode comer pois já está comendo")

    def andar(self):

        if self.comendo == False:
            if self.andando == False:
                if self.dormimdo == False:
                    print(f"{self.nome} já está andando")
                    self.andando = True

                else:
                    print(f"{self.nome} não pode dormir pois já esta dormindo")
            else:
                print(f"{self.nome} não pode andar pois já esta andando")
        else:
            print(f"{self.nome} não pode comer pois já está cpmendo")

    def dormir(self):

        if self.comendo == False:
            if self.andando == False:
                if self.dormindo == False:
                    print(f"{self.nome} já está dormindo")
                    self.dormindo = True

                else:
                    print(f"{self.nome} não pode dormir pois já está dormindo")
            else:
                print(f"{self.nome} não pode andar pois já está andando")
        else:
            print(f"{self.nome} não pode comer pois já está comendo")


class Animal:

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f" o {self.nome} está miando")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"o {self.nome} está latindo")
    def comer(self):
        print(f"O cachorrinho {self.nome} foi comer")
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def grunhir(self):
            print(f"o {self.nome} está grunhindo")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
            print(f"o {self.nome} está mugindo")


class Atleta:
    def __init__(self, nome, peso):
        self.nome=nome
        self.peso=peso
        self.aquecido=False
        self.aposentado=False
    def aposentar(self):
        if self.aposentado==False:
            print(f"{self.nome} foi aposentado com secesso !")
            self.aposentado=True
        else:
            print(f"{self.nome} não pode aposentar pq já está na rede")

    def aquecer(self):
        if self.aquecido==False:
            print(f"{self.nome} foi aquecer com secesso !")

        else:
            print(f"{self.nome} não pode aquecer pq já está aquecido")


class Corredor(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def correr(self):
        print(f"o {self.nome} foi correr")


class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def nadar(self):
        print(f"o {self.nome} já foi nadar")
class Ciclista(Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def pedalar(self):
        print(f"o {self.nome} já foi pedalar")

class Triatleta(Corredor, Nadador, Ciclista):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    def