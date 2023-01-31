def to_hex(num):
    '''function to convert numbers from base 10 to base 16'''
    num_list = []
    while num >= 16:
        mod_num = num % 16
        num_list.append(mod_num)
        num = int((num - mod_num) / 16)
    num_list.append(num)
    num_out = ''
    for i in reversed(num_list):
        if i > 9:
            i_out = "ABCDEF"[i - 10]
        else:
            i_out = str(i)
        num_out = num_out + i_out
    return num_out


if __name__ == '__main__':
    num_in = input("Number to convert: ")
    num_hex = to_hex(int(num_in))
    print(num_hex)
