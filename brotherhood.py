#coding:utf-8
from flask import Flask, request, render_template
import os
import time
import datetime
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

@app.route('/archived')
def archived_android():
	apkPath = 'static/apk'
	filePaths = os.listdir(apkPath)
	launchName = ''
	testName = ''
	preName = ''
	createTime = ''
	size = 0
	build = ''
	for path in filePaths:
		if not os.path.isdir(path):
			basename = os.path.basename(path)
			if not '.apk' in basename:
				continue
			if 'Launch' in basename:
				launchName = 'apk/' + basename
			elif 'Test' in basename:
				testName = 'apk/' + basename
			elif 'Pre' in basename:
				preName = 'apk/' + basename

	# print('filePaht:' + filePaths[1])
	createTime = get_file_createTime('static/apk/' + filePaths[1])
	size = get_file_size('static/apk/' + filePaths[1])

	# babyfs-build24-Launch-debug.apk
	nameArray = basename.split('-')
	for s in nameArray:
		if 'build' in s:
			build = s
	return render_template('archived.html', launchName=launchName, testName=testName, preName=preName,
		create_time=createTime, size=size, build=build)

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

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')