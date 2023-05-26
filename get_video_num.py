import os,sys
import cv2

# --long_gray_video
#     --sub_id
#         --segment_id

os.chdir(os.path.dirname(__file__))

num = 0
video_path = 'long_gray_video'
for sub in os.listdir(video_path):
    if sub == '.gitignore': continue
    sub_path  = os.path.join(video_path,sub)
    num += len(os.listdir(sub_path))

print('long_gray_video中共有{}个视频'.format(num)) # 270

# 查看其中一个视频
v0_path = './long_gray_video/S08/S08_002_01/Frame_000001823.jpg'
v = cv2.imread(v0_path)
print(v.shape) # (480,640,3) 虽然是灰度图像,但是仍然是3通道的

