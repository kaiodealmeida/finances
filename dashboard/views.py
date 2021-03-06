from django.shortcuts import render, redirect
from django.contrib import messages
from decimal import *
from .models import Acoes, Portfolio
from .serializers import AcoesSerializer
from rest_framework import viewsets
from django.db import IntegrityError
from dashboard import tickerassinc as ts
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('index_dashboard')


def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa se logar para acessar!')
        return render(request, 'contas/login.html')
    else:
        return render(request, 'dashboard/dashboard.html')


def portfolio(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')


def acoes(request):

    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa se logar para acessar!')
        return render(request, 'contas/login.html')

    ticker = request.GET.get('ticker')

    try:
    
        if ticker is None or not ticker:

            messages.add_message(request, messages.ERROR,
                                'Digite um ticker válido!')
            return redirect('index_dashboard')
        else:                
           
            adjclose = ts.atual(ticker)
            retornomedio = ts.retornomedio(ticker)
            txrisk = ts.txrisk(ticker)
            return render(request, 'dashboard/dashboard_result.html',  {
            'ticker': ticker,
            'adjclose': adjclose,
            'retornomedio': retornomedio,
            'txrisk': txrisk,
        })

    except (UnboundLocalError, IndexError):
        messages.error(request, 'Digite um ticker valido!')         
        return redirect('index_dashboard')


def inserir(request):
    if not request.user.is_authenticated:

        messages.error(request, 'Você precisa se logar para acessar!')
        return render(request, 'contas/login.html')
    try:
        acao = Acoes.objects.last()
        acao = Portfolio(ticker=acao.ticker, adjclose=acao.adjclose,
                    txrisk=acao.txrisk, retorno=acao.retorno, investidor=request.user)
        acao.save()
        return redirect('portfolio')
        
    except IntegrityError:  
        messages.error(request, 'Este ticker ja existe em seu Portfolio!')         
        return redirect('index_dashboard')


def excluir(request):

    if not request.user.is_authenticated:

        messages.error(request, 'Você precisa se logar para acessar!')
        return render(request, 'contas/login.html')
    
    else:

        obj = Portfolio.objects.filter(ticker=request.ticker)
        print(obj)
        return redirect('portfolio')    
   

def portfolio(request):

    if not request.user.is_authenticated:

        messages.error(request, 'Você precisa se logar para acessar!')
        return render(request, 'contas/login.html')
            
    else:
        obj = Portfolio.objects.filter(investidor=request.user)  
        list_tickers = []
        for i in obj:
            list_tickers.append(
            	{
                   'id': i.id,
            	   'ticker': i.ticker,
            	   'adjclose': i.adjclose,
            	   'adjtoday': ts.atual(i.ticker),
                   'rent': (float(ts.atual(i.ticker))/float(i.adjclose) - 1) * 100,
            	}
            )
          
        return render(request, 'dashboard/portfolio.html',  {
            'ticker': list_tickers,           
           
        })
            
       

def covariancia(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')


def correlacao(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')


class AcoesView(viewsets.ModelViewSet):
    serializer_class = AcoesSerializer
    queryset = Portfolio.objects.filter(investidor__isnull=False)
