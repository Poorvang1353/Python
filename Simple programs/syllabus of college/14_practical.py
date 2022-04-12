from pip import main


def duplicate(dupli_list):
    main_list = []
    for i in dupli_list:
        if i not in main_list:
            main_list.append(i)
    return main_list

lst = [1,2,3,2,5,3,2,7,3,6]
print("Origenal list: ", lst)
dupli_list = lst

print("Duplicates Removed list: ",duplicate(dupli_list))




# #self practice
# #this one uses loop 
# def using_loop(x):
#   num = []
#   for i in x:
#     if i not in num:
#       num.append(i)
#   return num

# #this one uses sets
# def using_set(x):
#     return list(set(x))

# lst = [1,2,3,4,3,2,1]
# print (lst)
# print ("Remove repeted numbers using loop: ",using_loop(lst))
# print ("Remove repeted numbers using set: ",using_set(lst))