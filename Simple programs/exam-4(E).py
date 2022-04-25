# (A)
lst = [1,4,9,16,25,36,49,64,81,100]
lst = [num for num in lst if num %2 == 0]
print(lst)


# (B)
lst = [1,2,3,4,5,6,7,8,9,10]
even_sq, odd_sq = [], []
for i in lst:
    lst = (even_sq if i%2==0 else odd_sq).append(i*i)
print(odd_sq)