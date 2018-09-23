# 问题一：字符串排序

s = "hello world"

# 请编写代码，将 s 以 [a-z] 顺序输出

# 问题二：数值比较

n = [9, 15, 23, 89, 33, 26, 2, 76]

# 请编写代码，找出数组中的最大数与最小数

# 问题三：替换

a = "i,am,a,student,in,chengdu"

# 请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
# 通过参数输入打印出完整的句子


def fun_1(s):
    s = list(s)
    s.sort()
    return ''.join(s)


def fun_2(n):
    return max(n), min(n)


def fun_3(a):
    a_list = a.split(',')
    identity = input('identity:')
    city = input('city:')
    a_list[3] = identity
    a_list[-1] = city
    return ','.join(a_list)


if __name__ == '__main__':
    print(fun_1(s))
    print(fun_2(n))
    print(fun_3(a))