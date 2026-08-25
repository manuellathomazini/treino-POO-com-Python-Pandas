import pandas as pd

#criando a classe principal
class Funcionario:
    def __init__(self, nome, taxa_desc, sal):
        self.nome = nome
        self.taxa_desc = taxa_desc
        self.sal = sal

    #função que calcula o desconto
    def calc_desc(self):
        desc = self.sal * self.taxa_desc / 100
        return desc

    #função que calcula o salário final
    def sal_final(self):
        sal_final = self.sal - self.calc_desc()
        return sal_final

    #função que apresenta os resultados
    def relatorio(self):
        return (f"-------------\nFuncionário: {self.nome}\nValor descontado: {self.calc_desc():.2f}\nSalário final: {self.sal_final()}")

#criando os objetos de exemplo
f1 = Funcionario("Ana", 5, 4500)
f2 = Funcionario("Joelma", 10, 7600)
f3 = Funcionario("Pedro", 27.5, 13700)
f4 = Funcionario("Luíz", 3, 2000)
f5 = Funcionario("Carlos", 50, 60000)

#armazenando os objetos em uma lista
funcionarios = [f1, f2, f3, f4, f5]

#laço de repetição para apresentar os resultados de cada objeto
for f in funcionarios:
    print(f.relatorio())

#criando lista de dados de cada funcionário em formato de dicionário para a leitura do pandas
dados = []
for f in funcionarios:
    linha = {
        'Funcionário': f.nome,
        'Taxa de desconto': f.taxa_desc,
        'Salário bruto': f.sal,
        'Valor descontado': f.calc_desc(),
        'Salário final': f.sal_final()
    }
    dados.append(linha)

#criando DataFrame
df = pd.DataFrame(dados)
print(df)