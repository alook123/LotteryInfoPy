import sys
import time
from PyQt5 import QtCore, QtGui, uic
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from xlwt import *
import requests
 
qtCreatorFile = "untitled.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        now_day = time.strftime("%Y-%m-%d", time.localtime())
        self.dateEdit.setDate(QtCore.QDate.fromString(now_day, 'yyyy-MM-dd'))

        self.btnManualOpen.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
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
        book.save('new.xls')

def get(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    return res.text

def getColorStyle(color):
    colors = {
        0 : None,
        1 : 'yellow',
        2 : 'blue',
        3 : 'gray_ega',
        4 : 'orange',
        5 : 'dark_blue_ega',
        6 : 'purple_ega',
        7 : 'gray25',
        8 : 'red',
        9 : 'dark_red_ega',
        10 : 'green'
    }
    style = XFStyle()
    fnt = Font()                        # 创建一个文本格式，包括字体、字号和颜色样式特性                              
    fnt.name = u'微软雅黑'                # 设置其字体为微软雅黑                                 
    fnt.colour_index = 1                # 设置其字体颜色             
    style.font = fnt  
    pattern = Pattern()
    pattern.pattern = Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = Style.colour_map[colors.get(color,None)]
    style.pattern = pattern
    return style

if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())