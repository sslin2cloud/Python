import tool
"""
名片管理系统入口
"""
# 用于保存名片
cards_list = [
    {
        "name": "2",
        "call": "123456789",
        "qq": "111111",
        "email": "111111@qq.com"
    },
    {
        "name": "3",
        "call": "987654321",
        "qq": "222222",
        "email": "222222@qq.com"
    }
]

while True:
    select = tool.card_menu()
    if select == 1:
        name = input("请输入查找姓名:")
        tool.find_card(cards_list, name)
    elif select == 2:
        cards_list = tool.add_card(cards_list)
    elif select == 3:
        name = input("请输入查找姓名:")
        cards_list = tool.del_card(cards_list, name)
    elif select == 3:
        print("退出系统！")
    else:
        print("输入错误！")
