#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from datetime import datetime

if os.name != 'posix':
    sys.exit('{} platform not supported'.format(os.name))

from demo_opts import get_device
from luma.core.render import canvas
from PIL import ImageFont

def show(device):
    # use custom font
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'fonts', 'code2000.ttf')) # 导入字体文件
    font2 = ImageFont.truetype(font_path, 20)   #设置字体类型和字体大小

    # 开始输出
    with canvas(device) as draw:
        # draw.text((x,y),"输出内容",font=字体,fill=颜色)
        # 这3行基本占满了128*64的oled屏幕
        draw.text((0, 0), "一二三四五", font=font2, fill="white")   
        draw.text((0, 22), "六七八九十", font=font2, fill="white")
        draw.text((0, 44), "Hello World", font=font2, fill="white")

def main():
    # 如果不写在循环里，执行完程序就退出了，就看不到内容
    while True:
        show(device)
        time.sleep(5)

if __name__ == "__main__":
    try:
        device = get_device()   # 获取并输出设备信息 demo_opts.get_device()
        main()
    except KeyboardInterrupt:   # ctrl+c退出
        pass
