from tvDatafeed import TvDatafeed, Interval
import requests
import pandas_ta as pandas_ta
from ta.trend import macd, macd_signal
from ta.momentum import RSIIndicator
from ta.trend import sma_indicator


def send_msg(text):
    url_req = 'https://api.telegram.org/bot5670518697:AAH3AEzOSUpoqbHH4InuQL4KWGaI4YN_7-I/sendMessage?chat_id=1592879913&text=' + text
    results = requests.get(url_req).json()
    return results

tv = TvDatafeed()

symbol_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'NEOUSDT', 'INJUSDT', 'SOLUSDT', 'MASKUSDT', 'DOTUSDT', 'MATICUSDT', 'LTCUSDT', 'LINKUSDT']
symbol_list_2 = ['XMRUSDT', 'ATOMUSDT', 'TRBUSDT', 'EOSUSDT', 'RNDRUSDT', 'UNIUSDT', 'FILUSDT', 'ANTUSDT', 'BURGERUSDT', 'AAVEUSDT', 'UNFIUSDT', 'FRONTUSDT']
symbol_list_3 = ['TOTAL', 'TOTAL2', 'TOTAL3']

sembol_listesi = [symbol_list, symbol_list_2]

for semboller in sembol_listesi:

    for symbol in semboller:

        df = tv.get_hist(symbol=symbol,exchange='BINANCE',interval=Interval.in_daily,n_bars=1000)
        fast = 8
        slow = 16
        signal = 11
        
        # Calculate short-term and long-term moving averages
        macd_value = macd(df['close'],slow,fast)
        df['macd'] = macd_value
        signal_value = pandas_ta.sma(macd_value,signal)
        df['signal'] = signal_value

        son_kapanis = df['close'].iloc[-1]
        onceki_kapanis = df['close'].iloc[-2]

        macd_son = df['macd'].iloc[-1]
        macd_son_1 = df['macd'].iloc[-2]
        signal_son = df['signal'].iloc[-1]
        signal_son_1 = df['signal'].iloc[-2]

        df['rsi'] = RSIIndicator(df['close'], window=14).rsi()

        rsi = df['rsi'].iloc[-1]
        rsi_1 = df['rsi'].iloc[-2]

        if((macd_son > signal_son and macd_son_1 < signal_son_1) & (rsi > rsi_1)):
            send_msg('⚡ ' + symbol + ' için günlükte MACD CROSS ve RSI YUKARI 🟢\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

        if((macd_son < signal_son and macd_son_1 > signal_son_1) & (rsi < rsi_1)):
            send_msg('⚡ ' + symbol + ' için günlükte MACD CROSS ve RSI AŞAĞI 🔴\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

for df2semboller in sembol_listesi:

    for symbol2 in df2semboller:

        df2 = tv.get_hist(symbol=symbol2,exchange='BINANCE',interval=Interval.in_4_hour,n_bars=1000)
        df2fast = 8
        df2slow = 16
        df2signal = 11
        
        # Calculate short-term and long-term moving averages
        df2macd_value = macd(df2['close'],df2slow,df2fast)
        df2['macd'] = df2macd_value
        df2signal_value = pandas_ta.sma(df2macd_value,df2signal)
        df2['signal'] = signal_value

        df2son_kapanis = df2['close'].iloc[-1]
        df2onceki_kapanis = df2['close'].iloc[-2]

        df2macd_son = df2['macd'].iloc[-1]
        df2macd_son_1 = df2['macd'].iloc[-2]
        df2signal_son = df2['signal'].iloc[-1]
        df2signal_son_1 = df2['signal'].iloc[-2]

        df2['rsi'] = RSIIndicator(df2['close'], window=14).rsi()

        df2rsi = df2['rsi'].iloc[-1]
        df2rsi_1 = df2['rsi'].iloc[-2]

        if((df2macd_son > df2signal_son and df2macd_son_1 < df2signal_son_1) & (df2rsi > df2rsi_1)):
            send_msg('⚡ ' + symbol2 + ' için 4 saatlikte MACD CROSS ve RSI YUKARI 🟢\n' + 'Anlık Değer: ' + str(df2son_kapanis) + '\n' + 'Önceki Değer: ' + str(df2onceki_kapanis))

        if((df2macd_son < df2signal_son and df2macd_son_1 > df2signal_son_1) & (df2rsi < df2rsi_1)):
            send_msg('⚡ ' + symbol2 + ' için 4 saatlikte MACD CROSS ve RSI AŞAĞI 🔴\n' + 'Anlık Değer: ' + str(df2son_kapanis) + '\n' + 'Önceki Değer: ' + str(df2onceki_kapanis))

intervals = [Interval.in_daily, Interval.in_4_hour]

for interval in intervals:

    for symbol3 in symbol_list_3:

        df3 = tv.get_hist(symbol=symbol3,exchange='CRYPTOCAP',interval=interval,n_bars=1000)
        df3fast = 8
        df3slow = 16
        df3signal = 11
        
        # Calculate short-term and long-term moving averages
        df3macd_value = macd(df3['close'],df3slow,df3fast)
        df3['macd'] = df3macd_value
        df3signal_value = pandas_ta.sma(df3macd_value,df3signal)
        df3['signal'] = signal_value

        df3son_kapanis = df3['close'].iloc[-1]
        df3onceki_kapanis = df3['close'].iloc[-2]

        df3macd_son = df3['macd'].iloc[-1]
        df3macd_son_1 = df3['macd'].iloc[-2]
        df3signal_son = df3['signal'].iloc[-1]
        df3signal_son_1 = df3['signal'].iloc[-2]

        df3['rsi'] = RSIIndicator(df3['close'], window=14).rsi()

        df3rsi = df3['rsi'].iloc[-1]
        df3rsi_1 = df3['rsi'].iloc[-2]

        if interval == Interval.in_daily:
            interval_text = "günlükte"

        if interval == Interval.in_4_hour:
            interval_text = "4 saatlikte"

        if((df3macd_son > df3signal_son and df3macd_son_1 < df3signal_son_1) & (df3rsi > df3rsi_1)):
            send_msg(symbol3 + ' için ' + interval_text + ' MACD CROSS ve RSI YUKARI 🟢\n' + 'Anlık Değer: ' + str(df3son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3onceki_kapanis))

        if((df3macd_son < df3signal_son and df3macd_son_1 > df3signal_son_1) & (df3rsi < df3rsi_1)):
            send_msg(symbol3 + ' için ' + interval_text + ' MACD CROSS ve RSI AŞAĞI 🔴\n' + 'Anlık Değer: ' + str(df3son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3onceki_kapanis))