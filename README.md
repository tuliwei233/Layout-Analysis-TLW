安装依赖  
pip install -r requirements.txt

数据集处理

1.运行xmltotxt.py把voc的xml标签文件转化为yolo的txt标签文件

2.运行filter.py过滤数据集，去除图片名与标签名不符合不匹配的数据

3.运行splitDataset.py划分数据集，默认train：val：test为7：2：1

训练

运行train.py或者命令行输入 yolo detect train data=dataset/data.yaml model=yolov10n.pt epochs=300 batch=16 imgsz=640 device=0

预测

运行predict.py

导出

运行exportmodel.py
