#ISANUR SARDAR
data = [115,55,1,23,5,51,2]

for i in range(len(data)-1):
  for ind in range(len(data)-1):
    fst_el = data[ind]
    snd_el = data[ind + 1]
    if fst_el > snd_el :
      data[ind] = snd_el
      data[ind + 1] = fst_el
    else:
      pass

print(data)
