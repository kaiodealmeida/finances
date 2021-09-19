import yfinance as yf
import pandas as pd
import numpy as np

ticker = (str)
adjclose = (float)


class Acoes():
    def calculos():
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
