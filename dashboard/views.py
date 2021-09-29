from django.shortcuts import render, redirect
from django.contrib import messages
from decimal import *
from .models import Acoes, Portfolio
from .serializers import AcoesSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.db import IntegrityError


import yfinance as yf
import pandas as pd
import numpy as np


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
            df = yf.download(ticker, group_by="Ticker", period="max")
            adjclose = df.iloc[-1].at['Adj Close']
            retorno = (df['Adj Close'] / df['Adj Close'].shift(1)) - 1
            retorno.to_csv(f'tx_retorno_{ticker}.csv')
            col_list = ['Date', 'Adj Close']
            retorno = pd.read_csv(f'tx_retorno_{ticker}.csv', usecols=col_list)
            retornomedio = (
                retorno['Adj Close'].iloc[3:].sum() / retorno.ndim) * 100
            df2 = df['Adj Close']
            retornolog = np.log(df2 / df2.shift(1))
            txrisk = (retornolog.std() * 250 ** 0.5) * 100
            acao = Acoes(ticker=ticker, adjclose=adjclose,
                        txrisk=txrisk, retorno=retornomedio)
            acao.save()
            return render(request, 'dashboard/dashboard_result.html',  {
            'ticker': ticker,
            'df': adjclose,
            'retorno': retornomedio,
            'txrisk': txrisk
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
        messages.error(request, 'Este ticker ja existe em seu Portfolio')         
        return redirect('index_dashboard')


def portfolio(request):

    if not request.user.is_authenticated:

        messages.error(request, 'Você precisa se logar para acessar!')
        return render(request, 'contas/login.html')
  
    else:
        
        obj = Portfolio.objects.filter(investidor=request.user)  
        return render(request, 'dashboard/portfolio.html',  {
            'ticker': obj,
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
