#!/usr/bin/env python3
#import os
"""
Copyright 2022. All rights reserved.
"""
__version__ = "1.7"
#def struct():import struct
#def pickle():import pickle
#def shelve():import shelve
_text_file='file'
_text_directory='directory'
_text_exists='exists'
def open_as_str(path):
	myfile=open(path,'r')
	text=''
	for line in myfile:
		text+=line
	myfile.close()
	return text
def open_as_list(path):
	#return [x.rstrip() for x in open(path,'r').readlines()]
	"""myfile=open(path,'r')
	text=[]
	for line in myfile:
		text.append(line.rstrip())
	myfile.close()
	return text"""
	with open(path,'r') as myfile: 
		return list(map((lambda line: line.rstrip()), myfile))
def open_as_dict(path):
	myfile=open(path,'r')
	text={}
	for line in myfile:
		line=line.rstrip().split('=')
		text[line[0]]=line[1]
	myfile.close()
	return text
def open_json(path):
	import json
	return json.load(open(path))
def get_request_text_as_str(url):
	import requests
	headers={"Accept":"text/plain"}
	response=requests.request("GET",url,headers=headers).text.split('\n')
	text=[]
	for line in response:
		text.append(line.rstrip())
	return text
def get_request_text_as_json(url,params=""):
	import requests
	resp = requests.get(url=url, params=params)
	data = resp.json()
	return data
def write_text(path,text):
	with open(path, 'w') as myfile: myfile.write(text)
	"""myfile=open(path,'w')
	myfile.write(text)
	myfile.close()"""
def write_list_as_text(path, list_text):
	text = ""
	for i in list_text:
		text+= i + "\n"
	with open(path, 'w') as myfile: myfile.write(text)
def write_text_as_json(path,text):
	import json
	json.dump(text, fp=open(path+".json",'w'),indent=4)
def check_file(path):
	import os
	if os.path.isfile(path): print(_text_file,path,_text_exists)
	else: print('there is no existing file (and therefore no existing file path) '+path)
def check_dir(path):
	import os
	if os.path.isdir(path):
		print(_text_directory,path,_text_exists)
		return True
	else: 
		print('there is no existing directory (and therefore no existing directory path) '+path)
		return False
def check_exists(path):
	import os
	if os.path.exists(path): print('file/directory',path,_text_exists)
	else: print('there is no existing file/directory (and therefore no existing file/directory path) '+path)
def dir_make(path):
	import os
	if path.endswith("/"): path=path[:-1]
	directory = path.split('/')
	directory.reverse()
	dir = directory[0]
	parent_dir = path[:path.find(dir)]
	#mode = 0o666
	mode = 0o777
	path = os.path.join(parent_dir, dir)
	try:
		os.mkdir(path, mode)
		print("Directory: '{}' created successfully, path: '{}'".format(dir,path))
	except Exception as error:
		#raise error
		if check_dir(path): pass
		else: print("Cannot create a directory '{}', path: '{}'".format(dir,path))
def dirs_make(path):
	import os
	if path.endswith("/"): path=path[:-1]
	directory = path.split('/')
	directory.reverse()
	dir = directory[0]
	parent_dir = path[:path.find(dir)]
	#mode = 0o666
	mode = 0o777
	path = os.path.join(parent_dir, dir)
	try:
		os.makedirs(path, mode)
		print("Directory: '{}' created successfully, path: '{}'".format(dir,path))
	except Exception as error:
		#raise error
		if check_dir(path): pass
		else: print("Cannot create a directory '{}', path: '{}'".format(dir,path))
	
if __name__ == '__main__':
	print(get_request_text_as_json("https://api.github.com/repos/babyish-retired0m/hostname_advanced_testing/contents/results3?ref=main"))