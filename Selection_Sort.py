#ISANUR SARDAR
data = [5, 1521, 5, 4, 84, 419, 67, 2, 1, 184, 466, 532,1]

l = len(data)

for i in range(l):
  in_ind = i
  in_data = data[i]
  for ind in range(i, l -1):
    if in_data > data[ind + 1]:
      in_data = data[ind + 1]
      data[i] , data[ind + 1] = data[ind + 1] , data[i]
    else:
      pass

print(data)
