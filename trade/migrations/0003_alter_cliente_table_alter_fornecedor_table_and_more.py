from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_clientebkp_itensvenda_delete_clientesbkp_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cliente',
            table='clientes',
        ),
        migrations.AlterModelTable(
            name='fornecedor',
            table='fornecedores',
        ),
        migrations.AlterModelTable(
            name='itensvenda',
            table='itensvendas',
        ),
        migrations.AlterModelTable(
            name='produto',
            table='produtos',
        ),
        migrations.AlterModelTable(
            name='venda',
            table='vendas',
        ),
        migrations.AlterModelTable(
            name='vendedor',
            table='vendedores',
        ),
    ]
