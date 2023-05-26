import os,sys


# --long_gray_video
#     --sub_id
#         --segment_id

os.chdir(os.path.dirname(__file__))

num = 0
video_path = 'long_gray_video'
for sub in os.listdir(video_path):
    sub_path  = os.path.join(video_path,sub)
    num += len(os.listdir(sub_path))

print(num) # 270