from tvDatafeed import TvDatafeed, Interval
import requests
import pandas_ta as pandas_ta
from ta.momentum import RSIIndicator

def send_msg(text):
    url_req = 'https://api.telegram.org/bot5670518697:AAH3AEzOSUpoqbHH4InuQL4KWGaI4YN_7-I/sendMessage?chat_id=1592879913&text=' + text
    results = requests.get(url_req).json()
    return results

tv = TvDatafeed()

symbol_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'NEOUSDT', 'INJUSDT', 'SOLUSDT', 'MASKUSDT', 'DOTUSDT', 'MATICUSDT', 'LTCUSDT', 'LINKUSDT']
symbol_list_2 = ['XMRUSDT', 'ATOMUSDT', 'TRBUSDT', 'EOSUSDT', 'RNDRUSDT', 'UNIUSDT', 'FILUSDT', 'ANTUSDT', 'BURGERUSDT', 'AAVEUSDT', 'UNFIUSDT', 'FRONTUSDT']

symbol_list_3 = ['THYAO','TTKOM','SISE','BIENY','MERCN','KLKIM','DZGYO','CRFSA','KONTR','DOAS','ENERY','GESAN','ENKAI','TMSN','ZOREN','KONKA','KOPOL','GSDHO']
symbol_list_4 = ['RAYSG','YEOTK','KCAER','TRCAS','BERA','CEMAS','METRO','KATMR','ADESE','EUPWR','KLSER','GWIND','GOKNR','SMRTG','HUNER','OYAKC','BRLSM','CANTE']

for symbol in symbol_list:

    df = tv.get_hist(symbol=symbol,exchange='BINANCE',interval=Interval.in_daily,n_bars=1000)

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

    if (rsi > rsi_1 and rsi > 60) & ((volume > volume_1*3)):
        send_msg(symbol + ' için günlükte VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

    if (rsi < rsi_1 and rsi < 60) & (df['close'].iloc[-1] < df['close'].iloc[-2]) & ((volume > volume_1*3)):
        send_msg(symbol + ' için günlükte VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

   
for symbol2 in symbol_list_2:

    df2 = tv.get_hist(symbol=symbol2,exchange='BINANCE',interval=Interval.in_daily,n_bars=1000)

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

    if (df2rsi > df2rsi_1 and df2rsi > 60) & ((df2volume > df2volume_1*3) | (df2volume_1 > df2volume_2*3)):
        send_msg(symbol2 + ' için günlükte VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(df2son_kapanis) + '\n' + 'Önceki Değer: ' + str(df2onceki_kapanis))

    if (df2rsi < df2rsi_1 and df2rsi < 60) & (df2['close'].iloc[-1] < df2['close'].iloc[-2]) & ((df2volume > df2volume_1*3)):
        send_msg(symbol2 + ' için günlükte VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(df2son_kapanis) + '\n' + 'Önceki Değer: ' + str(df2onceki_kapanis))

for symbol3 in symbol_list_3:

    df3 = tv.get_hist(symbol=symbol3,exchange='BIST',interval=Interval.in_daily,n_bars=1000)

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

    if (df3rsi > df3rsi_1 and df3rsi > 60) & ((df3volume > df3volume_1*3) | (df3volume_1 > df3volume_2*3)):
        send_msg(symbol3 + ' için günlükte VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(df3son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3onceki_kapanis))

    if (df3rsi < df3rsi_1 and df3rsi < 60) & (df3['close'].iloc[-1] < df3['close'].iloc[-2]) & ((df3volume > df3volume_1*3)):
        send_msg(symbol3 + ' için günlükte VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(df3son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3onceki_kapanis))

for symbol4 in symbol_list_4:

    df4 = tv.get_hist(symbol=symbol4,exchange='BIST',interval=Interval.in_daily,n_bars=1000)

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

    if (df4rsi > df4rsi_1 and df4rsi > 60) & ((df4volume > df4volume_1*3) | (df4volume_1 > df4volume_2*3)):
        send_msg(symbol4 + ' için günlükte VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(df4son_kapanis) + '\n' + 'Önceki Değer: ' + str(df4onceki_kapanis))

    if (df4rsi < df4rsi_1 and df4rsi < 60) & (df4['close'].iloc[-1] < df4['close'].iloc[-2]) & ((df4volume > df4volume_1*3)):
        send_msg(symbol4 + ' için günlükte VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(df4son_kapanis) + '\n' + 'Önceki Değer: ' + str(df4onceki_kapanis))