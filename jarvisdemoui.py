# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarviSinterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisMain(object):
    def setupUi(self, jarvisMain):
        jarvisMain.setObjectName("jarvisMain")
        jarvisMain.resize(981, 561)
        jarvisMain.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(jarvisMain)
        self.label.setGeometry(QtCore.QRect(300, 10, 381, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\sumit\\Desktop\\jarvis\\logoed.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ironimag = QtWidgets.QLabel(jarvisMain)
        self.ironimag.setGeometry(QtCore.QRect(730, 10, 241, 551))
        self.ironimag.setText("")
        self.ironimag.setPixmap(QtGui.QPixmap("C:\\Users\\sumit\\Desktop\\jarvis\\ironimage.jpg"))
        self.ironimag.setScaledContents(True)
        self.ironimag.setObjectName("ironimag")
        self.brain = QtWidgets.QLabel(jarvisMain)
        self.brain.setGeometry(QtCore.QRect(20, 380, 271, 111))
        self.brain.setText("")
        self.brain.setPixmap(QtGui.QPixmap("C:\\Users\\sumit\\Desktop\\jarvis\\JPFn.gif"))
        self.brain.setScaledContents(True)
        self.brain.setObjectName("brain")
        self.jinit = QtWidgets.QLabel(jarvisMain)
        self.jinit.setGeometry(QtCore.QRect(320, 80, 381, 391))
        self.jinit.setText("")
        self.jinit.setPixmap(QtGui.QPixmap("C:\\Users\\sumit\\Desktop\\jarvis\\ironui.gif"))
        self.jinit.setScaledContents(True)
        self.jinit.setObjectName("jinit")
        self.label_2 = QtWidgets.QLabel(jarvisMain)
        self.label_2.setGeometry(QtCore.QRect(0, 480, 711, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\sumit\\Desktop\\jarvis\\wave1.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.listening = QtWidgets.QLabel(jarvisMain)
        self.listening.setGeometry(QtCore.QRect(0, 20, 281, 191))
        self.listening.setText("")
        self.listening.setPixmap(QtGui.QPixmap("C:\\Users\\sumit\\Desktop\\jarvis\\listen.gif"))
        self.listening.setScaledContents(True)
        self.listening.setObjectName("listening")
        self.respond = QtWidgets.QLabel(jarvisMain)
        self.respond.setGeometry(QtCore.QRect(10, 380, 291, 101))
        self.respond.setText("")
        self.respond.setPixmap(QtGui.QPixmap("C:\\Users\\sumit\\Desktop\\jarvis\\respond.gif"))
        self.respond.setScaledContents(True)
        self.respond.setObjectName("respond")
        self.label_3 = QtWidgets.QLabel(jarvisMain)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 281, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Users\\sumit\\Desktop\\jarvis\\jargui.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(jarvisMain)
        self.frame.setGeometry(QtCore.QRect(10, 110, 281, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.terminalOutputbox = QtWidgets.QPlainTextEdit(self.frame)
        self.terminalOutputbox.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.terminalOutputbox.setObjectName("terminalOutputbox")
        self.exitm = QtWidgets.QPushButton(self.frame)
        self.exitm.setGeometry(QtCore.QRect(210, 180, 61, 20))
        self.exitm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitm.setMouseTracking(False)
        self.exitm.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.exitm.setObjectName("exitm")
        self.terminalInputbox = QtWidgets.QLineEdit(self.frame)
        self.terminalInputbox.setGeometry(QtCore.QRect(0, 210, 281, 41))
        self.terminalInputbox.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.terminalInputbox.setText("SAY WAKE UP JARVIS TO initiate the system")
        self.terminalInputbox.setObjectName("terminalInputbox")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(210, 220, 61, 24))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(jarvisMain)
        QtCore.QMetaObject.connectSlotsByName(jarvisMain)

    def retranslateUi(self, jarvisMain):
        _translate = QtCore.QCoreApplication.translate
        jarvisMain.setWindowTitle(_translate("jarvisMain", "...............JUST A REALLY VERY INTELLIGENT SYSTEM............."))
        self.exitm.setText(_translate("jarvisMain", "QUIT"))
        self.pushButton.setText(_translate("jarvisMain", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisMain = QtWidgets.QWidget()
    ui = Ui_jarvisMain()
    ui.setupUi(jarvisMain)
    jarvisMain.show()
    sys.exit(app.exec_())

