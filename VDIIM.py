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

print(df.head())