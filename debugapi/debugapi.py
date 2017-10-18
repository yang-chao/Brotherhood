#coding:utf-8
import json
from flask import request, abort

def newApi(request):
	if request.method == 'POST':
		url = request.form['url']
		json = request.form['json']		
		if (url and json):
			# wirte file
			urllist = url.encode('utf-8').split('/')
			filepath = ''
			for value in urllist:
				if (value):
					filepath += value

			jsonfile = open("debugapi/json/" + filepath + ".json", "w")
			jsonfile.write(json.encode('utf-8'))
			jsonfile.close()
			return customApi(filepath)

	f = open("templates/newapi.html")
	data = f.read()
	f.close()
	return data

def customApi(apiName):
	if apiName:
		try:
			f = open("debugapi/json/" + apiName + ".json")
			data = f.read()
			return data
		except IOError as e:
			abort(404)
	