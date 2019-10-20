# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jia Yuan\Desktop\ICT Project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import csv
from csvreader import get_menu , get_operating_time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.printdatetimenow = QtWidgets.QLabel(self.centralwidget)
        self.printdatetimenow.setGeometry(QtCore.QRect(400, 20, 141, 21))
        self.printdatetimenow.setObjectName("printdatetimenow")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(0, 20, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.MenuDisplayTab = QtWidgets.QTabWidget(self.centralwidget)
        self.MenuDisplayTab.setGeometry(QtCore.QRect(10, 70, 761, 311))
        self.MenuDisplayTab.setObjectName("MenuDisplayTab")
        self.westerntab = QtWidgets.QWidget()
        self.westerntab.setObjectName("westerntab")
        self.displaywestern = QtWidgets.QLabel(self.westerntab)
        self.displaywestern.setGeometry(QtCore.QRect(0, 0, 751, 281))
        self.displaywestern.setObjectName("displaywestern")
        self.MenuDisplayTab.addTab(self.westerntab, "")
        self.mixedricetab = QtWidgets.QWidget()
        self.mixedricetab.setObjectName("mixedricetab")
        self.displaymixedrice = QtWidgets.QLabel(self.mixedricetab)
        self.displaymixedrice.setGeometry(QtCore.QRect(0, 0, 751, 281))
        self.displaymixedrice.setObjectName("displaymixedrice")
        self.MenuDisplayTab.addTab(self.mixedricetab, "")
        self.koreantab = QtWidgets.QWidget()
        self.koreantab.setObjectName("koreantab")
        self.displaykorean = QtWidgets.QLabel(self.koreantab)
        self.displaykorean.setWordWrap(True)
        self.displaykorean.setGeometry(QtCore.QRect(0, 0, 751, 281))
        self.displaykorean.setObjectName("displaykorean")
        self.MenuDisplayTab.addTab(self.koreantab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textLabel_6 = QtWidgets.QLabel(self.tab_5)
        self.textLabel_6.setGeometry(QtCore.QRect(0, 0, 751, 281))
        self.textLabel_6.setObjectName("textLabel_6")
        self.MenuDisplayTab.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.textLabel_5 = QtWidgets.QLabel(self.tab_6)
        self.textLabel_5.setGeometry(QtCore.QRect(0, 0, 751, 281))
        self.textLabel_5.setObjectName("textLabel_5")
        self.MenuDisplayTab.addTab(self.tab_6, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textLabel_4 = QtWidgets.QLabel(self.tab_4)
        self.textLabel_4.setGeometry(QtCore.QRect(0, 0, 751, 281))
        self.textLabel_4.setObjectName("textLabel_4")
        self.MenuDisplayTab.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textLabel_3 = QtWidgets.QLabel(self.tab_3)
        self.textLabel_3.setGeometry(QtCore.QRect(0, 0, 751, 281))
        self.textLabel_3.setObjectName("textLabel_3")
        self.MenuDisplayTab.addTab(self.tab_3, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.textLabel_2 = QtWidgets.QLabel(self.tab_9)
        self.textLabel_2.setGeometry(QtCore.QRect(0, 0, 751, 281))
        self.textLabel_2.setObjectName("textLabel_2")
        self.MenuDisplayTab.addTab(self.tab_9, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textLabel = QtWidgets.QLabel(self.tab)
        self.textLabel.setGeometry(QtCore.QRect(0, 1, 751, 281))
        self.textLabel.setObjectName("textLabel")
        self.MenuDisplayTab.addTab(self.tab, "")
        self.dateandtimedisplay = QtWidgets.QLabel(self.centralwidget)
        self.dateandtimedisplay.setGeometry(QtCore.QRect(0, 0, 201, 16))
        self.dateandtimedisplay.setObjectName("dateandtimedisplay")
        self.currenttimedisplay = QtWidgets.QLabel(self.centralwidget)
        self.currenttimedisplay.setGeometry(QtCore.QRect(400, 0, 161, 21))
        self.currenttimedisplay.setObjectName("currenttimedisplay")

        #queue stuff

        self.howmanyppl = QtWidgets.QLabel(self.centralwidget)
        self.howmanyppl.setGeometry(QtCore.QRect(10, 50, 241, 16))
        self.howmanyppl.setObjectName("howmanyppl")
        self.inputpplinqueu = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputpplinqueu.setGeometry(QtCore.QRect(250, 50, 104, 21))
        self.inputpplinqueu.setObjectName("inputpplinqueu")
        self.printwaitingtime = QtWidgets.QLabel(self.centralwidget)
        self.printwaitingtime.setGeometry(QtCore.QRect(490, 50, 261, 16))
        self.printwaitingtime.setObjectName("printwaitingtime")

        self.queuebutton = QtWidgets.QPushButton(self.centralwidget)
        self.queuebutton.setGeometry(QtCore.QRect(360, 50, 101, 23))
        self.queuebutton.setObjectName("queuebutton")
        self.queuebutton.clicked.connect(self.on_click)

        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setGeometry(QtCore.QRect(250, 0, 101, 23))
        self.resetbutton.setObjectName("resetbutton")
        self.resetbutton.clicked.connect(self.resetmenu)

        self.setdatebutton = QtWidgets.QPushButton(self.centralwidget)
        self.setdatebutton.setGeometry(QtCore.QRect(250, 20, 101, 23))
        self.setdatebutton.setObjectName("setdatebutton")
        self.setdatebutton.clicked.connect(self.userdatetime)
        #end of queue stuff

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MenuDisplayTab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.displayTime)
        self.timer.start(1000)

    def resetmenu(self):
        _translate = QtCore.QCoreApplication.translate
        # can just set the tabs to the menu based to the system datetime
        systemdatetime_str = QtCore.QDateTime.currentDateTime().toString(self.dateTimeEdit.displayFormat())
        print(systemdatetime_str)
        # wen chengs shit can go here

        self.displaykorean.setText(_translate("MainWindow", "reset menu"))

    def userdatetime(self):

        _translate = QtCore.QCoreApplication.translate
        userdt = self.dateTimeEdit.dateTime()
        # dt.toString("dd.MM.yyyy hh:mm:am/pm")) or u can remove the argument inside to get the raw unformatted string
        userdt_string = userdt.toString(self.dateTimeEdit.displayFormat())
        print(userdt_string)
        # if this works then we can set the rest of the text aka westerntext, mixedf rice ....
        koreantext = "korean food bestt Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec non bibendum lacus, ut lacinia dolor. Vivamus et est massa. Donec nec turpis mattis, imperdiet diam a, congue nulla. Nam sodales, lacus sagittis porttitor laoreet, lorem ex laoreet urna, eu laoreet odio dui quis diam. Nam sodales in nisl at molestie. Aenean nulla nisi, blandit quis rutrum in, lobortis quis ex. Donec eu pretium nulla, et dignissim erat. Sed luctus imperdiet eros, eget vehicula mi pellentesque sit amet. Maecenas a magna nisl. Integer ac nulla nec nulla blandit posuere at et urna."
        self.displaykorean.setText(_translate("MainWindow", koreantext))
    def displayTime(self):
        self.printdatetimenow.setText(QtCore.QDateTime.currentDateTime().toString())
        # end of datetime stuff

        #end of datetime stuff
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "North Spine Food Court"))
        #self.printdatetimenow.setText(_translate("MainWindow", "display.time()"))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.westerntab), _translate("MainWindow", "western"))
        self.displaykorean.setText(_translate("MainWindow", 'test1'))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.mixedricetab), _translate("MainWindow", "Mixed Rice"))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.koreantab), _translate("MainWindow", "Korean"))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.tab_5), _translate("MainWindow", "Japanese"))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.tab_6), _translate("MainWindow", "Drinks"))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.tab_4), _translate("MainWindow", "Claypot"))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.tab_3), _translate("MainWindow", "Noodles"))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.tab_9), _translate("MainWindow", "Indian"))
        self.MenuDisplayTab.setTabText(self.MenuDisplayTab.indexOf(self.tab), _translate("MainWindow", "Malay"))
        self.dateandtimedisplay.setText(_translate("MainWindow", "Set date and time below!"))
        self.currenttimedisplay.setText(_translate("MainWindow", "Current Date and Time"))
        self.howmanyppl.setText(_translate("MainWindow", "Roughly how many people are queuing right now?:"))
        #self.printwaitingtime.setText(_translate("MainWindow", "Done by Wen Cheng, Yow Lim, Jia Yuan"))
        self.queuebutton.setText(_translate("MainWindow", "Tell me the time!"))
        self.resetbutton.setText(_translate("MainWindow", "Reset the menu!"))
        self.setdatebutton.setText(_translate("MainWindow", "Set my menus!"))

# queue function definition
    def on_click(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            headcount_str = self.inputpplinqueu.toPlainText()
            waiting_time_str = "You have to wait approximately " + str(round(1.5 * int(headcount_str))) + " minutes!"

            self.printwaitingtime.setText(_translate("MainWindow", waiting_time_str))

        except:
            self.printwaitingtime.setText(_translate("MainWindow", "Use an valid integer please!"))
#end of queue function



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())