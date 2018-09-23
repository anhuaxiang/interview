import re
# 使用 while 循环打印 1 3 5 7 9

# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”

l = [1, 5, 7, 8, 9]

# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序

s = "aAsnr3id2d4b6gs7DZsf9e1AF"


def fun_1():
    while True:
        i = 1
        while i < 10:
            yield i
            i += 2


def main_1(max_print):
    count = 0
    for i in fun_1():
        print(i)
        if count > max_print:
            break
        count += 1


def fun_2(l, num):
    flag = 0
    for i in l:
        if i == num:
            flag = 1
            break
    return 'found' if flag else 'not found'
    # return 'found' if num in l else 'not found'


def fun_3(s):
    n_list = re.findall(r'\d', s)
    n_list.sort()

    s_list = re.findall(r'[a-zA-Z]', s)
    s_list = list(map(lambda x: x.lower(), s_list))
    s_list.sort()
    return ''.join(n_list), ''.join(s_list)


if __name__ == '__main__':
    main_1(10)
    print(fun_2(l, 7))
    print(fun_3(s))
