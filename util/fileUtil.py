#coding:utf-8
import os, time, datetime, sys
# 获取文件大小
def get_file_size(path):
	fsize = os.path.getsize(path)
	fsize = fsize/float(1024*1024)
	return round(fsize, 2)

# 获取文件创建时间
def get_file_createTime(path):
	createTime = os.path.getctime(path)
	currentTime = time.time()
	diff = int(currentTime - createTime)
	result = ''
	if (diff / (24 * 3600) > 0):
		day = diff / (24 * 3600)
		result = str(day) + '天'
	elif (diff / 3600 > 0):
		hour = diff / 3600
		result = str(hour) + '小时'
	elif (diff / 60 > 0):
		minute = diff / 60
		result = str(minute) + '分钟'
	return result + '前'