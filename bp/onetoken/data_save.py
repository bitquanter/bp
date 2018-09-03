# -*- coding:utf-8 -*-
import time
import os
import redis

tick_cli=redis.StrictRedis.from_url('localhost:6379')


def data_write(path, file, data,cate):
    date_name = str(time.strftime("%Y-%m-%d"))
    File_Path =  "./data_save_directory/"+date_name + "/"+cate+"/" + path
    if not os.path.exists(File_Path):
        os.makedirs(File_Path)
        with open(File_Path + '/' + date_name+"_"+cate+"_"+file+".json", 'a') as f:
            f.write(data + '\n')
    else:
        with open(File_Path + '/' + date_name+"_"+cate+"_"+file+".json", 'a') as f:
            f.write(data + '\n')


def write_redis(key, data):
	tick_cli.set(key, data)
	pass
