from sklearn.preprocessing import MinMaxScaler

data = [4,3,5,3,8]

scaler = MinMaxScaler()
new_data = scaler.fit_transform(data)


from sklearn.preprocessing import MinMaxScaler
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
scaler = MinMaxScaler()
print(scaler.fit(data))
print(scaler.data_max_)
print(scaler.transform(data))
print(scaler.transform([[2, 2]]))