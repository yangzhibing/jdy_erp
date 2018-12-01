# -*- coding: utf-8 -*-
{
    "name": "My Training Classroom", #模块名
    "version": "1.0",        #模块版本
    "description": 'My Training Demo -- ClassRoom', #模块说明
    "author": "young",    #作者
    "website": "http://www.youngzhibing@163.com", #网址
    "depends": ["my_training"],                      #依赖的模块
    "data": [
        "lesson_view.xml",      # 需要继承的视图
        "classroom_view.xml",],   # 模块更新时读入的文件
    "demo": [],
    "installable": True,                #可否安装
    'auto_install': False,
 }

