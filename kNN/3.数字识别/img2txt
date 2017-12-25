'''
将任意图片转换为32*32的txt
'''
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def sum_rows(matrix): 
#     按行求和 
    sum_row_list=list(map(sum,matrix)) 
    return sum_row_list
def sum_cols(matrix): 
#     按列求和 
    sum_col_list=list(map(sum,list(zip(*matrix))))  
    return sum_col_list
def threshold(p_list,thresh,maxval):
#     列表的二值化
    for i in range(0,len(p_list)):
        if p_list[i]>thresh:
            p_list[i]=thresh
    return p_list

def cut_null_edge(thresh1):
	'''找出二值化的图片边缘的空白'''
	# 先去除过多的空白，以免严重变形
	# print(thresh1.shape) # 尺寸
	row,column = thresh1.shape
	# print(thresh1)
	# 上下空白
	sum_row_list = sum_rows(thresh1) # 按行求和
	sum_row_list = threshold(sum_row_list,1,1) # 列表的二值化
	# print(sum_row_list)
	null_row1 = sum_row_list.index(1) # 上部空白
	null_row2 = len(sum_row_list) - list(reversed(sum_row_list)).index(1) # 下部空白
	# 左右空白
	sum_col_list = sum_cols(thresh1)
	sum_col_list = threshold(sum_col_list,1,1) # 列表的二值化
	# print(sum_col_list)
	null_col1 = sum_col_list.index(1) # 左部空白
	null_col2 = len(sum_col_list) - list(reversed(sum_col_list)).index(1) # 右部空白
	'''去除空白'''
	# print(null_row1,null_row2,null_col1,null_col2)
	pic_cut = thresh1[null_row1:null_row2, null_col1:null_col2]
	return pic_cut

if __name__ == '__main__':
	import sys
	img_rec = sys.argv[1]
	'''二值化'''
	img_data = cv2.imread(img_rec)
	# 转灰度图
	GrayImage=cv2.cvtColor(img_data,cv2.COLOR_BGR2GRAY)
	# 二值化
	ret,thresh1=cv2.threshold(GrayImage,127,1,cv2.THRESH_BINARY_INV) # 大于127的值，设为1（其余为0）
	# 去除空白边界
	pic_cut = cut_null_edge(thresh1)
	# 图像变形
	img = cv2.resize(pic_cut, (32, 32))
	with open(img_rec+'.txt','w') as f:
	    for row in img:
	        for i in row:
	            f.write(str(i))
	        f.write('\n')
	print('已成功将图片转化为32*32的txt')
