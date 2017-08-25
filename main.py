# coding:utf-8
import cv2
import time
import os
import pygame
import argparse
from pydub import AudioSegment

# 将灰度值转为字符
def get_char(gray_number):
    if FLAGS.ascii_mode:
        return chr(int(93.0/256*gray_number)) + ' '
    else:
        if gray_number > 100:
            return FLAGS.zifu + ' '
        else:
            return '  '

# 将图片转为字符
def img_to_char(image, size):
    image = cv2.resize(image, size)
    text = ''
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            text += get_char(image[i, j])
        text += '\n'

    return text

# 播放一帧
def play(text, start_played_time, num, fps):
    now_time = time.time()

    # 帧率控制
    if now_time - start_played_time - num*1.0/fps < 0:
        time.sleep(num*1.0/fps - (now_time - start_played_time))

    os.system('clear')
    total_time = time.time() - start_played_time
    print(text + '原视频帧率：%f, 当前帧：%d，播放时长：%f，帧率：%f' % (fps, num, total_time, num*1.0/total_time))

# 获取缩放大小
def get_size(shape):
    tmp = shape[1]/FLAGS.video_scale
    size = (int(shape[1]/tmp), int(shape[0]/tmp))
    return size

def run():
    video = cv2.VideoCapture(FLAGS.video_dir)
    start_played_time = 0

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)

    num = 0
    while (video.isOpened()):
        ret, frame = video.read()
        size = get_size(frame.shape)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = img_to_char(gray, size)

        if start_played_time == 0:
            start_played_time = time.time()

            pygame.mixer.init()
            track = pygame.mixer.music.load("Audio_tmp.wav")
            pygame.mixer.music.play()

        play(text, start_played_time, num, fps)

        num += 1

    video.release()

def main():
    if os.path.isfile('Audio_tmp.mp3'):
        os.remove('Audio_tmp.mp3')

    if FLAGS.video_dir == '':
        print('请输入视频路径')
    else:
        if FLAGS.audio_mode:
            AudioSegment.from_file(FLAGS.video_dir, 'mp4').export('Audio_tmp.wav', format='wav')

        run()

        if os.path.isfile('Audio_tmp.mp3'):
            os.remove('Audio_tmp.mp3')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--video_dir',
        type=str,
        default='',
        help='视频路径'
    )
    parser.add_argument(
        '--ascii_mode',
        type=bool,
        default=False,
        help='采用灰度转ascii码模式'
    )
    parser.add_argument(
        '--audio_mode',
        type=bool,
        default=False,
        help='是否播放音频，需要pydub和ffmpeg支持'
    )
    parser.add_argument(
        '--zifu',
        type=str,
        default='@',
        help='可以指定替换字符，默认为@'
    )
    parser.add_argument(
        '--video_scale',
        type=int,
        default=64,
        help='像素缩放比例，默认64，值越大需要更高的计算性能'
    )

    FLAGS, unparsed = parser.parse_known_args()
    main()
