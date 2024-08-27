# 实现RTSP视频拉流并切帧

### 测试rtsp地址是否可用：

1.[Embedding IP Camera Live Video Stream into web page - IPCamLive.com](https://www.ipcamlive.com/streamtest)****

<img src="C:\Users\lab103\Documents\WeChat Files\wxid_2nz4t23rfqtd22\FileStorage\Temp\b793c2c553c09236740733946c676ef.png" alt="b793c2c553c09236740733946c676ef" style="zoom: 67%;" />

### 对demo更改TODO处进行使用

1.更改skip_interval进行自定跳过帧的时间间隔（单位：秒）

2.可直接进行推理

```python
import cv2
import os
import time


def vedio(input_path):

    if input_path is None:
        return jsonify({'error': 'Missing input'}), 400
    
    try:
        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            return jsonify({'error': 'Could not open video.'}), 500
        
        start_time = cap.get(cv2.CAP_PROP_POS_MSEC)
        skip_interval = 1  #跳过的帧的时间间隔（秒）
        frame_number = 0
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break

            current_time = cap.get(cv2.CAP_PROP_POS_MSEC)
            if (current_time - start_time) % (skip_interval * 1000) == 0:
                # 处理帧，其中 skip_interval 是您想要跳过的帧的时间间隔（秒）
                timestamp = current_time 
                
                ！
                # TODO 插入推理函数
                ！

                frame_number += 1

        # 所有帧处理完毕后返回推理结果
        return jsonify()
        cap.release()

    except KeyboardInterrupt:
        return jsonify({'error': 'Operation was interrupted by the user.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
       print('successfully done')

```

