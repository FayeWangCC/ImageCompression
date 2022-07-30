import os

from PIL import Image


# 读取图片
def get_image(r_path):
	# 获取图片列表
	img_list = os.listdir(r_path)

	# 存储图片路径
	img_dict = {}
	# 获取图片地址
	for img_name in img_list:
		# 拼接地址
		img_src = r_path + '\\' + img_name
		# 存储图片名称地址
		img_dict[img_name] = img_src
	return img_dict


# 压缩图片
def compression_image(img_dict, s_path, quality):
	# 遍历获取图片名称地址
	for name in img_dict.keys():
		# 加载image对象
		im = Image.open(img_dict[name])
		# 存储图片
		im.save(fp=s_path + '\\' + name, quality=quality)


if __name__ == '__main__':
	# 图片文件夹路径
	r_path = input('请输入图片文件目录：')
	# 存储路径
	s_path = input('请输入图片保存目录：')
	quantily = int(input('请输入图片质量< n/100 >'))
	# 获取图片地址信息
	img_dict = get_image(r_path)
	compression_image(img_dict, s_path, quantily)
