d = {"1":["a","b"], "2":["c","d"]}
new = list(d.values())
for i in new[0]:
  for j in new[1]:
    print(i+j)


# PEART - 2 of practical 12
# L = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# print("Orignal List: ", L)
# u_value = set(val for dic in L for val in dic.values())
# print("Unique values: ", u_value)