import plotly.graph_objects as go
import chart_studio.plotly as py
import numpy as np
import pandas as pd
import requests


url='https://kurs.web.id/api/v1/bca'
data = requests.get(url)
kursbeli = float(data.json()['beli'])

dfAAPL = pd.read_csv('AAPL.csv',index_col=False,parse_dates=['Date'])
dfAAPL.set_index('Date', inplace=True)
dfAAPL['Open'] = dfAAPL['Open']*kursbeli
dfAAPL['High'] = dfAAPL['High']*kursbeli
dfAAPL['Low'] = dfAAPL['Low']*kursbeli
dfAAPL['Close'] = dfAAPL['Close']*kursbeli
dfAAPL['Adj Close'] = dfAAPL['Adj Close']*kursbeli
#----------------------------------------------------------------------------------------------------
dfMSFT = pd.read_csv('MSFT.csv',index_col=False,parse_dates=['Date'])
dfMSFT.set_index('Date', inplace=True)
dfMSFT['Open'] = dfMSFT['Open']*kursbeli
dfMSFT['High'] = dfMSFT['High']*kursbeli
dfMSFT['Low'] = dfMSFT['Low']*kursbeli
dfMSFT['Close'] = dfMSFT['Close']*kursbeli
dfMSFT['Adj Close'] = dfMSFT['Adj Close']*kursbeli
#----------------------------------------------------------------------------------------------------
dfGOOG = pd.read_csv('GOOG.csv',index_col=False,parse_dates=['Date'])
dfGOOG.set_index('Date', inplace=True)
dfGOOG['Open'] = dfGOOG['Open']*kursbeli
dfGOOG['High'] = dfGOOG['High']*kursbeli
dfGOOG['Low'] = dfGOOG['Low']*kursbeli
dfGOOG['Close'] = dfGOOG['Close']*kursbeli
dfGOOG['Adj Close'] = dfGOOG['Adj Close']*kursbeli
#----------------------------------------------------------------------------------------------------
dfFB = pd.read_csv('FB.csv',index_col=False,parse_dates=['Date'])
dfFB.set_index('Date', inplace=True)
dfFB['Open'] = dfFB['Open']*kursbeli
dfFB['High'] = dfFB['High']*kursbeli
dfFB['Low'] = dfFB['Low']*kursbeli
dfFB['Close'] = dfFB['Close']*kursbeli
dfFB['Adj Close'] = dfFB['Adj Close']*kursbeli
#-----------------------------------------------------------------------------------------------------
dfTLKM = pd.read_csv('data-histori-sahamTELKOM.csv', parse_dates=['Tanggal'], index_col=False)
dfTLKM.set_index('Tanggal', inplace=True)
dfTLKM.sort_index(inplace=True)
#-----------------------------------------------------------------------------------------------------
dfISAT = pd.read_csv('data-histori-sahamISAT.csv', parse_dates=['Tanggal'], index_col=False)
dfISAT.set_index('Tanggal', inplace=True)
dfISAT.sort_index(inplace=True)
#----------------------------------------------------------------------------------------------------
dfEXCL = pd.read_csv('data-histori-sahamXL.csv', parse_dates=['Tanggal'], index_col=False)
dfEXCL.set_index('Tanggal', inplace=True)
dfEXCL.sort_index(inplace=True)
#----------------------------------------------------------------------------------------------------
dfFREN = pd.read_csv('data-histori-sahamSMARTFREN.csv', parse_dates=['Tanggal'], index_col=False)
dfFREN.set_index('Tanggal', inplace=True)
dfFREN.sort_index(inplace=True)
#----------------------------------------------------------------------------------------------------

fig = go.Figure(data=go.Scatter(
    y = dfAAPL['Close'],
    x = dfAAPL.index,
    name='Apple',
    mode='lines',
    marker=dict(
        size=4,
        color='blue', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
    )
))

fig.add_trace(go.Scatter(
    x=dfMSFT.index, y=dfMSFT['Close'],
    name='Microsoft',
    mode='lines',
    marker=dict(
        size=4,
        color='red', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))

fig.add_trace(go.Scatter(
    x=dfFB.index, y=dfFB['Close'],
    name='Facebook',
    mode='lines',
    marker=dict(
        size=4,
        color='yellow', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))

fig.add_trace(go.Scatter(
    x=dfGOOG.index, y=dfGOOG['Close'],
    name='Google',
    mode='lines',
    marker=dict(
        size=4,
        color='green', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))

fig.add_trace(go.Scatter(
    x=dfTLKM.index, y=dfTLKM['Close'],
    name='Telkomsel',
    mode='lines',
    marker=dict(
        size=4,
        color='black', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))

fig.add_trace(go.Scatter(
    x=dfISAT.index, y=dfISAT['Close'],
    name='Indosat',
    mode='lines',
    marker=dict(
        size=4,
        color='purple', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))

fig.add_trace(go.Scatter(
    x=dfEXCL.index, y=dfEXCL['Close'],
    name='XL Axiata',
    mode='lines',
    marker=dict(
        size=4,
        color='brown', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))

fig.add_trace(go.Scatter(
    x=dfFREN.index, y=dfFREN['Close'],
    name='Smartfren',
    mode='lines',
    marker=dict(
        size=4,
        color='pink', #set color equal to a variable
        # colorscale='Viridis', # one of plotly colorscales
        # showscale=True
)))
fig.show()