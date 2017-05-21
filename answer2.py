# encoding=utf-8

# BMI 指数，是用体重公斤数除以身高米数平方得出的数字

# BMI < 18.5 体重偏轻
# 18.5 <= BMI < 24 体重正常
# BMI >= 24 体重偏重

# 设计一个BMI计算器吧，看看自己体重是否正常。
# 输入：身高、体重值
# 输出：BMI 指数、是否正常

from math import sqrt

try:
    height = int(raw_input("请输入身高(cm)："))
    weight = int(raw_input("请输入体重(Kg)："))

    BIM = weight / sqrt(float(height) / 10)

    if BIM < 18.5:
        print "BIM指数是：%.2f ，体重偏轻" % BIM
    elif BIM >= 24:
        print "BIM指数是：%.2f ，体重偏重" % BIM
    else:
        print "BIM指数是：%.2f ，体重正常" % BIM

except Exception,e:
    print "输入有误"

