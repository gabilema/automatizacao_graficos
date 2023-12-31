
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas_datareader as web

#Preços WTI mês

def preco_wti_mes(mes, ano):
  ticker = 'CL=F'
  start_date = f'{ano}-{mes}-01'
  end_date = f'{ano}-{mes}-30'

  data = yf.download(ticker, start=start_date, end=end_date, progress=False)
  return data

mes_desejado = '06'
ano_desejado = '2023'

dados_petroleo_wti_mes = preco_wti_mes(mes_desejado, ano_desejado)

dados_petroleo_wti_mes

#Retorno acumulado

precos = dados_petroleo_wti_mes['Close']
retorno_acumulado = (precos.pct_change() + 1).cumprod()

retorno_acumulado

plt.plot(retorno_acumulado.index, retorno_acumulado)
plt.xlabel('Data')
plt.ylabel('Retorno Acumulado')
plt.title(f'Retorno Acumulado do Petróleo WTI - Junho/{ano_desejado}')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.plot(retorno_acumulado.index, retorno_acumulado)
#plt.xlabel('Data')
plt.title(f'Retorno Acumulado do Petróleo WTI - {mes_desejado}/{ano_desejado}')
plt.tick_params(left=False, right=False, labelleft=False)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Gráfico Anual

symbol = 'CL=F'
start_date_year = '2023-01-01'
end_date_year = '2023-06-30'

data_year = yf.download(symbol, start = start_date_year, end=end_date_year, progress=False)

data_year['Daily_Return'] = data_year['Close'].pct_change()  #retorno % diário
data_year['Cumulative_Return'] = (1 + data_year['Daily_Return']).cumprod() # Retorno acumulado

fig, ax = plt.subplots()
ax.plot(data_year.index, data_year['Cumulative_Return'])
ax.set_title('Retorno Acumulado do Petróleo WTI Anual')
#ax.set_xlabel('Data')
ax.set_ylabel('Retorno Acumulado')
date_fmt = mdates.DateFormatter('%m-%Y')
ax.xaxis.set_major_formatter(date_fmt)
fig.autofmt_xdate()

plt.show()

fig, ax = plt.subplots()
ax.plot(data_year.index, data_year['Cumulative_Return'])
ax.set_title('Retorno Acumulado do Petróleo WTI Anual')
#ax.set_xlabel('Data')
ax.yaxis.set_visible(False)
date_fmt = mdates.DateFormatter('%m-%Y')
ax.xaxis.set_major_formatter(date_fmt)
fig.autofmt_xdate()

plt.show()

#S&P 500

mes_sp = 6
ano_sp = 2023

ticker_sp = '^GSPC'
dados_sp_mes = yf.download(ticker_sp, start=f'{ano_sp}-{mes_sp:02}-01', end=f'{ano_sp}-{mes_sp+1:02}-01')

dados_sp_mes

plt.figure(figsize=(10,6))
plt.plot(dados_sp_mes.index, dados_sp_mes['Close'])
plt.title(f'S&P 500 - Junho /{ano_sp}')
#plt.xlabel('Data')
plt.tick_params(left=False, right=False, labelleft=False)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Grafico Anual

dados_sp_ano = yf.download(ticker_sp, start=f'{ano_sp}-01-01', end=f'{ano_sp}-12-31')

plt.figure(figsize=(10,6))
plt.plot(dados_sp_ano.index, dados_sp_ano['Close'])
plt.title(f'S&P 500 - {ano_sp}')
plt.tick_params(left=False, right=False, labelleft=False)
plt.xticks(rotation=45)
plt.tight_layout()
inicio_sp_ano = dados_sp_ano['Close'].iloc[0]
final_sp_ano = dados_sp_ano['Close'].iloc[-1]
plt.text(dados_sp_ano.index[0], inicio_sp_ano, f'{inicio_sp_ano:.2f}', fontsize=8, ha='right', va='bottom')
plt.text(dados_sp_ano.index[-1], final_sp_ano, f'{final_sp_ano:.2f}', fontsize=8, ha='left', va='top')
plt.show()

#Gráfico DXY - USD/BRL

mes_cambio = 6
ano_cambio = 2023

dxy =yf.download('DX-Y.NYB', start=f'{ano_cambio}-{mes_cambio}-01', end=f'{ano_cambio}-{mes_cambio}-30')
usd_brl = yf.download('BRL=X', start=f'{ano_cambio}-{mes_cambio}-01', end=f'{ano_cambio}-{mes_cambio}-30')

dxy_data = dxy.index
dxy_close = dxy['Close']

usd_brl_data = usd_brl.index
usd_brl_close = usd_brl['Close']

fig, ax1 = plt.subplots()

#DXY  no eixo primário

ax1.plot(dxy_data, dxy_close, 'b-', label='DXY')
ax1.set_xlabel('Data')
ax1.set_ylabel('DXY', color='b')
ax1.tick_params('y', colors='b')

#eixo secundário

ax2 = ax1.twinx()

ax2.plot(usd_brl_data, usd_brl_close, 'r-', label='USD/BRL')
ax2.set_ylabel('USD/BRL', color='r')
ax2.tick_params('y', colors='r')


#Ajustar eixo x
fig.autofmt_xdate()

#Adicionar legendda
lines = ax1.get_lines() + ax2.get_lines()
ax1.legend(lines, [line.get_label() for line in lines])

#Título
plt.title(f'Índice DXY vs. USD/BRL - {mes_cambio}/{ano_cambio}')

plt.show()

#Gráfico Anual

dxy_ano = yf.download('DX-Y.NYB', start=f'{ano_cambio}-01-01', end=f'{ano_cambio}-12-31')
usd_brl_ano = yf.download('BRL=X', start=f'{ano_cambio}-01-01', end=f'{ano_cambio}-12-31')

dxy_data_ano = dxy_ano.index
dxy_close_ano = dxy_ano['Close']

usd_brl_data_ano = usd_brl_ano.index
usd_brl_close_ano = usd_brl_ano['Close']

#figura

fig, ax1 = plt.subplots()

ax1.plot(dxy_data_ano, dxy_close_ano, 'b-', label='DXY')
ax1.set_xlabel('Data')
ax1.set_ylabel('DXY', color='b')
ax1.tick_params('y', colors='b')

#eixo 2º

ax2 = ax1.twinx()

ax2.plot(usd_brl_data_ano, usd_brl_close_ano, 'r-', label='USD/BRL')
ax2.set_ylabel('USD/BRL', color='r')
ax2.tick_params('y', colors='r')

fig.autofmt_xdate()

lines=ax1.get_lines() + ax2.get_lines()
ax1.legend(lines, [line.get_label() for line in lines])

plt.title(f'Índice DXY vs. USD/BRL - {ano_cambio}')

plt.show()

#Ibov

start_date_ibov = datetime.datetime(2023, 1, 1)
end_date_ibov = datetime.datetime(2023,6,20)

df_ibov = web.DataReader('^BVSP', data_source='yahoo', start=start_date_ibov, end=end_date_ibov)

