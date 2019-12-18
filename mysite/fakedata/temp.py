# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2019-12-16 10:38:27
# @Last Modified by:   Nessaj
# @Last Modified time: 2019-12-17 15:59:04

import json
import time
import random

allcamera=dict()
allcamera["camera0"]=0
allcamera["camera1"]=0
allcamera["camera2"]=0
allcamera["camera3"]=0


def get_json(timestamp,location,cameraID,warningType,info=None):
    """
    产生json数据
    Args:
        timestamp:时间戳
        location:摄像头位置
        cameraID:摄像头唯一标识号ID
        warningType:{0:无异常
                     1:黑名单人
                     2:未知人
                     3:外来车
                     4:碰撞
                     5:火情（红外）}
        info:额外备注信息，默认为空
    Returns:
        返回json格式数据
        示例：
        {"time": 1576324177, "location": 1, "cameraID": 3, "warningType": 3, "info": "fakenews"}
    """
    data=dict()

    data['time']=timestamp
    data['location']=location
    data['cameraID']=cameraID
    warninglist=["No-Waring","BlackList","UnknowPerson","UnknowCar","CarCrash","Fire"]
    warning={'warningType':warningType,'warningEvnet':warninglist[warningType]}
    data['warning']=warning
    data['info']=info

    myjson=json.dumps(data)
    return myjson


def randomdata(cid=0):


    # if(random.randint(0,2)==0):
    #     timestamp=time.time()
    #     location=cid
    #     cameraID=cid
    #     allcamera["camera"+str(cameraID)]=1
    #     warningType=random.randint(0,4)
    #     infolist=['fake-data','pseudo-data','mock-data']
    #     info=infolist[random.randint(0,2)]
    #     randomjson=get_json(timestamp,location,cameraID,warningType,info)

    #     return randomjson
    # else:

    #     return None

    timestamp=time.time()
    location=cid
    cameraID=cid
    if(random.randint(0,2)==0):

        allcamera["camera"+str(cameraID)]=1
        warningType=random.randint(1,5)
        infolist=['fake-data','pseudo-data','mock-data']
        info=infolist[random.randint(0,2)]

    else:
        allcamera["camera"+str(cameraID)]=0
        warningType=0
        info="No-Waring"
    randomjson=get_json(timestamp,location,cameraID,warningType,info)
    return randomjson


rd0=randomdata(0)
rd1=randomdata(1)
rd2=randomdata(2)
rd3=randomdata(3)
