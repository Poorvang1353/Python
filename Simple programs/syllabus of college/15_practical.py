def reverse():
    my_string  = 'silver oak university'
    print(my_string[::-1])
    my_list = my_string.split()
    my_reverse_string = " "
    print(my_reverse_string.join(my_list[::-1]))
    return reverse

reverse()