# 视频抽帧工具
import os
import sys
import cv2
import re
import subprocess

targetDir = ''

def get_video_time(path):
    cap = cv2.VideoCapture(path)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        duration = frame_num / rate
        return round(duration)
    return -1

def time_convert(seconds):
    M, H = 60, 3600
    if seconds < M:
        return f'OO:OO:O{seconds}' if seconds < 10 else f'00:00:{str(seconds)}'
    elif seconds < H:
        _m = int(seconds / M)
        _s = int(seconds % M)
        return f'00:{f"0{_m}" if _m < 10 else str(_m)}:{f"0{_s}" if _s < 10 else str(_s)}'
    else:
        return seconds

def get_video_duration(root_path):
    summary = {} 
    rate = input('输入抽帧频率：如0.25表示四秒一帧 \n') 
    print(rate)
    for root, dirs, files in os.walk(root_path):
        print(root)
        for file_name in files:
            if file_name.endswith('.MP4'):
                duration = get_video_time(os.path.join(root, file_name))
                print('file_name', file_name, 'duration=', time_convert(duration))
                summary[file_name] = {'duration': time_convert(duration)}
                seize(root_path, file_name, rate)
    return summary
def seize(path, name, rate):
    print(name, targetDir)
    
    tag = re.search('(?<=DJI_)\d{4}(?=\.MP4)', name)
    str = "ffmpeg -i " + path + "/" + name + " -r " + rate + " -f image2 " + targetDir + "/" + tag[0] + "_%3d.jpeg"
    subprocess.call(str, shell = True)

def writeSummary(dictD, path):
    file = open(os.path.join(path, 'summary.txt'), 'w')
    for key, value in dictD.items():
        file.write(key + '时长: ' + str(value["duration"]) + '\n')
    file.close()

def mkdir(path):
    target = path + '/extract_images'
    print(target)
    isExit = os.path.exists(target)
    isDir = os.path.isdir(target)
    if (not isDir) or (not isExit):
        os.makedirs(target)
    global targetDir
    targetDir = target
    print(targetDir)

def run():
    path = '/Volumes/2T-Experiment/blackCattle_20220723_162636/approximate'
    mkdir(path)
    summary = get_video_duration(path)
    print(summary)
    writeSummary(summary, path)

if __name__ == "__main__":
    run()