def card_menu():
    """
    菜单
    """
    print("#" * 30)
    print("欢迎进入卡片管理系统！！！")
    print("\t1.查询信息;")
    print("\t2.新建卡片;")
    print("\t3.删除卡片;")
    print("\t4.退出系统;")
    print("#" * 30)
    return int(input("请选择操作："))


def add_card(list):
    """
    添加卡片
    """
    dic = {}
    dic["name"] = input("请输入姓名：")
    dic["call"] = input("请输入电话：")
    dic["qq"] = input("请输入QQ：")
    dic["email"] = input("请输入邮箱：")

    list.append(dic)
    return list


def del_card(list, name):
    """
    删除卡片
    """
    for card in list:
        if card["name"] == name:
            list.remove(card)
            break
    else:
        print("没有这张卡片!")

    return list


def find_card(list, name):
    """
    查询卡片
    """
    for card in list:
        if card["name"] == name:
            print("姓名: %s" % name)
            print("电话: %s" % card["call"])
            print("QQ: %s" % card["qq"])
            print("邮箱: %s" % card["email"])
            break
    else:
        print("没有这张卡片!")
