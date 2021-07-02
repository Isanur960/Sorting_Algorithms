#ISANUR SARADR
data = [1,98,868,87,84,74,98,84,841,8,89,47,25,64,813,5247]

l = len(data)

for i in range(1,l):
  while data[i] < data[i - 1] and i != 0 :
    data[i], data[i - 1] = data[i - 1], data[i]
    i = i - 1

print(data)
