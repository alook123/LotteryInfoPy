import os
import sys
import time
import datetime #导入日期时间模块
import threading
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from bs4 import BeautifulSoup
from xlwt import *
import xlrd
from common import get,getColorStyle
from configparser import ConfigParser

qtCreatorFile = "untitled.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
cfg = ConfigParser()
cfg.read('config.ini')

 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    excelPath=''
    autoexcelpath=''
    now_day = datetime.date.today() #获得今天的日期
    today=str(now_day.year)+'-'+str(now_day.month)+'-'+str(now_day.day)
    yesterday = now_day - datetime.timedelta(days=1)
    yesterdayStr=str(yesterday.year)+'-'+str(yesterday.month)+'-'+str(yesterday.day)
    beforeday = now_day - datetime.timedelta(days=2)
    beforedayStr=str(beforeday.year)+'-'+str(beforeday.month)+'-'+str(beforeday.day)
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #获取当前时间并赋值
        #now_day = time.strftime("%Y-%m-%d", time.localtime())
        now_day = datetime.date.today() #获得今天的日期
        today=str(now_day.year)+'-'+str(now_day.month)+'-'+str(now_day.day)
        self.dateEdit.setDate(QtCore.QDate.fromString(today, 'yyyy-MM-dd'))
        self.btnSetDir.clicked.connect(self.SetDir)
        self.btnAutoDir.clicked.connect(self.LookDir)
        self.btnManualOpen.clicked.connect(self.LookExcelByDate)
        self.excelPath= path = os.path.abspath(cfg.get('path','excelPath'))
        self.autoexcelpath=path = os.path.abspath(cfg.get('path','autoexcelpath'))

        if not os.path.exists(self.excelPath):
            os.makedirs(self.excelPath)    
        if not os.path.exists(self.autoexcelpath):
            os.makedirs(self.autoexcelpath)  

        self.createExcel()
        t = threading.Thread(target=self.AutoSynchronize)
        t.start()
        #self.AutoSynchronize()

    def AutoSynchronize(self):
<<<<<<< HEAD
        if not os.path.isfile(self.autoexcelpath+'/'+self.yesterdayStr+'.xls'):
            book = Workbook() #创建一个Excel
            sheet1 = book.add_sheet('sheet1') #在其中创建一个sheet
            book.save(self.autoexcelpath+'/'+self.yesterdayStr+'.xls')
            self.WriteExcel(self.yesterdayStr,self.autoexcelpath)
        if not os.path.isfile(self.autoexcelpath+'/'+self.beforedayStr+'.xls'):
            book = Workbook() #创建一个Excel
            sheet1 = book.add_sheet('sheet1') #在其中创建一个sheet
            book.save(self.autoexcelpath+'/'+self.beforedayStr+'.xls')
=======
        if not os.path.isfile(self.autoexcelpath+'\\'+self.yesterdayStr+'.xls'):
            book = Workbook() #创建一个Excel
            sheet1 = book.add_sheet('sheet1') #在其中创建一个sheet
            book.save(self.autoexcelpath+'\\'+self.yesterdayStr+'.xls')
            self.WriteExcel(self.yesterdayStr,self.autoexcelpath)
        if not os.path.isfile(self.autoexcelpath+'\\'+self.beforedayStr+'.xls'):
            book = Workbook() #创建一个Excel
            sheet1 = book.add_sheet('sheet1') #在其中创建一个sheet
            book.save(self.autoexcelpath+'\\'+self.beforedayStr+'.xls')
>>>>>>> origin/master
            self.WriteExcel(self.beforedayStr,self.autoexcelpath)
        while True:
            self.WriteExcel(self.today,self.autoexcelpath)
            time.sleep(60*5)
        
        

    def createExcel(self):
<<<<<<< HEAD
        if not os.path.isfile(self.autoexcelpath+'/'+self.today+'.xls'):
            book = Workbook() #创建一个Excel
            sheet1 = book.add_sheet('sheet1') #在其中创建一个sheet
            book.save(self.autoexcelpath+'/'+self.today+'.xls')
=======
        if not os.path.isfile(self.autoexcelpath+'\\'+self.today+'.xls'):
            book = Workbook() #创建一个Excel
            sheet1 = book.add_sheet('sheet1') #在其中创建一个sheet
            book.save(self.autoexcelpath+'\\'+self.today+'.xls')
>>>>>>> origin/master

    def LookDir(self):
        path = os.path.abspath(self.autoexcelpath)
        os.system("explorer.exe "+path)

    def SetDir(self):
        directory1 = QtWidgets.QFileDialog.getExistingDirectory(self,"选取文件夹","./") #起始路径
        self.autoexcelpath=directory1
        cfg.set('path','autoexcelpath',self.autoexcelpath)
        # write to file
        with open("config.ini","w+") as f:
            cfg.write(f)

    def WriteExcel(self,datestr,filepath):
<<<<<<< HEAD
        data = xlrd.open_workbook(filepath+'/'+datestr+'.xls')
        table = data.sheets()[0] 
        rows=table.nrows   #获取行数
        cols=table.ncols    #获取列数
        userstr=''
        if rows > 0 :
            userstr = table.row(0)[0].value
=======
        print("时间:"+str(datestr))
        print("文件夹:"+str(datestr))
        userstr=''
        if not os.path.isfile(self.autoexcelpath+'\\'+self.beforedayStr+'.xls'):
            data = xlrd.open_workbook(filepath+'\\'+datestr+'.xls')
            table = data.sheets()[0] 
            rows=table.nrows   #获取行数
            cols=table.ncols    #获取列数
            if rows > 0 :
                userstr = table.row(0)[0].value
>>>>>>> origin/master

        book = Workbook() #创建一个Excel
        sheet1 = book.add_sheet('sheet1') #在其中创建一个sheet

        sheet1.write_merge(0,2,0,11,userstr)

        sheet1.write(3,0,'期数')
        sheet1.write(3,1,'时间')
        sheet1.write(3,2,'号码1')
        sheet1.write(3,3,'号码2')
        sheet1.write(3,4,'号码3')
        sheet1.write(3,5,'号码4')
        sheet1.write(3,6,'号码5')
        sheet1.write(3,7,'号码6')
        sheet1.write(3,8,'号码7')
        sheet1.write(3,9,'号码8')
        sheet1.write(3,10,'号码9')
        sheet1.write(3,11,'号码10')

        url="https://www.1396j.com/pk10/kaijiang?date="+datestr
        soup=BeautifulSoup(get(url))
        for index,item in enumerate(soup.select('#history tbody tr')):
            id= item.find("i", class_="font_gray666").string
            sheet1.write(index+4,0,id)
            date= item.find("i", class_="font_gray999").string
            sheet1.write(index+4,1,date)
            numstr=''
            listnum=[]
            count=0
            for index2,item2 in enumerate(item.find("div", class_="number_pk10").children):
                numstr+=item2.string.strip()
                if item2.string.strip()!='':
                    listnum.append(item2.string.strip())
                    #style = getColorStyle(int(item2.string.strip()))
                    style1 = easyxf(num_format_str='0')#数据格式设置
                    sheet1.write(index+4,count+2,int(item2.string.strip()),style=style1)
                    count+=1
<<<<<<< HEAD
        book.save(filepath+'/'+datestr+'.xls')
=======
        print("保存路径:"+filepath+'\\'+datestr+'.xls')
        book.save(filepath+'\\'+datestr+'.xls')
>>>>>>> origin/master

    def LookExcelByDate(self):
        #获取dateEdit的时间
        yyyy = self.dateEdit.sectionText(self.dateEdit.sectionAt(0))
        mm=self.dateEdit.sectionText(self.dateEdit.sectionAt(1))
        dd=self.dateEdit.sectionText(self.dateEdit.sectionAt(2))
        datestr=yyyy+'-'+mm+'-'+dd

        self.WriteExcel(datestr,self.excelPath)
<<<<<<< HEAD
        path = os.path.abspath(self.excelPath+'/'+datestr+'.xls')
=======
        path = os.path.abspath(self.excelPath+'\\'+datestr+'.xls')
>>>>>>> origin/master
        os.startfile(path)

if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())