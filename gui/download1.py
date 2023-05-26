import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import importlib

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

def download1(uid, token):
    def select_course():
        selected_course = numlist[check_box_var1.get()]
        returnlist['tutorid'] = courselist[selected_course]
        returnlist['courseid'] = idlist[selected_course]
        returnlist['name'] = selected_course
        root.destroy()
        returnlist['extensiveornot'] = 'True' if var.get() == 1 else 'False'

    root = ttk.Window(title='乐读视频下载器-下载', themename="morph")
    root.geometry('1280x720')
    data = get_course(uid, token)
    courselist, idlist, numlist, returnlist = {}, {}, [], {}
    var = ttk.IntVar()
    var.set(0)

    for course in data:
        courselist[course['courseName']] = course['tutorId']
        idlist[course['courseName']] = course['stdCourseId']

    check_box_var1 = ttk.IntVar()
    for index, course_name in enumerate(courselist):
        numlist.append(course_name)
        radiobutton = ttk.Radiobutton(text=course_name, bootstyle="primary-outline-toolbutton", variable=check_box_var1, value=index)
        radiobutton.pack(anchor='w')

    extensiveornot = ttk.Checkbutton(text='延伸课程', bootstyle="default-round-toggle", variable=var)
    extensiveornot.pack(anchor='w')
    submit = ttk.Button(text='提交', bootstyle="primary", command=select_course)
    submit.pack(anchor='w')
    root.mainloop()
    importlib.reload(ttk.style)
    return returnlist