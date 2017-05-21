# encoding=utf-8

# 在微信发群红包，设定了总金额和总人数之后，每个人能抢到多少红包是随机的。
# 要求：使用函数模拟一个随机分配红包的方法

from random import randint

def redpacket(money,people):
    result = []
    while people>1:
        people -= 1
        m = randint(1,money)
        money -= m
        result.append(m/100.0)
    if people == 1:
        m = money
        result.append(m/100.0)
    return result

try:
    money = float(raw_input("请输入红包总金额（元）："))
    people = int(raw_input("请输入红包个数："))

    if money <= 0 or people <=0:
        print "输入有误"
    elif money < people/10.0:
        print "每人需至少有一分钱"
    else:
        print redpacket(money*100,people)
except Exception,e:
    print "请输入数字"

