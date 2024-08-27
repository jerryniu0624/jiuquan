# 酒泉

## 项目介绍

本项目分为6个算法：5个非暂停算法；1个暂停算法。

非暂停算法：

1.人员计数：对不同摄像头下的人员进行计数，有的摄像头之间的重复人员不能重复计数

2.车辆计数：对摄像头下的救护车与消防车进行计数

3.异物检测：对摄像头下的异常物品进行检测

4.关键设备计数：对摄像头下的医药箱进行计数

5.异常行为识别：对摄像头下是否存在人进行反应（与1重复，但也是一个需求，研究所如是）

暂停算法：

对设备健康状况进行评价

## 算法介绍

### 人员计数

先使用yolov8在coco上的预训练模型进行人员检测，得到人的框图；然后使用Clip-Reid在market1501上的预训练模型进行行人重识别，对重复人员进行去重

yolov8地址：https://github.com/ultralytics/ultralytics

Clip-Reid地址：https://github.com/Syliz517/CLIP-ReID

链接: https://pan.baidu.com/s/121OOzKCH5Wal4PeNWOhi0A?pwd=6cpc 提取码: 6cpc 

10358 /data7/nyz/CLIP-ReID-master

### 车辆计数

先使用yolov8在coco上的预训练模型进行车辆检测，类别时truck和bus（好像是），得到潜在车的框图；然后使用3分类resnet在采集的分类数据集上进行分类（消防车；救护车；其他车辆）

链接: https://pan.baidu.com/s/14UQv6ms5aYuG2ZUsE4KTag?pwd=7pjv 提取码: 7pjv 

10358 /data7/nyz/nyz_flask_vehicle_count

### 异物检测

使用TransCD在CDnet2014上预训练模型进行变化检测，只不过应用时输入一张清场图和一个场景视频流，显示变化检测的框的位置

TransCD地址：https://github.com/wangle53/TransCD

链接: https://pan.baidu.com/s/1lmFvYyMGmIdzbztrCIaNRQ?pwd=5t2c 提取码: 5t2c 

10358 /data1/nyz/TransCD-main

### 关键设备计数

使用langsam以box为关键词进行潜在医药箱的计数（效果比用grounding dino好）；然后使用resnet在2分类数据集上预训练模型进行2分类（医药箱；其他箱子）

langsam地址：https://github.com/luca-medeiros/lang-segment-anything

链接: https://pan.baidu.com/s/1p3Q20_PjRicMHN-hRvmUqw?pwd=3qwm 提取码: 3qwm 

10358 /data7/nyz/lang-segment-anything-main

### 异常行为识别

使用yolov8在coco上的预训练模型进行人员检测，看看有没有人

链接: https://pan.baidu.com/s/1k1JPUAApsC822_ap3UWnAw?pwd=6fwe 提取码: 6fwe 

10358 /data7/nyz/nyz_flask_anomaly_detection

### 设备健康评价

基于ISO7919轴振动评价标准的设备健康评价

来源：https://blog.csdn.net/m0_47410750/article/details/127342045

链接: https://pan.baidu.com/s/1aJspVDWLERPwHOjIW7Fsvw?pwd=btkf 提取码: btkf 

10358 /data7/nyz/device_health_assessment



## 项目要求

非暂停算法：

1.docker封装

2.flask进行前后端端口映射，并基于flask进行前后端链接，输入大部分是视频流，少部分是base64图片。全部是post json格式输入。

3.输出的算法结果以kafka消息队列来进行

4.以可执行程序运行算法服务

5.算法定时报废

暂停算法：

1.docker封装

2.flask进行前后端端口映射，并基于flask进行前后端链接，以post形式输入json

注：整个算法打包过程详见《酒泉docker封装方法.md》

注：flask接口设置以及kafka的message设置详见《接口要求.docx》
