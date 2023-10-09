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

sembol_listesi = [symbol_list, symbol_list_2]
intervals = [Interval.in_5_minute, Interval.in_15_minute, Interval.in_30_minute]

for interval in intervals:
    for semboller in sembol_listesi:
        for symbol in semboller:

            df = tv.get_hist(symbol=symbol,exchange='BINANCE',interval=interval,n_bars=1000)

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

            if interval == Interval.in_5_minute:
                interval_text = "5 dakikalıkta"
                carpan = 6

            if interval == Interval.in_15_minute:
                interval_text = "15 dakikalıkta"
                carpan = 5

            if interval == Interval.in_30_minute:
                interval_text = "30 dakikalıkta"
                carpan = 5

            if (rsi > rsi_1 and rsi > 60) & ((volume > volume_1*carpan)):
                send_msg(symbol + ' için ' + interval_text + ' VOLUME PUMP 🟢\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

            if (rsi < rsi_1 and rsi < 60) & (df['close'].iloc[-1] < df['close'].iloc[-2]) & ((volume > volume_1*carpan)):
                send_msg(symbol + ' için ' + interval_text + ' VOLUME DUMP 🔴\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

