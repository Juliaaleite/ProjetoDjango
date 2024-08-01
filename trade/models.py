from django.db import models  # Importa o módulo de modelos do Django para definir modelos de dados

# Define o modelo Vendedor
class Vendedor(models.Model):
    idvende = models.AutoField(primary_key=True)  # Identificador único e auto-incremento para o vendedor
    codivende = models.CharField(max_length=10)  # Código do vendedor, limitado a 10 caracteres
    nomevende = models.CharField(max_length=100)  # Nome do vendedor, limitado a 100 caracteres
    razasocvende = models.CharField(max_length=100)  # Razão social do vendedor, limitado a 100 caracteres
    fonevende = models.CharField(max_length=20)  # Telefone do vendedor, limitado a 20 caracteres
    porcvende = models.FloatField()  # Percentual de comissão do vendedor

    class Meta:
        db_table = 'vendedor'  # Nome da tabela no banco de dados

# Define o modelo Produto
class Produto(models.Model):
    idprod = models.AutoField(primary_key=True)  # Identificador único e auto-incremento para o produto
    codiprod = models.CharField(max_length=20)  # Código do produto, limitado a 20 caracteres
    descprod = models.CharField(max_length=100)  # Descrição do produto, limitado a 100 caracteres
    valorprod = models.FloatField()  # Valor ou preço do produto
    situprod = models.CharField(max_length=1)  # Situação do produto (e.g., disponível ou fora de estoque)
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)  # Chave estrangeira referenciando o fornecedor

    class Meta:
        db_table = 'produto'  # Nome da tabela no banco de dados

# Define o modelo Fornecedor
class Fornecedor(models.Model):
    idforn = models.AutoField(primary_key=True)  # Identificador único e auto-incremento para o fornecedor
    codiforn = models.CharField(max_length=10)  # Código do fornecedor, limitado a 10 caracteres
    nomeforn = models.CharField(max_length=100)  # Nome do fornecedor, limitado a 100 caracteres
    razasocforn = models.CharField(max_length=100)  # Razão social do fornecedor, limitado a 100 caracteres
    foneforn = models.CharField(max_length=20)  # Telefone do fornecedor, limitado a 20 caracteres

    class Meta:
        db_table = 'fornecedor'  # Nome da tabela no banco de dados

# Define o modelo Cliente
class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True, verbose_name="ID do Cliente")  # Identificador único e auto-incremento para o cliente de backup
    codcli = models.CharField(max_length=10, verbose_name="Código do Cliente")  # Código do cliente, limitado a 10 caracteres
    nomecli = models.CharField(max_length=100, verbose_name="Nome do Cliente")  # Nome do cliente, limitado a 100 caracteres
    razasoccli = models.CharField(max_length=100, verbose_name="Razão Social do Cliente")  # Razão social do cliente, limitado a 100 caracteres
    datacli = models.DateField(verbose_name="Data de Nascimento")  # Data de cadastro ou nascimento do cliente
    cnpjcli = models.CharField(max_length=20, verbose_name="CNPJ do Cliente")  # CNPJ do cliente, limitado a 20 caracteres
    fonecli = models.CharField(max_length=20, verbose_name="Telefone do Cliente")  # Telefone do cliente, limitado a 20 caracteres
    cidcli = models.CharField(max_length=50, verbose_name="Cidade do Cliente")  # Cidade do cliente, limitado a 50 caracteres
    estcli = models.CharField(max_length=100, verbose_name="Estado do Cliente")  # Estado do cliente, limitado a 100 caracteres

    class Meta:
        db_table = 'cliente'  # Nome da tabela no banco de dados

# Define o modelo ItensVenda
class ItensVenda(models.Model):
    iditvend = models.AutoField(primary_key=True)  # Identificador único e auto-incremento para o item da venda
    idvend = models.ForeignKey('Venda', on_delete=models.CASCADE)  # Chave estrangeira referenciando a venda
    idprod = models.ForeignKey('Produto', on_delete=models.CASCADE)  # Chave estrangeira referenciando o produto
    valoritvend = models.FloatField()  # Valor do item da venda
    qtditvend = models.IntegerField()  # Quantidade do item na venda
    descitvend = models.FloatField()  # Desconto aplicado ao item da venda

    class Meta:
        db_table = 'itensvenda'  # Nome da tabela no banco de dados

# Define o modelo Venda
class Venda(models.Model):
    idvend = models.AutoField(primary_key=True)  # Identificador único e auto-incremento para a venda
    codivend = models.CharField(max_length=10)  # Código da venda, limitado a 10 caracteres
    idcli = models.ForeignKey('Cliente', on_delete=models.CASCADE)  # Chave estrangeira referenciando o cliente
    idforn = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)  # Chave estrangeira referenciando o fornecedor
    idvende = models.ForeignKey('Vendedor', on_delete=models.CASCADE)  # Chave estrangeira referenciando o vendedor
    valorvend = models.FloatField()  # Valor total da venda
    descvend = models.FloatField()  # Desconto aplicado à venda
    totalvend = models.FloatField()  # Total da venda após descontos
    datavend = models.DateField()  # Data da venda
    valorcomissao = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da comissão da venda, com precisão decimal

    class Meta:
        db_table = 'venda'  # Nome da tabela no banco de dados

# Define o modelo ClienteBkp (provavelmente um backup ou tabela histórica)
class ClienteBkp(models.Model):
    idcli = models.AutoField(primary_key=True, verbose_name="ID do Cliente")  # Identificador único e auto-incremento para o cliente de backup
    codcli = models.CharField(max_length=10, verbose_name="Código do Cliente")  # Código do cliente, limitado a 10 caracteres
    nomecli = models.CharField(max_length=100, verbose_name="Nome do Cliente")  # Nome do cliente, limitado a 100 caracteres
    razasoccli = models.CharField(max_length=100, verbose_name="Razão Social do Cliente")  # Razão social do cliente, limitado a 100 caracteres
    datacli = models.DateField()  # Data de cadastro ou nascimento do cliente
    cnpjcli = models.CharField(max_length=20, verbose_name="CNPJ do Cliente")  # CNPJ do cliente, limitado a 20 caracteres
    fonecli = models.CharField(max_length=20, verbose_name="Telefone do Cliente")  # Telefone do cliente, limitado a 20 caracteres
    cidcli = models.CharField(max_length=50, verbose_name="Cidade do Cliente")  # Cidade do cliente, limitado a 50 caracteres
    estcli = models.CharField(max_length=100, verbose_name="Estado do Cliente")  # Estado do cliente, limitado a 100 caracteres

    class Meta:
        db_table = 'clientesbkp'  # Nome da tabela no banco de dados

