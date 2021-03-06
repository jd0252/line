# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:37:47 2021

@author: jd025
"""

import requests
import twstock
import pandas_datareader as web
import datetime

e = datetime.datetime.today()
# 下載最新收盤價價
close = web.DataReader(name='^TWII', data_source='yahoo',start='2021-01-01')['Close'][-1]
original=16408.35
market_ret=(close-original)/original

stocklist=['2317',
'6415',
'6488',
'2881',
'2882',
'2454',
'2886',
'6282',
'3141',
'5483',
'2727',
'8255',
'2634',
'8069',
'8454']

cost=['103.75',
'3935',
'758',
'74.95',
'56.8',
'869',
'33',
'28.8',
'139',
'174.5',
'157.5',
'194.75',
'28.35',
'71.5',
'1575']

df=twstock.realtime.get(stocklist)
ret=0
message=f'現在時間 {e:%Y-%m-%d (%a) %H:%M:%S}\n'
for i,j in zip(stocklist,range(len(stocklist))):
    n=df[i]['info']['name']
    p=float(df[i]['realtime']['latest_trade_price'])
    c=float(cost[j])
    r=round((p-c)/c*100,2)
    ret+=r
    message+=f'{j+1} {n:.5s} 現價 {p:.0f} 成本 {c:.0f} 報酬率 {r}% \n'
message+=f'\n-----------總結----------- \n當日大盤{close:.2f}\n 10/4大盤 {original:.2f} \n 大盤報酬 {market_ret*100:.2f} % 投組報酬 {ret/15:.2f} →{ret/15-market_ret*100:.2f} %  \n'


# 課程的token
# 由：https://notify-bot.line.me/my/ 取得
# AmNKsAT6xU1jCiIyAjvKj65FXXZdQatBv8mSZ9g0rQf  私募
token ='FoOOUvlvFlvcl2kB3fsXWZe6UvriZSSpongEVDhPUNZ'  # 自己


url = "https://notify-api.line.me/api/notify"  # --> 不支援http, 只能用https
headers = {"Authorization" : "Bearer "+ token}
title = '測試'
payload = {"message" :  message}

r = requests.post(url ,headers = headers ,params=payload)
r
