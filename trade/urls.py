from django.urls import path  # Importa a função path do módulo urls do Django, usada para definir rotas de URL
from . import views  # Importa o módulo views da mesma pasta para associar URLs às funções de visualização

# Define a lista de padrões de URL para o aplicativo
urlpatterns = [
    path('', views.login_view, name='login'), # URL raiz (página inicial) associada à login em views, nomeada como 'login'
    path('home/', views.home, name='home'),  # URL '/home/' associada à função home em views, nomeada como 'home'
    path('logout/', views.logout_view, name='logout'),  # URL '/logout/' associada à função logout_view em views, nomeada como 'logout'
    path('register/', views.register_view, name='register'),  # URL '/register/' associada à função register_view em views, nomeada como 'register'
    path('cadastro_clientes/', views.cadastro_clientes, name='cadastro_clientes'),  # URL '/cadastro_clientes/' associada à função cadastro_clientes em views, nomeada como 'cadastro_clientes'
    path('demonstrativo_tabelas/', views.demonstrativo_tabelas, name='demonstrativo_tabelas'),  # URL '/demonstrativo_tabelas/' associada à função demonstrativo_tabelas em views, nomeada como 'demonstrativo_tabelas'
    path('galeria_produtos/', views.galeria_produtos, name='galeria_produtos'),  # URL '/galeria_produtos/' associada à função galeria_produtos em views, nomeada como 'galeria_produtos'
    path('realizar_venda/', views.realizar_venda, name='realizar_venda'),  # URL '/realizar_venda/' associada à função realizar_venda em views, nomeada como 'realizar_venda'
]

