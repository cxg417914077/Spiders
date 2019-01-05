import sqlalchemy, sqlite3, jieba
from pandas import read_sql
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread

engine = sqlalchemy.create_engine('sqlite:///lagou.sqlite')
df = read_sql('select * from position', engine)
# 生成词云
# positionAdvantage = df['positionAdvantage']
# text = ''
# for line in positionAdvantage:
#     text += line
# cut_text = ''.join(jieba.cut(text))
# color_mask = imread('timg.jpg')  # 设置背景图
# cloud = WordCloud(
#     font_path='Yahei.ttf',
#     background_color='white',
#     mask=color_mask,
#     max_words=1000,
#     max_font_size=100
# )
#
# word_cloud = cloud.generate(cut_text)
# # 保存词云图片
# word_cloud.to_file('word_cloud.jpg')
# plt.imshow(word_cloud)
# plt.axis('off')
# plt.show()

# 工资直方图
pattern = '\d+'
# 将字符串转化为列表,再取区间的前25%，比较贴近现实
df['salary'] = df['salary'].str.findall(pattern)

avg_salary = []
for k in df['salary']:
    int_list = [int(n) for n in k]
    avg_wage = int_list[0] + (int_list[1] - int_list[0]) / 4
    avg_salary.append(avg_wage)

df['月工资'] = avg_salary
print('python工资描述：\n{}'.format(df['月工资'].describe()))
plt.hist(df['月工资'], bins=12, width=2)
plt.xlabel('工资 (千元)')
plt.ylabel('频数')
plt.title("工资直方图")
plt.savefig('histogram.jpg')
plt.show()
