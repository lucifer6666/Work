import sys
from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery,QSqlTableModel
from PyQt4.QtGui import QTableView,QApplication
import sqlite3
from tkinter import *
from PyQt4 import QtGui,QtCore,QtSql
from datetime import *
global nameg
global compg
global mnog
global extrag
conn = sqlite3.connect('test.db')
cursor=conn.execute("CREATE TABLE IF NOT EXISTS COMPANY2(ORDER_NO VARCHAR PRIMARY KEY NOT NULL, ORDER_DATE VARCHAR, RETURNING_DATE VARCHAR, NAME VARCHAR, PHONE_NO VARCHAR, ADDRESS VARCHAR, PARTICULARS VARCHAR, QUANTITY VARCHAR, STD_PRICE VARCHAR, AMOUNT VARCHAR, TOTAL_AMOUNT VARCHAR);")
class Neworder(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Neworder,self).__init__(parent)
        self.setGeometry(150,150,960,630)
        self.setWindowTitle('New Order')
        self.setWindowIcon(QtGui.QIcon('logo1.png'))
        self.name=QtGui.QLabel('Name',self)
        self.name.setGeometry(10,100,60,30)
        self.name1=QtGui.QLineEdit('',self)
        self.name1.setGeometry(80,100,250,30)
        self.order=QtGui.QLabel('Order No.',self)
        self.order.setGeometry(520,100,60,30)
        a=datetime.now()
        dat=a.strftime('U%dS%Y%H%M%S')
        self.order1=QtGui.QLabel(dat,self)
        self.order1.setGeometry(600,100,250,30)
        datcur=a.strftime('%d/%m/%Y')
        self.curdat=QtGui.QLabel('Date : '+datcur,self)
        self.curdat.setGeometry(780,100,180,30)
        self.redat=QtGui.QLabel('Returning Date:',self)
        self.redat.setGeometry(520,140,150,30)
        self.redate=QtGui.QLineEdit(datcur,self)
        self.redate.setGeometry(670,140,100,30)
        self.add=QtGui.QLabel('Adderess',self)
        self.add.setGeometry(10,135,60,30)
        self.add1=QtGui.QLineEdit('',self)
        self.add1.setGeometry(80,135,250,30)
        self.no=QtGui.QLabel('Phone No.',self)
        self.no.setGeometry(10,170,60,30)
        self.no1=QtGui.QLineEdit('',self)
        self.no1.setGeometry(80,170,250,30)
        self.sno=QtGui.QLabel('S.No.',self)
        self.sno.setGeometry(10,220,40,30)
        self.sno1=QtGui.QLineEdit('',self)
        self.sno1.setGeometry(10,255,100,30)
        self.sno2=QtGui.QLineEdit('',self)
        self.sno2.setGeometry(10,290,100,30)
        self.sno3=QtGui.QLineEdit('',self)
        self.sno3.setGeometry(10,325,100,30)
        self.product=QtGui.QLabel('Particulars',self)
        self.product.setGeometry(120,220,80,30)
        self.product1=QtGui.QLineEdit('',self)
        self.product1.setGeometry(120,255,290,30)
        self.product2=QtGui.QLineEdit('',self)
        self.product2.setGeometry(120,290,290,30)
        self.product3=QtGui.QLineEdit('',self)
        self.product3.setGeometry(120,325,290,30)
        self.stdp=QtGui.QLabel('Std Price Q/P',self)
        self.stdp.setGeometry(420,220,80,30)
        self.stdp1=QtGui.QLineEdit('',self)
        self.stdp1.setGeometry(420,255,190,30)
        self.stdp2=QtGui.QLineEdit('',self)
        self.stdp2.setGeometry(420,290,190,30)
        self.stdp3=QtGui.QLineEdit('',self)
        self.stdp3.setGeometry(420,325,190,30)
        self.quantity=QtGui.QLabel('Quantity',self)
        self.quantity.setGeometry(620,220,70,30)
        self.quantity1=QtGui.QLineEdit('',self)
        self.quantity1.setGeometry(620,255,170,30)
        self.quantity2=QtGui.QLineEdit('',self)
        self.quantity2.setGeometry(620,290,170,30)
        self.quantity3=QtGui.QLineEdit('',self)
        self.quantity3.setGeometry(620,325,170,30)
        self.amount=QtGui.QLabel('Amount',self)
        self.amount.setGeometry(800,220,60,30)
        self.amount1=QtGui.QLineEdit('',self)
        self.amount1.setGeometry(800,255,150,30)
        self.amount2=QtGui.QLineEdit('',self)
        self.amount2.setGeometry(800,290,150,30)
        self.amount3=QtGui.QLineEdit('',self)
        self.amount3.setGeometry(800,325,150,30)
        self.total=QtGui.QPushButton('Total Amount :',self)
        self.total.setGeometry(570,500,110,30)
        self.total.clicked.connect(self.tamoun)
        self.total1=QtGui.QLineEdit('',self)
        self.total1.setGeometry(700,500,250,30)
        self.output=QtGui.QLabel(self)
        self.output.setGeometry(700,535,250,30)
        self.btn=QtGui.QPushButton('Conform Order',self)
        self.btn.setGeometry(800,580,150,30)
        self.btn.clicked.connect(self.conform)
        self.btn2=QtGui.QPushButton('Reset',self)
        self.btn2.setGeometry(640,580,150,30)
        self.btn2.clicked.connect(self.reset)
        self.new()
        
    def tamoun(self):
        am1=int(self.amount1.text())
        am2=int(self.amount2.text())
        am3=int(self.amount3.text())
        tt=int(am1+am2+am3)
        self.total1.setText(str(tt))
    def reset(self):
        a=datetime.now()
        data=a.strftime('U%dS%Y%H%M%S')
        datere=a.strftime('%d/%m/%Y')
        self.order1.setText(data)
        self.name1.setText('')
        self.add1.setText('')
        self.no1.setText('')
        self.product1.setText('')
        self.product2.setText('')
        self.product3.setText('')
        self.stdp1.setText('')
        self.stdp2.setText('')
        self.stdp3.setText('')
        self.quantity1.setText('')
        self.quantity2.setText('')
        self.quantity3.setText('')
        self.amount1.setText('')
        self.amount2.setText('')
        self.amount3.setText('')
        self.total1.setText('')
        self.redate.setText(datere)
    def new(self):
        self.name=QtGui.QLabel('New Order',self)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setGeometry(360,5,300,90)
    def conform(self):
        a=datetime.now()
        dateor=a.strftime('%d/%m/%y')
        orn=self.order1.text()
        n=self.name1.text()
        ad=self.add1.text()
        pn=self.no1.text()
        pra=self.product1.text()
        prb=self.product2.text()
        prc=self.product3.text()
        spa=self.stdp1.text()
        spb=self.stdp2.text()
        spc=self.stdp3.text()
        qua=self.quantity1.text()
        qub=self.quantity2.text()
        quc=self.quantity3.text()
        ama=self.amount1.text()
        amb=self.amount2.text()
        amc=self.amount3.text()
        tam=self.total1.text()
        datere=self.redate.text()
        conn.execute('''INSERT INTO COMPANY2 VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(orn, dateor, datere, n, pn, ad, pra+','+prb+','+prc, qua+','+qub+','+quc, spa+','+spb+','+spc, ama+','+amb+','+amc, tam))
        conn.commit()
        self.output.setText('Data Updated')
        self.order1.setText('')
        self.name1.setText('')
        self.add1.setText('')
        self.no1.setText('')
        self.product1.setText('')
        self.product2.setText('')
        self.product3.setText('')
        self.stdp1.setText('')
        self.stdp2.setText('')
        self.stdp3.setText('')
        self.quantity1.setText('')
        self.quantity2.setText('')
        self.quantity3.setText('')
        self.amount1.setText('')
        self.amount2.setText('')
        self.amount3.setText('')
        self.total1.setText('')
        self.reset()
        self.close()
        
        


class Oldorder(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Oldorder,self).__init__(parent)
        self.setGeometry(150,150,960,630)
        self.setWindowTitle('Old Order')
        self.setWindowIcon(QtGui.QIcon('logo1.png'))
        self.btn1=QtGui.QPushButton('Retrieve Data',self)
        self.btn1.setGeometry(10,10,200,50)
        self.btn1.clicked.connect(self.data)
        self.orno=QtGui.QLineEdit('',self)
        self.orno.setGeometry(220,10,300,30)
        self.find=QtGui.QPushButton('FIND',self)
        self.find.setGeometry(530,10,100,30)
        self.find.clicked.connect(self.act1)
        
        
    def data(self):
        self.db=QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.open()
        query=QtSql.QSqlQuery("select * from COMPANY2")
        self.projectModel=QtSql.QSqlTableModel()
        self.projectModel.setQuery(query)
        self.projectModel.select()
        self.projectView = QTableView(self)
        self.projectView.setGeometry(10,60,940,560)
        self.projectView.setModel(self.projectModel)
        self.projectView.show()
        self.db.close()

    def act1(self):
        orna=self.orno.text()
        self.db=QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.open()
        query=QtSql.QSqlQuery("select * from COMPANY2 WHERE ORDER_NO =+orna+")
        self.projectMode2=QtSql.QSqlTableModel()
        self.projectMode2.setQuery(query)
        self.projectMode2.select()
        self.projectView1 = QTableView(self)
        self.projectView1.setGeometry(10,60,940,560)
        self.projectView1.setModel(self.projectMode2)
        self.projectView1.show()
        self.db.close()

class Design(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Design,self).__init__(parent)
        self.setGeometry(150,150,300,340)
        self.setWindowTitle('Designer')
        self.setWindowIcon(QtGui.QIcon('logo1.png'))
        self.dialogTextBrowser4 = Samples(self)
        self.name2=QtGui.QLabel('Name :',self)
        self.name2.setGeometry(10,100,60,30)
        self.company=QtGui.QLabel('Company :;',self)
        self.company.setGeometry(10,140,60,30)
        self.pno1=QtGui.QLabel('M.No.',self)
        self.pno1.setGeometry(10,180,60,30)
        self.text1=QtGui.QLabel('E-Mail :',self)
        self.text1.setGeometry(10,220,60,30)
        self.name3=QtGui.QLineEdit('',self)
        self.name3.setGeometry(90,100,200,30)
        self.company1=QtGui.QLineEdit('',self)
        self.company1.setGeometry(90,140,200,30)
        self.pno2=QtGui.QLineEdit('',self)
        self.pno2.setGeometry(90,180,200,30)
        self.texta1=QtGui.QTextEdit('',self)
        self.texta1.setGeometry(90,220,200,70)
        self.sample=QtGui.QPushButton('Show Samples',self)
        self.sample.setGeometry(190,300,100,30)
        self.sample.clicked.connect(self.action6)
        self.name6=QtGui.QLabel('Designer',self)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.name6.setFont(font)
        self.name6.setGeometry(10,5,280,90)
    def action6(self):
        global nameg
        global compg
        global mnog
        global extrag
        nameg=self.name3.text()
        compg=self.company1.text()
        mnog=self.pno2.text()
        extrag=self.texta1.toPlainText()
        self.dialogTextBrowser4.exec_()
        

class Samples(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Samples,self).__init__(parent)
        self.setGeometry(150,150,850,530)
        self.setWindowTitle('Samples')
        self.setWindowIcon(QtGui.QIcon('logo1.png'))
        self.img1=QtGui.QLabel('',self)
        self.img1.setGeometry(10,10,400,240)
        myPixmap = QtGui.QPixmap('C:\Python34\card3.jpg')
        myScaledPixmap = myPixmap.scaled(self.img1.size())
        self.img1.setPixmap(myScaledPixmap)
        global nameg
        global compg
        global mnog
        global extrag
        self.nameg1=QtGui.QLabel('Microsoft',self)
        self.nameg1.setGeometry(50,50,240,50)
        self.compg1=QtGui.QLabel('Utkarsh Shrivastav',self)
        self.compg1.setGeometry(50,100,240,30)
        self.mnog1=QtGui.QLabel('M.No.:8225991379',self)
        self.mnog1.setGeometry(260,180,150,20)
        self.extra1=QtGui.QLabel('utkarsh@hotmail.com',self)
        self.extra1.setGeometry(260,200,150,20)
        self.nameg1.setStyleSheet("QLabel {font-size:30px; color : blue;}");
        self.compg1.setStyleSheet("QLabel {font-size:22px; color : cyan;}");
        self.mnog1.setStyleSheet("QLabel {font-size:22; color : grey;;}");
        self.extra1.setStyleSheet("QLabel {font-size:22; color : grey;;}");
        self.img2=QtGui.QLabel('',self)
        self.img2.setGeometry(10,260,400,240)
        myPixmap = QtGui.QPixmap('C:\Python34\card4.png')
        myScaledPixmap = myPixmap.scaled(self.img2.size())
        self.img2.setPixmap(myScaledPixmap)
        self.nameg2=QtGui.QLabel('Microsoft',self)
        self.nameg2.setGeometry(240,340,150,50)
        self.compg2=QtGui.QLabel('Utkarsh Shrivastav',self)
        self.compg2.setGeometry(240,390,300,30)
        self.mnog2=QtGui.QLabel('M.No.:8225991379',self)
        self.mnog2.setGeometry(240,420,150,20)
        self.extra2=QtGui.QLabel('utkarsh@hotmail.com',self)
        self.extra2.setGeometry(240,440,150,20)
        self.nameg2.setStyleSheet("QLabel {font-size:30px; color : pink;}");
        self.compg2.setStyleSheet("QLabel {font-size:19px; color : violet;}");
        self.mnog2.setStyleSheet("QLabel {font-size:12px; color : purple;;}");
        self.extra2.setStyleSheet("QLabel {font-size:12px; color : purple;;}");
        self.img3=QtGui.QLabel('',self)
        self.img3.setGeometry(430,10,400,240)
        myPixmap = QtGui.QPixmap('C:\Python34\card5.png')
        myScaledPixmap = myPixmap.scaled(self.img3.size())
        self.img3.setPixmap(myScaledPixmap)
        self.nameg3=QtGui.QLabel('Microsoft',self)
        self.nameg3.setGeometry(650,60,150,50)
        self.compg3=QtGui.QLabel('Utkarsh Shrivastav',self)
        self.compg3.setGeometry(650,110,300,30)
        self.mnog3=QtGui.QLabel('M.No.:8225991379',self)
        self.mnog3.setGeometry(650,140,150,20)
        self.extra3=QtGui.QLabel('utkarsh@hotmail.com',self)
        self.extra3.setGeometry(650,160,150,20)
        self.nameg3.setStyleSheet("QLabel {font-size:30px; color : purple;}");
        self.compg3.setStyleSheet("QLabel {font-size:19px; color : sky blue;}");
        self.mnog3.setStyleSheet("QLabel {font-size:12px; color : grey;;}");
        self.extra3.setStyleSheet("QLabel {font-size:12px; color : grey;;}");
        self.img4=QtGui.QLabel('',self)
        self.img4.setGeometry(430,260,400,240)
        myPixmap = QtGui.QPixmap('C:\Python34\card6.png')
        myScaledPixmap = myPixmap.scaled(self.img4.size())
        self.img4.setPixmap(myScaledPixmap)
        self.nameg4=QtGui.QLabel('Microsoft',self)
        self.nameg4.setGeometry(520,290,150,50)
        self.compg4=QtGui.QLabel('Utkarsh Shrivastav',self)
        self.compg4.setGeometry(480,360,300,30)
        self.mnog4=QtGui.QLabel('M.No.:8225991379',self)
        self.mnog4.setGeometry(480,400,150,20)
        self.extra4=QtGui.QLabel('utkarsh@hotmail.com',self)
        self.extra4.setGeometry(480,420,150,20)
        self.nameg4.setStyleSheet("QLabel {font-size:35px; color : white;}");
        self.compg4.setStyleSheet("QLabel {font-size:19px; color : white;}");
        self.mnog4.setStyleSheet("QLabel {font-size:12px; color : grey;;}");
        self.extra4.setStyleSheet("QLabel {font-size:12px; color : grey;;}");





class Editor(QtGui.QDialog):
    def __init__(self,parent=None):
        super(Editor,self).__init__(parent)
        self.setGeometry(100,100,950,800)
        self.setWindowTitle('Editor')
        self.view=QtGui.QLabel('',self)
        self.view.setGeometry(200,200,400,250)
        self.name = QtGui.QLineEdit(self)
        self.name.setGeometry(QtCore.QRect(70, 80, 113, 23))
        self.label = QtGui.QLabel('Name :',self)
        self.label.setGeometry(QtCore.QRect(20, 80, 57, 17))
        self.label_2 = QtGui.QLabel('M.No.:',self)
        self.label_2.setGeometry(QtCore.QRect(200, 80, 57, 17))
        self.no = QtGui.QLineEdit(self)
        self.no.setGeometry(QtCore.QRect(250, 80, 113, 23))
        self.label_3 = QtGui.QLabel('Company:',self)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 71, 17))
        self.comp = QtGui.QLineEdit(self)
        self.comp.setGeometry(QtCore.QRect(90, 110, 113, 23))
        self.label_4 = QtGui.QLabel('E-Mail:',self)
        self.label_4.setGeometry(QtCore.QRect(220, 110, 57, 17))
        self.email = QtGui.QLineEdit(self)
        self.email.setGeometry(QtCore.QRect(270, 110, 113, 23))
        self.label_5 = QtGui.QLabel('Extra:',self)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 57, 17))
        self.extra = QtGui.QTextEdit(self)
        self.extra.setGeometry(QtCore.QRect(80, 140, 301, 61))
        self.addin = QtGui.QPushButton('Add In View',self)
        self.addin.setGeometry(QtCore.QRect(260, 210, 101, 31))
        self.addin.clicked.connect(self.act4)
        self.label_6 = QtGui.QLabel('Font Style',self)
        self.label_6.setGeometry(QtCore.QRect(590, 260, 71, 20))
        self.label_7 = QtGui.QLabel('Color',self)
        self.label_7.setGeometry(QtCore.QRect(590, 200, 57, 17))
        self.color = QtGui.QLineEdit(self)
        self.color.setGeometry(QtCore.QRect(680, 200, 151, 23))
        self.line_2 = QtGui.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(100, 530, 401, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.label_25 = QtGui.QLabel('400',self)
        self.label_25.setGeometry(QtCore.QRect(250, 540, 57, 17))
        
        self.line_3 = QtGui.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(490, 520, 20, 31))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_4 = QtGui.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(92, 520, 20, 31))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        
        
             
        self.line_6 = QtGui.QFrame(self)
        self.line_6.setGeometry(QtCore.QRect(513, 300, 20, 231))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7 = QtGui.QFrame(self)
        self.line_7.setGeometry(QtCore.QRect(500, 293, 31, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8 = QtGui.QFrame(self)
        self.line_8.setGeometry(QtCore.QRect(500, 523, 31, 16))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.label_27 = QtGui.QLabel('225',self)
        self.label_27.setGeometry(QtCore.QRect(530, 390, 57, 17))
        self.line_9 = QtGui.QFrame(self)
        self.line_9.setGeometry(QtCore.QRect(100, 300, 50, 231))
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_10 = QtGui.QFrame(self)
        self.line_10.setGeometry(QtCore.QRect(125, 300, 50, 231))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_11 = QtGui.QFrame(self)
        self.line_11.setGeometry(QtCore.QRect(150, 300, 50, 231))
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_12 = QtGui.QFrame(self)
        self.line_12.setGeometry(QtCore.QRect(150, 300, 50, 231))
        self.line_12.setFrameShape(QtGui.QFrame.VLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_13 = QtGui.QFrame(self)
        self.line_13.setGeometry(QtCore.QRect(175, 300, 50, 231))
        self.line_13.setFrameShape(QtGui.QFrame.VLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_14 = QtGui.QFrame(self)
        self.line_14.setGeometry(QtCore.QRect(175, 300, 50, 231))
        self.line_14.setFrameShape(QtGui.QFrame.VLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_15 = QtGui.QFrame(self)
        self.line_15.setGeometry(QtCore.QRect(175, 300, 50, 231))
        self.line_15.setFrameShape(QtGui.QFrame.VLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_16 = QtGui.QFrame(self)
        self.line_16.setGeometry(QtCore.QRect(200, 300, 50, 231))
        self.line_16.setFrameShape(QtGui.QFrame.VLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_17 = QtGui.QFrame(self)
        self.line_17.setGeometry(QtCore.QRect(225, 300, 50, 231))
        self.line_17.setFrameShape(QtGui.QFrame.VLine)
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_18 = QtGui.QFrame(self)
        self.line_18.setGeometry(QtCore.QRect(275, 300, 50, 231))
        self.line_18.setFrameShape(QtGui.QFrame.VLine)
        self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line_19 = QtGui.QFrame(self)
        self.line_19.setGeometry(QtCore.QRect(250, 300, 50, 231))
        self.line_19.setFrameShape(QtGui.QFrame.VLine)
        self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_20 = QtGui.QFrame(self)
        self.line_20.setGeometry(QtCore.QRect(300, 300, 50, 231))
        self.line_20.setFrameShape(QtGui.QFrame.VLine)
        self.line_20.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_21 = QtGui.QFrame(self)
        self.line_21.setGeometry(QtCore.QRect(425, 300, 50, 231))
        self.line_21.setFrameShape(QtGui.QFrame.VLine)
        self.line_21.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_22 = QtGui.QFrame(self)
        self.line_22.setGeometry(QtCore.QRect(325, 300, 50, 231))
        self.line_22.setFrameShape(QtGui.QFrame.VLine)
        self.line_22.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_23 = QtGui.QFrame(self)
        self.line_23.setGeometry(QtCore.QRect(400, 300, 50, 231))
        self.line_23.setFrameShape(QtGui.QFrame.VLine)
        self.line_23.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_24 = QtGui.QFrame(self)
        self.line_24.setGeometry(QtCore.QRect(450, 300, 50, 231))
        self.line_24.setFrameShape(QtGui.QFrame.VLine)
        self.line_24.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_25 = QtGui.QFrame(self)
        self.line_25.setGeometry(QtCore.QRect(375, 300, 50, 231))
        self.line_25.setFrameShape(QtGui.QFrame.VLine)
        self.line_25.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_26 = QtGui.QFrame(self)
        self.line_26.setGeometry(QtCore.QRect(350, 300, 50, 231))
        self.line_26.setFrameShape(QtGui.QFrame.VLine)
        self.line_26.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_27 = QtGui.QFrame(self)
        self.line_27.setGeometry(QtCore.QRect(100, 300, 401, 50))
        self.line_27.setFrameShape(QtGui.QFrame.HLine)
        self.line_27.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_28 = QtGui.QFrame(self)
        self.line_28.setGeometry(QtCore.QRect(100, 325, 401, 50))
        self.line_28.setFrameShape(QtGui.QFrame.HLine)
        self.line_28.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_29 = QtGui.QFrame(self)
        self.line_29.setGeometry(QtCore.QRect(100, 350, 401, 50))
        self.line_29.setFrameShape(QtGui.QFrame.HLine)
        self.line_29.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_30 = QtGui.QFrame(self)
        self.line_30.setGeometry(QtCore.QRect(100, 350, 401, 50))
        self.line_30.setFrameShape(QtGui.QFrame.HLine)
        self.line_30.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_31 = QtGui.QFrame(self)
        self.line_31.setGeometry(QtCore.QRect(100, 425, 401, 50))
        self.line_31.setFrameShape(QtGui.QFrame.HLine)
        self.line_31.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_32 = QtGui.QFrame(self)
        self.line_32.setGeometry(QtCore.QRect(100, 375, 401, 50))
        self.line_32.setFrameShape(QtGui.QFrame.HLine)
        self.line_32.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_33 = QtGui.QFrame(self)
        self.line_33.setGeometry(QtCore.QRect(100, 425, 401, 50))
        self.line_33.setFrameShape(QtGui.QFrame.HLine)
        self.line_33.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_34 = QtGui.QFrame(self)
        self.line_34.setGeometry(QtCore.QRect(100, 400, 401, 50))
        self.line_34.setFrameShape(QtGui.QFrame.HLine)
        self.line_34.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_36 = QtGui.QFrame(self)
        self.line_36.setGeometry(QtCore.QRect(100, 450, 401, 50))
        self.line_36.setFrameShape(QtGui.QFrame.HLine)
        self.line_36.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_37 = QtGui.QFrame(self)
        self.line_37.setGeometry(QtCore.QRect(100, 475, 401, 50))
        self.line_37.setFrameShape(QtGui.QFrame.HLine)
        self.line_37.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_8 = QtGui.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(140, 260, 71, 21))
        self.line_35 = QtGui.QFrame(self)
        self.line_35.setGeometry(QtCore.QRect(40, 275, 400, 20))
        self.line_35.setFrameShape(QtGui.QFrame.HLine)
        self.line_35.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_38 = QtGui.QFrame(self)
        self.line_38.setGeometry(QtCore.QRect(60, 250, 20, 381))
        self.line_38.setFrameShape(QtGui.QFrame.VLine)
        self.line_38.setFrameShadow(QtGui.QFrame.Sunken)
        self.xaxis = QtGui.QLineEdit(self)
        self.xaxis.setGeometry(QtCore.QRect(680, 290, 113, 23))
        self.yaxis = QtGui.QLineEdit(self)
        self.yaxis.setGeometry(QtCore.QRect(680, 320, 113, 23))
        self.label_9 = QtGui.QLabel('X',self)
        self.label_9.setGeometry(QtCore.QRect(450, 270, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_10 = QtGui.QLabel('Y',self)
        self.label_10.setGeometry(QtCore.QRect(50, 630, 16, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.origin=QtGui.QLabel('0',self)
        self.origin.setGeometry(50,265,30,20)
        self.origin.setFont(font)
        self.label_16 = QtGui.QLabel('X',self)
        self.label_16.setGeometry(QtCore.QRect(800, 290, 16, 17))
        self.label_17 = QtGui.QLabel('Y',self)
        self.label_17.setGeometry(QtCore.QRect(800, 320, 21, 17))
        self.xb = QtGui.QPushButton('Change',self)
        self.xb.setGeometry(QtCore.QRect(820, 290, 71, 21))
        self.xb.clicked.connect(self.act5)
        self.label_29 = QtGui.QLabel('Background',self)
        self.label_29.setGeometry(QtCore.QRect(590, 390, 81, 17))
        self.backg = QtGui.QLineEdit(self)
        self.backg.setGeometry(QtCore.QRect(680, 390, 113, 23))
        self.bgb = QtGui.QPushButton('Change',self)
        self.bgb.setGeometry(QtCore.QRect(820, 390, 71, 21))
        self.bgb.clicked.connect(self.act7)
        self.label_30 = QtGui.QLabel('EDITOR',self)
        self.label_30.setGeometry(QtCore.QRect(13, 0, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel {color : red}");
        self.fstyle = QtGui.QFontComboBox(self)
        self.fstyle.setGeometry(QtCore.QRect(680, 260, 151, 23))
        self.fsize = QtGui.QLineEdit(self)
        self.fsize.setGeometry(QtCore.QRect(680, 230, 151, 23))
        self.label_18 = QtGui.QLabel('Font Size',self)
        self.label_18.setGeometry(QtCore.QRect(590, 230, 71, 20))
        self.namer = QtGui.QRadioButton('Name',self)
        self.namer.setGeometry(QtCore.QRect(570, 110, 104, 21))
        self.namer.setChecked(True)
        self.mnor = QtGui.QRadioButton('M.No.',self)
        self.mnor.setGeometry(QtCore.QRect(690, 110, 104, 21))
        self.comr = QtGui.QRadioButton('Company',self)
        self.comr.setGeometry(QtCore.QRect(810, 110, 104, 21))
        self.emailr = QtGui.QRadioButton('E-Mail',self)
        self.emailr.setGeometry(QtCore.QRect(570, 140, 104, 21))
        self.extrar = QtGui.QRadioButton('Extra',self)
        self.extrar.setGeometry(QtCore.QRect(690, 140, 104, 21))
        self.colorb = QtGui.QPushButton('Change',self)
        self.colorb.setGeometry(QtCore.QRect(840, 200, 71, 21))
        self.colorb.clicked.connect(self.act1)
        self.fsizeb = QtGui.QPushButton('Change',self)
        self.fsizeb.setGeometry(QtCore.QRect(840, 230, 71, 21))
        self.fsizeb.clicked.connect(self.act2)
        self.fstyleb = QtGui.QPushButton('Change',self)
        self.fstyleb.setGeometry(QtCore.QRect(840, 260, 71, 21))
        self.fstyleb.clicked.connect(self.act3)
        self.editwindow = QtGui.QLabel(self)
        self.editwindow.setGeometry(QtCore.QRect(100, 300, 400, 225))
        self.editwindow.setText("")
        self.editwindow.raise_()
        self.name.raise_()
        self.nameo=QtGui.QLabel('',self)
        self.nameo.setGeometry(100,300,400,40)
        self.mnoo=QtGui.QLabel('',self)
        self.mnoo.setGeometry(100,340,400,40)
        self.como=QtGui.QLabel('',self)
        self.como.setGeometry(100,380,400,40)
        self.emo=QtGui.QLabel('',self)
        self.emo.setGeometry(100,420,400,40)
        self.exo=QtGui.QLabel('',self)
        self.exo.setGeometry(100,460,400,60)
        self.line_361 = QtGui.QFrame(self)
        self.line_362 = QtGui.QFrame(self)
        self.line_363 = QtGui.QFrame(self)
        self.line_364 = QtGui.QFrame(self)
        self.line_361.setGeometry(QtCore.QRect(100, 300, 400, 1))
        self.line_361.setFrameShape(QtGui.QFrame.HLine)
        self.line_362.setGeometry(QtCore.QRect(100, 525, 400, 1))
        self.line_362.setFrameShape(QtGui.QFrame.HLine)
        self.line_363.setGeometry(QtCore.QRect(100, 300, 1, 225))
        self.line_363.setFrameShape(QtGui.QFrame.VLine)
        self.line_364.setGeometry(QtCore.QRect(500, 300, 1, 225))
        self.line_364.setFrameShape(QtGui.QFrame.VLine)
        self.A=QtGui.QPushButton('A',self)
        self.A.setGeometry(920,200,21,81)
        self.A.clicked.connect(self.font)
        self.label19=QtGui.QLabel(self)
        self.label19.setGeometry(425,300,75,75)
        self.labp=QtGui.QLineEdit('',self)
        self.labp.setGeometry(680,430,113,23)
        self.labx=QtGui.QLineEdit('',self)
        self.labx.setGeometry(620,490,113,23)
        self.laby=QtGui.QLineEdit('',self)
        self.laby.setGeometry(810,490,113,23)
        self.labw=QtGui.QLineEdit('',self)
        self.labw.setGeometry(620,550,113,23)
        self.labh=QtGui.QLineEdit('',self)
        self.labh.setGeometry(810,550,113,23)
        
        self.logo12=QtGui.QLabel('LOGO',self)
        self.logo12.setGeometry(590,430,61,17)

        self.position=QtGui.QLabel('Position',self)
        self.position.setGeometry(580,470,57,17)

        self.label1=QtGui.QLabel('X',self)
        self.label1.setGeometry(600,490,16,17)

        self.logox=QtGui.QLabel('Y',self)
        self.logox.setGeometry(760,490,21,17)

        self.label1y=QtGui.QLabel('Size',self)
        self.label1y.setGeometry(600,520,57,17)

        self.label1s=QtGui.QLabel('Width',self)
        self.label1s.setGeometry(570,550,57,17)

        self.labelh=QtGui.QLabel('Height',self)
        self.labelh.setGeometry(760,550,41,17)
        self.lab12=QtGui.QPushButton('Change',self)
        self.lab12.setGeometry(820,430,71,21)
        self.lab12.clicked.connect(self.act8)

        self.lab122=QtGui.QPushButton('Change',self)
        self.lab122.setGeometry(850,520,71,21)
        self.lab122.clicked.connect(self.act9)

        self.lab123=QtGui.QPushButton('Change',self)
        self.lab123.setGeometry(850,580,71,21)
        self.lab123.clicked.connect(self.act10)


    def act8(self):
        backg12=self.labp.text()
        myPixmap = QtGui.QPixmap(backg12)
        myScaledPixmap = myPixmap.scaled(self.label19.size())
        self.label19.setPixmap(myScaledPixmap)

    def act9(self):
        logox=int(self.labx.text())
        logoy=int(self.laby.text())
        self.label19.move(100+logox,300+logoy)

    def act10(self):
        logow=int(self.labw.text())
        logoh=int(self.labh.text())
        self.label19.resize(logow,logoh)
        
        


    def act1(self):   #Color
        col=self.color.text()
        if self.namer.isChecked()==True:
            self.nameo.setStyleSheet("QLabel {color : "+col+";}");
        elif self.mnor.isChecked()==True:
            self.mnoo.setStyleSheet("QLabel {color : "+col+";}");
        elif self.comr.isChecked()==True:
            self.como.setStyleSheet("QLabel {color : "+col+";}");
        elif self.emailr.isChecked()==True:
            self.emo.setStyleSheet("QLabel {color : "+col+";}");
        elif self.extrar.isChecked()==True:
            self.exo.setStyleSheet("QLabel {color : "+col+";}");



    def font(self):   #All Font
        col=self.color.text()
        fsz=self.fsize.text()
        fsy=self.fstyle.currentText()
        if self.namer.isChecked()==True:
            self.nameo.setStyleSheet("QLabel {font-family : "+fsy+"; font-size : "+fsz+"px ; color : "+col+";}");
        elif self.mnor.isChecked()==True:
            self.mnoo.setStyleSheet("QLabel {font-family : "+fsy+"; font-size : "+fsz+"px ; color : "+col+";}");
        elif self.comr.isChecked()==True:
            self.como.setStyleSheet("QLabel {font-family : "+fsy+"; font-size : "+fsz+"px ; color : "+col+";}");
        elif self.emailr.isChecked()==True:
            self.emo.setStyleSheet("QLabel {font-family : "+fsy+"; font-size : "+fsz+"px ; color : "+col+";}");
        elif self.extrar.isChecked()==True:
            self.exo.setStyleSheet("QLabel {font-family : "+fsy+"; font-size : "+fsz+"px ; color : "+col+";}");


    def act2(self):   #front size
        fsz=self.fsize.text()
        if self.namer.isChecked()==True:
            self.nameo.setStyleSheet("QLabel {font-size : "+fsz+"px;}");
        elif self.mnor.isChecked()==True:
            self.mnoo.setStyleSheet("QLabel {font-size : "+fsz+"px;}");
        elif self.comr.isChecked()==True:
            self.como.setStyleSheet("QLabel {font-size : "+fsz+"px;}");
        elif self.emailr.isChecked()==True:
            self.emo.setStyleSheet("QLabel {font-size : "+fsz+"px;}");
        elif self.extrar.isChecked()==True:
            self.exo.setStyleSheet("QLabel {font-size : "+fsz+"px;}");

    def act3(self):   #front style
        fsy=self.fstyle.currentText()
        if self.namer.isChecked()==True:
            self.nameo.setStyleSheet("QLabel {font-family : "+fsy+";}");
        elif self.mnor.isChecked()==True:
            self.mnoo.setStyleSheet("QLabel {font-family : "+fsy+";}");
        elif self.comr.isChecked()==True:
            self.como.setStyleSheet("QLabel {font-family : "+fsy+";}");
        elif self.emailr.isChecked()==True:
            self.emo.setStyleSheet("QLabel {font-family : "+fsy+";}");
        elif self.extrar.isChecked()==True:
            self.exo.setStyleSheet("QLabel {font-family : "+fsy+";}");
        

    def act4(self):    #insert into editor
        nama1=self.name.text()
        mno1=self.no.text()
        com1=self.comp.text()
        email1=self.email.text()
        extra1=self.extra.toPlainText()
        self.nameo.setText(nama1)
        self.mnoo.setText(mno1)
        self.como.setText(com1)
        self.emo.setText(email1)
        self.exo.setText(extra1)

    def act5(self):    #change x cordinate
        global namer
        global mnor
        xax=int(self.xaxis.text())
        xaxis1=int(100+xax)
        yax=int(self.yaxis.text())
        yaxis1=int(300+yax)
        if self.namer.isChecked()==True:
            self.nameo.setGeometry(xaxis1,yaxis1,200,40)
        elif self.mnor.isChecked()==True:
            self.mnoo.setGeometry(xaxis1,yaxis1,200,40)
        elif self.comr.isChecked()==True:
            self.como.setGeometry(xaxis1,yaxis1,200,40)
        elif self.emailr.isChecked()==True:
            self.emo.setGeometry(xaxis1,yaxis1,200,40)
        elif self.extrar.isChecked()==True:
            self.exo.setGeometry(xaxis1,yaxis1,200,60)

    def act7(self):   #change background image
        backg1=self.backg.text()
        myPixmap = QtGui.QPixmap(backg1)
        myScaledPixmap = myPixmap.scaled(self.editwindow.size())
        self.editwindow.setPixmap(myScaledPixmap)


        
        
        
class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.setGeometry(100,100,600,690)
        self.setWindowTitle('PrintB.Card')
        self.setWindowIcon(QtGui.QIcon('C:\Python34\logo1.png'))
        self.dialogTextBrowser1 = Neworder(self)
        self.dialogTextBrowser2 = Oldorder(self)
        self.dialogTextBrowser3 = Design(self)
        self.dialogTextBrowser4 = Samples(self)
        self.dialogTextBrowser5 = Editor(self)
        self.img=QtGui.QLabel(self)
        self.img.setGeometry(30,60,540,180)
        myPixmap = QtGui.QPixmap('C:\Python34\card.jpg')
        myScaledPixmap = myPixmap.scaled(self.img.size())
        self.img.setPixmap(myScaledPixmap)
        self.home()
    def home(self):
        self.name=QtGui.QLabel('Home',self)
        self.name.setGeometry(230,10,200,50)
        font = QtGui.QFont()
        font.setFamily("Arial Nova")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.newor=QtGui.QPushButton('New Order',self)
        self.newor.setGeometry(30,240,150,30)
        self.newor.clicked.connect(self.action1)
        self.oldor=QtGui.QPushButton('Existing Order',self)
        self.oldor.setGeometry(420,240,150,30)
        self.oldor.clicked.connect(self.action2)
        self.design=QtGui.QPushButton('Card Design',self)
        self.design.setGeometry(200,240,200,30)
        self.design.clicked.connect(self.action3)
        self.editor=QtGui.QPushButton('Editor',self)
        self.editor.setGeometry(200,275,200,30)
        self.editor.clicked.connect(self.action4)
        self.refresh=QtGui.QPushButton('Refresh',self)
        self.refresh.setGeometry(30,275,150,30)
        self.refresh.clicked.connect(self.action5)
        a=datetime.now()
        curdate=a.strftime('%d%m%Y')
        self.db=QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.open()
        query=QtSql.QSqlQuery("select ORDER_NO, RETURNING_DATE, NAME, PARTICULARS from COMPANY2 WHERE RETURNING_DATE > "+curdate+" ")
        self.projectModel=QtSql.QSqlTableModel()
        self.projectModel.setQuery(query)
        self.projectModel.select()
        self.projectView = QTableView(self)
        self.projectView.setGeometry(10,320,580,360)
        self.projectView.setModel(self.projectModel)
        self.projectView.show()
        self.db.close()

        self.show()
        
    def action1(self):
        self.dialogTextBrowser1.exec_()
    def action2(self):
        self.dialogTextBrowser2.exec_()
    def action3(self):
        self.dialogTextBrowser3.exec_()
    def action4(self):
        self.dialogTextBrowser5.exec_()
    def action5(self):
        a=datetime.now()
        curdate=a.strftime('%d%m%Y')
        self.db=QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.open()
        query=QtSql.QSqlQuery("select ORDER_NO, RETURNING_DATE, NAME, PARTICULARS from COMPANY2 WHERE RETURNING_DATE > "+curdate+" ")
        self.projectModel=QtSql.QSqlTableModel()
        self.projectModel.setQuery(query)
        self.projectModel.select()
        self.projectView = QTableView(self)
        self.projectView.setGeometry(10,320,580,360)
        self.projectView.setModel(self.projectModel)
        self.projectView.show()
        self.db.close()






app=QtGui.QApplication(sys.argv)
GUI=Window()
sys.exit(app.exec_())
