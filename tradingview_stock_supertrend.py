from tvDatafeed import TvDatafeed, Interval
import requests

def send_msg(text):
    url_req = 'https://api.telegram.org/bot5670518697:AAH3AEzOSUpoqbHH4InuQL4KWGaI4YN_7-I/sendMessage?chat_id=1592879913&text=' + text
    results = requests.get(url_req).json()
    return results

tv = TvDatafeed()

symbol_list = ['THYAO','TTKOM','SISE','BIENY','MERCN','KLKIM','DZGYO','CRFSA','KONTR','DOAS','ENERY','GESAN','ENKAI','TMSN','ZOREN','KONKA','KOPOL','GSDHO']

for symbol in symbol_list:

    df = tv.get_hist(symbol=symbol,exchange='BIST',interval=Interval.in_4_hour,n_bars=1000)

    # Define SuperTrend parameters
    period = 7
    multiplier = 3

    # Calculate the SuperTrend indicator
    def calculate_super_trend(data, period, multiplier):
        data['ATR'] = data['high'] - data['low']
        data['ATR'] = data['ATR'].rolling(period).mean()
        data['UpperBand'] = data['high'] - multiplier * data['ATR']
        data['LowerBand'] = data['low'] + multiplier * data['ATR']
        data['Trend'] = 1

        for i in range(1, len(data)):
            if data['close'][i] > data['UpperBand'][i - 1]:
                data['Trend'].copy()[i] = -1.
                data['LowerBand'].copy()[i] = data['UpperBand'].copy()[i]
            elif data['close'][i] < data['LowerBand'][i - 1]:
                data['Trend'].copy()[i] = 1
                data['UpperBand'].copy()[i] = data['LowerBand'].copy()[i]
            else:
                data['Trend'].copy()[i] = data['Trend'].copy()[i - 1]
                if data['Trend'].copy()[i] == 1:
                    data['LowerBand'].copy()[i] = data['LowerBand'].copy()[i - 1]
                else:
                    data['UpperBand'].copy()[i] = data['UpperBand'].copy()[i - 1]

        data['SuperTrend'] = data['UpperBand'] if data['Trend'][len(data) - 1] == 1 else data['LowerBand']

        return data

    # Calculate the SuperTrend for the stock data
    df = calculate_super_trend(df, period, multiplier)


    supertrend = df['SuperTrend']
    son_supertrend_deger = supertrend.iloc[-1]
    onceki_supertrend_deger = supertrend.iloc[-2]

    son_kapanis = df['close'].iloc[-1]
    onceki_kapanis = df['close'].iloc[-2]

    # renk yeşile dönüyor, trend yükselişe geçti
    if son_kapanis > son_supertrend_deger and onceki_kapanis < onceki_supertrend_deger:
        send_msg(symbol + ' için AL sinyali 🟢')

    # renk kırmızıya dönüyor, trend düşüşe geçti
    if son_kapanis < son_supertrend_deger and onceki_kapanis > onceki_supertrend_deger:
        send_msg(symbol + ' için SAT sinyali 🔴')

    print(symbol + ' taranıyor...')