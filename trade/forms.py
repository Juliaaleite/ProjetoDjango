from django import forms  # Importa o módulo de formulários do Django
from .models import Cliente  # Importa o modelo Cliente do arquivo models.py
from django.contrib.auth.models import User  # Importa o modelo User do Django para autenticação
from django.contrib.auth.forms import UserCreationForm  # Importa o formulário de criação de usuário do Django

class UserRegisterForm(UserCreationForm):  # Define um formulário para registro de novos usuários
    email = forms.EmailField(required=True)  # Adiciona um campo de e-mail ao formulário, tornando-o obrigatório

    class Meta:
        model = User  # Especifica que o modelo para este formulário é o User
        fields = ('username', 'email', 'password1', 'password2')  # Define quais campos serão incluídos no formulário
class ClienteForm(forms.ModelForm):  # Define um formulário para o modelo Cliente
    class Meta:
        model = Cliente  # Especifica que o modelo para este formulário é o Cliente
        fields = '__all__'  # Inclui todos os campos do modelo Cliente no formulário
