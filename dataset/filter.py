import os

# 图片和标签文件夹路径
img_path = 'dataset/fish/images'
label_path = 'dataset/fish/labels'

# 定义可接受的图片格式
image_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}

# 获取图片文件名（不含扩展名）和标签文件名（不含扩展名）
img_files = {os.path.splitext(f)[0] for f in os.listdir(img_path) if os.path.splitext(f)[1].lower() in image_extensions}
label_files = {os.path.splitext(f)[0] for f in os.listdir(label_path) if f.endswith('.txt')}

# 过滤出匹配和不匹配的文件
matched_files = img_files & label_files
unmatched_imgs = img_files - matched_files
unmatched_labels = label_files - matched_files

# 输出未匹配的文件
print("未匹配的图片文件:", unmatched_imgs)
print("未匹配的标签文件:", unmatched_labels)
