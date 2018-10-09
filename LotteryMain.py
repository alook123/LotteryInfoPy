import os
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from bs4 import BeautifulSoup
from xlwt import *
from common import get,getColorStyle

 
qtCreatorFile = "untitled.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #获取当前时间并赋值
        now_day = time.strftime("%Y-%m-%d", time.localtime())
        self.dateEdit.setDate(QtCore.QDate.fromString(now_day, 'yyyy-MM-dd'))
        self.btnManualOpen.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        #获取dateEdit的时间
        yyyy = self.dateEdit.sectionText(self.dateEdit.sectionAt(0))
        mm=self.dateEdit.sectionText(self.dateEdit.sectionAt(1))
        dd=self.dateEdit.sectionText(self.dateEdit.sectionAt(2))
        datestr=yyyy+'-'+mm+'-'+dd

        book = Workbook() #创建一个Excel
        sheet1 = book.add_sheet('sheet1') #在其中创建一个sheet
        sheet1.write(0,0,'期数')
        sheet1.write(0,1,'时间')
        sheet1.write(0,2,'号码1')
        sheet1.write(0,3,'号码2')
        sheet1.write(0,4,'号码3')
        sheet1.write(0,5,'号码4')
        sheet1.write(0,6,'号码5')
        sheet1.write(0,7,'号码6')
        sheet1.write(0,8,'号码7')
        sheet1.write(0,9,'号码8')
        sheet1.write(0,10,'号码9')
        sheet1.write(0,11,'号码10')

        url="https://www.1396j.com/pk10/kaijiang?date="+datestr
        soup=BeautifulSoup(get(url))
        for index,item in enumerate(soup.select('#history tbody tr')):
            print(index)
            id= item.find("i", class_="font_gray666").string
            sheet1.write(index+1,0,id)
            date= item.find("i", class_="font_gray999").string
            sheet1.write(index+1,1,date)
            numstr=''
            listnum=[]
            count=0
            for index2,item2 in enumerate(item.find("div", class_="number_pk10").children):
                numstr+=item2.string.strip()
                if item2.string.strip()!='':
                    listnum.append(item2.string.strip())
                    style = getColorStyle(int(item2.string.strip()))
                    sheet1.write(index+1,count+2,item2.string.strip(),style=style)
                    count+=1
            print(listnum)
        book.save(datestr+'.xls')
        os.startfile(datestr+'.xls')

if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())