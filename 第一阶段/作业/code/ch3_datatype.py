#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time   : 2019/8/14 下午5:49
# Author : fred


'''练习一'''

name = ' alberT'
# 1 移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 2 判断 name 变量对应的值是否以 "al" 开头,并输出结果
print(name.startswith('al'))
# 3 判断 name 变量对应的值是否以 "T" 结尾,并输出结果
print(name.endswith('T'))
# 4 将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
print(name.replace('l', 'p'))
# 5 将 name 变量对应的值根据 “l” 分割,并输出结果
print(name.split('l'))
# 6 将 name 变量对应的值变大写,并输出结果
print(name.upper())
# 7 将 name 变量对应的值变小写,并输出结果
print(name.lower())
# 8 请输出 name 变量对应的值的第 2 个字符
print(name[2])
# 9 请输出 name 变量对应的值的前 3 个字符
print(name[:3])
# 10 请输出 name 变量对应的值的后 2 个字符
print(name[-2:])
# 11 请输出 name 变量对应的值中 “e” 所在索引位置
print(name.index('e'))
# 12 获取子序列,去掉最后一个字符。如: albert 则获取 alber
print(name[:-1])


'''
练习二

有列表data=['albert',18,[2000,1,1]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量。

'''
data = ['albert', 18, [2000, 1, 1]]
name = data[0]
age = data[1]

year = data[2][0]
month = data[2][1]
day = data[2][2]

print('name:{}, age:{},birth_year:{},birth_month:{}, birth_day:{}'.format(name, age, year, month, day))

''' 
练习三
有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中，即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
'''
dic = {'k1': [], 'k2': []}
data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
for item in data:
    if item > 66:
        dic['k1'].append(item)
    elif item < 66:
        dic['k2'].append(item)

print(dic)

''' 
练习四
1.列表l=['a','b',1,'a','a']，列表元素均为可不可变类型，去重得到新列表,且新列表无需保持列表原来的顺序
2.在上题的基础上，保存列表原来的顺序
3.有如下列表，列表元素为可变类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
'''
l = ['a', 'b', 1, 'a', 'a']

# 1无序去重
print(set(l))

# 2有序去重
l1 = []
for i in l:
    if i not in l:
        l1.append(i)
print(l1)

# 3字典去重
l = [

    {'name': 'albert', 'age': 18, 'sex': 'male'},

    {'name': 'james', 'age': 35, 'sex': 'male'},

    {'name': 'taylor', 'age': 25, 'sex': 'female'},

    {'name': 'albert', 'age': 18, 'sex': 'male'},

    {'name': 'albert', 'age': 18, 'sex': 'male'},

]

def func(items, key=None):
    s = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item


print(list(func(l, key=lambda dic: (dic['name'], dic['age'], dic['sex']))))

'''
练习五
使用至少两种方法统计字符串 s='hello albert albert say hello world world'中每个单词的个数
'''

s = 'hello albert albert say hello world world'

#方法一
dict1 = {}
words = s.split()
for word in words:
    dict1[word] = s.count(word)
print(dict1)

#方法二
dict2 = {}
words = s.split()
for word in words:
    dict2.setdefault(word, s.count(word))

print(dict2)

'''
练习六
实现简易购物程序,要求如下：首先打印商品详细信息，然后请用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入
'''
msg_dic = {
    'apple': 10,
    'tesla': 1000000,
    'mac': 10000,
    'iphone': 8000,
    'chicken': 30,
    'pen': 3,
    'ruler': 5
}

goods_list = []
while True:
    for product, price in msg_dic.items():
        print('product: %s, price: %s' % (product, price))
    choice = input('please choose a product>>:').strip()
    if choice == 'q':
        break
    elif choice not in msg_dic:
        print('The product you choose is invalid')
        continue
    else:
        while True:
            count = input('please input the number of the product you want buy>>:').strip()
            if not count.isdigit():
                print('The count you input is not a number')
                continue
            else:
                goods_list.append((choice, msg_dic[choice], count))
                print('已购买商品：', goods_list)
                break