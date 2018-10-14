import requests
from xlwt import *

def get(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    return res.text

def getColorStyle(color):
    colors = {
        0 : None,
        1 : 'yellow',
        2 : 'blue',
        3 : 'gray_ega',
        4 : 'orange',
        5 : 'dark_blue_ega',
        6 : 'purple_ega',
        7 : 'gray25',
        8 : 'red',
        9 : 'dark_red_ega',
        10 : 'green'
    }
    style = XFStyle()
    fnt = Font()                        # 创建一个文本格式，包括字体、字号和颜色样式特性                              
    fnt.name = u'微软雅黑'                # 设置其字体为微软雅黑                                 
    fnt.colour_index = 1                # 设置其字体颜色             
    style.font = fnt  
    pattern = Pattern()
    pattern.pattern = Pattern.SOLID_PATTERN
    #pattern.pattern_fore_colour = Style.colour_map[colors.get(color,None)]
    style.pattern = pattern
    return style