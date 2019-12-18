from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


import json
import time
import random
from . import temp



timeinterval=10

# rd0=randomdata(0)
# rd1=randomdata(1)
# rd2=randomdata(2)
# rd3=randomdata(3)

from apscheduler.scheduler import Scheduler  

sched = Scheduler()  #实例化，固定格式
 
@sched.interval_schedule(seconds=3)  #装饰器，seconds=60意思为该函数为1分钟运行一次
  
def runall():
    data0()
    data1()
    data2()
    data3()

  
sched.start()  #启动该脚本


def data0():
    # return HttpResponse("Hello, world. You're at the polls index.")
    if json.loads(temp.rd0)['warning']['warningType']==0:
        temp.rd0=temp.randomdata(0)
    elif time.time()-json.loads(temp.rd0)['time']>timeinterval:
        temp.rd0=temp.randomdata(0)
    else:
        pass
    # return HttpResponse(temp.rd0)
    return temp.rd0

def data1():
    # return HttpResponse("Hello, world. You're at the polls index.")
    if json.loads(temp.rd1)['warning']['warningType']==0:
        temp.rd1=temp.randomdata(1)
    elif time.time()-json.loads(temp.rd1)['time']>timeinterval:
        temp.rd1=temp.randomdata(1)
    else:
        pass
    # return HttpResponse(temp.rd1)
    return temp.rd1

def data2():
    # return HttpResponse("Hello, world. You're at the polls index.")
    if json.loads(temp.rd2)['warning']['warningType']==0:
        temp.rd2=temp.randomdata(2)
    elif time.time()-json.loads(temp.rd2)['time']>timeinterval:
        temp.rd2=temp.randomdata(2)
    else:
        pass
    # return HttpResponse(temp.rd2)
    return temp.rd2


def data3():
    # return HttpResponse("Hello, world. You're at the polls index.")
    if json.loads(temp.rd3)['warning']['warningType']==0:
        temp.rd3=temp.randomdata(3)
    elif time.time()-json.loads(temp.rd3)['time']>timeinterval:
        temp.rd3=temp.randomdata(3)
    else:
        pass
    # return HttpResponse(temp.rd3)
    return temp.rd3


def info(request):
    if request.method=='POST':

        for k,v in {0:temp.rd0,1:temp.rd1,2:temp.rd2,3:temp.rd3}.items():
            if json.loads(v)['warning']['warningType']==0:
                temp.allcamera["camera"+str(k)]=0
            else:
                temp.allcamera["camera"+str(k)]=1

        return HttpResponse(json.dumps(temp.allcamera))
    else:
        return HttpResponse("forbiden, plz use POST method ")


def data(request):
    if request.method=='POST':
        try :
            b=request.body
            cid=str(b, encoding="utf-8")
            cid=eval(cid)['cid']
            if cid==0:
                return HttpResponse(data0())
            elif cid==1:
                return HttpResponse(data1())
            elif cid==2:
                return HttpResponse(data2())
            elif cid==3:
                return HttpResponse(data3())
            else:
                # return HttpResponse("invalid body cid : %s"%cid)
                return HttpResponse('invalid cid:%s'%cid)
        except Exception as e:
            return HttpResponse('invalid body: %s'%e)

    else:
        return HttpResponse("forbiden, plz use POST method with right HEADERS")


def index(request):
    # if request.method=='POST':
        # print("the POST method")
        # concat = request.POST
        # postBody = request.body
        # print(concat)
        # print(type(postBody))
        # # print(postBody)
        # return HttpResponse('''Get fatadata from ./cid=?   and
        #                         ? can be 0,1,2,3   and
        #                         Get all camerainfo from ./info''')
        # name=request.META.get('HTTP_CID')
        # return HttpResponse(name)

    # else:
    #     return HttpResponse('503 forbiden111')
    
    return HttpResponse("use POST method with HEADERS cid=[0,1,2,3] at url='./data'   and use POST method to gain all camerainfo at url='./info' ")


