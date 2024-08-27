# 实现RTSP视频拉流并切帧

### 测试rtsp地址是否可用：

1.[Embedding IP Camera Live Video Stream into web page - IPCamLive.com](https://www.ipcamlive.com/streamtest)**（不推荐）**

<img src="C:\Users\lab103\Documents\WeChat Files\wxid_2nz4t23rfqtd22\FileStorage\Temp\b793c2c553c09236740733946c676ef.png" alt="b793c2c553c09236740733946c676ef" style="zoom: 67%;" />

### 2.推荐

```python
import cv2

url = 'rtsp://admin:admin@222.128.10.5:10054/live/ikFPcVyIg'
cap = cv2.VideoCapture(url)
while(cap.isOpened()):  
    # Capture frame-by-frame  
    ret, frame = cap.read()  
    # Display the resulting frame  
    cv2.imshow('frame',frame)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
# When everything done, release the capture   
cap.release()  
cv2.destroyAllWindows()

```



### 对demo更改TODO处进行使用

1.更改target_fps进行自定帧率

2.可选择直接进行推理或者保存图片

```python
import cv2
import os
import time


def get_rtsp(path):

    # RTSP视频流的URL
    rtsp_url = path

    # 获取当前日期和时间
    current_time = time.strftime('%Y%m%d')

    # 设置保存图片的文件夹路径，按年月日命名
    save_folder = f'saved_frames_{current_time}'
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # 创建视频捕获对象
    cap = cv2.VideoCapture(rtsp_url)
    # 设置超时时间（以毫秒为单位）
    # cap.set(cv2.CAP_PROP_NETWORK_TIMEOUT, 5000)  # 例如，这里设置为5000毫秒

    # 检查视频流是否成功打开
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # 目标帧率 
    # TODO 根据自己算法更改帧率

    target_fps = 1  # 1秒1帧 
    frame_interval = 1 / target_fps

    # 帧计数器
    frame_number = 0

    try:
        start_time = time.time()
        while True:
            # 计算当前时间与开始时间的差值
            current_time = time.time() - start_time

            # 计算应该读取下一帧的时间点
            next_frame_time = frame_number / target_fps

            # 如果当前时间小于下一帧的时间点，则等待
            if current_time < next_frame_time:
                time.sleep(next_frame_time - current_time)

            # 读取一帧
            ret, frame = cap.read()

            # 如果正确读取帧，ret为True
            if not ret:
                print("Error: No more frames to read.")
                break

            
            # 不保存帧，直接进行推理
            # TODO 插入推理函数

            
            # # 保存帧为图片
            # # 生成唯一的文件名，按年月日时秒帧号命名
            # timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
            # filename = os.path.join(save_folder, f'{timestamp}_{frame_number:04d}.jpg')
            # cv2.imwrite(filename, frame)
            # print(f"Success: {frame_number} frame saved ")

            # 更新帧计数器
            frame_number += 1

    except KeyboardInterrupt:
        # 处理用户中断
        print("\nOperation was interrupted by the user.")

    except Exception as e:
        # 处理其他异常
        print(f"An error occurred: {e}")

    finally:
        print('Successfully done')

        # 释放视频捕获对象
        cap.release()

if __name__ == '__main__':
    url = 'rtsp://admin:admin@222.128.10.5:10054/live/ikFPcVyIg'
    get_rtsp(url)

```

