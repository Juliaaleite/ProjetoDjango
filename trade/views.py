from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar URLs
from .models import Produto, Venda, ItensVenda, Cliente, Fornecedor, Vendedor  # Importa os modelos utilizados
from .forms import ClienteForm, UserRegisterForm  # Importa os formulários para cliente e registro de usuário
from django.contrib.auth import login, logout, authenticate  # Importa funções para autenticação e gerenciamento de sessão
from django.contrib.auth.forms import AuthenticationForm  # Importa o formulário de autenticação padrão

def home(request):
    # Renderiza a página inicial do site
    return render(request, 'trade/home.html')

def login_view(request):
    # Lida com a visualização de login
    if request.method == "POST":  # Se a requisição for POST, processa o formulário de login
        form = AuthenticationForm(request, data=request.POST)  # Cria uma instância do formulário de autenticação com os dados POST
        if form.is_valid():  # Verifica se o formulário é válido
            username = form.cleaned_data.get('username')  # Obtém o nome de usuário
            password = form.cleaned_data.get('password')  # Obtém a senha
            user = authenticate(username=username, password=password)  # Autentica o usuário
            if user is not None:  # Se o usuário for autenticado com sucesso
                login(request, user)  # Faz o login do usuário
                return redirect('home')  # Redireciona para a página inicial
    else:
        form = AuthenticationForm()  # Cria um formulário vazio para GET requests
    return render(request, 'trade/login.html', {'form': form})  # Renderiza a página de login com o formulário

def cadastro_clientes(request):
    # Lida com o cadastro de novos clientes
    if request.method == 'POST':  # Se a requisição for POST, processa o formulário de cliente
        form = ClienteForm(request.POST)  # Cria uma instância do formulário de cliente com os dados POST
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva o novo cliente no banco de dados
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = ClienteForm()  # Cria um formulário vazio para GET requests
    return render(request, 'trade/cadastro_clientes.html', {'form': form})  # Renderiza a página de cadastro de clientes com o formulário

def demonstrativo_tabelas(request):
    # Lida com a visualização dos dados das tabelas
    clientes = Cliente.objects.all()  # Obtém todos os clientes
    fornecedores = Fornecedor.objects.all()  # Obtém todos os fornecedores
    produtos = Produto.objects.all()  # Obtém todos os produtos
    vendas = Venda.objects.all()  # Obtém todas as vendas
    return render(request, 'trade/demonstrativo_tabelas.html', {  # Renderiza a página com os dados das tabelas
        'clientes': clientes,
        'fornecedores': fornecedores,
        'produtos': produtos,
        'vendas': vendas,
    })

def register_view(request):
    # Lida com o registro de novos usuários
    if request.method == "POST":  # Se a requisição for POST, processa o formulário de registro
        form = UserRegisterForm(request.POST)  # Cria uma instância do formulário de registro com os dados POST
        if form.is_valid():  # Verifica se o formulário é válido
            user = form.save()  # Salva o novo usuário no banco de dados
            login(request, user)  # Faz o login do usuário
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = UserRegisterForm()  # Cria um formulário vazio para GET requests
    return render(request, 'trade/register.html', {'form': form})  # Renderiza a página de registro com o formulário

def galeria_produtos(request):
    # Lida com a visualização da galeria de produtos
    produtos = Produto.objects.all()  # Obtém todos os produtos
    return render(request, 'trade/galeria_produtos.html', {'produtos': produtos})  # Renderiza a página da galeria de produtos com os produtos

def logout_view(request):
    # Lida com a operação de logout
    logout(request)  # Faz o logout do usuário
    return redirect('login')  # Redireciona para a página de login

def realizar_venda(request):
    # Lida com o processo de realização de vendas
    if request.method == 'POST':  # Se a requisição for POST, processa a venda
        cliente_id = request.POST.get('cliente')  # Obtém o ID do cliente
        produto_id = request.POST.get('produto')  # Obtém o ID do produto
        quantidade = request.POST.get('quantidade')  # Obtém a quantidade
        cliente = Cliente.objects.get(idcli=cliente_id)  # Obtém o cliente correspondente ao ID
        produto = Produto.objects.get(idprod=produto_id)  # Obtém o produto correspondente ao ID
        vendedor = Vendedor.objects.first()  # Obtém o primeiro vendedor, assumido como padrão
        fornecedor = produto.idforn  # Obtém o fornecedor do produto

        valor_venda = produto.valorprod * int(quantidade)  # Calcula o valor total da venda
        venda = Venda.objects.create(  # Cria uma nova venda
            codivend='12345',  # Código de venda gerado automaticamente
            idcli=cliente,
            idforn=fornecedor,
            idvende=vendedor,
            valorvend=valor_venda,
            descvend=0,
            totalvend=valor_venda,
            datavend='2023-07-19',  # Data da venda (fixa no exemplo)
            valorcomissao=valor_venda * vendedor.porcvende / 100  # Calcula o valor da comissão
        )

        ItensVenda.objects.create(  # Cria um item de venda
            idvend=venda,
            idprod=produto,
            valoritvend=produto.valorprod,
            qtditvend=quantidade,
            descitvend=0
        )

        return redirect('home')  # Redireciona para a página inicial após a venda ser registrada

    clientes = Cliente.objects.all()  # Obtém todos os clientes
    produtos = Produto.objects.all()  # Obtém todos os produtos
    return render(request, 'trade/realizar_venda.html', {  # Renderiza a página de realizar venda com os clientes e produtos
        'clientes': clientes,
        'produtos': produtos,
    })
