## PythonCharacterVideoPlayer

[![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)](https://github.com/yp05327/PythonCharacterVideoPlayer/LICENSE) [![Python](https://img.shields.io/badge/python-2.7%2C3.+-blue.svg)](https://github.com/yp05327/PythonCharacterVideoPlayer#) 

# 说明
python编写的实时字符动画播放器，实时解码并转换为字符，同时自带音频播放（需要安装ffmpeg，如果使用音频播放，在播放目录下会生成一个临时文件，正常退出时会自动删除）  
BadApple.mp4:[点击此处](http://odxw2uear.bkt.clouddn.com/BadApple.mp4)

# 更新记录
[点击此处](https://github.com/yp05327/PythonCharacterVideoPlayer/blob/master/update.md)

# 安装
运行环境需要python，目前支持的python版本：

```
python2.7
python3.+(未测试)
```

安装依赖库，使用pip，Linux、Mac非root需要添加sudo

```shell
pip install -r requirements.txt
```

# 使用
运行

```shell
python main.py --各种参数
```

参数说明：
* --video_dir 必填，视频文件所在目录，如果在main.py同一目录下则只需要文件名
* --ascii_mode 灰度值直接映射可见ascii码，不建议使用，默认为False
* --audio_mode 是否播放音频，需要ffmpeg支持，安装方法自行查询，默认为False
* --zifu 可替换显示字符，优先级低于--ascii_mode参数，默认为@
* --video_scale 视频播放比例，数值越大需要越高的计算能力，默认64

示例(未安装ffmpeg)：
```shell
python main.py --video_dir BadApple.mp4
```

示例(安装了ffmpeg)：
```shell
python main.py --video_dir BadApple.mp4 --audio_mode True
```


