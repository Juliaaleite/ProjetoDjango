from django.contrib import admin  # Importa o módulo de administração do Django para gerenciar modelos via interface administrativa
from .models import Vendedor, Fornecedor, Produto, Cliente, ClienteBkp, Venda, ItensVenda  # Importa os modelos que serão registrados no admin

# Registra o modelo Vendedor no site de administração do Django
admin.site.register(Vendedor)

# Registra o modelo Fornecedor no site de administração do Django
admin.site.register(Fornecedor)

# Registra o modelo Produto no site de administração do Django
admin.site.register(Produto)

# Registra o modelo Cliente no site de administração do Django
admin.site.register(Cliente)

# Registra o modelo ClienteBkp no site de administração do Django
admin.site.register(ClienteBkp)

# Registra o modelo Venda no site de administração do Django
admin.site.register(Venda)

# Registra o modelo ItensVenda no site de administração do Django
admin.site.register(ItensVenda)

