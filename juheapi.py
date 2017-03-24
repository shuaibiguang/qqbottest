#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib,urllib.parse,urllib.request
#----------------------------------
# 问答机器人调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/112
#----------------------------------
header={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36',"Content-Type":'text/html; charset=utf-8'}
def main(text = '哈哈哈'):
 
    #配置您申请的APPKey
    appkey = "4e12dcc365328a9295a41a69185ffa78"

    #1.问答
    return request1(appkey,"GET",text)
 
    #2.数据类型
    # request2(appkey,"GET")
 
 
 
#问答
def request1(appkey, m="GET", text="哈哈"):
    url = "http://op.juhe.cn/robot/index"
    params = {
        "key" : appkey, #您申请到的本接口专用的APPKEY
        "info" : text, #要发送给机器人的内容，不要超过30个字符
        "dtype" : "", #返回的数据的格式，json或xml，默认为json
        "loc" : "", #地点，如北京中关村
        "lon" : "", #经度，东经116.234632（小数点后保留6位），需要写为116234632
        "lat" : "", #纬度，北纬40.234632（小数点后保留6位），需要写为40234632
        "userid" : "", #1~32位，此userid针对您自己的每一个用户，用于上下文的关联
 
    }
    params = urllib.parse.urlencode(params)
    if m =="GET":
        req = urllib.request.Request("%s?%s" % (url, params), data=None,headers=header)
        f = urllib.request.urlopen(req)
    else:
        req = urllib.request.Request(url+params, data=None,headers=header)
        f = urllib.request.urlopen(req)
 
    content = f.read().decode()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            # print (res["result"])
            # return res['result']
            # print (res['result']['text'])
            return res['result']['text']
        else:
            err = json.dumps(res)
            with open('log.txt','a+') as oo:
                oo.write(err+"\n\r"+text) 
            # print ("%s:%s" % (res["error_code"],res["reason"]))
            return "我好像出错了$%$*%*&^#$@#%$@#%"
    else:
        return "我的接口好像出错了，哈哈哈，创造我的人技术不行啊"
 
#数据类型
def request2(appkey, m="GET"):
    url = "http://op.juhe.cn/robot/code"
    params = {
        "dtype" : "", #返回的数据格式，json或xml，默认json
        "key" : appkey, #您申请本接口的APPKEY，请在应用详细页查询
 
    }
    params = urllib.parse.urlencode(params)
    if m =="GET":
        req = urllib.request.Request("%s?%s" % (url, params), data=None,headers=header)
        f = urllib.request.urlopen(req)
    else:
        req = urllib.request.Request(url+params, data=None,headers=header)
        f = urllib.request.urlopen(req)
 
    content = f.read().decode()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print (res["result"])
        else:
            print ("%s:%s" % (res["error_code"],res["reason"]))
    else:
        print ("request api error")
 
 