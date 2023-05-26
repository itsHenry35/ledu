from tkinter.ttk import Progressbar
from ttkbootstrap.constants import *
import requests
import os, sys
import subprocess
from pyaria2 import Aria2RPC
import ttkbootstrap as ttk
import time
import threading

def get_lecturers(course_list, user_id, access_token):
    url = "https://course-api-online.saasp.vdyoo.com/course/v1/student/course/user-live-list"
    global course_id, class_id, subject_id, tutor_id, lecturer_id, course_name
    course_id = course_list['courseid']
    tutor_id = course_list['tutorid']
    course_name = course_list['name']
    additional_data = f'?stuId={user_id}&stdCourseId={course_id}&type=1&needPage=1&page=1&perPage=500&order=asc'
    url += additional_data
    headers = {
        "Host": "course-api-online.saasp.vdyoo.com",
        "stuId": user_id,
        "resVer": "1.0.6",
        "terminal": "pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "token": access_token,
        "version": "3.21.0.84",
        "Referer": "https://speiyou.cn/",
    }
    response = requests.get(url, headers=headers)
    lecturers_data = response.json()
    class_id = lecturers_data[0]['stdClassId']
    subject_id = lecturers_data[0]['stdSubject']
    lecturer_id = lecturers_data[0]['lecturerId']
    return lecturers_data

def get_download_url(lecture, user_id, access_token):
    live_type = lecture['liveTypeString']
    headers = {
        "Host": "classroom-api-online.saasp.vdyoo.com",
        "stuId": user_id,
        "appClientType": "xes",
        "lecturerId": lecturer_id,
        "stdSubject": subject_id,
        "tutorId": tutor_id,
        "stdCourseId": course_id,
        "resVer": "1.0.6",
        "liveId": str(lecture['liveId']),
        "liveType": live_type,
        "terminal": "pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "stdClassId": class_id,
        "expireTime": "0",
        "token": access_token,
        "version": "3.21.0.84",
        "Referer": "https://speiyou.cn/",
    }
    if live_type == 'SMALL_GROUPS_V2_MODE':
        url = 'https://classroom-api-online.saasp.vdyoo.com/playback/v1/video/init'
        response = requests.get(url, headers=headers)
        video_data = response.json()
        video_url = ""
        error_message = ""
        try:
            video_url = video_data['videoUrls'][2]
            success = 'True'
        except:
            error_message = video_data['message']
            success = 'False'
    if live_type == 'RECORD_MODE':
        url = 'https://classroom-api-online.saasp.vdyoo.com/classroom-ai/record/v1/resources'
        response = requests.get(url, headers=headers)
        video_data = response.json()
        video_url = ""
        error_message = ""
        try:
            definitions = video_data['definitions']
            values = list(definitions.values())
            video_url = values[-1][0]
            success = 'True'
        except:
            error_message = video_data['message']
            success = 'False'
    return {
        "url": video_url,
        "success": success,
        "errmsg": error_message,
    }

def get_cram_class(course, user_id, access_token):
    url = "https://classroom-api-online.saasp.vdyoo.com/classroom/basic/v1/real-record/init/auth"
    if "tasks" not in course:
        ttk.dialogs.dialogs.Messagebox.ok("当前课程没有延申课程！", title='提示', alert=True, parent=None)
        sys.exit()
    additional_data = f'?curriculumId={course["tasks"][0]["curriculumId"]}&taskId={course["tasks"][0]["taskId"]}&taskTypeString=ONLINE_REAL_RECORD&coursewareId={course["tasks"][0]["coursewareId"]}'
    url += additional_data
    headers = {
        "stuId": user_id,
        "token": access_token,
        "terminal": "pc",
        "version": "3.25.0.170",
    }
    response = requests.get(url, headers=headers)
    live_id = response.json()['initData']['task']['realRecordId']
    url = 'https://classroom-api-online.saasp.vdyoo.com/classroom-ai/record/v1/resources'
    headers = {
        "lecturerId": lecturer_id,
        "liveId": str(live_id),
        "liveType": "ONLINE_REAL_RECORD",
        "stuId": user_id,
        "token": access_token,
    }
    response = requests.get(url, headers=headers)
    video_data = response.json()
    video_url = ""
    error_message = ""
    try:
        definitions = video_data['definitions']
        values = list(definitions.values())
        video_url = values[-1][0]
        success = 'True'
    except:
        error_message = video_data['message']
    return {
        "url": video_url,
        "success": success,
        "errmsg": error_message,
    }

def download2(course_list, user_id, access_token, aria2_path):
    gid_group = {}
    def aria2_download(link, path, filename):
        options = {"dir": path, "out": filename}
        download_ = jsonrpc.addUri([link], options=options)
        gid_group[filename] = download_
    def update_download_status():
        while True:
            for filename in gid_group:
                stat = jsonrpc.tellStatus(gid=str(gid_group[filename]))
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
    root = ttk.Window(title='乐读视频下载器-下载', themename="morph")
    root.geometry('1280x720')
    aria2process = subprocess.Popen(aria2_path + ' --enable-rpc --rpc-listen-port=6800 --max-connection-per-server=16 --file-allocation=none --max-concurrent-downloads=64', shell=True)
    time.sleep(1)
    jsonrpc = Aria2RPC()
    lecturers = get_lecturers(course_list, user_id, access_token)
    download_urls = {}
    extensive_or_not = course_list['extensiveornot']
    count = 1
    for lecture in lecturers:
        if extensive_or_not == 'False':
            result = get_download_url(lecture, user_id, access_token)
            filename = f'第{count}讲.mp4'
        if extensive_or_not == 'True':
            result = get_cram_class(lecture, user_id, access_token)
            filename = f'第{count}讲_延伸内容.mp4'
        download_urls[filename] = result
        count += 1
    count = 2
    tkinterlist = {}
    text = ttk.Label(text='下载中~')
    text.grid(row=1, column=0)
    for filename in download_urls:
        text = ttk.Label(text=filename)
        text.grid(row=count, column=0)
        progress = ttk.Progressbar(bootstyle="striped")
        progress.grid(row=count, column=1)
        progress.maximum = 100
        progress.value = 0
        text0 = ttk.Label(text='0%')
        text0.grid(row=count, column=2)
        text1 = ttk.Label(text='下载速度：Nah')
        text1.grid(row=count, column=3)
        tkinterlist[filename] = {
            'progress': progress,
            'percentage': text0,
            'speed': text1,
        }
        count += 1
    download_path = os.path.join('乐读-下载', course_name)
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    open_path_button = ttk.Button(text='打开下载目录', command=lambda: os.startfile(download_path))
    open_path_button.grid(row=count+1, column=0)
    for filename in download_urls:
         if download_urls[filename]['success'] == 'True':
                aria2_download(download_urls[filename]['url'], download_path, filename)
         else:
                tkinterlist[filename]['percentage'].configure(text='下载失败')
                tkinterlist[filename]['speed'].configure(text=download_urls[filename]['errmsg'])
    thread = threading.Thread(target=update_download_status)
    thread.setDaemon(True)
    thread.start()
    root.mainloop()
    aria2process.kill()
    return