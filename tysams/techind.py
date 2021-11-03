# Imports
import pandas as pd


def ichimoku_cloud(high, low, close, period1, period2, period3):

    #Tenkan Sen (Conversion Line): (9-period high + 9-period low)/2))
    tenkan_max= high.rolling(window = period1, min_periods = 0).max()
    tenkan_min = low.rolling(window = period1, min_periods = 0).min()
    tenkan_avg = (tenkan_max + tenkan_min) / 2

    #Kijun Sen (Base Line): (26-period high + 26-period low)/2))
    kijun_max = high.rolling(window = period2, min_periods = 0).max()
    kijun_min = low.rolling(window = period2, min_periods = 0).min()
    kijun_avg = (kijun_max + kijun_min) / 2

    #Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2))
    #(Kijun + Tenkan) / 2 Shifted ahead by 26 periods
    senkou_a = ((kijun_avg + tenkan_avg) / 2).shift(period2)

    #Senkou Span B (Leading Span B): (52-period high + 52-period low)/2))
    #52 period High + Low / 2
    senkou_b_max = high.rolling(window = period3, min_periods = 0).max()
    senkou_b_min = low.rolling(window = period3, min_periods = 0).min()
    senkou_b = ((senkou_b_max + senkou_b_min) / 2).shift(period3)

    #Chikou Span (Lagging Span): Close plotted 26 days in the past
    #Current close shifted -26
    chikou = (close).shift(-period2)

    return [tenkan_avg, kijun_avg, senkou_a, senkou_b, chikou]