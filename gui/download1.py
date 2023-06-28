import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib
from tkinter.filedialog import askdirectory
import tkinter.messagebox as mb

def get_course(uid, token):
    url = "https://course-api-online.saasp.vdyoo.com/course/v1/student/course/list"
    headers = {
        "Host": "course-api-online.saasp.vdyoo.com",
        "stuId": uid,
        "resVer": "1.0.6",
        "terminal": "pc",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "expireTime": "0",
        "branchId": "",
        "token": token,
        "version": "3.21.0.84",
        "Referer": "https://speiyou.cn/",
    }
    additional_data = f'?stuId={uid}&courseStatus=0&stdSubject=&page=1&perPage=500&order=asc'
    url += additional_data
    response = requests.get(url, headers=headers)
    return response.json()

def select_path():
    global path
    path = askdirectory()

def download1(uid, token):
    global path
    def submit():
        count = 0
        for i, widget in enumerate(widgetlist):
            if 'selected' in widget.state():
                returnlist.append({})
                returnlist[count]['tutorid'] = courselist[numlist[i]]
                returnlist[count]['courseid'] = idlist[numlist[i]]
                returnlist[count]['name'] = numlist[i]
                returnlist[count]['extensiveornot'] = 'True' if var.get() == 1 else 'False'
                count+=1
        if count == 0:
            mb.showwarning(title='警告', message='未选择课程')
        else:
            root.destroy()


    root = ttk.Window(title='乐读视频下载器-下载', themename="morph")
    root.geometry("")
    data = get_course(uid, token)
    courselist, idlist, numlist, returnlist = {}, {}, [], []
    var = ttk.IntVar()
    var.set(0)
    path = ""

    for course in data:
        courselist[course['courseName']] = course['tutorId']
        idlist[course['courseName']] = course['stdCourseId']

    widgetlist = []
    for course_name in courselist:
        numlist.append(course_name)
        checkbutton = ttk.Checkbutton(text=course_name, bootstyle="round-toggle")
        checkbutton.pack(anchor='w')
        widgetlist.append(checkbutton)

    extensiveornot = ttk.Checkbutton(text='延伸课程', bootstyle="default-square-toggle", variable=var)
    extensiveornot.pack(anchor='w')
    submit = ttk.Button(text='提交', bootstyle="primary", command=submit)
    submit.pack(anchor='w')
    selectpath = ttk.Button(text='选择自定义路径（可不选，默认为程序所在目录）', bootstyle="primary-outline-toolbutton", command=select_path)
    selectpath.pack(anchor='w')
    root.mainloop()
    importlib.reload(ttk.style)
    return returnlist, path