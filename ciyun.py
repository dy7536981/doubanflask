from PIL import Image  # 图片处理
from matplotlib import pyplot as plt  # 绘图数据可视化
from wordcloud import WordCloud
import numpy as np
import sqlite3
import jieba

def fetch_movie_introductions(db_path):
    """从数据库中获取所有电影简介。"""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT introduction FROM movie250")
        introductions = cursor.fetchall()
    # 将所有简介合并为一个字符串
    return " ".join([intro[0] for intro in introductions])

def generate_wordcloud(text, mask_image_path, font_path, output_path):
    """生成词云并保存为图片。"""
    # 分词
    cut_text = " ".join(jieba.cut(text))
    
    # 打印分词后的字符串长度（可选）
    print(f"分词后字符串长度: {len(cut_text)}")
    
    # 加载遮罩图片
    mask_image = np.array(Image.open(mask_image_path))
    
    # 创建词云对象
    wc = WordCloud(
        background_color="white",
        mask=mask_image,
        font_path=font_path,
        max_words=2000,
        max_font_size=100,
        random_state=42,
        width=mask_image.shape[1],
        height=mask_image.shape[0]
    )
    
    # 生成词云
    wc.generate(cut_text)
    
    # 使用matplotlib展示词云
    plt.figure(figsize=(10, 8))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    
    # 保存词云图片
    plt.savefig(output_path, dpi=500, bbox_inches='tight')
    plt.show()

def fetch_all_movies(db_path):
    """从数据库中获取所有电影数据。"""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movie250")
        movies = cursor.fetchall()
    return movies

def main():
    db_path = "movie250.db"
    mask_image_path = "/home/huishuohuademao/workspace/doubanflask/static/assets/img/tree2.jpg"
    font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
    output_path = "./static/assets/img/wordcloud.jpg"
    
    # 获取所有电影简介
    text = fetch_movie_introductions(db_path)
    
    # 生成并保存词云
    generate_wordcloud(text, mask_image_path, font_path, output_path)
    
    # 获取并打印所有电影数据
    movies = fetch_all_movies(db_path)
    for movie in movies:
        print(movie)

if __name__ == "__main__":
    main()
