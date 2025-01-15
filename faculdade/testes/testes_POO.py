# Python internamente já trabalha em POO
print(type("olá"))  # função type retorna o tipo de dado
print(type(10))
print(type(1.5))

"olá".upper() #.upper() é um método

################################################################

# CRIANDO UMA CLASSE E MÉTODO

class Jogador:      #Decalarando a classe
    def jogar(self):    #def nesse contexto cria o método.
                        #self é um parâmetro usado para invocar o próprio objeto que usou o método.
        print('Método jogar foi inicializado')

j1 = Jogador()  #Variável recebe a classe
j1.jogar()  #invocou o método

##################################################################

# CRIANDO UM CONSTRUTOR

class Pessoa:                                   # Se criarmos um atributo usando apenas a identação,
    def __init__(self, nome, idade):            # ele será estático e global na classe. É preciso criar o atributo em um
        self.nome = nome                        # construtor (__init__) para ser dinâmico e servir apenas para um objeto específico
        self.idade = idade

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e minha idade é {self.idade}')

p1 = Pessoa('Mario' , 30)
p1.apresentar()
p2 = Pessoa('Luigi' , 25)
p2.apresentar()

#####################################################################################

# HERANÇAS com PASS

class Funcionario(Pessoa):  #Classe Filha ou Subclasse, hedando o conteúdo da classe mãe ou superclasse
    pass                    #comando não faz nada, mas permite que o código continue sem erros.
                            #Mantém a estrutura do código válida até que se escreva a lógica final.

f1 = Funcionario()
f1.apresentar()

#####################################################################################

# HERANÇAS com ATRIBUTOS ESPECÍFICOS

class Funcionario(Pessoa):              # Para além dos atributos da superclasse, precisamos de um atributo a mais na subclasse
    def __init__(self, nome, idade, cadastro):    # Nesse caso reescrevemos o construtor e adicionamos o atributo que precisamos
        self.nome = nome
        self.idade = idade
        self.cadastro = cadastro

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e minha idade é {self.idade}')

f1 = Funcionario('Peach', 20,1001)
f2 = Funcionario('Bowser', 4, 1002)

f1.apresentar()
print(f1.cadastro)

f2.apresentar()

#######################################################################

# REFERENCIANDO MÉTODOS E CONSTRUTORES DA SUPERCLASSE

class Cliente(Pessoa):
    quantidadeClientes = 0  # Variável globlal da classe ou variável estática (servirá para todos os atributos
    def __init__ (self, nome, idade):
        super().__init__(nome,idade)        #super(). referencia o construtor da superclasse
        Cliente.quantidadeClientes += 1     #variável contadora incrementando 1 à var static
        self.cadastro = 1000 + Cliente.quantidadeClientes    #criando número de cadastro automáticamente
        #dessa forma o código coloca sozinho o número de cadastro sem a necessidade
        #de colocarmos manualmente no parâmetro do construtor

    def apresentar(self):
        super().apresentar() #referencia o método da superclasse
        print(f'e sou cliente de cadastro: {self.cadastro}')


c1 = Cliente('yoshi', 15)
c2 = Cliente('Toad',10)
c1.apresentar()
c2.apresentar()

######################################################################################################

#EXEMPLO PRÁTICO

class Aluno:
    totalAlunos = 0
    def __init__(self, nome, nota):
        Aluno.totalAlunos += 1
        self.nome = nome
        self.nota = nota    #0-100
        self.ru = 1000 + Aluno.totalAlunos

    def info(self,):
        print(f'Nome: {self.nome}\n RU: {self.ru}\n Nota:{self.nota}')

    def getNota(self):      #get pega o valor do local especificado
        return self.nota

class Turma:
    def __init__(self, nome, limiteAlunos):
        self.nome =  nome
        self.limiteAlunos = limiteAlunos
        self.listaAlunos = []

    def addAluno(self, aluno):
        if len(self.listaAlunos) < self.limiteAlunos:
            self.listaAlunos.append(aluno)
            return True
        return False

    def mediaTurma(self):
        soma = 0
        for aluno in self.listaAlunos:
            soma += aluno.getNota()
        return soma/len(self.listaAlunos)

a1 = Aluno('Mario', 90)
a2 = Aluno('Luigi', 80)
a3 = Aluno('Yoshi', 40)

t1 =  Turma('Programação', 2)
t1.addAluno(a1)
t1.addAluno(a2)
t1.addAluno(Aluno('Peach', 100))

print(t1.addAluno(a3))
print(t1.mediaTurma())
'''