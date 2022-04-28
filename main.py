# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter.ttk import Combobox
import cryptography
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

name = ""
uid = ""

host = "localhost"
user = "root"
password = "********"
dbname = "system_choose_course"
def update_info(v, e):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "UPDATE studentinfo SET {}='{}' WHERE sid='{}'"
        cur.execute(sql.format(v, e, uid))
        db.commit()
        print("successful", "更新成功")
    except pymysql.Error as e:
        print("unsuccessful", "更新失败" + str(e))
        db.rollback()
    db.close()


def person_info():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT * FROM studentinfo where sid = '{}'"
        cur.execute(sql.format(uid))
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()


def update_it(win):
    root = Toplevel(win)
    root.title("change_info")
    root.geometry("500x230")
    Label(root, text="{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}".format(
        "学生编号", "专业", "姓名", "学院", "性别", "出生日期")).grid(row=0, column=0, columnspan=2,
                                                      pady=9, sticky="w")
    var = StringVar()
    rels = person_info()
    cb = Combobox(root, textvariable=var, width=17)
    cb["value"] = ("major", "dept", "gender", "birthday")
    i = 1
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5]))
        Label(root, text=s1).grid(row=i, column=0, columnspan=2, padx=5, pady=30, sticky="w")
        i = i + 1
    e1 = Entry(root)
    Label(root, text="请选择将要修改的信息").grid(padx=5, row=i, pady=8, column=0, sticky="e")
    cb.grid(padx=5, row=i, column=1, pady=8, sticky="w")
    i = i + 1
    Label(root, text="请输入要修改的值").grid(padx=5, row=i, column=0, sticky="e")
    e1.grid(padx=5, row=i, column=1, sticky="w")
    Button(root, text="提交", command=lambda: update_info(var, e1)).grid(row=i + 1, column=0, columnspan=2)


def insert_course(e):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "INSERT INTO sc(sId,cId) VALUES (%s,%s)"
        value = (uid, e)
        cur.execute(sql, value)
        db.commit()
        print("successful", "插入成功")
    except pymysql.Error as e:
        print("unsuccessful", "插入失败" + str(e))
        db.rollback()
    db.close()

def quit_course(e):
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname, )
        cur = db.cursor()
        sql = "DELETE FROM sc WHERE (sId,cId) = (%s,%s)"
        value = (uid, e)
        cur.execute(sql, value)
        db.commit()
        print("successful", "退课成功")
    except pymysql.Error as e:
        print("unsuccessful", "退课失败" + str(e))
        db.rollback()
    db.close()


def cour_all():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT courseinfo.*,teacherinfo. tname ,classroom_arr. crId FROM courseinfo,teach, teacherinfo,classroom,classroom_arr WHERE  teach. tId =teacherinfo. tId  AND classroom. crId =classroom_arr. crId  AND classroom_arr. cId =courseinfo. cId  AND teach. cId =courseinfo. cId  ORDER BY courseinfo. cId  "
        cur.execute(sql)
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()


def choose_course(win):
    rels = cour_all()
    i = 1
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}{:>14}{:>14}{:>14}{:>14}{:>14}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5], rel[6], rel[7]))

        i = i + 1
    ee = Entry(root)

    Button(root, text="提交", command=lambda: insert_course(ee)).grid(row=i + 1, column=0, columnspan=2)


def chaKe():
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        print("数据库连接成功")
        cur = db.cursor()
        sql = "SELECT studentinfo.sId,studentinfo.name,courseinfo.cName,courseinfo.cId,courseinfo.cIntro,courseinfo.cCredit,courseinfo.cWeek,teacherinfo.tName,classroom.crId FROM studentinfo, sc,courseinfo,teach, teacherinfo,classroom,classroom_arr WHERE studentinfo.sId = sc.sId AND courseinfo.cId=sc.cId AND  teach.tId=teacherinfo.tId AND classroom.crId=classroom_arr.crId AND classroom_arr.cId=courseinfo.cId AND teach.cId=courseinfo.cId AND studentinfo.name = '%s' "
        cur.execute((sql % name))
        results = cur.fetchall()
        return results

    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()


def stu_course(win):
    root = Toplevel(win)
    root.title("stu_course")
    root.geometry("600x500")
    Label(root, text="学生学号   学生姓名   课程名称    课程id       课程介绍      课程学分    课程星期    老师姓名    班级号").pack(padx=5, pady=14,
                                                                                                    anchor="nw")
    rels = chaKe()
    for rel in rels:
        s1 = (
            "{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}{:<14}".format(
                rel[0], rel[1], rel[2], rel[3], rel[4], rel[5], rel[6], rel[7], rel[8]))
        Label(root, text=s1).pack(padx=5, pady=14, anchor="nw")


def update_sql(table, pwd0, pwd1, pwd2):
    if pwd0 != widgets.pwd.text():
        tkinter.messagebox.showwarning("error", "原密码错误")
    if pwd1 == "":
        tkinter.messagebox.showwarning("error", "请不要输入空值")
    elif pwd2 != pwd1:
        tkinter.messagebox.showwarning("error", "上下密码不相等")
    else:
        try:
            db = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=dbname,
                                 )
            cur = db.cursor()
            sql = "UPDATE " + table + " SET pwd= " + pwd1 + " WHERE name= " + "'" + name + "'"
            cur.execute(sql)
            db.commit()
            tkinter.messagebox.showinfo("成功", "修改成功")
        except pymysql.Error as e:
            print(e)
            tkinter.messagebox.showinfo("失败", "修改失败")
            db.rollback()
        db.close()


def change_password(win, table):
    change_pwd = Toplevel(win)
    change_pwd.title("登录")
    change_pwd.geometry("350x200")
    idE = Entry(change_pwd, width=30)
    pwdE = Entry(change_pwd, width=30)
    Label(change_pwd, text="修改密码", font="微软雅黑 14").grid(row=0, column=0, columnspan=2, sticky="w",
                                                        pady=10)
    Label(change_pwd, text="新密码", font="微软雅黑 14").grid(row=1, column=0, sticky="w")
    idE.grid(row=1, column=1, sticky="e", padx=40)
    Label(change_pwd, text="确认密码", font="微软雅黑 14").grid(row=2, column=0, sticky="w")
    pwdE.grid(row=2, column=1, sticky="e", padx=40)
    Button(change_pwd, text="修改", font="微软雅黑 10", relief="solid",
           command=lambda: update_sql(table, pwdE.get(), idE.get())).grid(row=3, column=0,
                                                                          columnspan=2,
                                                                          pady=20,
                                                                          padx=20)


def admin_operate():
    admin_log = Tk()
    admin_log.title("管理员操作台")
    admin_log.geometry("310x310")
    Label(admin_log, text="Hello," + name + "\n请选择您的操作\n"
          , font="微软雅黑 14", justify=LEFT).grid(row=0, column=0, columnspan=2, sticky='w')
    Button(admin_log, text="增加学生", font="微软雅黑 12").grid(row=1, column=0, sticky="w")
    Button(admin_log, text="增加老师", font="微软雅黑 12").grid(row=1, column=1, padx=90)
    Button(admin_log, text="修改老师信息", font="微软雅黑 12").grid(row=2, column=0, sticky="w", pady=10)
    Button(admin_log, text="修改学生信息", font="微软雅黑 12").grid(row=2, column=1, padx=90)
    Button(admin_log, text="给老师加课", font="微软雅黑 12").grid(row=3, column=0, sticky="w")
    Button(admin_log, text="给学生加课", font="微软雅黑 12").grid(row=3, column=1, padx=90)
    Button(admin_log, text="修改成绩", font="微软雅黑 12").grid(row=4, column=0, sticky="w")
    Button(admin_log, text="修改密码", font="微软雅黑 12").grid(row=4, column=1, padx=90, pady=10)
    Button(admin_log, text="增加课程", font="微软雅黑 12").grid(row=5, column=0, sticky="w")


def teacher_operate():
    teacher_log = Tk()
    teacher_log.title("老师操作台")
    teacher_log.geometry("250x220")
    Label(teacher_log, text="Hello," + name + "\n请选择您的操作\n"
          , font="微软雅黑 12", justify=LEFT).grid(row=0, column=0, columnspan=2, sticky="w", pady=10)
    Button(teacher_log, text="修改密码", font="微软雅黑 12", relief="solid",
           command=lambda: change_password(teacher_log, "teacherpwd")).grid(row=1, column=0)
    Button(teacher_log, text="输入成绩", font="微软雅黑 12", relief="solid").grid(row=1, column=1, sticky="e", padx=80)
    Button(teacher_log, text="查看课程信息", font="微软雅黑 12", relief="solid").grid(row=2, column=1)
    Button(teacher_log, text="修改信息", font="微软雅黑 12", relief="solid").grid(row=2, column=0, pady=20)


def stu_operate():
    stu_log = Tk()
    stu_log.title("学生操作台")
    stu_log.geometry("250x220")
    Label(stu_log, text="Hello," + name + "\nchoose your choices\n"
          , font="微软雅黑 12", justify=LEFT).grid(row=0, column=0, columnspan=2, sticky="w", pady=10)
    Button(stu_log, text="修改密码", font="微软雅黑 12", relief="solid",
           command=lambda: change_password(stu_log, "stupwd")).grid(row=1, column=0)
    Button(stu_log, text="选课", font="微软雅黑 12", relief="solid", command=lambda: choose_course(stu_log)).grid(row=1,
                                                                                                            column=1,
                                                                                                            padx=80,
                                                                                                            sticky="e")
    Button(stu_log, text="查课", font="微软雅黑 12", relief="solid", command=lambda: stu_course(stu_log)).grid(row=2,
                                                                                                         column=0,
                                                                                                         pady=20,
                                                                                                         sticky="w")
    Button(stu_log, text="修改信息", font="微软雅黑 12", relief="solid", command=lambda: update_it(stu_log)).grid(row=2,
                                                                                                          column=1)


def check_pwd(s1, s2, DB):
    global name
    global uid
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=dbname,
                             )
        cur = db.cursor()
        sql = "select * from " + DB + " where id= " + s1 + " and " + " pwd= " + s2
        marked = cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            uid = row[0]
            name = row[2]
        return marked
    except pymysql.Error as e:
        print("数据查询失败" + str(e))
    db.close()


def checkInfo(kind):
    Id = widgets.id.text()
    pwd = widgets.pwd.text()
    if kind == "student login":
        marked = check_pwd(Id, pwd, "stupwd")
        if marked:
            # 这里进入学生选课操作界面
            print(name + " login successfully")
            widgets.welcome.setText("Welcome to course choose system " + name)
            widgets.stackedWidget.setCurrentWidget(widgets.student_table)
        else:
            messagebox.showerror("error", "password is not right,please input again")

    elif kind == "teacher login":
        marked = check_pwd(Id, pwd, "teacherpwd")
        if marked:
            print(name)
            widgets.welcome_2.setText("Welcome to course choose system Teacher version Dr." + name)
            widgets.stackedWidget.setCurrentWidget(widgets.teacher_table)
        else:
            messagebox.showerror("error", "password is not right,please input again")
    else:
        marked = check_pwd(Id, pwd, "adminpwd")
        if marked:
            print(name)
            widgets.welcome_3.setText("Welcome to course choose system Agent version " + name)
            widgets.stackedWidget.setCurrentWidget(widgets.agent_table)
        else:
            messagebox.showerror("error", "password is not right,please input again")




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Course-Choose-System"
        description = "Course-Choose-System based on PyDracula"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.login_page)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.btn_share.clicked.connect(self.buttonClick)
        widgets.pushButton.clicked.connect(self.buttonClick)
        widgets.btn_student_login.clicked.connect(self.buttonClick)
        widgets.btn_course_check.clicked.connect(self.buttonClick)
        widgets.btn_pwd_change.clicked.connect(self.buttonClick)
        widgets.btn_pwd_change_confirm.clicked.connect(self.buttonClick)
        widgets.btn_course_choose.clicked.connect(self.buttonClick)
        widgets.confirm_btn.clicked.connect(self.buttonClick)
        widgets.btn_teacher_login.clicked.connect(self.buttonClick)
        widgets.btn_agent_login.clicked.connect(self.buttonClick)
        widgets.btn_pwd_change_2.clicked.connect(self.buttonClick)
        widgets.btn_info_change.clicked.connect(self.buttonClick)
        widgets.btn_info_change_confirm_3.clicked.connect(self.buttonClick)
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.login_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.student_table) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        if btnName == "btn_save":
            print("Save BTN clicked!")
        if btnName == "btn_student_login":
            checkInfo('student login')
        if btnName == "btn_teacher_login":
            checkInfo('teacher login')
        if btnName == "btn_agent_login":
            checkInfo('agent')

        # PRINT BTN NAME
        if btnName == "btn_course_check":
            widgets.stackedWidget.setCurrentWidget(widgets.check_page)  # SET PAGE
            rels = chaKe()
            i = 1
            for rel in rels:
                s1 = (
                    "{:<14}{:<14}{:<14}{:>14}{:>14}{:>14}{:>14}{:>14}".format(
                        rel[0], rel[1], rel[2], rel[3], rel[4], rel[5], rel[6], rel[7]))
                row_number = i
                widgets.course_display.insertRow(row_number)
                widgets.course_display.setItem(row_number, 0, QTableWidgetItem(str(rel[0])))
                widgets.course_display.setItem(row_number, 1, QTableWidgetItem(str(rel[1])))
                widgets.course_display.setItem(row_number, 2, QTableWidgetItem(str(rel[2])))
                widgets.course_display.setItem(row_number, 3, QTableWidgetItem(str(rel[3])))
                widgets.course_display.setItem(row_number, 4, QTableWidgetItem(str(rel[4])))
                widgets.course_display.setItem(row_number, 5, QTableWidgetItem(str(rel[5])))
                widgets.course_display.setItem(row_number, 6, QTableWidgetItem(str(rel[6])))
                widgets.course_display.setItem(row_number, 7, QTableWidgetItem(str(rel[7])))
                widgets.course_display.setItem(row_number, 8, QTableWidgetItem(str(rel[8])))
                i = i + 1
        if btnName == "btn_pwd_change":
            widgets.stackedWidget.setCurrentWidget(widgets.pwd_change_page)  # SET PAGE
        if btnName == "btn_pwd_change_confirm":
            update_sql("stupwd", widgets.pwd_current.text(), widgets.pwd_new.text(), widgets.pwd_new_check.text())
            widgets.stackedWidget.setCurrentWidget(widgets.student_table)  # SET PAGE

        if btnName == "btn_course_choose":
            widgets.stackedWidget.setCurrentWidget(widgets.choose_course_page)  # SET PAGE
            rels = cour_all()
            i = 1
            for rel in rels:
                row_number = i
                widgets.course_all_display.insertRow(row_number)
                widgets.course_all_display.setItem(row_number, 0, QTableWidgetItem(str(rel[0])))
                widgets.course_all_display.setItem(row_number, 1, QTableWidgetItem(str(rel[1])))
                widgets.course_all_display.setItem(row_number, 2, QTableWidgetItem(str(rel[2])))
                widgets.course_all_display.setItem(row_number, 3, QTableWidgetItem(str(rel[3])))
                widgets.course_all_display.setItem(row_number, 4, QTableWidgetItem(str(rel[4])))
                widgets.course_all_display.setItem(row_number, 5, QTableWidgetItem(str(rel[5])))
                widgets.course_all_display.setItem(row_number, 6, QTableWidgetItem(str(rel[6])))
                widgets.course_all_display.setItem(row_number, 7, QTableWidgetItem(str(rel[7])))
                i = i + 1
        if btnName == "confirm_btn":
            if widgets.choose_check_btn.isChecked() and not widgets.quit_check_btn.isChecked():
              print(uid + 'insert' + 'course' + widgets.course_id.text())
              insert_course(widgets.course_id.text())
            elif widgets.quit_check_btn.isChecked() and not widgets.choose_check_btn.isChecked():
              print(uid + 'quit' + 'course' + widgets.course_id.text())
              quit_course(widgets.course_id.text())
            else:
              print("error")

        if btnName == "btn_info_change":
              infs = person_info()
              for inf in infs:
                  i = 1
                  row_number = i
                  widgets.student_info.insertRow(row_number)
                  widgets.student_info.setItem(row_number, 0, QTableWidgetItem(str(inf[0])))
                  widgets.student_info.setItem(row_number, 1, QTableWidgetItem(str(inf[1])))
                  widgets.student_info.setItem(row_number, 2, QTableWidgetItem(str(inf[2])))
                  widgets.student_info.setItem(row_number, 3, QTableWidgetItem(str(inf[3])))
                  widgets.student_info.setItem(row_number, 4, QTableWidgetItem(str(inf[4])))
                  widgets.student_info.setItem(row_number, 5, QTableWidgetItem(str(inf[5])))
                  i = i + 1
              widgets.stackedWidget.setCurrentWidget(widgets.info_page)

        if btnName == "btn_info_change_confirm_3":
            update_info(widgets.select_info.currentText(), widgets.changed_info.text())

        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
