from tvDatafeed import TvDatafeedLive, Interval
import requests
import pandas_ta as ta
import pandas as pd
import numpy as np

def send_msg(text):
    url_req = 'https://api.telegram.org/bot5670518697:AAH3AEzOSUpoqbHH4InuQL4KWGaI4YN_7-I/sendMessage?chat_id=1592879913&text=' + text
    results = requests.get(url_req).json()
    return results

tv = TvDatafeedLive()

symbol_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'SOLUSDT', 'TRXUSDT', 'DOTUSDT', 'MATICUSDT', 'LTCUSDT', 'LINKUSDT']
symbol_list_2 = ['XLMUSDT', 'ATOMUSDT', 'VETUSDT', 'EOSUSDT', 'XTZUSDT', 'UNIUSDT', 'FILUSDT', 'BAKEUSDT', 'BURGERUSDT', 'FLMUSDT', 'UNFIUSDT', 'FRONTUSDT']

for symbol in symbol_list:

    df = tv.get_hist(symbol=symbol,exchange='BINANCE',interval=Interval.in_30_minute,n_bars=1000)

    close_1 = df['close'].iloc[-1]
    close_2 = df['close'].iloc[-2]

    high_1 = df['high'].iloc[-1]
    high_2 = df['high'].iloc[-2]
    high_3 = df['high'].iloc[-3]
    high_4 = df['high'].iloc[-4]

    low_1 = df['low'].iloc[-1]
    low_2 = df['low'].iloc[-2]
    low_3 = df['low'].iloc[-3]
    low_4 = df['low'].iloc[-4]

    if (close_1 > close_2) & (high_1 - low_1 > (high_2-low_2 + high_3-low_3)):
        send_msg(symbol + ' için PUMP 🟢\n' + 'Anlık Değer: ' + str(close_1) + '\n' + 'Önceki Değer: ' + str(close_2))

    elif (close_1 < close_2) & (high_1 - low_1 > (high_2-low_2 + high_3-low_3)):
        send_msg(symbol + ' için DUMP 🔴\n' + 'Anlık Değer: ' + str(close_1) + '\n' + 'Önceki Değer: ' + str(close_2))

for symbol2 in symbol_list_2:

    df2 = tv.get_hist(symbol=symbol2,exchange='BINANCE',interval=Interval.in_30_minute,n_bars=1000)

    close_1_df2 = df2['close'].iloc[-1]
    close_2_df2 = df2['close'].iloc[-2]

    high_1_df2 = df2['high'].iloc[-1]
    high_2_df2 = df2['high'].iloc[-2]
    high_3_df2 = df2['high'].iloc[-3]
    high_4_df2 = df2['high'].iloc[-4]

    low_1_df2 = df2['low'].iloc[-1]
    low_2_df2 = df2['low'].iloc[-2]
    low_3_df2 = df2['low'].iloc[-3]
    low_4_df2 = df2['low'].iloc[-4]

    if (close_1_df2 > close_2_df2) & (high_1_df2 - low_1_df2 > (high_2_df2-low_2_df2 + high_3_df2-low_3_df2)):
        send_msg(symbol2 + ' için PUMP 🟢\n' + 'Anlık Değer: ' + str(close_1_df2) + '\n' + 'Önceki Değer: ' + str(close_2_df2))

    elif (close_1_df2 < close_2_df2) & (high_1_df2 - low_1_df2 > (high_2_df2-low_2_df2 + high_3_df2-low_3_df2)):
        send_msg(symbol2 + ' için DUMP 🔴\n' + 'Anlık Değer: ' + str(close_1_df2) + '\n' + 'Önceki Değer: ' + str(close_2_df2))
