import pandas as pd
import numpy as np

df = pd.read_csv("Nifty50dataset.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])

df.set_index("timestamp", inplace = True)

df.sort_index(inplace = True)

df = df[["open", "high", "low", "close"]]

df = df.between_time("09:15", "15:30")

df["log_return"] = np.log(df["close"] / df["close"].shift(1))

df.dropna(inplace = True)

# 15 min rolling volatility
df["rolling_vol_15"] = df["log_return"].rolling(window = 15).std()

# intraday candle range
df["intraday_cnadle_range"] = (df["high"] - df["low"]) / df["close"]

# atr (average true range)
df["prev_close"] = df["close"].shift(1)

df["tr1"] = df["high"] - df["low"]
df["tr2"] = abs(df["high"] - df["prev_close"])
df["tr3"] = abs(df["low"] - df["prev_close"])

df["true_range"] = df[["tr1", "tr2", "tr3"]].max(axis = 1)

df["atr_14"] = df["true_range"].rolling(window = 14).mean()

df.drop(columns = ["prev_close", "tr1", "tr2", "tr3"], inplace = True)

print(df[["rolling_vol_15", "atr_14"]].describe())