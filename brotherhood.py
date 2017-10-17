#coding:utf-8
from flask import Flask, request, render_template
import os, time, datetime, sys
from util import fileUtil
from debugapi import debugapi

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

@app.route('/')
def archived_android():
	apkPath = 'static/apk'
	filePaths = os.listdir(apkPath)
	launchName = ''
	testName = ''
	preName = ''
	createTime = ''
	size = 0
	build = ''
	version = ''
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

	if (launchName):
		createTime = fileUtil.get_file_createTime('static/' + launchName)
		size = fileUtil.get_file_size('static/' + launchName)

	# babyfs-v2.0.2-build24-Launch-debug.apk
	nameArray = basename.split('-')
	for s in nameArray:
		if 'build' in s:
			build = s
		elif 'v' in s:
			version = s
	return render_template('archived.html', launchName=launchName, testName=testName, preName=preName,
		create_time=createTime, size=size, build=build, version=version)

#debugapi
@app.route('/debugapi')
@app.route('/debugapi/new', methods=['GET', 'POST'])
def new_api():
	return debugapi.newApi(request)

@app.route('/debugapi/custom/<apiName>')
def custom_api(apiName):
	return debugapi.customApi(apiName)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)