values = [1,2,3]
def shift(list):
    new_list=[]

    for i in list:
        new_list.insert(len(new_list)-1,i)
    return new_list

print(shift(values))