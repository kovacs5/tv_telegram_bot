from tvDatafeed import TvDatafeed, Interval
import requests
import pandas_ta as pandas_ta
from ta.momentum import RSIIndicator

def send_msg(text):
    url_req = 'https://api.telegram.org/bot5670518697:AAH3AEzOSUpoqbHH4InuQL4KWGaI4YN_7-I/sendMessage?chat_id=1592879913&text=' + text
    results = requests.get(url_req).json()
    return results

tv = TvDatafeed()

symbol_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'AVAXUSDT', 'INJUSDT', 'SOLUSDT', 'MASKUSDT', 'DOTUSDT', 'MATICUSDT', 'LTCUSDT', 'LINKUSDT']
symbol_list_2 = ['XMRUSDT', 'ATOMUSDT', 'TRBUSDT', 'EOSUSDT', 'RNDRUSDT', 'UNIUSDT', 'FILUSDT', 'ANTUSDT', 'BURGERUSDT', 'AAVEUSDT', 'UNFIUSDT', 'FRONTUSDT']

for symbol in symbol_list:

    df = tv.get_hist(symbol=symbol,exchange='BINANCE',interval=Interval.in_15_minute,n_bars=1000)

    df['rsi'] = RSIIndicator(df['close'], window=14).rsi()

    rsi = df['rsi'].iloc[-1]
    rsi_1 = df['rsi'].iloc[-2]

    df['mom'] = pandas_ta.mom(df['close'])

    mom = df['mom'].iloc[-1]
    mom_1 = df['mom'].iloc[-2]
    mom_2 = df['mom'].iloc[-3]

    volume = df['volume'].iloc[-1]
    volume_1 = df['volume'].iloc[-2]
    volume_2 = df['volume'].iloc[-3]
    volume_3 = df['volume'].iloc[-4]

    son_kapanis = df['close'].iloc[-1]
    onceki_kapanis = df['close'].iloc[-2]

    if (rsi > rsi_1 and rsi > 60) & ((volume > volume_1*4) | (volume_1 > volume_2*4)):
        send_msg(symbol + ' için 15 dakikalıkta VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

    if (rsi < rsi_1 and rsi < 60) & (df['close'].iloc[-1] < df['close'].iloc[-2]) & ((volume > volume_1*4) | (volume_1 > volume_2*4)):
        send_msg(symbol + ' için 15 dakikalıkta VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

   
for symbol2 in symbol_list_2:

    df2 = tv.get_hist(symbol=symbol2,exchange='BINANCE',interval=Interval.in_15_minute,n_bars=1000)

    df2['rsi'] = RSIIndicator(df2['close'], window=14).rsi()

    df2rsi = df2['rsi'].iloc[-1]
    df2rsi_1 = df2['rsi'].iloc[-2]

    df2['mom'] = pandas_ta.mom(df2['close'])

    df2mom = df2['mom'].iloc[-1]
    df2mom_1 = df2['mom'].iloc[-2]
    df2mom_2 = df2['mom'].iloc[-3]

    df2volume = df2['volume'].iloc[-1]
    df2volume_1 = df2['volume'].iloc[-2]
    df2volume_2 = df2['volume'].iloc[-3]
    df2volume_3 = df2['volume'].iloc[-4]

    df2son_kapanis = df2['close'].iloc[-1]
    df2onceki_kapanis = df2['close'].iloc[-2]

    if (df2rsi > df2rsi_1 and df2rsi > 60) & ((df2volume > df2volume_1*4) | (df2volume_1 > df2volume_2*4)):
        send_msg(symbol2 + ' için 15 dakikalıkta VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(df2son_kapanis) + '\n' + 'Önceki Değer: ' + str(df2onceki_kapanis))

    if (df2rsi < df2rsi_1 and df2rsi < 60) & (df2['close'].iloc[-1] < df2['close'].iloc[-2]) & ((df2volume > df2volume_1*4) | (df2volume_1 > df2volume_2*4)):
        send_msg(symbol2 + ' için 15 dakikalıkta VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(df2son_kapanis) + '\n' + 'Önceki Değer: ' + str(df2onceki_kapanis))

for symbol3 in symbol_list:

    df3 = tv.get_hist(symbol=symbol3,exchange='BINANCE',interval=Interval.in_5_minute,n_bars=1000)

    df3['rsi'] = RSIIndicator(df3['close'], window=14).rsi()

    df3rsi = df3['rsi'].iloc[-1]
    df3rsi_1 = df3['rsi'].iloc[-2]

    df3['mom'] = pandas_ta.mom(df3['close'])

    df3mom = df3['mom'].iloc[-1]
    df3mom_1 = df3['mom'].iloc[-2]
    df3mom_2 = df3['mom'].iloc[-3]

    df3volume = df3['volume'].iloc[-1]
    df3volume_1 = df3['volume'].iloc[-2]
    df3volume_2 = df3['volume'].iloc[-3]
    df3volume_3 = df3['volume'].iloc[-4]

    df3son_kapanis = df3['close'].iloc[-1]
    df3onceki_kapanis = df3['close'].iloc[-2]

    if (df3rsi > df3rsi_1 and df3rsi > 60) & ((df3volume > df3volume_1*5) | (df3volume_1 > df3volume_2*5)):
        send_msg(symbol3 + ' için 5 dakikalıkta VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(df3son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3onceki_kapanis))

    if (df3rsi < df3rsi_1 and df3rsi < 60) & (df3['close'].iloc[-1] < df3['close'].iloc[-2]) & ((df3volume > df3volume_1*5) | (df3volume_1 > df3volume_2*5)):
        send_msg(symbol3 + ' için 5 dakikalıkta VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(df3son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3onceki_kapanis))

for symbol4 in symbol_list_2:

    df4 = tv.get_hist(symbol=symbol4,exchange='BINANCE',interval=Interval.in_5_minute,n_bars=1000)

    df4['rsi'] = RSIIndicator(df4['close'], window=14).rsi()

    df4rsi = df4['rsi'].iloc[-1]
    df4rsi_1 = df4['rsi'].iloc[-2]

    df4['mom'] = pandas_ta.mom(df4['close'])

    df4mom = df4['mom'].iloc[-1]
    df4mom_1 = df4['mom'].iloc[-2]
    df4mom_2 = df4['mom'].iloc[-3]

    df4volume = df4['volume'].iloc[-1]
    df4volume_1 = df4['volume'].iloc[-2]
    df4volume_2 = df4['volume'].iloc[-3]
    df4volume_3 = df4['volume'].iloc[-4]

    df4son_kapanis = df4['close'].iloc[-1]
    df4onceki_kapanis = df4['close'].iloc[-2]

    if (df4rsi > df4rsi_1 and df4rsi > 60) & ((df4volume > df4volume_1*5) | (df4volume_1 > df4volume_2*5)):
        send_msg(symbol4 + ' için 5 dakikalıkta VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(df4son_kapanis) + '\n' + 'Önceki Değer: ' + str(df4onceki_kapanis))

    if (df4rsi < df4rsi_1 and df4rsi < 60) & (df4['close'].iloc[-1] < df4['close'].iloc[-2]) & ((df4volume > df4volume_1*5) | (df4volume_1 > df4volume_2*5)):
        send_msg(symbol4 + ' için 5 dakikalıkta VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(df4son_kapanis) + '\n' + 'Önceki Değer: ' + str(df4onceki_kapanis))

for symbol5 in symbol_list:

    df5 = tv.get_hist(symbol=symbol5,exchange='BINANCE',interval=Interval.in_30_minute,n_bars=1000)

    df5['rsi'] = RSIIndicator(df5['close'], window=14).rsi()

    df5rsi = df5['rsi'].iloc[-1]
    df5rsi_1 = df5['rsi'].iloc[-2]

    df5['mom'] = pandas_ta.mom(df5['close'])

    df5mom = df5['mom'].iloc[-1]
    df5mom_1 = df5['mom'].iloc[-2]
    df5mom_2 = df5['mom'].iloc[-3]

    df5volume = df5['volume'].iloc[-1]
    df5volume_1 = df5['volume'].iloc[-2]
    df5volume_2 = df5['volume'].iloc[-3]
    df5volume_3 = df5['volume'].iloc[-4]

    df5son_kapanis = df5['close'].iloc[-1]
    df5onceki_kapanis = df5['close'].iloc[-2]

    if (df5rsi > df5rsi_1 and df5rsi > 60) & ((df5volume > df5volume_1*3.5) | (df5volume_1 > df5volume_2*3.5)):
        send_msg(symbol5 + ' için 30 dakikalıkta VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(df5son_kapanis) + '\n' + 'Önceki Değer: ' + str(df5onceki_kapanis))

    if (df5rsi < df5rsi_1 and df5rsi < 60) & (df5['close'].iloc[-1] < df5['close'].iloc[-2]) & ((df5volume > df5volume_1*3.5) | (df5volume_1 > df5volume_2*3.5)):
        send_msg(symbol5 + ' için 30 dakikalıkta VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(df5son_kapanis) + '\n' + 'Önceki Değer: ' + str(df5onceki_kapanis))

for symbol6 in symbol_list_2:

    df6 = tv.get_hist(symbol=symbol6,exchange='BINANCE',interval=Interval.in_30_minute,n_bars=1000)

    df6['rsi'] = RSIIndicator(df6['close'], window=14).rsi()

    df6rsi = df6['rsi'].iloc[-1]
    df6rsi_1 = df6['rsi'].iloc[-2]

    df6['mom'] = pandas_ta.mom(df6['close'])

    df6mom = df6['mom'].iloc[-1]
    df6mom_1 = df6['mom'].iloc[-2]
    df6mom_2 = df6['mom'].iloc[-3]

    df6volume = df6['volume'].iloc[-1]
    df6volume_1 = df6['volume'].iloc[-2]
    df6volume_2 = df6['volume'].iloc[-3]
    df6volume_3 = df6['volume'].iloc[-4]

    df6son_kapanis = df6['close'].iloc[-1]
    df6onceki_kapanis = df6['close'].iloc[-2]

    if (df6rsi > df6rsi_1 and df6rsi > 60) & ((df6volume > df6volume_1*3.5) | (df6volume_1 > df6volume_2*3.5)):
        send_msg(symbol6 + ' için 30 dakikalıkta VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(df6son_kapanis) + '\n' + 'Önceki Değer: ' + str(df6onceki_kapanis))

    if (df6rsi < df6rsi_1 and df6rsi < 60) & (df6['close'].iloc[-1] < df6['close'].iloc[-2]) & ((df6volume > df6volume_1*3.5) | (df6volume_1 > df6volume_2*3.5)):
        send_msg(symbol6 + ' için 30 dakikalıkta VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(df6son_kapanis) + '\n' + 'Önceki Değer: ' + str(df6onceki_kapanis))
