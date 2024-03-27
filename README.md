# lumaDemo
一个简单的lumaDemo,在一个通过I2C连接到树莓派的OLED屏上输出几个字符。

## luma安装
见 [luma.examples](https://github.com/rm-hull/luma.examples)  
安装依赖包

```
$ sudo usermod -a -G i2c,spi,gpio pi
$ sudo apt install python3-dev python3-pip python3-numpy libfreetype6-dev libjpeg-dev build-essential
$ sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev
```

然后下载luma.examples文件夹  

```
$ git clone https://github.com/rm-hull/luma.examples.git
```

进入文件夹安装luma组件  

```
$ cd luma.examples
$ sudo -H pip install -e .
```

## luma部署到Docker
基于balenalib/rpi-raspbian镜像

Dockerfile:

```
FROM balenalib/rpi-raspbian:latest
ENTRYPOINT []

RUN apt-get -q update
RUN apt-get -q upgrade
RUN apt install python3-dev python3-pip python3-numpy libfreetype6-dev libjpeg->
RUN apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev>
RUN pip install rpi.gpio

RUN git clone https://github.com/rm-hull/luma.examples.git
RUN cd luma.examples && pip install -e .

CMD ["python3","luma.examples/examples/3d_box.py"]
```

**注：** 运行镜像时需要添加--privileged，否则无法访问GPIO

生成镜像并运行后会执行自带的3d_box.py

可自行修改Dockerfile文件嵌入自己的python程序，或者把这个作为基础镜像再生成新的镜像

## oled屏幕的I2C连接
树莓派                                                OLED    
PIN 1(3V3)           --------------->           VCC    
PIN 3(SDA.1)       --------------->           SDA    
PIN 5(SCL.1)        --------------->           SCL    
PIN 6(0V)              --------------->           GND  


<img src="gpio.png" width="400" alt="GPIO引脚图"/>

## 输出
<img src="output.jpg" width="400" alt="输出图"/>

## 注意
本Demo基于luma.example中的例子修改简化而成，  
* show_text.py为显示字符的程序
* demo_opt.py是原example中的文件,用于获取屏幕信息
* fonts文件夹中为字体文件，其中code2000.ttf支持中文（似乎支持所有语言的字符）
