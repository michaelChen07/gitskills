# encoding=utf-8

# 学习 wordcloud 基本用法，然后生成一张词云图

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# 读取文件
text = open(path.join(d, ur'wordcloud1/Jane Eyre(简·爱).txt')).read()

# read the mask image
alice_mask = np.array(Image.open(path.join(d, r"wordcloud1/anne.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)
# 生成词云
wc.generate(text)

# 保存到文件夹中
wc.to_file(path.join(d, r"wordcloud1/anne1.png"))

# 绘制词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()