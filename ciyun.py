from PIL import Image # 图片处理
from matplotlib import pyplot as plt #绘图数据可视化
from wordcloud import WordCloud
import numpy as np
import sqlite3
import jieba

conn = sqlite3.connect("movie250.db")
sql = "select introduction from movie250"
cur = conn.cursor()
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
#print(text)

cur.close()
conn.close()

cut = jieba.cut(text)
string = " ".join(cut)
print(len(string))

img = Image.open(r"/home/huishuohuademao/workspace/doubanflask/static/assets/img/tree2.jpg") #打开遮罩图片
img_array = np.array(img)

wc = WordCloud(
    background_color= "white", #设置背景颜色
    mask = img_array, #遮罩文件为数组
    font_path= (r"/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")
)

wc.generate_from_text(text)

# 使用matplotlib展示词云
flg = plt.figure(1) #从第一个位置开始绘图
plt.imshow(wc, interpolation="bilinear")  # 用双线性插值显示图片
plt.axis("off")  # 关闭坐标轴
plt.show()
plt.savefig(r"./static/assets/img/wordcloud.jpg", dpi = 500) #设置储存路径和分辨率为500

dataList = []
conn = sqlite3.connect("movie250.db")
cursor = conn.cursor()
sql = "SELECT * FROM movie250"
data = cursor.execute(sql)
for item in data:
    print(item)
    dataList.append(item)
cursor.close()
conn.close()
