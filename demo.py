def get_int_by_0x(str):
    width=32  # 16进制数所占位数
    dec_data=int(str, 16)
    if dec_data > 2 ** (width-1)- 1:
        dec_data = 2 ** width-dec_data
        dec_data = 0 - dec_data
    return dec_data
print(get_int_by_0x('0xffffffff'))
