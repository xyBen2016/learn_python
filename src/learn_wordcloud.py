from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import jieba


# 文字路径
txt_path = "auto.txt"
# 图片路径
img_path = "earth.jpg"
# 字体路径
font = r"C:\Windows\Fonts\STCAIYUN.TTF"
# 读取文字
text = open(txt_path, 'r', encoding='utf-8').read()

jb_txt = jieba.cut(text, cut_all=True)
fin_txt = " ".join(jb_txt)

# 读取mask图片
alice_mask = np.array(Image.open(img_path))

image_colors = ImageColorGenerator(alice_mask)
# 生成词云
wordcould = WordCloud(background_color="white", mask=alice_mask,
                      font_path=font, max_words=2000).generate(fin_txt)
# 展示图片
# plt.imshow(wordcould)
plt.imshow(wordcould.recolor(color_func=image_colors),
           interpolation="bilinear")
plt.axis("off")
plt.show()
# 保存图片
wordcould.to_file('wc.png')
