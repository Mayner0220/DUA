import pandas as pd

train_data = pd.read_csv("./dataset/train.csv", encoding="euc-kr")
train_data["DateTime"] = pd.to_datetime(train_data.DateTime)
train_data["date"] = train_data.DateTime.dt.date
train_data = train_data("data").sum().reset_index()