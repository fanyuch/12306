# -*- coding: utf-8 -*-
import urllib2
import urllib
import ssl
import json

#由于12306网站是不受信的网站，关闭证书的验证功能
ssl._create_default_https_context = ssl._create_unverified_context

def getImfo():

    url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train" \
          "_date=2017-07-14&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=ICW&purpose_codes=ADULT"
    req = urllib2.Request(url)
    #模拟浏览器设置一个请求head文件结构。head结构中"user-agent"字段是用来标识浏览器个性信息的
    req.add_header(
        "User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    html = urllib2.urlopen(req).read()
    #观察发现这是一个json格式的数据，我们把他转化成python的字典类型
    req = json.loads(html)
    return req["data"]["result"]




if __name__ == '__main__':
    number = 0
    #车次=3
    #出发时间=8
    #到达时间=9
    #二等座=30
    #一等座=31
    #商务座=32
    for i in getImfo():
        for n in i.split("|"):
            print "[%d] %s" % (number, n)
            number += 1
        break



    pass