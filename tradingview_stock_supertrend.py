from tvDatafeed import TvDatafeed, Interval
import requests
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

    # Define SuperTrend parameters
    period = 10
    multiplier = 3

    supertrend = pandas_ta.supertrend(df['high'],df['low'],df['close'],period,multiplier)

    df['supertrend'] = supertrend['SUPERT_10_3.0']
    
    son_supertrend_deger = df['supertrend'].iloc[-1]
    onceki_supertrend_deger = df['supertrend'].iloc[-2]

    son_kapanis = df['close'].iloc[-1]
    onceki_kapanis = df['close'].iloc[-2]
    
    # renk yeşile dönüyor, trend yükselişe geçti
    if (son_kapanis > son_supertrend_deger and onceki_kapanis < onceki_supertrend_deger) | (son_kapanis > onceki_supertrend_deger and onceki_kapanis < onceki_supertrend_deger):
        send_msg(symbol + ' için 4 saatlikte Supertrend AL sinyali 🟢\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))

    # renk kırmızıya dönüyor, trend düşüşe geçti
    if (son_kapanis < son_supertrend_deger and onceki_kapanis > onceki_supertrend_deger) | (son_kapanis < onceki_supertrend_deger and onceki_kapanis > onceki_supertrend_deger):
        send_msg(symbol + ' için 4 saatlikte Supertrend SAT sinyali 🔴\n' + 'Anlık Değer: ' + str(son_kapanis) + '\n' + 'Önceki Değer: ' + str(onceki_kapanis))
    
    print(df.tail(1))

for symbol2 in symbol_list:

    df2 = tv.get_hist(symbol=symbol2,exchange='BIST',interval=Interval.in_1_hour,n_bars=1000)

    # Define SuperTrend parameters
    df2_period = 10
    df2_multiplier = 3

    df2_supertrend = pandas_ta.supertrend(df2['high'],df2['low'],df2['close'],df2_period,df2_multiplier)

    df2['supertrend'] = df2_supertrend['SUPERT_10_3.0']
    
    df2_son_supertrend_deger = df2['supertrend'].iloc[-1]
    df2_onceki_supertrend_deger = df2['supertrend'].iloc[-2]

    df2_son_kapanis = df2['close'].iloc[-1]
    df2_onceki_kapanis = df2['close'].iloc[-2]
    
    # renk yeşile dönüyor, trend yükselişe geçti
    if (df2_son_kapanis > df2_son_supertrend_deger and df2_onceki_kapanis < df2_onceki_supertrend_deger) | (df2_son_kapanis > df2_onceki_supertrend_deger and df2_onceki_kapanis < df2_onceki_supertrend_deger):
        send_msg(symbol2 + ' için 1 saatlikte Supertrend AL sinyali 🟢\n' + 'Anlık Değer: ' + str(df2_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df2_onceki_kapanis))

    # renk kırmızıya dönüyor, trend düşüşe geçti
    if (df2_son_kapanis < df2_son_supertrend_deger and df2_onceki_kapanis > df2_onceki_supertrend_deger) | (df2_son_kapanis < df2_onceki_supertrend_deger and df2_onceki_kapanis > df2_onceki_supertrend_deger):
        send_msg(symbol2 + ' için 1 saatlikte Supertrend SAT sinyali 🔴\n' + 'Anlık Değer: ' + str(df2_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df2_onceki_kapanis))
    
    print(df2.tail(1))

for symbol3 in symbol_list_2:

    df3 = tv.get_hist(symbol=symbol3,exchange='BIST',interval=Interval.in_4_hour,n_bars=1000)

    # Define SuperTrend parameters
    df3_period = 10
    df3_multiplier = 3

    df3_supertrend = pandas_ta.supertrend(df3['high'],df3['low'],df3['close'],df3_period,df3_multiplier)

    df3['supertrend'] = df3_supertrend['SUPERT_10_3.0']
    
    df3_son_supertrend_deger = df3['supertrend'].iloc[-1]
    df3_onceki_supertrend_deger = df3['supertrend'].iloc[-2]

    df3_son_kapanis = df3['close'].iloc[-1]
    df3_onceki_kapanis = df3['close'].iloc[-2]
    
    # renk yeşile dönüyor, trend yükselişe geçti
    if (df3_son_kapanis > df3_son_supertrend_deger and df3_onceki_kapanis < df3_onceki_supertrend_deger) | (df3_son_kapanis > df3_onceki_supertrend_deger and df3_onceki_kapanis < df3_onceki_supertrend_deger):
        send_msg(symbol3 + ' için 4 saatlikte Supertrend AL sinyali 🟢\n' + 'Anlık Değer: ' + str(df3_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3_onceki_kapanis))

    # renk kırmızıya dönüyor, trend düşüşe geçti
    if (df3_son_kapanis < df3_son_supertrend_deger and df3_onceki_kapanis > df3_onceki_supertrend_deger) | (df3_son_kapanis < df3_onceki_supertrend_deger and df3_onceki_kapanis > df3_onceki_supertrend_deger):
        send_msg(symbol3 + ' için 4 saatlikte Supertrend SAT sinyali 🔴\n' + 'Anlık Değer: ' + str(df3_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df3_onceki_kapanis))
    
    print(df3.tail(1))

for symbol4 in symbol_list_2:

    df4 = tv.get_hist(symbol=symbol4,exchange='BIST',interval=Interval.in_1_hour,n_bars=1000)

    # Define SuperTrend parameters
    df4_period = 10
    df4_multiplier = 3

    df4_supertrend = pandas_ta.supertrend(df4['high'],df4['low'],df4['close'],df4_period,df4_multiplier)

    df4['supertrend'] = df4_supertrend['SUPERT_10_3.0']
    
    df4_son_supertrend_deger = df4['supertrend'].iloc[-1]
    df4_onceki_supertrend_deger = df4['supertrend'].iloc[-2]

    df4_son_kapanis = df4['close'].iloc[-1]
    df4_onceki_kapanis = df4['close'].iloc[-2]
    
    # renk yeşile dönüyor, trend yükselişe geçti
    if (df4_son_kapanis > df4_son_supertrend_deger and df4_onceki_kapanis < df4_onceki_supertrend_deger) | (df4_son_kapanis > df4_onceki_supertrend_deger and df4_onceki_kapanis < df4_onceki_supertrend_deger):
        send_msg(symbol4 + ' için 1 saatlikte Supertrend AL sinyali 🟢\n' + 'Anlık Değer: ' + str(df4_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df4_onceki_kapanis))

    # renk kırmızıya dönüyor, trend düşüşe geçti
    if (df4_son_kapanis < df4_son_supertrend_deger and df4_onceki_kapanis > df4_onceki_supertrend_deger) | (df4_son_kapanis < df4_onceki_supertrend_deger and df4_onceki_kapanis > df4_onceki_supertrend_deger):
        send_msg(symbol4 + ' için 1 saatlikte Supertrend SAT sinyali 🔴\n' + 'Anlık Değer: ' + str(df4_son_kapanis) + '\n' + 'Önceki Değer: ' + str(df4_onceki_kapanis))
    
    print(df4.tail(1))
