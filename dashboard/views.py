from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa se logar para acessar!')
        return render(request, 'contas/login.html')


def portfolio(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')


def acoes(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')


def covariancia(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')


def correlacao(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')
