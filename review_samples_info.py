# 参考：https://zhuanlan.zhihu.com/p/56571623

import cv2

video_path = './samples/big_buck_bunny_720p_5mb.mp4'

# 读取视频
cap = cv2.VideoCapture(video_path)

# 获取帧率
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
print(cap.get(cv2.CAP_PROP_FPS))
# 分辨率-宽度
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 分辨率-高度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 获取总帧数
frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

cap.release()
cv2.destroyAllWindows()
# 时长，单位s
duration = frame_counter / fps

print(f'帧率:{fps},时长:{duration}s')