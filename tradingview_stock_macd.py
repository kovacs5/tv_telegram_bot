from tvDatafeed import TvDatafeed, Interval
import requests
from ta.trend import macd, macd_signal
import pandas_ta as pandas_ta

def send_msg(text):
    url_req = 'https://api.telegram.org/bot5670518697:AAH3AEzOSUpoqbHH4InuQL4KWGaI4YN_7-I/sendMessage?chat_id=1592879913&text=' + text
    results = requests.get(url_req).json()
    return results

tv = TvDatafeed()

symbol_list = ['THYAO','TTKOM','SISE','BIENY','MERCN','KLKIM','DZGYO','CRFSA','KONTR','DOAS','ENERY','GESAN','ENKAI','TMSN','ZOREN','KONKA','KOPOL','GSDHO']
symbol_list_2 = ['RAYSG','YEOTK','KCAER','TRCAS','BERA','CEMAS','METRO','KATMR','ADESE','EUPWR','KLSER','GWIND','GOKNR','SMRTG','HUNER','OYAKC','BRLSM','CANTE']

for symbol in symbol_list:

    df = tv.get_hist(symbol=symbol,exchange='BIST',interval=Interval.in_4_hour,n_bars=1000)

    if(len(df) > 700):

        # Calculate short-term and long-term moving averages
        macd_1 = macd(df['close'],window_slow=26,window_fast=12)
        macd_signal_1 = macd_signal(df['close'],window_slow=26,window_fast=12,window_sign=9)

        df['macd'] = macd_1
        df['signal'] = macd_signal_1

        son_kapanis = df['close'].iloc[-1]
        onceki_kapanis = df['close'].iloc[-2]

        macd_son = df['macd'].iloc[-1]
        macd_son_1 = df['macd'].iloc[-2]
        macd_son_2 = df['macd'].iloc[-3]
        signal_son = df['signal'].iloc[-1]
        signal_son_1 = df['signal'].iloc[-2]
        signal_son_2 = df['signal'].iloc[-3]

        if ((macd_son > signal_son and macd_son_1 < signal_son_1) | (macd_son > signal_son and macd_son_2 < signal_son_2)):
            send_msg(symbol + ' için 4 saatlikte MACD CROSS al sinyali 🟢\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

        elif ((macd_son < signal_son and macd_son_1 > signal_son_1) | (macd_son < signal_son and macd_son_2 > signal_son_2)):
            send_msg(symbol + ' için 4 saatlikte MACD CROSS sat sinyali 🔴\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

        ########################################################################

        sma_50 = pandas_ta.sma(df['close'],50)
        sma_200 = pandas_ta.sma(df['close'],200)

        df['sma_50'] = sma_50
        df['sma_200'] = sma_200

        sma_50_son = df['sma_50'].iloc[-1]
        sma_50_son_1 = df['sma_50'].iloc[-2]
        sma_50_son_2 = df['sma_50'].iloc[-3]
        sma_200_son = df['sma_200'].iloc[-1]
        sma_200_son_1 = df['sma_200'].iloc[-2]
        sma_200_son_2 = df['sma_200'].iloc[-3]

        if ((sma_50_son > sma_200_son and sma_50_son_1 < sma_200_son_1) | (sma_50_son > sma_200_son and sma_50_son_2 < sma_200_son_2)):
            send_msg(symbol + ' için 4 saatlikte GOLDEN CROSS al sinyali 🟢\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

        elif ((sma_50_son < sma_200_son and sma_50_son_1 > sma_200_son_1) | (sma_50_son < sma_200_son and sma_50_son_2 > sma_200_son_2)):
            send_msg(symbol + ' için 4 saatlikte GOLDEN CROSS sat sinyali 🔴\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

        print(df.tail(1))

    else:
        print(symbol + ' için yeterli veri yok.')

for symbol3 in symbol_list_2:

    df3 = tv.get_hist(symbol=symbol3,exchange='BIST',interval=Interval.in_4_hour,n_bars=1000)

    if(len(df3) > 700):

        # Calculate short-term and long-term moving averages
        macd_1_df3 = macd(df3['close'],window_slow=26,window_fast=12)
        macd_signal_1_df3 = macd_signal(df3['close'],window_slow=26,window_fast=12,window_sign=9)

        df3['macd'] = macd_1_df3
        df3['signal'] = macd_signal_1_df3

        df3_son_kapanis = df3['close'].iloc[-1]
        df3_onceki_kapanis = df3['close'].iloc[-2]

        macd_son_df3 = df3['macd'].iloc[-1]
        macd_son_1_df3 = df3['macd'].iloc[-2]
        macd_son_2_df3 = df3['macd'].iloc[-3]
        signal_son_df3 = df3['signal'].iloc[-1]
        signal_son_1_df3 = df3['signal'].iloc[-2]
        signal_son_2_df3 = df3['signal'].iloc[-3]

        if ((macd_son_df3 > signal_son_df3 and macd_son_1_df3 < signal_son_1_df3) | (macd_son_df3 > signal_son_df3 and macd_son_2_df3 < signal_son_2_df3)):
            send_msg(symbol3 + ' için 4 saatlikte MACD CROSS al sinyali 🟢\n' + 'Anlık Değer: ' + str(df3_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3_onceki_kapanis))

        elif ((macd_son_df3 < signal_son_df3 and macd_son_1_df3 > signal_son_1_df3) | (macd_son_df3 < signal_son_df3 and macd_son_2_df3 > signal_son_2_df3)):
            send_msg(symbol3 + ' için 4 saatlikte MACD CROSS sat sinyali 🔴\n' + 'Anlık Değer: ' + str(df3_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3_onceki_kapanis))

        ########################################################################

        sma_50_df3 = pandas_ta.sma(df3['close'],50)
        sma_200_df3 = pandas_ta.sma(df3['close'],200)

        df3['sma_50'] = sma_50_df3
        df3['sma_200'] = sma_200_df3

        sma_50_df3_son = df3['sma_50'].iloc[-1]
        sma_50_df3_son_1 = df3['sma_50'].iloc[-2]
        sma_50_df3_son_2 = df3['sma_50'].iloc[-3]
        sma_200_df3_son = df3['sma_200'].iloc[-1]
        sma_200_df3_son_1 = df3['sma_200'].iloc[-2]
        sma_200_df3_son_2 = df3['sma_200'].iloc[-3]

        if ((sma_50_df3_son > sma_200_df3_son and sma_50_df3_son_1 < sma_200_df3_son_1) | (sma_50_df3_son > sma_200_df3_son and sma_50_df3_son_2 < sma_200_df3_son_2)):
            send_msg(symbol3 + ' için 4 saatlikte GOLDEN CROSS al sinyali 🟢\n' + 'Anlık Değer: ' + str(df3_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3_onceki_kapanis))

        elif ((sma_50_df3_son < sma_200_df3_son and sma_50_df3_son_1 > sma_200_df3_son_1) | (sma_50_df3_son < sma_200_df3_son and sma_50_df3_son_2 > sma_200_df3_son_2)):
            send_msg(symbol3 + ' için 4 saatlikte GOLDEN CROSS sat sinyali 🔴\n' + 'Anlık Değer: ' + str(df3_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3_onceki_kapanis))

        print(df3.tail(1))

    else:
        print(symbol3 + ' için yeterli veri yok.')
