# encoding=utf-8

# 三人斗地主手牌规则：
# 一副牌 54 张（4 种花色各 13 张，大小王），一人 17 张，留 3 张做底牌。

# 要求：
# 将一副牌随机打乱（洗牌）后分配给 3 位玩家（发牌），输出每个人的手牌和剩余底牌。
# 可使用 list 和 random 完成。

import random

color = ["红桃","黑桃","方片","梅花"]
num = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
other = ["大王","小王"]

cards = []
for i in range(len(num)):
    for j in range(len(color)):
        cards.append("".join(color[j]+num[i]))
cards = cards + other

random.shuffle(cards) # 洗牌
print str(cards).decode('string_escape')

p1 = []
p2 = []
p3 = []

# 每次取出3张牌，给每人分1张
for loop in range(17):
    card = random.sample(cards,3)
    p1.append(card[0])
    p2.append(card[1])
    p3.append(card[2])
    cards.remove(card[0])
    cards.remove(card[1])
    cards.remove(card[2])

print str(p1).decode('string_escape')
print str(p2).decode('string_escape')
print str(p3).decode('string_escape')
print str(cards).decode('string_escape')