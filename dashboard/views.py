from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django_pandas.managers import DataFrameManager

# Importar bibliotecas para tickers

import numpy as np
import yfinance as yf
import pandas as pd

objects = DataFrameManager()


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
    if ticker is None or not ticker:
        messages.add_message(request, messages.ERROR,
                             'Digite um ticker válido!')
        return redirect('index_dashboard')
    # função do yfinance para trabalhar com dados de vários tickers
    df = yf.download(ticker, group_by="Ticker", period="1d")
    df['Ticker'] = ticker
    df.rename(columns={'Adj Close': 'Preço de Fechamento R$:'}, inplace=True)
    # salva o arquivo com o nome ticker_TICKER
    df.to_csv(f'ticker_{ticker}.csv')
    # Define a lista de colunas como Data, ticker e preço de fechamento ajustado
    col_list = ['Preço de Fechamento R$:']
    df = pd.read_csv(f'ticker_{ticker}.csv', usecols=col_list, na_filter=False)
    # add esta coluna, pois o dataframe não contém uma com o nome do ticker
    return render(request, 'dashboard/dashboard_result.html',  {'df': df})


def covariancia(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')


def correlacao(request):
    messages.error(request, 'Precisa logar para acessar!')
    return render(request, 'contas/login.html')
