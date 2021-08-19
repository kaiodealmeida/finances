
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.db.models import Exists
from django.core.validators import validate_email
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method != 'POST':
        return render(request, 'contas/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = authenticate(request, username=usuario, password=senha)
    if user is None:
        messages.error(request, 'Dados incorretos!')
        return render(request, 'contas/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Usuário logado com sucesso!')
        return render(request, './dashboard/dashboard.html')


def logout(request):
    return render(request, 'contas/login.html')


def cadastro(request):

    if request.method != 'POST':
        return render(request, 'contas/cadastro.html')

    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not usuario or not email or not senha or not senha2:
        messages.error(request, 'Os campos não podem ser vazios!')
        return render(request, 'contas/cadastro.html')

    if senha != senha2:
        messages.error(request, 'As senhas devem ser iguais!')
        return render(request, 'contas/cadastro.html')
    try:
        email = validate_email(email)
    except:
        messages.error(request, 'O email está incorreto!')
        return render(request, 'contas/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'O usuário deve ter mais que 6 caracteres!')
        return render(request, 'contas/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'A senha deve ter mais que 6 caracteres!')
        return render(request, 'contas/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'O usuário já existe!')
        return render(request, 'contas/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'O email já existe!')
        return render(request, 'contas/cadastro.html')

    messages.success(request, 'Usuário cadastrado com sucesso.')

    usuario = User.objects.create_user(
        username=usuario, password=senha, email=email)
    usuario.save()

    return redirect('login')
