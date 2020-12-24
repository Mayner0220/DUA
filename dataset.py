import pandas as pd

train_data = pd.read_csv("./dataset/train.csv", encoding="euc-kr")
train_data["DateTime"] = pd.to_datetime(train_data.DateTime)
train_data["date"] = train_data.DateTime.dt.date
train  = train_data.groupby("date").sum().reset_index()

mini = train_data.iloc[:, 1:].min()
size = train_data.iloc[:,1:].max() - train_data.iloc[:,1:].min()
train_data.iloc[:,1:] = (train_data.iloc[:,1:] -  mini) / size

