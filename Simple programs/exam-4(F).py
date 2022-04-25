d = {"1":["a","b"], "2":["c","d"]}
new = list(d.values())
for i in new[0]:
  for j in new[1]:
    print(i+j)