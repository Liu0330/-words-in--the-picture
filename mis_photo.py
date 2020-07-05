# coding=utf-8
# By liuwangxuezhang

from PIL import Image, ImageDraw, ImageFont
# 给好参数大小,以及文字显示内容+图片地址
font_size = 10
text = '刘旺学长！'
img_path = './test.jpg'

#读取图片创建一张相同尺寸画布
img_raw = Image.open(img_path)
img_array = img_raw.load()
img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc', font_size)

# 字符生成器
def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

# 将画布内插入文字
for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

# 保存图片
img_new.convert('RGB').save('result.jpg')
