import os, shutil, random
from tqdm import tqdm

def split_img(img_path, label_path, split_list):
    try:
        # 目标文件夹路径（确保路径分隔符一致）
        Data = r'D:\Downloads\yolov10-main\yolov10-main\dataset\fish\ImageSets'

        # 创建数据集路径
        train_img_dir = os.path.join(Data, 'images', 'train')
        val_img_dir = os.path.join(Data, 'images', 'val')
        test_img_dir = os.path.join(Data, 'images', 'test')
        train_label_dir = os.path.join(Data, 'labels', 'train')
        val_label_dir = os.path.join(Data, 'labels', 'val')
        test_label_dir = os.path.join(Data, 'labels', 'test')

        # 使用 exist_ok=True 避免文件夹重复创建
        os.makedirs(train_img_dir, exist_ok=True)
        os.makedirs(train_label_dir, exist_ok=True)
        os.makedirs(val_img_dir, exist_ok=True)
        os.makedirs(val_label_dir, exist_ok=True)
        os.makedirs(test_img_dir, exist_ok=True)
        os.makedirs(test_label_dir, exist_ok=True)

    except Exception as e:
        print(f'文件目录创建出现错误: {e}')

    train, val, test = split_list
    all_img = os.listdir(img_path)
    all_img_path = [os.path.join(img_path, img) for img in all_img]

    # 分割训练集
    train_img = random.sample(all_img_path, int(train * len(all_img_path)))
    train_label = [toLabelPath(img, label_path) for img in train_img]
    for i in tqdm(range(len(train_img)), desc='train ', ncols=80, unit='img'):
        _copy(train_img[i], train_img_dir)
        _copy(train_label[i], train_label_dir)
        all_img_path.remove(train_img[i])

    # 分割验证集
    val_img = random.sample(all_img_path, int(val / (val + test) * len(all_img_path)))
    val_label = [toLabelPath(img, label_path) for img in val_img]
    for i in tqdm(range(len(val_img)), desc='val ', ncols=80, unit='img'):
        _copy(val_img[i], val_img_dir)
        _copy(val_label[i], val_label_dir)
        all_img_path.remove(val_img[i])

    # 剩余为测试集
    test_img = all_img_path
    test_label = [toLabelPath(img, label_path) for img in test_img]
    for i in tqdm(range(len(test_img)), desc='test ', ncols=80, unit='img'):
        _copy(test_img[i], test_img_dir)
        _copy(test_label[i], test_label_dir)

def _copy(from_path, to_path):
    if os.path.exists(from_path):
        shutil.copy(from_path, to_path)
    else:
        print(f"文件不存在: {from_path}")


def toLabelPath(img_path, label_path):
    img = os.path.basename(img_path)
    label = img.rsplit('.', 1)[0] + '.txt'
    return os.path.join(label_path, label)

if __name__ == '__main__':
    img_path = r'D:\Downloads\yolov10-main\yolov10-main\dataset\fish\images'
    label_path = r'D:\Downloads\yolov10-main\yolov10-main\dataset\fish\labels'
    split_list = [0.7, 0.2, 0.1]
    split_img(img_path, label_path, split_list)
