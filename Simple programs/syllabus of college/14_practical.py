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