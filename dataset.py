import pandas as pd
import numpy as np

train_data = pd.read_csv("./dataset/train.csv", encoding="euc-kr")
train_data["DateTime"] = pd.to_datetime(train_data.DateTime)
train_data["date"] = train_data.DateTime.dt.date
train_data = train_data.groupby("date").sum().reset_index()

mini = train_data.iloc[:, 1:].min()
size = train_data.iloc[:,1:].max() - train_data.iloc[:,1:].min()
train_data.iloc[:,1:] = (train_data.iloc[:,1:] -  mini) / size

input_window = 30
output_window = 7

window_x = np.zeros((train_data.shape[0] - (input_window + output_window), input_window, 4))
window_y = np.zeros((train_data.shape[0] - (input_window + output_window), output_window, 4))

for start in range(train_data.shape[0] - (input_window + output_window)):
    end = start + input_window
    window_x[start, :, :] = train_data.iloc[start : end, 1:].values
    window_y[start, :, :] = train_data.iloc[end : end + output_window, 1:].values