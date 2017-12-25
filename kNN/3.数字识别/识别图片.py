'''
仅能识别单个数字的图片
运行前，需要先运行kNN_test04_tz.py生成model.dat模型文件
'''
import cv2
import img2txt
import sys
import pickle
import numpy as np
img_rec = sys.argv[1]
'''二值化'''
img_data = cv2.imread(img_rec)
# 转灰度图
GrayImage=cv2.cvtColor(img_data,cv2.COLOR_BGR2GRAY)
# 二值化
ret,thresh1=cv2.threshold(GrayImage,127,1,cv2.THRESH_BINARY_INV) # 大于127的值，设为1（其余为0）
# 去除空白边界
pic_cut = img2txt.cut_null_edge(thresh1)
# 图像变形
img = cv2.resize(pic_cut, (32, 32))

# 加载模型
with open('model.dat','rb') as f:
    model = pickle.load(f)
# 识别
img_vector = np.reshape(img,(1,1024))
rec_result = model.predict(img_vector)
print("分类返回结果为%d" %rec_result)
