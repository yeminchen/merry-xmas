import matplotlib.pyplot as plt
import re
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

word_list=[]
with open('static/九品芝麻官剧本.txt') as f:
    words = f.read()
words = " ".join(jieba.cut(words))
for word in words.split():
    word = re.sub(r'[A-Za-z0-9\!\%\[\]\，\。“”]','',word)
    word_list.append(word)
words = ' '.join(word_list)
background_image = plt.imread("static/timg.jpg")
wc = WordCloud(font_path='static/MSYH.TTF',mask=background_image,background_color='white',max_words=100)
my_wc = wc.generate_from_text(words)
image_colors = ImageColorGenerator(background_image)
plt.imshow(my_wc.recolor(color_func=image_colors),)
plt.axis("off")
my_wc.to_file('merry.png')