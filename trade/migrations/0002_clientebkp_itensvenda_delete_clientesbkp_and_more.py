# Importa módulos necessários do Django
import django.db.models.deletion
from django.db import migrations, models

# Define uma classe de migração
class Migration(migrations.Migration):

    # Define dependências para esta migração
    dependencies = [
        ('trade', '0001_initial'),  # Depende da migração inicial do app 'trade'
    ]

    # Lista de operações a serem realizadas na migração
    operations = [
        # Criação da tabela ClienteBkp
        migrations.CreateModel(
            name='ClienteBkp',
            fields=[
                ('idcli', models.AutoField(primary_key=True, serialize=False)),  # ID do cliente, chave primária
                ('codcli', models.CharField(max_length=10)),  # Código do cliente
                ('nomecli', models.CharField(max_length=100)),  # Nome do cliente
                ('razasoccli', models.CharField(max_length=100)),  # Razão social do cliente
                ('datacli', models.DateField()),  # Data de registro do cliente
                ('cnpjcli', models.CharField(max_length=20)),  # CNPJ do cliente
                ('fonecli', models.CharField(max_length=20)),  # Telefone do cliente
                ('cidcli', models.CharField(max_length=50)),  # Cidade do cliente
                ('estcli', models.CharField(max_length=100)),  # Estado do cliente
            ],
            options={
                'db_table': 'clientesbkp',  # Nome da tabela no banco de dados
            },
        ),
        # Criação da tabela ItensVenda
        migrations.CreateModel(
            name='ItensVenda',
            fields=[
                ('iditvend', models.AutoField(primary_key=True, serialize=False)),  # ID do item da venda, chave primária
                ('valoritvend', models.FloatField()),  # Valor do item da venda
                ('qtditvend', models.IntegerField()),  # Quantidade do item da venda
                ('descitvend', models.FloatField()),  # Desconto no item da venda
            ],
            options={
                'db_table': 'itensvenda',  # Nome da tabela no banco de dados
            },
        ),
        # Deleção da tabela ClientesBkp
        migrations.DeleteModel(
            name='ClientesBkp',
        ),
        # Alteração dos nomes das tabelas para várias modelos
        migrations.AlterModelTable(
            name='cliente',
            table='cliente',  # Define o nome da tabela no banco de dados como 'cliente'
        ),
        migrations.AlterModelTable(
            name='fornecedor',
            table='fornecedor',  # Define o nome da tabela no banco de dados como 'fornecedor'
        ),
        migrations.AlterModelTable(
            name='produto',
            table='produto',  # Define o nome da tabela no banco de dados como 'produto'
        ),
        migrations.AlterModelTable(
            name='venda',
            table='venda',  # Define o nome da tabela no banco de dados como 'venda'
        ),
        migrations.AlterModelTable(
            name='vendedor',
            table='vendedor',  # Define o nome da tabela no banco de dados como 'vendedor'
        ),
        # Adição de campos de chave estrangeira à tabela ItensVenda
        migrations.AddField(
            model_name='itensvenda',
            name='idprod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.produto'),  # Chave estrangeira para Produto
        ),
        migrations.AddField(
            model_name='itensvenda',
            name='idvend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.venda'),  # Chave estrangeira para Venda
        ),
        # Deleção da tabela ItemVenda
        migrations.DeleteModel(
            name='ItemVenda',
        ),
    ]

