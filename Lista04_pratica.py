#1. Crie uma classe "Pessoa" com um atributo privado "nome" e um método getter para acessá-lo.

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado nome

    def get_nome(self):
        return self.__nome
    
pessoa1 = Pessoa('José')
print(pessoa1.get_nome())



#2. Adcione um setter para o atributo "nome" da classe "Pessoa" para garantir que o nome não esteja vazio.


class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado nome

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('Nome Inválido')

pessoa1 = Pessoa('José')
print(pessoa1.get_nome())

pessoa1.set_nome('Maria José')
print(pessoa1.get_nome())



# 3. Crie uma classe "Carro" com um atributo privado "modelo" e use getter e setter para acessá-lo e modificá-lo.


class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo  # Atributo privado modelo

    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self,modelo):
        if isinstance (modelo,str) and len(modelo) > 0:
            self.__modelo = modelo
        else:
            print('Modelo Inválido')

pessoa1 = Carro('Hb20')
print(pessoa1.get_modelo())

pessoa1.set_modelo('Corsa')
print(pessoa1.get_modelo())



#4. Crie uma classe "ContaBancaria" com um atributo "saldo" e métodos para depositar e sacar, garantindo que o saldo nunca seja negativo.

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo if saldo >= 0 else 0
        
    def depositar (self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor Depositado Inválido')
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Valor de Saque inválido!')

    def get_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.get_saldo())

conta.sacar(2000)
print(conta.get_saldo())
        

# 5. Crie uma classe "Aluno" com atributos privados "nome" e "nota". Crie getters e setters para ambos os atributos.

class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = nota
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        if isinstance(nome,str) and len(nome)>0:
            self.__nome = nome
        else:
            print('Nome errado!')
    
    def get_nota(self):
        return self.__nota
    
    def set__nota(self,nota):
        if  0 <= nota <= 10:
            self.__nota = nota
        else:
            print('Nota Inválida')


aluno1 = Aluno('José ', 10)
print(aluno1.get_nome(), aluno1.get_nota())
aluno1.set_nome('Cleudiane')
aluno1.set__nota(9)
print(aluno1.get_nome(), aluno1.get_nota())

# 6. Crie uma classe "Produto" com atributo privado "preço". Adcione validação no setter para que o preço seja sempre positivo.

class Produto:
    def __init__(self,preco):
        self.__preco = preco  
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        if preco > 0:
            self.__preco = preco
        else:
            print("Preço inválido.")

produto1 = Produto('R$ 90.00' )
print(produto1.get_preco())

produto1.set_preco(80.00)
print(produto1.get_preco())
            

# 7. Crie uma classe "Livro" com atributos privados "titulo" e "autor". Crie métodos para acessar e modificar esses atributos.
class Livro:
        def __init__(self, titulo, autor):
            self.__titulo = titulo
            self.__autor = autor

        def get_titulo(self):
            return self.__titulo

        def set_titulo(self, titulo):
            self.__titulo = titulo

        def get_autor(self):
            return self.__autor

        def set_autor(self, autor):
            self.__autor = autor

livro1 = Livro('{Título: Os Mobrais}', '{Autor: Luky King}')
print(livro1.get_titulo(), livro1.get_autor())

livro1.set_titulo('{Título: Rivotril Litrão}' )
livro1.set_autor('{Autor: Logan}')
print(livro1.get_titulo(), livro1.get_autor())


# 8. Crie uma classe "Funcionário" com um atributo "salário" 
# e métodos getter e setter para modificar o salário, garantindo que o valor seja positivo.

class Funcionario:
    def __init__(self, salario):
        self.__salario = salario  
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        if salario > 0:
           self.__salario = salario
        else:
            print("O salário deve ser sempre um valor positivo.")


funcionario1 = Funcionario(2500)
print(funcionario1.get_salario()) 

funcionario1.set_salario(3000)
print(funcionario1.get_salario()) 




# 9. Crie uma classe "Casa" com atributos privados "endereço" e "valor". 
# Crie métodos para acessar e modificar esses atribubutos.

class Casa:
    def __init__(self, endereco, valor):
        self.__endereco = endereco
        self.__valor = valor

    def get_endereco(self):
        return self.__endereco
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        if valor > 100.000:
            self.__valor = valor
        else:
            print('Valor Inválido!')

      
casa1 = Casa('Rua 3B, Quadra 414 Casa 1',  500.000)
print(casa1.get_endereco(), casa1.get_valor())  

casa1.set_endereco('Rua 4D, Quadra 522, Casa 10')
casa1.set_valor(90.000)
print(casa1.get_endereco(), casa1.get_valor())





# 10. Crie uma clase "Celular" com atributo privado "marca" e métodos para definir e obter a marca.

class Celular:
    def __init__(self, marca):
        self.__marca = marca  

    def get_marca(self):
        return self.__marca
    
    def set_marca(self,marca):
        if isinstance (marca,str) and len(marca) > 0:
            self.__marca = marca
        else:
            print('Marca Inválida')

celular = Celular('Samsung')
print(celular.get_marca())

celular.set_marca('Motorola')
print(celular.get_marca())


# 11. Crie uma classe "Animal" com um atributo "raca" e um método setter que garante que a idade seja uma string.

class Animal:
    def __init__(self, raca):
        self.__raca = raca  

    def get_raca(self):
        return self.__raca
    
    def set_raca(self,raca):
        if isinstance (raca,str) and len(raca) > 0:
            self.__raca =raca
        else:
            print('raca Inválida')

animal = Animal('Cachorro Pastor Alemão ')
print(animal.get_raca())

animal.set_raca('Cachorro HottWeiller')
print(animal.get_raca())


# 12. Crie uma classe "Estudante" com atributos privados "Nome" e "Matrícula". 
# Use  getters e setters para modificar e acessar os atributos.

class Estudante:
    def __init__(self, nome, matricula):
        self.__nome = nome  
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('Nome Inválido')
    
    def get_matricula(self):
        return self.__matricula
    def set_matricula(self,matricula):
        if matricula > 0:
            self.__matricula = matricula
        else:
            print('Matrícula Inválido')

        
estudante = Estudante('José', 12456)
print(estudante.get_nome(), estudante.get_matricula())

estudante.set_nome('Cleudiane')
estudante.set_matricula(45678)
print(estudante.get_nome(), estudante.get_matricula())



# 13. Crie uma classe "Veículo" com um atributo privado "velocidade_maxima" e um método que retorne esse valor.

class Veiculo:
    def __init__(self, velocidade_maxima):
        self.__velocidade_maxima = velocidade_maxima

    def get_velocidade_maxima(self):
        return self.__velocidade_maxima
    
    def set_velocidade_maxima(self,velocidade_maxima):      
        if velocidade_maxima > 0:
            self.__velocidade_maxima = velocidade_maxima
        else:
            print("Erro: A velocidade máxima deve ser um valor positivo.")
    
carro = Veiculo(200) 
velocidade = carro.get_velocidade_maxima() 
print(f"A velocidade máxima do veículo é: {velocidade} km/h")

carro.set_velocidade_maxima(180)
print(carro.get_velocidade_maxima())


# 14. Crie uma classe "Computador" com atributo privado "memoria_ram" e um método setter que só permita valores maiores que zero.

class Computador:
    def __init__(self,memoria_ram):
        self.__memoria_ram = memoria_ram  
    
    def get_memoria_ram(self):
        return self.__memoria_ram
    
    def set_memoria_ram(self, memoria_ram):
        if memoria_ram > 0:
           self.__memoria_ram = memoria_ram
        else:
            print("Valor da Memoria ram inválido.")


computador = Computador(2000)
print(computador.get_memoria_ram()) 

computador.set_memoria_ram(1500)
print(computador.get_memoria_ram()) 


# 15. Crie uma classe "Curso" com atributos privados "nome" e "duracao".
# Crie nétodos para modificar e acessar esses atributos.


class Curso:
    def __init__(self, nome, duracao):
        self.__nome = nome  
        self.__duracao = duracao

    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('Nome Inválido')
    
    def get_duracao(self):
        return self.__duracao
    def set_duracao(self,duracao):
        if duracao > 0:
            self.__duracao = duracao
        else:
            print('Duração Inválido')

        
curso = Curso('Desemvolvimento Web', 550)
print(curso.get_nome(), curso.get_duracao())

curso.set_nome('Python Básico')
curso.set_duracao(400)
print(curso.get_nome(), curso.get_duracao())


# 16. Crie uma classe "Jogo" com um atributo privado "pontuacao" e um método getter para acessar a pontuação.

class Jogo:
    def __init__(self,pontuacao):
        self.__pontuacao = pontuacao  
    
    def get_pontuacao(self):
        return self.__pontuacao


pontuacao = int(input('Digite a pontuação de inicio do jogo: '))
jogo = Jogo(pontuacao)
print(f'Pontuação final do jogo: {jogo.get_pontuacao()}') 
 



# 17. Crie uma classe "Empresa" com atributos privados "nome" e "numero_funcionarios". 
# Crie métodos para acessar e modificar esses atributos.

class Empresa:
    def __init__(self, nome, numero_funcionarios):
        self.__nome = nome  
        self.__numero_funcionarios = numero_funcionarios

    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('Nome Inválido')
    
    def get_numero_funcionarios(self):
        return self.__numero_funcionarios
    
    def set_numero_funcionarios(self,numero_funcionarios):
        if numero_funcionarios > 0:
            self.__numero_funcionarios = numero_funcionarios
        else:
            print('Números de funcionarios é Inválido')

        
empresa = Empresa('Vip Vigilância', 125)
print(empresa.get_nome(), empresa.get_numero_funcionarios())

empresa.set_nome('Fortesul')
empresa.set_numero_funcionarios(100)
print(empresa.get_nome(), empresa.get_numero_funcionarios())



#18. Crie uma classe "Filme" com atributos privados "titulo" e "ano_lancamento".
# Use getters e setters para esses atributos.

class Filme:
    def __init__(self, titulo, ano_lancamento):
        self.__titulo = titulo  
        self.__ano_lancamento = ano_lancamento

    def get_titulo(self):
        return self.__titulo
    def set_titulo(self,titulo):
        if isinstance (titulo,str) and len(titulo) > 0:
            self.__titulo = titulo
        else:
            print('Título Inválido')
    
    def get_ano_lancamento(self):
        return self.__ano_lancamento
    
    def set_ano_lancamento(self,ano_lancamento):
        if ano_lancamento > 0:
            self.__ano_lancamento = ano_lancamento
        else:
            print('Ano de Lançamento incorreto')

        
filme = Filme('O chamado', 2014)
print(filme.get_titulo(), filme.get_ano_lancamento())

filme.set_titulo('Dracula')
filme.set_ano_lancamento(2018)
print(filme.get_titulo(), filme.get_ano_lancamento())



# 19. Crie uma classe "Cidade" com atributos privados "nome" e "populcao".
# Adicione métodos para acessar e modificar esses atributos.

class Cidade:
    def __init__(self, nome, populacao):
        self.__nome = nome  
        self.__populacao = populacao

    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('NOme Inválido')
    
    def get_populacao(self):
        return self.__populacao
    
    def set_populacao(self,populacao):
        if populacao > 0:
            self.__populacao = populacao
        else:
            print('Dados da População incorretos')

        
cidade = Cidade('Goiânia', 1.437366)
print(cidade.get_nome(), cidade.get_populacao())

cidade.set_nome('Aparecida de Goiânia')
cidade.set_populacao(527.796)
print(cidade.get_nome(), cidade.get_populacao())


# 20. Crie uma classe "Professor" com atributos privados "nome" e "disciplina".
# Crie métodos modificar e acessar esses atributos.

class Professor:
    def __init__(self, nome, disciplina):
        self.__nome = nome  
        self.__disciplina = disciplina

    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('Nome Inválido')
    
    def get_disciplina(self):
        return self.__disciplina
    
    def set_disciplina(self,disciplina):
        self.__disciplina = disciplina
        

        
professor = Professor('Ighor', 'POO')
print(professor.get_nome(), professor.get_disciplina())

professor.set_nome('Fábio')
professor.set_disciplina('Matemática')
print(professor.get_nome(),professor.get_disciplina())