from os import dup

    
def duplicate(duplilist):
    mainlist = []
    for i in duplilist:
        if i not in mainlist:
            mainlist.append(i)
    return mainlist

lst = [1,3,2,4,2,3,5,3,34,3,4,1,5,6]
print("Orignal list :",lst)

duplilist = lst
print("duplicate removed list :",duplicate(duplilist))