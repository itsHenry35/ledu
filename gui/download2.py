# import the things we need
from tkinter.ttk import Progressbar
from ttkbootstrap.constants import *
import requests
import os, sys
import subprocess
from pyaria2 import Aria2RPC
import ttkbootstrap as ttk
import time
import threading

def getlecturers(list, uid, token):
    url = "https://course-api-online.saasp.vdyoo.com/course/v1/student/course/user-live-list" #all the lecturers
    global courseid #used in getlecturerinfo
    global classid
    global subjectid
    global tutorid
    global lecturerid
    global name
    courseid = list['courseid']
    tutorid = list['tutorid']
    name = list['name'] #get the name of the course
    adddata = '?stuId='+ uid + '&stdCourseId=' + courseid + '&type=1&needPage=1&page=1&perPage=500&order=asc'
    url = url + adddata
    headers = {
        "Host": "course-api-online.saasp.vdyoo.com",
        "stuId": uid,
        "resVer": "1.0.6",
        "terminal": "pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "token": token,
        "version": "3.21.0.84",
        "Referer": "https://speiyou.cn/",
    }
    data = requests.get(url, headers = headers) # get lecturers
    json = data.json()
    classid = json[0]['stdClassId']
    subjectid = json[0]['stdSubject'] #get the classid and subjectid
    lecturerid = json[0]['lecturerId'] #get the lecturer id all from the first lecturer
    return json

def getdownloadurl(i, uid, token):
    type = i['liveTypeString']
    headers = {
        "Host": "classroom-api-online.saasp.vdyoo.com",
        "stuId": uid,
        "appClientType": "xes",
        "lecturerId": lecturerid,
        "stdSubject": subjectid,
        "tutorId": tutorid,
        "stdCourseId": courseid,
        "resVer": "1.0.6",
        "liveId": str(i['liveId']),
        "liveType": type,
        "terminal": "pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "stdClassId": classid,
        "expireTime": "0",
        "token": token,
        "version": "3.21.0.84",
        "Referer": "https://speiyou.cn/",
    }
    if type == 'SMALL_GROUPS_V2_MODE':
        url = 'https://classroom-api-online.saasp.vdyoo.com/playback/v1/video/init'
        data = requests.get(url, headers = headers) # get one lecturer info
        json = data.json()
        videourl = ""
        errmsg = ""
        try:
            videourl = json['videoUrls'][2] # get the download url of mp4 from the info
            success = 'True'
        except:
            errmsg = json['message']
            success = 'False'
    if type == 'RECORD_MODE':
        url = 'https://classroom-api-online.saasp.vdyoo.com/classroom-ai/record/v1/resources'
        data = requests.get(url, headers = headers) # get one recorded class info
        json = data.json()
        videourl = ""
        errmsg = ""
        try:
            definations = data.json()['definitions']
            values = list(definations.values())
            videourl = values[len(values)-1][0]
            success = 'True'
        except:
            errmsg = json['message']
            success = 'False'
    return {
        "url" : videourl,
        "success" : success,
        "errmsg" : errmsg,
    }

def getcramclass(course, uid, token):
    url = "https://classroom-api-online.saasp.vdyoo.com/classroom/basic/v1/real-record/init/auth"
    if "tasks" not in course:
        ttk.dialogs.dialogs.Messagebox.ok("当前课程没有延申课程！", title='提示', alert=True, parent=None, )
        sys.exit()
    adddata = '?curriculumId=' + course['tasks'][0]['curriculumId'] + '&taskId=' + course['tasks'][0]['taskId'] + '&taskTypeString=ONLINE_REAL_RECORD&coursewareId=' + course['tasks'][0]['coursewareId']
    url = url + adddata
    headers = {
    "stuId": uid,
    "token": token,
    "terminal" : "pc",
    "version" : "3.25.0.170",
    }
    data = requests.get(url, headers = headers) # get cram class info
    liveid = data.json()['initData']['task']['realRecordId']
    url = 'https://classroom-api-online.saasp.vdyoo.com/classroom-ai/record/v1/resources'
    headers = {
    "lecturerId": lecturerid,
    "liveId": str(liveid),
    "liveType": "ONLINE_REAL_RECORD",
    "stuId": uid,
    "token": token,
    }
    data = requests.get(url, headers = headers)
    json = data.json()
    videourl = ""
    errmsg = ""
    try:
        definations = data.json()['definitions']
        values = list(definations.values())
        videourl = values[len(values)-1][0]
        success = 'True'
    except:
        errmsg = json['message']
    return {
        "url" : videourl,
        "success" : success,
        "errmsg" : errmsg,
    }
    

def download2(list, uid, token, path__):
    gid_group = {}
    def aria2_download(link, path, filename):
        options = {"dir": path, "out": filename, }
        download_ = jsonrpc.addUri([link], options = options)
        gid_group[filename] = download_
    def get_stat():
        while True:
            for filename in gid_group:
                stat = jsonrpc.tellStatus(gid = str(gid_group[filename]))
                if stat['status'] != 'complete':
                    stat = jsonrpc.tellStatus(str(gid_group[filename]))
                    if int(stat['totalLength']) != 0 and int(stat['completedLength']) != 0:
                        tkinterlist[filename]['progress']['value'] = int(stat['completedLength']) / int(stat['totalLength']) * 100
                        tkinterlist[filename]['progress'].update()
                        tkinterlist[filename]['percentage'].configure(text=str("%.2f"%((int(stat['completedLength']) / int(stat['totalLength']) * 100))) + '%')
                        tkinterlist[filename]['speed'].configure(text='下载速度：' + str(round(int(stat['downloadSpeed'])/1024/1024, 2)) + 'MB/s')
                if stat['status'] == 'complete':
                    tkinterlist[filename]['progress']['value'] = 100
                    tkinterlist[filename]['progress'].update()
                    tkinterlist[filename]['percentage'].configure(text='100%')
                    tkinterlist[filename]['speed'].configure(text='已完成')
            time.sleep(0.1)
    root = ttk.Window(title = '乐读视频下载器-下载', themename="morph")
    root.geometry('1280x720')
    aria2process = subprocess.Popen(path__ + ' --enable-rpc --rpc-listen-port=6800 --max-connection-per-server=16 --file-allocation=none --max-concurrent-downloads=64',shell=True)
    time.sleep(1) #wait because rpc will take some time to start
    jsonrpc = Aria2RPC()
    lecturers = getlecturers(list, uid, token)
    downloadurls = {}
    extensiveornot = list['extensiveornot']
    count = 1
    for i in lecturers:
        if extensiveornot == 'False':
            result = getdownloadurl(i, uid, token)
            filename = '第'+ str(count) + '讲.mp4'
        if extensiveornot == 'True':
            result = getcramclass(i, uid, token)
            filename = '第'+ str(count) + '讲_延伸内容.mp4'
        downloadurls[filename] = result
        count += 1
    count = 2
    tkinterlist = {}
    text = ttk.Label(text = '下载中~')
    text.grid(row=1, column=0)
    for i in downloadurls:
        text = ttk.Label(text = i)
        text.grid(row=count, column=0)
        progress = ttk.Progressbar(bootstyle="striped")
        progress.grid(row=count, column=1)
        progress.maximum = 100
        progress.value = 0
        text0 = ttk.Label(text = '0%')
        text0.grid(row=count, column=2)
        text1 = ttk.Label(text = '下载速度：Nah')
        text1.grid(row=count, column=3)
        tkinterlist[i] = {
            'progress': progress,
            'percentage': text0,
            'speed': text1,
        }
        count += 1
    path = os.path.join('乐读-下载', name) #create a folder to store the downloaded files
    if not os.path.exists(path):
        os.makedirs(path)
    openpathbutton = ttk.Button(text = '打开下载目录', command = lambda: os.startfile(path))
    openpathbutton.grid(row=count+1, column=0)
    for i in downloadurls:
         if downloadurls[i]['success'] == 'True':
                aria2_download(downloadurls[i]['url'], path, i)
         else:
                tkinterlist[i]['percentage'].configure(text='下载失败')
                tkinterlist[i]['speed'].configure(text=downloadurls[i]['errmsg'])
    thread = threading.Thread(target=get_stat)
    thread.setDaemon(True)
    thread.start()
    root.mainloop()
    aria2process.kill()
    return