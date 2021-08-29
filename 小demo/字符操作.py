#coding=utf-8
from collections import Counter

# 获取字符串的字符个数统计结果
class string_sta:
    def __init__(self, string) -> None:
        self.strings = string
        self.result = Counter(self.strings)

    def sta_print(self):
        print(self.result.most_common())

        # 获取统计结果中出现次数为1的字符
        print(''.join([i[0] for i in self.result.items() if i[1]==1]))

str = string_sta('afgdsfgkjfklsahdfuihaerjghulsihgi')
str.sta_print()

# 带符号十六进制转化为十进制
def get_int_by_0x(str):
    width=32  # 16进制数所占位数
    dec_data=int(str, 16)
    if dec_data > 2 ** (width-1)- 1:
        dec_data = 2 ** width-dec_data
        dec_data = 0 - dec_data
    return dec_data
print(get_int_by_0x('0xffffffff'))