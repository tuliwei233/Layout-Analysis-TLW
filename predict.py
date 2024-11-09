from ultralytics import YOLOv10
import glob
import os
import xml.etree.ElementTree as ET

device = "cpu"

model = YOLOv10("runs/detect/train/weights/best.pt")  # best.pt
model.to(device)

test_folder = "dataset/fish/ImageSets/images/val" # /home/data/test
image_paths = glob.glob(os.path.join(test_folder, "*.*"))

#创建输出目录
output_dir = "runs/output" # output
os.makedirs(output_dir, exist_ok=True)

#每张图片进行预测
for image_path in image_paths:
    results = model.predict(image_path)

    #创建XML文件
    root = ET.Element("annotation")

    #获取图像文件名
    filename = os.path.basename(image_path)
    ET.SubElement(root, "filename").text = filename

    #遍历每个结果
    for result in results:
        if result is not None:
            boxes = result.boxes.xyxy  # 获取边界框坐标
            conf = result.boxes.conf  # 获取置信度
            classes = result.boxes.cls  # 获取类别标签
            # 保存label后的图片
            for result in results:
                if result:  # 确保结果非空
                    result.save(filename=os.path.join(output_dir, f"{os.path.basename(image_path)}.jpg"))
            # 保存xml
            for box, c, score in zip(boxes, classes, conf):
                obj = ET.SubElement(root, "object")
                ET.SubElement(obj, "name").text = str(int(c))  # 类别可以映射到类别名
                ET.SubElement(obj, "confidence").text = str(score.item())  # 置信度
                bndbox = ET.SubElement(obj, "bndbox")
                ET.SubElement(bndbox, "xmin").text = str(int(box[0].item()))
                ET.SubElement(bndbox, "ymin").text = str(int(box[1].item()))
                ET.SubElement(bndbox, "xmax").text = str(int(box[2].item()))
                ET.SubElement(bndbox, "ymax").text = str(int(box[3].item()))

    xml_tree = ET.ElementTree(root)
    xml_file_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.xml")
    xml_tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)
    print(f"已保存{filename}的xml文件 至 {xml_file_path}")
