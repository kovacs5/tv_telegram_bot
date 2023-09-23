from tvDatafeed import TvDatafeed, Interval
import requests
from ta.trend import macd, macd_signal

def send_msg(text):
    url_req = 'https://api.telegram.org/bot5670518697:AAH3AEzOSUpoqbHH4InuQL4KWGaI4YN_7-I/sendMessage?chat_id=1592879913&text=' + text
    results = requests.get(url_req).json()
    return results

tv = TvDatafeed()

symbol_list = ['THYAO','TTKOM','SISE','BIENY','MERCN','KLKIM','DZGYO','CRFSA','KONTR','DOAS','ENERY','GESAN','ENKAI','TMSN','ZOREN','KONKA','KOPOL','GSDHO']
symbol_list_2 = ['RAYSG','YEOTK','KCAER','TRCAS','BERA','CEMAS','METRO','KATMR','ADESE','EUPWR','KLSER','GWIND','GOKNR','SMRTG','HUNER','OYAKC','BRLSM','CANTE']

for symbol in symbol_list:

    df = tv.get_hist(symbol=symbol,exchange='BIST',interval=Interval.in_4_hour,n_bars=1000)

    # Calculate short-term and long-term moving averages
    macd_1 = macd(df['close'],window_slow=26,window_fast=12)
    macd_signal_1 = macd_signal(df['close'],window_slow=26,window_fast=12,window_sign=9)

    df['macd'] = macd_1
    df['signal'] = macd_signal_1

    macd_son = df['macd'].iloc[-1]
    macd_son_1 = df['macd'].iloc[-2]
    macd_son_2 = df['macd'].iloc[-3]
    signal_son = df['signal'].iloc[-1]
    signal_son_1 = df['signal'].iloc[-2]
    signal_son_2 = df['signal'].iloc[-3]

    if ((macd_son > signal_son and macd_son_1 < signal_son_1) | (macd_son > signal_son and macd_son_2 < signal_son_2)):
        send_msg(symbol + ' için 4 saatlikte MACD CROSS al sinyali 🟢')

    elif ((macd_son < signal_son and macd_son_1 > signal_son_1) | (macd_son < signal_son and macd_son_2 > signal_son_2)):
        send_msg(symbol + ' için 4 saatlikte MACD CROSS sat sinyali 🔴')

    print(df.tail(1))

for symbol3 in symbol_list_2:

    df3 = tv.get_hist(symbol=symbol3,exchange='BIST',interval=Interval.in_4_hour,n_bars=1000)

    # Calculate short-term and long-term moving averages
    macd_1_df3 = macd(df3['close'],window_slow=26,window_fast=12)
    macd_signal_1_df3 = macd_signal(df3['close'],window_slow=26,window_fast=12,window_sign=9)

    df3['macd'] = macd_1_df3
    df3['signal'] = macd_signal_1_df3

    macd_son_df3 = df3['macd'].iloc[-1]
    macd_son_1_df3 = df3['macd'].iloc[-2]
    macd_son_2_df3 = df3['macd'].iloc[-3]
    signal_son_df3 = df3['signal'].iloc[-1]
    signal_son_1_df3 = df3['signal'].iloc[-2]
    signal_son_2_df3 = df3['signal'].iloc[-3]

    if ((macd_son_df3 > signal_son_df3 and macd_son_1_df3 < signal_son_1_df3) | (macd_son_df3 > signal_son_df3 and macd_son_2_df3 < signal_son_2_df3)):
        send_msg(symbol3 + ' için 4 saatlikte MACD CROSS al sinyali 🟢')

    elif ((macd_son_df3 < signal_son_df3 and macd_son_1_df3 > signal_son_1_df3) | (macd_son_df3 < signal_son_df3 and macd_son_2_df3 > signal_son_2_df3)):
        send_msg(symbol3 + ' için 4 saatlikte MACD CROSS sat sinyali 🔴')

    print(df3.tail(1))
